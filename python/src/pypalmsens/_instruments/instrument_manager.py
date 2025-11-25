from __future__ import annotations

import asyncio
import sys
import warnings
from contextlib import contextmanager
from time import sleep
from typing import TYPE_CHECKING, Any, Generator

import clr
import PalmSens
import System
from PalmSens import Method, MuxModel
from PalmSens.Comm import CommManager, MuxType
from PalmSens.Plottables import (
    Curve,
    CurveEventHandler,
    EISData,
    EISDataEventHandler,
)
from System import EventHandler
from typing_extensions import override

from .._data._shared import ArrayType, get_values_from_NETArray
from .._methods import CURRENT_RANGE, BaseTechnique
from ..data import Measurement
from ._common import Callback, Instrument, create_future, firmware_warning

WINDOWS = sys.platform == 'win32'
LINUX = not WINDOWS

if WINDOWS:
    from PalmSens.Windows.Devices import (
        BLEDevice,
        BluetoothDevice,
        FTDIDevice,
        USBCDCDevice,
        WinUSBDevice,
    )
else:
    from PalmSens.Core.Linux.Comm.Devices import FTDIDevice, SerialPortDevice


if TYPE_CHECKING:
    from PalmSens import Measurement as PSMeasurement
    from PalmSens import Method as PSMethod
    from PalmSens.Data import DataArray as PSDataArray
    from PalmSens.Plottables import Curve as PSCurve
    from PalmSens.Plottables import EISData as PSEISData


def discover(
    ftdi: bool = True,
    usbcdc: bool = True,
    winusb: bool = True,
    bluetooth: bool = False,
    serial: bool = True,
    ignore_errors: bool = False,
) -> list[Instrument]:
    """Discover instruments.

    For a list of device interfaces, see:
        https://sdk.palmsens.com/python/latest/#compatibility

    Parameters
    ----------
    ftdi : bool
        If True, discover ftdi devices
    usbcdc : bool
        If True, discover usbcdc devices (Windows only)
    winusb : bool
        If True, discover winusb devices (Windows only)
    bluetooth : bool
        If True, discover bluetooth devices (Windows only)
    serial : bool
        If True, discover serial devices
    ignore_errors : False
        Ignores errors in device discovery

    Returns
    -------
    discovered : list[Instrument]
        List of dataclasses with discovered instruments.
    """
    args = [''] if WINDOWS else []
    interfaces: dict[str, Any] = {}

    if ftdi:
        interfaces['ftdi'] = FTDIDevice

    if WINDOWS:
        if usbcdc:
            interfaces['usbcdc'] = USBCDCDevice

        if winusb:
            interfaces['winusb'] = WinUSBDevice

        if bluetooth:
            interfaces['bluetooth'] = BluetoothDevice
            interfaces['ble'] = BLEDevice

    if LINUX:
        if serial:
            interfaces['serial'] = SerialPortDevice

    instruments: list[Instrument] = []

    for name, interface in interfaces.items():
        try:
            devices = interface.DiscoverDevices(*args)
        except System.DllNotFoundException:
            if ignore_errors:
                continue

            if name == 'ftdi':
                msg = (
                    'Cannot discover FTDI devices (missing driver).'
                    '\nfor more information see: '
                    'https://sdk.palmsens.com/python/latest/installation.html#ftdisetup'
                    '\nSet `ftdi=False` to hide this message.'
                )
                warnings.warn(msg, stacklevel=2)
                continue
            raise

        if WINDOWS:
            devices = devices[0]

        for device in devices:
            instruments.append(
                Instrument(
                    id=device.ToString(),
                    interface=name,
                    device=device,
                )
            )

    instruments.sort(key=lambda instrument: instrument.id)

    return instruments


def connect(
    instrument: None | Instrument = None,
) -> InstrumentManager:
    """Connect to instrument and return InstrumentManager.

    Connects to any plugged-in PalmSens USB device.
    Error if multiple devices are plugged-in.

    Parameters
    ----------
    instrument : Instrument, optional
        Connect to a specific instrument.
        Use `pypalmsens.discover()` to discover instruments.

    Returns
    -------
    manager : InstrumentManager
        Return instance of `InstrumentManager` connected to the given instrument.
    """
    if not instrument:
        available_instruments = discover(ignore_errors=True)

        if not available_instruments:
            raise ConnectionError('No instruments were discovered.')

        if len(available_instruments) > 1:
            raise ConnectionError('More than one device discovered.')

        instrument = available_instruments[0]

    manager = InstrumentManager(instrument)
    manager.connect()
    return manager


def measure(
    method: BaseTechnique,
    instrument: None | Instrument = None,
) -> Measurement:
    """Run measurement.

    Executes the given method on any plugged-in PalmSens USB device.
    Error if multiple devices are plugged-in.

    Parameters
    ----------
    instrument : Instrument, optional
        Connect to and meassure on a specific instrument.
        Use `pypalmsens.discover()` to discover instruments.

    Returns
    -------
    measurement : Measurement
        Finished measurement.
    """
    with connect(instrument=instrument) as manager:
        measurement = manager.measure(method)

    assert measurement

    return measurement


class InstrumentManager:
    """Instrument manager for PalmSens instruments.

    Parameters
    ----------
    instrument: Instrument
        Instrument to connect to, use `discover()` to find connected instruments.
    callback: Callback, optional
        If specified, call this function on every new set of data points.
        New data points are batched, and contain all points since the last
        time it was called. Each point is a dictionary containing
        `frequency`, `z_re`, `z_im` for impedimetric techniques and
        `index`, `x`, `x_unit`, `x_type`, `y`, `y_unit` and `y_type` for
        non-impedimetric techniques.
    """

    def __init__(self, instrument: Instrument, *, callback: None | Callback = None):
        self.callback: None | Callback = callback
        """This callback is called on every data point."""

        self.instrument: Instrument = instrument
        """Instrument to connect to."""

        self._comm: CommManager
        self._measuring: bool = False
        self._active_measurement: PSMeasurement | None = None
        self._active_measurement_error: str | None = None

    @override
    def __repr__(self):
        return (
            f'{self.__class__.__name__}({self.instrument.id}, connected={self.is_connected()})'
        )

    def __enter__(self):
        if not self.is_connected():
            _ = self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        _ = self.disconnect()

    @contextmanager
    def _lock(self) -> Generator[CommManager, Any, Any]:
        self.ensure_connection()

        self._comm.ClientConnection.Semaphore.Wait()

        yield self._comm

        if self._comm.ClientConnection.Semaphore.CurrentCount == 0:
            # release lock on library (required when communicating with instrument)
            _ = self._comm.ClientConnection.Semaphore.Release()

    def is_connected(self) -> bool:
        """Return True if an instrument connection exists."""
        try:
            self._comm
        except AttributeError:
            return False
        else:
            return True

    def ensure_connection(self):
        """Raises connection error if the instrument is not connected."""
        if not self.is_connected():
            raise ConnectionError('Not connected to an instrument')

    def connect(self) -> None:
        """Connect to instrument."""
        if self.is_connected():
            return

        psinstrument = self.instrument.device
        try:
            psinstrument.Open()
        except System.UnauthorizedAccessException as err:
            raise ConnectionError(
                f'Cannot open instrument connection (reason: {err.Message}). Check if the device is already in use.'
            ) from err

        self._comm = CommManager(psinstrument)

        firmware_warning(self._comm.Capabilities)

    def set_cell(self, cell_on: bool):
        """Turn the cell on or off.

        Parameters
        ----------
        cell_on : bool
            If true, turn on the cell
        """
        with self._lock():
            self._comm.CellOn = cell_on

    def set_potential(self, potential: float):
        """Set the potential of the cell.

        Parameters
        ----------
        potential : float
            Potential in V
        """
        with self._lock():
            self._comm.Potential = potential

    def set_current_range(self, current_range: CURRENT_RANGE):
        """Set the current range for the cell.

        Parameters
        ----------
        current_range: CURRENT_RANGE
            Set the current range, use `pypalmsens.settings.CURRENT_RANGE`.
        """
        with self._lock():
            self._comm.CurrentRange = current_range._to_psobj()

    def read_current(self) -> None | float:
        """Read the current in µA.

        Returns
        -------
        float
            Current in µA."
        """
        with self._lock():
            current = self._comm.Current  # in µA

        return current

    def read_potential(self) -> float:
        """Read the potential in V.

        Returns
        -------
        float
            Potential in V."""

        with self._lock():
            potential = self._comm.Potential  # in V

        return potential

    def get_instrument_serial(self) -> str:
        """Return instrument serial number.

        Returns
        -------
        serial : str
            Instrument serial.
        """
        with self._lock():
            serial = self._comm.DeviceSerial.ToString()

        return serial

    def validate_method(self, psmethod: PSMethod) -> tuple[bool, str | None]:
        """Validate method."""
        self.ensure_connection()

        errors = psmethod.Validate(self._comm.Capabilities)

        if any(error.IsFatal for error in errors):
            return False, 'Method not compatible:\n' + '\n'.join(
                [error.Message for error in errors]
            )

        return True, None

    def measure(self, method: BaseTechnique):
        """Start measurement using given method parameters.

        Parameters
        ----------
        method: MethodParameters
            Method parameters for measurement
        """
        psmethod = method._to_psmethod()

        self.ensure_connection()

        self._active_measurement_error = None

        is_valid, message = self.validate_method(psmethod)
        if not is_valid:
            raise ValueError(message)

        loop = asyncio.new_event_loop()
        begin_measurement_event = asyncio.Event()
        end_measurement_event = asyncio.Event()

        def begin_measurement(measurement: PSMeasurement):
            self._active_measurement = measurement
            begin_measurement_event.set()

        def end_measurement():
            self._measuring = False
            end_measurement_event.set()

        def curve_new_data_added(curve: PSCurve, start: int, count: int):
            data: list[dict[str, float | str]] = []
            for i in range(start, start + count):
                point: dict[str, float | str] = {}
                point['index'] = i + 1
                point['x'] = get_values_from_NETArray(curve.XAxisDataArray, start=i, count=1)[0]
                point['x_unit'] = curve.XUnit.ToString()
                point['x_type'] = ArrayType(curve.XAxisDataArray.ArrayType).name
                point['y'] = get_values_from_NETArray(curve.YAxisDataArray, start=i, count=1)[0]
                point['y_unit'] = curve.YUnit.ToString()
                point['y_type'] = ArrayType(curve.YAxisDataArray.ArrayType).name
                data.append(point)

            if self.callback:
                self.callback(data)

        def eis_data_new_data_added(eis_data: PSEISData, start: int, count: int):
            data: list[dict[str, float | str]] = []
            arrays: list[PSDataArray] = [array for array in eis_data.EISDataSet.GetDataArrays()]
            for i in range(start, start + count):
                point: dict[str, float | str] = {}
                point['index'] = i + 1
                for array in arrays:
                    array_type = ArrayType(array.ArrayType)
                    if array_type == ArrayType.Frequency:
                        point['frequency'] = get_values_from_NETArray(array, start=i, count=1)[
                            0
                        ]
                    elif array_type == ArrayType.ZRe:
                        point['zre'] = get_values_from_NETArray(array, start=i, count=1)[0]
                    elif array_type == ArrayType.ZIm:
                        point['zim'] = get_values_from_NETArray(array, start=i, count=1)[0]
                data.append(point)

            if self.callback:
                self.callback(data)

        def comm_error():
            self._measuring = False
            self._active_measurement_error = (
                'measurement failed due to a communication or parsing error'
            )
            begin_measurement_event.set()
            end_measurement_event.set()

        def begin_measurement_callback(sender, measurement: PSMeasurement):
            loop.call_soon_threadsafe(lambda: begin_measurement(measurement))

        def end_measurement_callback(sender, args):
            loop.call_soon_threadsafe(end_measurement)

        def curve_data_added_callback(curve: PSCurve, args):
            start = args.StartIndex
            count = curve.NPoints - start
            loop.call_soon_threadsafe(lambda: curve_new_data_added(curve, start, count))

        def curve_finished_callback(curve: PSCurve, args):
            curve.NewDataAdded -= curve_data_added_handler
            curve.Finished -= curve_finished_handler

        def begin_receive_curve_callback(sender, args):
            curve = args.GetCurve()
            curve.NewDataAdded += curve_data_added_handler
            curve.Finished += curve_finished_handler

        def eis_data_data_added_callback(eis_data: PSEISData, args):
            start = args.Index
            count = 1
            loop.call_soon_threadsafe(lambda: eis_data_new_data_added(eis_data, start, count))

        def eis_data_finished_callback(eis_data: PSEISData, args):
            eis_data.NewDataAdded -= eis_data_data_added_handler
            eis_data.Finished -= eis_data_finished_handler

        def begin_receive_eis_data_callback(sender, eis_data: PSEISData):
            eis_data.NewDataAdded += eis_data_data_added_handler
            eis_data.Finished += eis_data_finished_handler

        def comm_error_callback(sender, args):
            loop.call_soon_threadsafe(comm_error)

        begin_measurement_handler = CommManager.BeginMeasurementEventHandler(
            begin_measurement_callback
        )
        end_measurement_handler = EventHandler(end_measurement_callback)
        begin_receive_curve_handler = CurveEventHandler(begin_receive_curve_callback)
        curve_data_added_handler = Curve.NewDataAddedEventHandler(curve_data_added_callback)
        curve_finished_handler = EventHandler(curve_finished_callback)
        eis_data_finished_handler = EventHandler(eis_data_finished_callback)
        begin_receive_eis_data_handler = EISDataEventHandler(begin_receive_eis_data_callback)
        eis_data_data_added_handler = EISData.NewDataEventHandler(eis_data_data_added_callback)
        comm_error_handler = EventHandler(comm_error_callback)

        def setup_measurement():
            # subscribe to events indicating the start and end of the measurement
            self._comm.BeginMeasurement += begin_measurement_handler
            self._comm.EndMeasurement += end_measurement_handler
            self._comm.Disconnected += comm_error_handler

            if self.callback is not None:
                self._comm.BeginReceiveEISData += begin_receive_eis_data_handler
                self._comm.BeginReceiveCurve += begin_receive_curve_handler

        def teardown_measurement():  # unsubscribe to events indicating the start and end of the measurement
            self._comm.BeginMeasurement -= begin_measurement_handler
            self._comm.EndMeasurement -= end_measurement_handler
            self._comm.Disconnected -= comm_error_handler

            if self.callback is not None:
                self._comm.BeginReceiveEISData -= begin_receive_eis_data_handler
                self._comm.BeginReceiveCurve -= begin_receive_curve_handler

            if self._active_measurement_error is not None:
                print(self._active_measurement_error)

        @contextmanager
        def _measurement_context():
            try:
                setup_measurement()

                yield

            except Exception:
                if self._comm.ClientConnection.Semaphore.CurrentCount == 0:
                    # release lock on library (required when communicating with instrument)
                    _ = self._comm.ClientConnection.Semaphore.Release()

                self._measuring = False

                raise

            finally:
                teardown_measurement()

        async def await_measurement():
            # obtain lock on library (required when communicating with instrument)
            await create_future(self._comm.ClientConnection.Semaphore.WaitAsync())

            # send and execute the method on the instrument
            _ = self._comm.Measure(psmethod)
            self._measuring = True

            # release lock on library (required when communicating with instrument)
            _ = self._comm.ClientConnection.Semaphore.Release()

            _ = await begin_measurement_event.wait()
            _ = await end_measurement_event.wait()

        with _measurement_context():
            loop.run_until_complete(await_measurement())
            loop.close()

        measurement = self._active_measurement
        self._active_measurement = None
        return Measurement(psmeasurement=measurement)

    def wait_digital_trigger(self, wait_for_high: bool):
        """Wait for digital trigger.

        Parameters
        ----------
        wait_for_high: bool
            Wait for digital line high before starting
        """
        with self._lock():
            while True:
                if self._comm.DigitalLineD0 == wait_for_high:
                    break
                sleep(0.05)

    def abort(self) -> None:
        """Abort measurement."""
        if self._measuring is False:
            return

        with self._lock():
            self._comm.Abort()

    def initialize_multiplexer(self, mux_model: int) -> int:
        """Initialize the multiplexer.

        Parameters
        ----------
        mux_model: int
            The model of the multiplexer.
            - 0 = 8 channel
            - 1 = 16 channel
            - 2 = 32 channel

        Returns
        -------
        channels : int
            Number of available multiplexes channels
        """
        with self._lock():
            model = MuxModel(mux_model)

            if model == MuxModel.MUX8R2 and (
                self._comm.ClientConnection.GetType().Equals(
                    clr.GetClrType(PalmSens.Comm.ClientConnectionPS4)
                )
                or self._comm.ClientConnection.GetType().Equals(
                    clr.GetClrType(PalmSens.Comm.ClientConnectionMS)
                )
            ):
                self._comm.ClientConnection.ReadMuxInfo()

            self._comm.Capabilities.MuxModel = model

            if self._comm.Capabilities.MuxModel == MuxModel.MUX8:
                self._comm.Capabilities.NumMuxChannels = 8
            elif self._comm.Capabilities.MuxModel == MuxModel.MUX16:
                self._comm.Capabilities.NumMuxChannels = 16
            elif self._comm.Capabilities.MuxModel == MuxModel.MUX8R2:
                self._comm.ClientConnection.ReadMuxInfo()

            channels = self._comm.Capabilities.NumMuxChannels

        return channels

    def set_mux8r2_settings(
        self,
        connect_sense_to_working_electrode: bool = False,
        combine_reference_and_counter_electrodes: bool = False,
        use_channel_1_reference_and_counter_electrodes: bool = False,
        set_unselected_channel_working_electrode: int = 0,
    ):
        """Set the settings for the Mux8R2 multiplexer.

        Parameters
        ---------
        connect_sense_to_working_electrode: float
            Connect the sense electrode to the working electrode. Default is False.
        combine_reference_and_counter_electrodes: float
            Combine the reference and counter electrodes. Default is False.
        use_channel_1_reference_and_counter_electrodes: float
            Use channel 1 reference and counter electrodes for all working electrodes. Default is False.
        set_unselected_channel_working_electrode: float
            Set the unselected channel working electrode to disconnected/floating (0), ground (1), or standby potential (2). Default is 0.
        """
        if self._comm.Capabilities.MuxModel != MuxModel.MUX8R2:
            raise ValueError(
                f"Incompatible mux model: {self._comm.Capabilities.MuxModel}, expected 'MUXR2'."
            )

        mux_settings = Method.MuxSettings(False)
        mux_settings.ConnSEWE = connect_sense_to_working_electrode
        mux_settings.ConnectCERE = combine_reference_and_counter_electrodes
        mux_settings.CommonCERE = use_channel_1_reference_and_counter_electrodes
        mux_settings.UnselWE = Method.MuxSettings.UnselWESetting(
            set_unselected_channel_working_electrode
        )

        with self._lock():
            self._comm.ClientConnection.SetMuxSettings(MuxType(1), mux_settings)

    def set_multiplexer_channel(self, channel: int):
        """Sets the multiplexer channel.

        Parameters
        ----------
        channel : int
            Index of the channel to set.
        """
        with self._lock():
            self._comm.ClientConnection.SetMuxChannel(channel)

    def disconnect(self):
        """Disconnect from the instrument."""
        if not self.is_connected():
            return

        self._comm.Disconnect()
        self._comm = None
        self._measuring = False

        del self._comm
