from __future__ import annotations

import asyncio
from contextlib import contextmanager
from typing import TYPE_CHECKING

from PalmSens.Comm import CommManager
from PalmSens.Plottables import (
    Curve,
    CurveEventHandler,
    EISData,
    EISDataEventHandler,
)
from System import EventHandler

from .._data import Measurement
from .._data._shared import ArrayType, get_values_from_NETArray
from ._common import Callback, create_future

if TYPE_CHECKING:
    from PalmSens import Measurement as PSMeasurement
    from PalmSens import Method as PSMethod
    from PalmSens.Data import DataArray as PSDataArray
    from PalmSens.Plottables import Curve as PSCurve
    from PalmSens.Plottables import EISData as PSEISData


class MeasurementManager:
    def __init__(
        self,
        *,
        comm: CommManager,
        callback: Callback | None = None,
    ):
        self.callback = callback
        self.comm = comm

        self.is_measuring: bool = False
        self.last_measurement: PSMeasurement | None = None

        self.loop: asyncio.AbstractEventLoop

        self.begin_measurement_event: asyncio.Event
        self.end_measurement_event: asyncio.Event

        self.setup_handlers()

    def setup_handlers(self):
        self.begin_measurement_handler: EventHandler = CommManager.BeginMeasurementEventHandler(
            self.begin_measurement_callback
        )

        self.end_measurement_handler: EventHandler = EventHandler(self.end_measurement_callback)
        self.begin_receive_curve_handler: EventHandler = CurveEventHandler(
            self.begin_receive_curve_callback
        )
        self.curve_data_added_handler: EventHandler = Curve.NewDataAddedEventHandler(
            self.curve_data_added_callback
        )

        self.curve_finished_handler: EventHandler = EventHandler(self.curve_finished_callback)
        self.eis_data_finished_handler: EventHandler = EventHandler(
            self.eis_data_finished_callback
        )

        self.begin_receive_eis_data_handler: EventHandler = EISDataEventHandler(
            self.begin_receive_eis_data_callback
        )

        self.eis_data_data_added_handler: EventHandler = EISData.NewDataEventHandler(
            self.eis_data_data_added_callback
        )

        self.comm_error_handler: EventHandler = EventHandler(self.comm_error_callback)

    def setup(self):
        """Subscribe to events indicating the start and end of the measurement."""
        self.is_measuring = True
        self.comm.BeginMeasurement += self.begin_measurement_handler
        self.comm.EndMeasurement += self.end_measurement_handler
        self.comm.Disconnected += self.comm_error_handler

        if self.callback is not None:
            self.comm.BeginReceiveEISData += self.begin_receive_eis_data_handler
            self.comm.BeginReceiveCurve += self.begin_receive_curve_handler

    def teardown(self):
        """Unsubscribe to events indicating the start and end of the measurement."""
        self.comm.BeginMeasurement -= self.begin_measurement_handler
        self.comm.EndMeasurement -= self.end_measurement_handler
        self.comm.Disconnected -= self.comm_error_handler

        if self.callback is not None:
            self.comm.BeginReceiveEISData -= self.begin_receive_eis_data_handler
            self.comm.BeginReceiveCurve -= self.begin_receive_curve_handler

        self.is_measuring = False

    @contextmanager
    def _measurement_context(self):
        try:
            self.setup()

            yield

        except Exception:
            if self.comm.ClientConnection.Semaphore.CurrentCount == 0:
                # release lock on library (required when communicating with instrument)
                _ = self.comm.ClientConnection.Semaphore.Release()

            raise

        finally:
            self.teardown()

    async def await_measurement(self, method: PSMethod):
        # obtain lock on library (required when communicating with instrument)
        await create_future(self.comm.ClientConnection.Semaphore.WaitAsync())

        _ = self.comm.Measure(method)

        # release lock on library (required when communicating with instrument)
        _ = self.comm.ClientConnection.Semaphore.Release()

        _ = await self.begin_measurement_event.wait()
        _ = await self.end_measurement_event.wait()

    def measure(
        self,
        method: PSMethod,
    ) -> Measurement:
        self.loop = asyncio.new_event_loop()
        self.begin_measurement_event = asyncio.Event()
        self.end_measurement_event = asyncio.Event()

        with self._measurement_context():
            self.loop.run_until_complete(self.await_measurement(method=method))
            self.loop.close()

        assert self.last_measurement
        return Measurement(psmeasurement=self.last_measurement)

    def begin_measurement(self, measurement: PSMeasurement):
        self.last_measurement = measurement
        self.begin_measurement_event.set()

    def end_measurement(self):
        self.end_measurement_event.set()

    def begin_measurement_callback(self, sender, measurement: PSMeasurement):
        _ = self.loop.call_soon_threadsafe(self.begin_measurement, measurement)

    def end_measurement_callback(self, sender, args):
        _ = self.loop.call_soon_threadsafe(self.end_measurement)

    def curve_new_data_added(self, curve: PSCurve, args):
        start = args.StartIndex
        count = curve.NPoints - start

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

    def curve_data_added_callback(self, curve: PSCurve, args):
        _ = self.loop.call_soon_threadsafe(self.curve_new_data_added, curve, args)

    def curve_finished_callback(self, curve: PSCurve, args):
        curve.NewDataAdded -= self.curve_data_added_handler
        curve.Finished -= self.curve_finished_handler

    def begin_receive_curve_callback(self, sender, args):
        curve = args.GetCurve()
        curve.NewDataAdded += self.curve_data_added_handler
        curve.Finished += self.curve_finished_handler

    def eis_data_new_data_added(self, eis_data: PSEISData, args):
        start = args.Index
        count = 1

        data: list[dict[str, float | str]] = []
        arrays: list[PSDataArray] = [array for array in eis_data.EISDataSet.GetDataArrays()]
        for i in range(start, start + count):
            point: dict[str, float | str] = {}
            point['index'] = i + 1
            for array in arrays:
                array_type = ArrayType(array.ArrayType)
                if array_type == ArrayType.Frequency:
                    point['frequency'] = get_values_from_NETArray(array, start=i, count=1)[0]
                elif array_type == ArrayType.ZRe:
                    point['zre'] = get_values_from_NETArray(array, start=i, count=1)[0]
                elif array_type == ArrayType.ZIm:
                    point['zim'] = get_values_from_NETArray(array, start=i, count=1)[0]
            data.append(point)

        if self.callback:
            self.callback(data)

    def eis_data_data_added_callback(self, eis_data: PSEISData, args):
        _ = self.loop.call_soon_threadsafe(
            self.eis_data_new_data_added,
            eis_data,
            args,
        )

    def eis_data_finished_callback(self, eis_data: PSEISData, args):
        eis_data.NewDataAdded -= self.eis_data_data_added_handler
        eis_data.Finished -= self.eis_data_finished_handler

    def begin_receive_eis_data_callback(self, sender, eis_data: PSEISData):
        eis_data.NewDataAdded += self.eis_data_data_added_handler
        eis_data.Finished += self.eis_data_finished_handler

    def comm_error(self):
        self.begin_measurement_event.set()
        self.end_measurement_event.set()

        raise ConnectionError('Measurement failed due to a communication or parsing error')

    def comm_error_callback(self, sender, args):
        _ = self.loop.call_soon_threadsafe(self.comm_error)
