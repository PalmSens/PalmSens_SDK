from __future__ import annotations

import asyncio
from contextlib import contextmanager
from typing import TYPE_CHECKING

from System.Threading.Tasks import Task


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
from ._common import Callback, create_future

if TYPE_CHECKING:
    from PalmSens import Measurement as PSMeasurement
    from PalmSens import Method as PSMethod
    from PalmSens.Data import DataArray as PSDataArray
    from PalmSens.Plottables import Curve as PSCurve
    from PalmSens.Plottables import EISData as PSEISData


class MeasurementManagerAsync:
    def __init__(
        self,
        *,
        comm: CommManager,
        callback: None | Callback = None,
    ):
        self.callback = callback
        self.comm = comm

        self.is_measuring: bool = False
        self.last_measurement: PSMeasurement | None = None

        self.loop: asyncio.AbstractEventLoop
        self.begin_measurement_event: asyncio.Event
        self.end_measurement_event: asyncio.Event

        self.setup_handlers()

    def setup_handlers(self): ...

    def setup(self):
        """Subscribe to events indicating the start and end of the measurement."""
        ...

    def teardown(self):
        """Unsubscribe to events indicating the start and end of the measurement."""
        ...

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
        ...

    def measure(self, method: PSMethod) -> Measurement:
        ...

        return Measurement(psmeasurement=self.last_measurement)
