from __future__ import annotations

import asyncio
import sys
import warnings
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, AsyncGenerator

import clr
import PalmSens
import System
from PalmSens import AsyncEventHandler, MuxModel
from PalmSens.Comm import CommManager, MuxType
from PalmSens.Plottables import (
    Curve,
    CurveEventHandler,
    EISData,
    EISDataEventHandler,
)
from System import EventHandler
from System.Threading.Tasks import Task
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

if LINUX:
    from PalmSens.Core.Linux.Comm.Devices import FTDIDevice, SerialPortDevice


if TYPE_CHECKING:
    from PalmSens import Measurement as PSMeasurement
    from PalmSens import Method as PSMethod
    from PalmSens.Data import DataArray as PSDataArray
    from PalmSens.Plottables import Curve as PSCurve
    from PalmSens.Plottables import EISData as PSEISData


async def discover_async(
    ftdi: bool = False,
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
            devices = await create_future(interface.DiscoverDevicesAsync())
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


async def connect_async(
    instrument: None | Instrument = None,
) -> InstrumentManagerAsync:
    """Async connect to instrument and return `InstrumentManagerAsync`.

    Connects to any plugged-in PalmSens USB device.
    Error if multiple devices are plugged-in.

    Parameters
    ----------
    instrument : Instrument, optional
        Connect to a specific instrument.
        Use `pypalmsens.discover_async()` to discover instruments.

    Returns
    -------
    manager : InstrumentManagerAsync
        Return instance of `InstrumentManagerAsync` connected to the given instrument.
    """
    if not instrument:
        available_instruments = await discover_async()

        if not available_instruments:
            raise ConnectionError('No instruments were discovered.')

        if len(available_instruments) > 1:
            raise ConnectionError('More than one device discovered.')

        instrument = available_instruments[0]

    manager = InstrumentManagerAsync(instrument)
    await manager.connect()
    return manager


async def measure_async(
    method: BaseTechnique,
    instrument: None | Instrument = None,
) -> Measurement:
    """Run measurement async.

    Executes the given method on any plugged-in PalmSens USB device.
    Error if multiple devices are plugged-in.

    Parameters
    ----------
    instrument : Instrument, optional
        Connect to and meassure on a specific instrument.
        Use `pypalmsens.discover_async()` to discover instruments.

    Returns
    -------
    measurement : Measurement
        Finished measurement.
    """
    async with await connect_async(instrument=instrument) as manager:
        measurement = await manager.measure(method)

    assert measurement

    return measurement


class InstrumentManagerAsync:
    """Asynchronous instrument manager for PalmSens instruments.

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

    @override
    def __repr__(self):
        return (
            f'{self.__class__.__name__}({self.instrument.id}, connected={self.is_connected()})'
        )

    async def __aenter__(self):
        if not self.is_connected():
            _ = await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        _ = await self.disconnect()

    @property
    def is_measuring(self) -> bool:
        """Return True if device is measuring."""
        return int(self._comm.State) == CommManager.DeviceState.Measurement

    @asynccontextmanager
    async def _lock(self) -> AsyncGenerator[CommManager, Any]:
        self.ensure_connection()

        await create_future(self._comm.ClientConnection.Semaphore.WaitAsync())

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

    async def connect(self) -> None:
        """Connect to instrument."""
        if self.is_connected():
            return

        psinstrument = self.instrument.device
        try:
            await create_future(psinstrument.OpenAsync())
        except System.UnauthorizedAccessException as err:
            raise ConnectionError(
                f'Cannot open instrument connection (reason: {err.Message}). Check if the device is already in use.'
            ) from err

        self._comm = await create_future(CommManager.CommManagerAsync(psinstrument))

        firmware_warning(self._comm.Capabilities)

    async def set_cell(self, cell_on: bool) -> None:
        """Turn the cell on or off.

        Parameters
        ----------
        cell_on : bool
            If true, turn on the cell
        """
        async with self._lock():
            await create_future(self._comm.SetCellOnAsync(cell_on))

    async def set_potential(self, potential: float) -> None:
        """Set the potential of the cell.

        Parameters
        ----------
        potential : float
            Potential in V
        """
        async with self._lock():
            await create_future(self._comm.SetPotentialAsync(potential))

    async def set_current_range(self, current_range: CURRENT_RANGE):
        """Set the current range for the cell.

        Parameters
        ----------
        current_range: CURRENT_RANGE
            Set the current range, use `pypalmsens.settings.CURRENT_RANGE`.
        """
        async with self._lock():
            await create_future(self._comm.SetCurrentRangeAsync(current_range._to_psobj()))

    async def read_current(self) -> float:
        """Read the current in µA.

        Returns
        -------
        current : float
            Current in µA.
        """
        async with self._lock():
            current = await create_future(self._comm.GetCurrentAsync())

        return current

    async def read_potential(self) -> float:
        """Read the potential in V.

        Returns
        -------
        potential : float
            Potential in V.
        """

        async with self._lock():
            potential = await create_future(self._comm.GetPotentialAsync())  # in V

        return potential

    async def get_instrument_serial(self) -> str:
        """Return instrument serial number.

        Returns
        -------
        serial : str
            Instrument serial.
        """
        async with self._lock():
            serial = await create_future(self._comm.GetDeviceSerialAsync())

        return serial

    def validate_method(self, method: PSMethod | BaseTechnique) -> None:
        """Validate method.

        Raise ValueError if the method cannot be validated."""
        self.ensure_connection()

        if not isinstance(method, PSMethod):
            method = method._to_psmethod()

        errors = method.Validate(self._comm.Capabilities)

        if any(error.IsFatal for error in errors):
            message = '\n'.join([error.Message for error in errors])
            raise ValueError(f'Method not compatible:\n{message}')

    async def measure(self, method: BaseTechnique, hardware_sync_initiated_event=None):
        """Start measurement using given method parameters.

        Parameters
        ----------
        method: MethodParameters
            Method parameters for measurement
        hardware_sync_initiated_event:
            ...
        """
        psmethod = method._to_psmethod()
        if self._comm is None:
            raise ConnectionError('Not connected to an instrument')

        self.__active_measurement_error = None

        self.validate_method(psmethod)

        loop = asyncio.get_running_loop()
        begin_measurement_event = asyncio.Event()
        end_measurement_event = asyncio.Event()

        def begin_measurement(measurement: PSMeasurement):
            self.__active_measurement = measurement
            begin_measurement_event.set()

        def end_measurement():
            self.__measuring = False
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
            self.__measuring = False
            self.__active_measurement_error = (
                'measurement failed due to a communication or parsing error'
            )
            begin_measurement_event.set()
            end_measurement_event.set()

        def begin_measurement_callback(sender, args):
            loop.call_soon_threadsafe(lambda: begin_measurement(args.NewMeasurement))
            return Task.CompletedTask

        def end_measurement_callback(sender, args):
            loop.call_soon_threadsafe(end_measurement)
            return Task.CompletedTask

        def curve_data_added_callback(curve: PSCurve, args):
            start = args.StartIndex
            count = curve.NPoints - start
            future = asyncio.run_coroutine_threadsafe(
                curve_new_data_added_coroutine(curve, start, count), loop
            )
            future.result()  # block c# core library thread to apply backpressure and prevent unnescessary load on the python asyncio eventloop

        async def curve_new_data_added_coroutine(curve: PSCurve, start: int, count: int):
            curve_new_data_added(curve, start, count)

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

        begin_measurement_handler = AsyncEventHandler[
            CommManager.BeginMeasurementEventArgsAsync
        ](begin_measurement_callback)
        end_measurement_handler = AsyncEventHandler[CommManager.EndMeasurementAsyncEventArgs](
            end_measurement_callback
        )
        begin_receive_curve_handler = CurveEventHandler(begin_receive_curve_callback)
        curve_data_added_handler = Curve.NewDataAddedEventHandler(curve_data_added_callback)
        curve_finished_handler = EventHandler(curve_finished_callback)
        eis_data_finished_handler = EventHandler(eis_data_finished_callback)
        begin_receive_eis_data_handler = EISDataEventHandler(begin_receive_eis_data_callback)
        eis_data_data_added_handler = EISData.NewDataEventHandler(eis_data_data_added_callback)
        comm_error_handler = EventHandler(comm_error_callback)

        # try:
        # subscribe to events indicating the start and end of the measurement
        self._comm.BeginMeasurementAsync += begin_measurement_handler
        self._comm.EndMeasurementAsync += end_measurement_handler
        self._comm.Disconnected += comm_error_handler

        if self.callback is not None:
            self._comm.BeginReceiveEISData += begin_receive_eis_data_handler
            self._comm.BeginReceiveCurve += begin_receive_curve_handler

        # obtain lock on library (required when communicating with instrument)
        await create_future(self._comm.ClientConnection.Semaphore.WaitAsync())

        # send and execute the method on the instrument
        _ = await create_future(self._comm.MeasureAsync(psmethod))
        self.__measuring = True

        # release lock on library (required when communicating with instrument)
        _ = self._comm.ClientConnection.Semaphore.Release()

        _ = await begin_measurement_event.wait()

        if hardware_sync_initiated_event is not None:
            hardware_sync_initiated_event.set()

        _ = await end_measurement_event.wait()

        # unsubscribe to events indicating the start and end of the measurement
        self._comm.BeginMeasurementAsync -= begin_measurement_handler
        self._comm.EndMeasurementAsync -= end_measurement_handler
        self._comm.Disconnected -= comm_error_handler

        if self.callback is not None:
            self._comm.BeginReceiveEISData -= begin_receive_eis_data_handler
            self._comm.BeginReceiveCurve -= begin_receive_curve_handler

        if self.__active_measurement_error is not None:
            print(self.__active_measurement_error)
            return None

        measurement = self.__active_measurement
        self.__active_measurement = None
        return Measurement(psmeasurement=measurement)

        # except Exception:
        #     traceback.print_exc()

        #     if self._comm.ClientConnection.Semaphore.CurrentCount == 0:
        #         # release lock on library (required when communicating with instrument)
        #         _= self._comm.ClientConnection.Semaphore.Release()

        #     self.__active_measurement = None
        #     self._comm.BeginMeasurementAsync -= begin_measurement_handler
        #     self._comm.EndMeasurementAsync -= end_measurement_handler
        #     self._comm.Disconnected -= comm_error_handler

        #     if self.new_data_callback is not None:
        #         self._comm.BeginReceiveEISData -= begin_receive_eis_data_handler
        #         self._comm.BeginReceiveCurve -= begin_receive_curve_handler

        #     self.__measuring = False
        #     return None

    def initiate_hardware_sync_follower_channel(
        self, method: BaseTechnique
    ) -> int | tuple[Any, Any]:
        """Initiate hardware sync follower channel.

        Parameters
        ----------
        method : MethodParameters
            Method parameters


        Returns
        -------
        tuple[event, future]
            Activate the event to start the measurement.
            The second item is a future that contains the data once the measurement is finished.
        """
        if self._comm is None:
            raise ConnectionError('Not connected to an instrument')

        hardware_sync_channel_initiated_event = asyncio.Event()
        measurement_finished_future = asyncio.Future()  # type: ignore

        async def start_measurement(
            self, method, hardware_sync_channel_initiated_event, measurement_finished_future
        ):
            measurement = await self.measure(
                method, hardware_sync_initiated_event=hardware_sync_channel_initiated_event
            )
            measurement_finished_future.set_result(measurement)

        asyncio.run_coroutine_threadsafe(
            start_measurement(
                self, method, hardware_sync_channel_initiated_event, measurement_finished_future
            ),
            asyncio.get_running_loop(),
        )

        return hardware_sync_channel_initiated_event.wait(), measurement_finished_future

    async def wait_digital_trigger(self, wait_for_high: bool) -> None:
        """Wait for digital trigger.

        Parameters
        ----------
        wait_for_high: bool
            Wait for digital line high before starting
        """
        async with self._lock():
            while True:
                if await create_future(self._comm.DigitalLineD0Async()) == wait_for_high:
                    break
                await asyncio.sleep(0.05)

    async def abort(self) -> None:
        """Abort measurement."""
        async with self._lock():
            await create_future(self._comm.AbortAsync())

    async def initialize_multiplexer(self, mux_model: int) -> int:
        """Initialize the multiplexer.

        Parameters
        ----------
        mux_model: int
            The model of the multiplexer. 0 = 8 channel, 1 = 16 channel, 2 = 32 channel.

        Returns
        -------
        int
            Number of available multiplexes channels
        """
        async with self._lock():
            model = MuxModel(mux_model)

            if model == MuxModel.MUX8R2 and (
                self._comm.ClientConnection.GetType().Equals(
                    clr.GetClrType(PalmSens.Comm.ClientConnectionPS4)
                )
                or self._comm.ClientConnection.GetType().Equals(
                    clr.GetClrType(PalmSens.Comm.ClientConnectionMS)
                )
            ):
                await create_future(self._comm.ClientConnection.ReadMuxInfoAsync())

            self._comm.Capabilities.MuxModel = model

            if self._comm.Capabilities.MuxModel == MuxModel.MUX8:
                self._comm.Capabilities.NumMuxChannels = 8
            elif self._comm.Capabilities.MuxModel == MuxModel.MUX16:
                self._comm.Capabilities.NumMuxChannels = 16
            elif self._comm.Capabilities.MuxModel == MuxModel.MUX8R2:
                await create_future(self._comm.ClientConnection.ReadMuxInfoAsync())

        channels = self._comm.Capabilities.NumMuxChannels
        return channels

    async def set_mux8r2_settings(
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
        self.ensure_connection()

        if self._comm.Capabilities.MuxModel != MuxModel.MUX8R2:
            raise ValueError(
                f"Incompatible mux model: {self._comm.Capabilities.MuxModel}, expected 'MUXR2'."
            )

        mux_settings = PSMethod.MuxSettings(False)
        mux_settings.ConnSEWE = connect_sense_to_working_electrode
        mux_settings.ConnectCERE = combine_reference_and_counter_electrodes
        mux_settings.CommonCERE = use_channel_1_reference_and_counter_electrodes
        mux_settings.UnselWE = PSMethod.MuxSettings.UnselWESetting(
            set_unselected_channel_working_electrode
        )

        async with self._lock():
            await create_future(
                self._comm.ClientConnection.SetMuxSettingsAsync(MuxType(1), mux_settings)
            )

    async def set_multiplexer_channel(self, channel: int):
        """Sets the multiplexer channel.

        Parameters
        ----------
        channel : int
            Index of the channel to set.
        """
        async with self._lock():
            await create_future(self._comm.ClientConnection.SetMuxChannelAsync(channel))

    async def disconnect(self):
        """Disconnect from the instrument."""
        if not self.is_connected():
            return

        await create_future(self._comm.DisconnectAsync())
        del self._comm
