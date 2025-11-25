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

from pypalmsens.data import Measurement

from .._data._shared import ArrayType, get_values_from_NETArray
from ._common import create_future

if TYPE_CHECKING:
    from PalmSens import Measurement as PSMeasurement
    from PalmSens.Data import DataArray as PSDataArray
    from PalmSens.Plottables import Curve as PSCurve
    from PalmSens.Plottables import EISData as PSEISData


class MeasurementManager:
    def __init__(self, *, callback, comm, method) -> None:
        self.callback = callback
        self.comm = comm
        self.method = method

        self._measuring: bool = False
        self._active_measurement: PSMeasurement | None = None
        self._active_measurement_error: str | None = None

        self.begin_measurement_event: asyncio.Event
        self.end_measurement_event: asyncio.Event

        self.begin_measurement_handler = CommManager.BeginMeasurementEventHandler(
            self.begin_measurement_callback
        )
        self.end_measurement_handler = EventHandler(self.end_measurement_callback)
        self.begin_receive_curve_handler = CurveEventHandler(self.begin_receive_curve_callback)
        self.curve_data_added_handler = Curve.NewDataAddedEventHandler(
            self.curve_data_added_callback
        )
        self.curve_finished_handler = EventHandler(self.curve_finished_callback)
        self.eis_data_finished_handler = EventHandler(self.eis_data_finished_callback)
        self.begin_receive_eis_data_handler = EISDataEventHandler(
            self.begin_receive_eis_data_callback
        )
        self.eis_data_data_added_handler = EISData.NewDataEventHandler(
            self.eis_data_data_added_callback
        )
        self.comm_error_handler = EventHandler(self.comm_error_callback)

    def setup_measurement(self):
        """Subscribe to events indicating the start and end of the measurement."""
        self.comm.BeginMeasurement += self.begin_measurement_handler
        self.comm.EndMeasurement += self.end_measurement_handler
        self.comm.Disconnected += self.comm_error_handler

        if self.callback is not None:
            self.comm.BeginReceiveEISData += self.begin_receive_eis_data_handler
            self.comm.BeginReceiveCurve += self.begin_receive_curve_handler

    def teardown_measurement(self):
        """Unsubscribe to events indicating the start and end of the measurement."""
        self.comm.BeginMeasurement -= self.begin_measurement_handler
        self.comm.EndMeasurement -= self.end_measurement_handler
        self.comm.Disconnected -= self.comm_error_handler

        if self.callback is not None:
            self.comm.BeginReceiveEISData -= self.begin_receive_eis_data_handler
            self.comm.BeginReceiveCurve -= self.begin_receive_curve_handler

        if self._active_measurement_error is not None:
            print(self._active_measurement_error)

    @contextmanager
    def _measurement_context(self):
        try:
            self.setup_measurement()

            yield

        except Exception:
            if self.comm.ClientConnection.Semaphore.CurrentCount == 0:
                # release lock on library (required when communicating with instrument)
                _ = self.comm.ClientConnection.Semaphore.Release()

            self._measuring = False

            raise

        finally:
            self.teardown_measurement()

    async def await_measurement(self):
        # obtain lock on library (required when communicating with instrument)
        await create_future(self.comm.ClientConnection.Semaphore.WaitAsync())

        # send and execute the method on the instrument
        _ = self.comm.Measure(self.method)
        self._measuring = True

        # release lock on library (required when communicating with instrument)
        _ = self.comm.ClientConnection.Semaphore.Release()

        _ = await self.begin_measurement_event.wait()
        _ = await self.end_measurement_event.wait()

    def measure(self) -> Measurement:
        self._active_measurement_error = None

        self.loop = asyncio.new_event_loop()
        self.begin_measurement_event = asyncio.Event()
        self.end_measurement_event = asyncio.Event()

        with self._measurement_context():
            self.loop.run_until_complete(self.await_measurement())
            self.loop.close()

        measurement = self._active_measurement
        self._active_measurement = None
        return Measurement(psmeasurement=measurement)

    def begin_measurement(self, measurement: PSMeasurement):
        self._active_measurement = measurement
        self.begin_measurement_event.set()

    def end_measurement(self):
        self._measuring = False
        self.end_measurement_event.set()

    def curve_new_data_added(self, curve: PSCurve, start: int, count: int):
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

    def eis_data_new_data_added(self, eis_data: PSEISData, start: int, count: int):
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

    def comm_error(
        self,
    ):
        self._measuring = False
        self._active_measurement_error = (
            'measurement failed due to a communication or parsing error'
        )
        self.begin_measurement_event.set()
        self.end_measurement_event.set()

    def begin_measurement_callback(self, sender, measurement: PSMeasurement):
        self.loop.call_soon_threadsafe(lambda: self.begin_measurement(measurement))

    def end_measurement_callback(self, sender, args):
        self.loop.call_soon_threadsafe(self.end_measurement)

    def curve_data_added_callback(self, curve: PSCurve, args):
        start = args.StartIndex
        count = curve.NPoints - start
        self.loop.call_soon_threadsafe(lambda: self.curve_new_data_added(curve, start, count))

    def curve_finished_callback(self, curve: PSCurve, args):
        curve.NewDataAdded -= self.curve_data_added_handler
        curve.Finished -= self.curve_finished_handler

    def begin_receive_curve_callback(self, sender, args):
        curve = args.GetCurve()
        curve.NewDataAdded += self.curve_data_added_handler
        curve.Finished += self.curve_finished_handler

    def eis_data_data_added_callback(self, eis_data: PSEISData, args):
        start = args.Index
        count = 1
        self.loop.call_soon_threadsafe(
            lambda: self.eis_data_new_data_added(eis_data, start, count)
        )

    def eis_data_finished_callback(self, eis_data: PSEISData, args):
        eis_data.NewDataAdded -= self.eis_data_data_added_handler
        eis_data.Finished -= self.eis_data_finished_handler

    def begin_receive_eis_data_callback(self, sender, eis_data: PSEISData):
        eis_data.NewDataAdded += self.eis_data_data_added_handler
        eis_data.Finished += self.eis_data_finished_handler

    def comm_error_callback(self, sender, args):
        self.loop.call_soon_threadsafe(self.comm_error)
