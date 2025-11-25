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

    def measure(self) -> Measurement:
        self._active_measurement_error = None

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
            self.comm.BeginMeasurement += begin_measurement_handler
            self.comm.EndMeasurement += end_measurement_handler
            self.comm.Disconnected += comm_error_handler

            if self.callback is not None:
                self.comm.BeginReceiveEISData += begin_receive_eis_data_handler
                self.comm.BeginReceiveCurve += begin_receive_curve_handler

        def teardown_measurement():  # unsubscribe to events indicating the start and end of the measurement
            self.comm.BeginMeasurement -= begin_measurement_handler
            self.comm.EndMeasurement -= end_measurement_handler
            self.comm.Disconnected -= comm_error_handler

            if self.callback is not None:
                self.comm.BeginReceiveEISData -= begin_receive_eis_data_handler
                self.comm.BeginReceiveCurve -= begin_receive_curve_handler

            if self._active_measurement_error is not None:
                print(self._active_measurement_error)

        @contextmanager
        def _measurement_context():
            try:
                setup_measurement()

                yield

            except Exception:
                if self.comm.ClientConnection.Semaphore.CurrentCount == 0:
                    # release lock on library (required when communicating with instrument)
                    _ = self.comm.ClientConnection.Semaphore.Release()

                self._measuring = False

                raise

            finally:
                teardown_measurement()

        async def await_measurement():
            # obtain lock on library (required when communicating with instrument)
            await create_future(self.comm.ClientConnection.Semaphore.WaitAsync())

            # send and execute the method on the instrument
            _ = self.comm.Measure(self.method)
            self._measuring = True

            # release lock on library (required when communicating with instrument)
            _ = self.comm.ClientConnection.Semaphore.Release()

            _ = await begin_measurement_event.wait()
            _ = await end_measurement_event.wait()

        with _measurement_context():
            loop.run_until_complete(await_measurement())
            loop.close()

        measurement = self._active_measurement
        self._active_measurement = None
        return Measurement(psmeasurement=measurement)
