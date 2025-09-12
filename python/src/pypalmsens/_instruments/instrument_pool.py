from __future__ import annotations

import asyncio

from .._methods import MethodSettings
from ._common import Instrument
from .instrument_manager_async import InstrumentManagerAsync


class InstrumentPoolAsync:
    def __init__(self, devices: list[Instrument]):
        self.managers = [InstrumentManagerAsync(device) for device in devices]

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        return await self.disconnect()

    async def connect(self):
        """Connect all instrument managers in the pool."""
        tasks = []
        for manager in self.managers:
            tasks.append(manager.connect())
        await asyncio.gather(*tasks)

    async def disconnect(self):
        """Disconnect all instrument managers in the pool."""
        tasks = []
        for manager in self.managers:
            tasks.append(manager.disconnect())
        await asyncio.gather(*tasks)

    async def measure(self, method: MethodSettings):
        """Concurrently start measurement on all managers in the pool.

        Parameters
        ----------
        method : MethodSettings
            Method parameters for measurement.
        """
        tasks = []
        for manager in self.managers:
            tasks.append(manager.measure(method))
        return tasks
