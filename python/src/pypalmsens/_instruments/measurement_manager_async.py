from __future__ import annotations

import asyncio
import json
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Generator

import PalmSens
from PalmSens import AsyncEventHandler, Plottables
from PalmSens.Comm import CommManager
from pydantic import Field
from pydantic.dataclasses import dataclass
from System import EventHandler
from System.Threading.Tasks import Task

from .._data import DataSet
from ..data import DataArray, Measurement
from .callback import Callback, CallbackData, CallbackDataEIS, CallbackEIS
from .shared import create_future


@dataclass
class Callbacks:
    comm_error: list[Callable[[], None]] = Field(default_factory=list)
    # measurement begin
    measurement_end: list[Callable[[], None]] = Field(default_factory=list)
    curve_begin_receive: list[Callable[[], None]] = Field(default_factory=list)
    # new data
    curve_finished: list[Callable[[], None]] = Field(default_factory=list)
    # eis begin
    # eis new data
    # eis end


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
        self.last_measurement: PalmSens.Measurement | None = None

        self.loop: asyncio.AbstractEventLoop

        self.begin_measurement_event: asyncio.Event
        self.end_measurement_event: asyncio.Event

        self.setup_callbacks()
        self.setup_handlers()

    def setup_callbacks(self):
        self.callbacks = Callbacks()

        def stream_writer(message: str):
            def _inner():
                assert self.stream
                _ = self.stream.write(json.dumps(message).encode())
                _ = self.stream.write(b'\n')
                self.stream.flush()

            return _inner

        self.callbacks.comm_error.append(stream_writer('Comm error'))
        self.callbacks.measurement_end.append(stream_writer('Measurement end'))
        self.callbacks.curve_begin_receive.append(stream_writer('Curve begin'))
        self.callbacks.curve_finished.append(stream_writer('Curve finished'))

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

        self.comm.BeginReceiveEISData += self.begin_receive_eis_data_handler
        self.comm.BeginReceiveCurve += self.begin_receive_curve_handler

    def teardown(self):
        """Unsubscribe to events indicating the start and end of the measurement."""
        self.comm.BeginMeasurementAsync -= self.begin_measurement_handler
        self.comm.EndMeasurementAsync -= self.end_measurement_handler
        self.comm.Disconnected -= self.comm_error_handler

        if self.callback is not None:
            self.comm.BeginReceiveEISData -= self.begin_receive_eis_data_handler
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

        self.callback = callback

        with self._measurement_context(stream=stream):
            await self.await_measurement(method=method, sync_event=sync_event)

        assert self.last_measurement
        return Measurement(psmeasurement=self.last_measurement)

    def begin_measurement_callback(self, sender, args) -> Task.CompletedTask:
        """Called when the measurement begins."""

        def func(measurement: PalmSens.Measurement):
            self.last_measurement = measurement
            self.begin_measurement_event.set()

            meas = Measurement(psmeasurement=args.NewMeasurement)

            if self.stream:
                _ = self.stream.write(meas.metadata_json())
                _ = self.stream.write(b'\n')

                self.stream.flush()

        _ = self.loop.call_soon_threadsafe(func, args.NewMeasurement)
        return Task.CompletedTask

    def end_measurement_callback(self, sender, args) -> Task.CompletedTask:
        """Called when the measurement ends."""

        def func():
            self.end_measurement_event.set()

            for callback in self.callbacks.measurement_end:
                callback()

        _ = self.loop.call_soon_threadsafe(func)
        return Task.CompletedTask

    def curve_data_added_callback(self, curve: Plottables.Curve, args):
        """Called when new data is added to the curve."""

        data = CallbackData(
            x_array=DataArray(psarray=curve.XAxisDataArray),
            y_array=DataArray(psarray=curve.YAxisDataArray),
            start=args.StartIndex,
        )

        if self.callback:
            _ = self.loop.call_soon_threadsafe(self.callback, data)  # type: ignore

        if self.stream:

            def func(data):
                assert self.stream
                for point in data.new_datapoints():
                    _ = self.stream.write(json.dumps(point).encode())
                    _ = self.stream.write(b'\n')
                self.stream.flush()

            _ = self.loop.call_soon_threadsafe(func, data)  # type: ignore

    def curve_finished_callback(self, curve: Plottables.Curve, args):
        """Unsubscribe to curve finished / new data added events."""
        curve.NewDataAdded -= self.curve_data_added_handler
        curve.Finished -= self.curve_finished_handler

        def func():
            for callback in self.callbacks.curve_finished:
                callback()

        _ = self.loop.call_soon_threadsafe(func)  # type: ignore

    def begin_receive_curve_callback(self, sender, args):
        """Subscribe to curve finished / new data added events."""
        curve = args.GetCurve()
        curve.NewDataAdded += self.curve_data_added_handler
        curve.Finished += self.curve_finished_handler

        def func():
            for callback in self.callbacks.curve_begin_receive:
                callback()

        _ = self.loop.call_soon_threadsafe(func)  # type: ignore

    def eis_data_data_added_callback(self, eis_data: Plottables.EISData, args):
        """Called when a new EIS data points is obtained. Requires a callback."""
        assert self.callback

        data = CallbackDataEIS(
            data=DataSet(psdataset=eis_data.EISDataSet),
            start=args.Index,
        )

        _ = self.loop.call_soon_threadsafe(self.callback, data)  # type: ignore

    def eis_data_finished_callback(self, eis_data: Plottables.EISData, args):
        """Unsubscribes to EIS data events."""
        eis_data.NewDataAdded -= self.eis_data_data_added_handler
        eis_data.Finished -= self.eis_data_finished_handler

    def begin_receive_eis_data_callback(self, sender, eis_data: Plottables.EISData):
        """Subscribes to EIS data events."""
        eis_data.NewDataAdded += self.eis_data_data_added_handler
        eis_data.Finished += self.eis_data_finished_handler

    def comm_error_callback(self, sender, args):
        """Called when a communication error occurs."""

        def func():
            self.begin_measurement_event.set()
            self.end_measurement_event.set()

            for callback in self.callbacks.comm_error:
                callback()

            raise ConnectionError('Measurement failed due to a communication or parsing error')

        _ = self.loop.call_soon_threadsafe(func)
