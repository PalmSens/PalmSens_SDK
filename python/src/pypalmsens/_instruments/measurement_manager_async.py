from __future__ import annotations

import asyncio
import json
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Generator

import PalmSens
import System
from PalmSens import AsyncEventHandler, Plottables
from PalmSens.Comm import CommManager
from pydantic import Field
from pydantic.dataclasses import dataclass
from System import EventHandler
from System.Threading.Tasks import Task

from .._data import DataSet
from ..data import Curve, DataArray, Measurement
from .callback import Callback, CallbackData, CallbackDataEIS, CallbackEIS
from .shared import create_future


@dataclass
class Callbacks:
    comm_error: list[Callable[[], None]] = Field(default_factory=list)
    measurement_begin: list[Callable[[Measurement], None]] = Field(default_factory=list)
    measurement_end: list[Callable[[], None]] = Field(default_factory=list)
    curve_start: list[Callable[[Curve], None]] = Field(default_factory=list)
    curve_new_data: list[Callable[[CallbackData], None]] = Field(default_factory=list)
    curve_finished: list[Callable[[Curve], None]] = Field(default_factory=list)
    eis_curve_start: list[Callable[[], None]] = Field(default_factory=list)
    eis_curve_new_data: list[Callable[[CallbackDataEIS], None]] = Field(default_factory=list)
    eis_curve_end: list[Callable[[], None]] = Field(default_factory=list)


class MeasurementManagerAsync:
    """Measurement helper class that manages the instrument communication and handles events."""

    def __init__(
        self,
        *,
        comm: CommManager,
    ):
        self.comm: CommManager = comm
        self.callback: Callback | CallbackEIS | None = None

        self.is_measuring: bool = False
        self.last_measurement: Measurement | None = None

        self.loop: asyncio.AbstractEventLoop

        self.begin_measurement_event: asyncio.Event
        self.end_measurement_event: asyncio.Event

        self.setup_callbacks()
        self.setup_handlers()
        self.eis_index = 0

    def setup_callbacks(self):
        self.callbacks = Callbacks()

        def stream_writer(message: str):
            def _inner(*args):
                assert self.stream
                _ = self.stream.write(json.dumps(message).encode())
                _ = self.stream.write(b'\n')
                self.stream.flush()

            return _inner

        self.callbacks.comm_error.append(stream_writer('Comm error'))
        self.callbacks.measurement_end.append(stream_writer('Measurement end'))
        self.callbacks.curve_start.append(stream_writer('Curve begin'))
        self.callbacks.curve_finished.append(stream_writer('Curve finished'))

        def write_metadata_to_stream(measurement: Measurement):
            _ = self.stream.write(measurement.metadata_json())
            _ = self.stream.write(b'\n')

            self.stream.flush()

        self.callbacks.measurement_begin.append(write_metadata_to_stream)

        def write_data_to_stream(data: CallbackData):
            assert self.stream
            for point in data.new_datapoints():
                _ = self.stream.write(json.dumps(point).encode())
                _ = self.stream.write(b'\n')
            self.stream.flush()

        self.callbacks.curve_new_data.append(write_data_to_stream)

        self.callbacks.eis_curve_start.append(stream_writer('EIS curve start'))
        self.callbacks.eis_curve_end.append(stream_writer('EIS curve end'))

        def write_eis_data_to_stream(data: CallbackDataEIS):
            assert self.stream
            for point in data.new_datapoints():
                _ = self.stream.write(json.dumps(point).encode())
                _ = self.stream.write(b'\n')
            self.stream.flush()

        self.callbacks.eis_curve_new_data.append(write_eis_data_to_stream)

    def setup_handlers(self):
        self.begin_measurement_handler: AsyncEventHandler = AsyncEventHandler[
            CommManager.BeginMeasurementEventArgsAsync
        ](self.begin_measurement_callback)

        self.end_measurement_handler: AsyncEventHandler = AsyncEventHandler[
            CommManager.EndMeasurementAsyncEventArgs
        ](self.end_measurement_callback)

        self.begin_receive_curve_handler: EventHandler = Plottables.CurveEventHandler(
            self.begin_receive_curve_callback
        )
        self.curve_data_added_handler: EventHandler = Plottables.Curve.NewDataAddedEventHandler(
            self.curve_data_added_callback
        )

        self.curve_finished_handler: EventHandler = EventHandler(self.curve_finished_callback)

        self.eis_data_finished_handler: EventHandler = EventHandler(
            self.eis_data_finished_callback
        )

        self.begin_receive_eis_data_handler: EventHandler = Plottables.EISDataEventHandler(
            self.begin_receive_eis_data_callback
        )

        self.eis_data_data_added_handler: EventHandler = Plottables.EISData.NewDataEventHandler(
            self.eis_data_data_added_callback
        )

        self.comm_error_handler: EventHandler = EventHandler(self.comm_error_callback)

    def setup(self):
        """Subscribe to events indicating the start and end of the measurement."""
        self.is_measuring = True
        self.comm.BeginMeasurementAsync += self.begin_measurement_handler
        self.comm.EndMeasurementAsync += self.end_measurement_handler
        self.comm.Disconnected += self.comm_error_handler

        if self.callbacks.eis_curve_new_data:
            self.comm.BeginReceiveEISData += self.begin_receive_eis_data_handler

        if self.callbacks.curve_new_data:
            self.comm.BeginReceiveCurve += self.begin_receive_curve_handler

    def teardown(self):
        """Unsubscribe to events indicating the start and end of the measurement."""
        self.comm.BeginMeasurementAsync -= self.begin_measurement_handler
        self.comm.EndMeasurementAsync -= self.end_measurement_handler
        self.comm.Disconnected -= self.comm_error_handler

        if self.callbacks.eis_curve_new_data:
            self.comm.BeginReceiveEISData -= self.begin_receive_eis_data_handler

        if self.callbacks.curve_new_data:
            self.comm.BeginReceiveCurve -= self.begin_receive_curve_handler

        self.is_measuring = False

    @contextmanager
    def _measurement_context(self, stream: Path | str | None) -> Generator[None, Any, Any]:
        """Context manager to manage the connection to the communication object."""
        try:
            self.setup()

            self.stream = open(stream, 'wb') if stream else None

            yield

        except Exception:
            if self.comm.ClientConnection.Semaphore.CurrentCount == 0:
                _ = self.comm.ClientConnection.Semaphore.Release()

            raise

        finally:
            self.teardown()

            if self.stream:
                self.stream.close()

    async def await_measurement(
        self,
        method: PalmSens.Method,
        sync_event: asyncio.Event | None = None,
    ):
        """Helper function to handle the measurement.

        Obtaining a lock on the `ClientConnection` (via semaphore) is required when
        communicating with the instrument."""
        await create_future(self.comm.ClientConnection.Semaphore.WaitAsync())

        _ = await create_future(self.comm.MeasureAsync(method))

        _ = self.comm.ClientConnection.Semaphore.Release()

        _ = await self.begin_measurement_event.wait()

        if sync_event is not None:
            sync_event.set()

        _ = await self.end_measurement_event.wait()

    async def measure(
        self,
        method: PalmSens.Method,
        callback: Callback | CallbackEIS | None = None,
        sync_event: asyncio.Event | None = None,
        stream: Path | str | None = None,
    ) -> Measurement:
        """Measure given method.

        Parameters
        ----------
        method: MethodParameters
            Method parameters for measurement
        callback: Callback, optional
            Gets called every time new data is added
        sync_event: Event, optional
            Used to pass event for hardware synchronization

        Returns
        -------
        measurement : Measurement
        """
        self.loop = asyncio.get_running_loop()
        self.begin_measurement_event = asyncio.Event()
        self.end_measurement_event = asyncio.Event()

        if callback:
            self.callbacks.curve_new_data.append(callback)  # TODO: Support callback EIS
            self.callbacks.eis_curve_new_data.append(callback)  # TODO: Support callback EIS

        with self._measurement_context(stream=stream):
            await self.await_measurement(method=method, sync_event=sync_event)

        assert self.last_measurement
        return self.last_measurement

    def begin_measurement_callback(
        self, sender: PalmSens.Comm.CommManager, args
    ) -> Task.CompletedTask:
        """Called when the measurement begins."""
        measurement = Measurement(psmeasurement=args.NewMeasurement)

        self.last_measurement = measurement

        _ = self.loop.call_soon_threadsafe(self.begin_measurement_event.set)

        for callback in self.callbacks.measurement_begin:
            callback(measurement)

        return Task.CompletedTask

    def end_measurement_callback(
        self, comm: PalmSens.Comm.CommManager, args
    ) -> Task.CompletedTask:
        """Called when the measurement ends."""

        _ = self.loop.call_soon_threadsafe(self.end_measurement_event.set)

        for callback in self.callbacks.measurement_end:
            _ = self.loop.call_soon_threadsafe(callback)

        return Task.CompletedTask

    def curve_data_added_callback(
        self,
        pscurve: Plottables.Curve,
        args: PalmSens.Data.ArrayDataAddedEventArgs,
    ):
        """Called when new data is added to the curve."""

        data = CallbackData(
            x_array=DataArray(psarray=pscurve.XAxisDataArray),
            y_array=DataArray(psarray=pscurve.YAxisDataArray),
            start=args.StartIndex,
        )

        for callback in self.callbacks.curve_new_data:
            _ = self.loop.call_soon_threadsafe(callback, data)  # type: ignore

    def curve_finished_callback(
        self,
        pscurve: Plottables.Curve,
        args: PalmSens.FinishedEventArgs,
    ):
        """Unsubscribe to curve finished / new data added events."""
        pscurve.NewDataAdded -= self.curve_data_added_handler
        pscurve.Finished -= self.curve_finished_handler

        curve = Curve(pscurve=pscurve)

        for callback in self.callbacks.curve_finished:
            _ = self.loop.call_soon_threadsafe(callback, curve)  # type: ignore

    def begin_receive_curve_callback(
        self,
        sender: PalmSens.Comm.CommManager,
        args: PalmSens.Plottables.CurveEventArgs,
    ):
        """Subscribe to curve finished / new data added events."""
        pscurve = args.GetCurve()
        pscurve.NewDataAdded += self.curve_data_added_handler
        pscurve.Finished += self.curve_finished_handler

        curve = Curve(pscurve=pscurve)

        for callback in self.callbacks.curve_start:
            _ = self.loop.call_soon_threadsafe(callback, curve)  # type: ignore

    def eis_data_data_added_callback(self, eis_data: Plottables.EISData, args):
        """Called when a new EIS data points is obtained. Requires a callback."""
        data = CallbackDataEIS(
            data=DataSet(psdataset=eis_data.EISDataSet),
            start=self.eis_index,
        )

        for callback in self.callbacks.eis_curve_new_data:
            _ = self.loop.call_soon_threadsafe(callback, data)  # type: ignore

        # self.eis_index = int(eis_data.NPoints)

    def eis_data_finished_callback(
        self,
        eis_data: Plottables.EISData,
        args,
    ):
        """Unsubscribes to EIS data events."""

        eis_data.NewDataAdded -= self.eis_data_data_added_handler
        eis_data.Finished -= self.eis_data_finished_handler

        for callback in self.callbacks.eis_curve_end:
            _ = self.loop.call_soon_threadsafe(callback)  # type: ignore

    def begin_receive_eis_data_callback(
        self,
        sender: PalmSens.Comm.CommManager,
        eis_data: Plottables.EISData,
    ):
        """Subscribes to EIS data events."""
        eis_data.NewDataAdded += self.eis_data_data_added_handler
        eis_data.Finished += self.eis_data_finished_handler

        for callback in self.callbacks.eis_curve_start:
            _ = self.loop.call_soon_threadsafe(callback)  # type: ignore

    def comm_error_callback(self, sender: PalmSens.Comm.CommManager, args: System.EventArgs):
        """Called when a communication error occurs."""

        for callback in self.callbacks.comm_error:
            _ = self.loop.call_soon_threadsafe(callback)

        def teardown_and_raise():
            self.begin_measurement_event.set()
            self.end_measurement_event.set()

            raise ConnectionError('Measurement failed due to a communication or parsing error')

        _ = self.loop.call_soon_threadsafe(teardown_and_raise)
