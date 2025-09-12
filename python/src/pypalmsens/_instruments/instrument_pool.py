from __future__ import annotations

import asyncio
from typing import Any, Callable, Protocol

from .._methods import MethodSettings
from ._common import Instrument
from .instrument_manager_async import InstrumentManagerAsync

# from typing_extensions import Protocol  # if you're using Python 3.6


class CustomFunc(Protocol):
    def __call__(self, manager: InstrumentManagerAsync, **kwargs: Any): ...


class InstrumentPoolAsync:
    def __init__(self, devices: list[Instrument], callback: None | Callable = None):
        self.managers = [
            InstrumentManagerAsync(device, callback=callback) for device in devices
        ]

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

    async def submit(self, func: CustomFunc, **kwargs: Any):
        """Concurrently start measurement on all managers in the pool.

        Parameters
        ----------
        func : Callable
            This function gets called with an instance of
            `InstrumentManagerAsync` as the argument.
        **kwargs
            These keyword arguments are passed on to the submitted functio.
        """
        print(kwargs)
        tasks = []
        for manager in self.managers:
            tasks.append(func(manager, **kwargs))
        return tasks

    async def measure_hw_sync(self, method: MethodSettings, *, main_channel: int = 0):
        """Concurrently start measurement on all managers in the pool.

        Parameters
        ----------
        method : MethodSettings
            Method parameters for measurement.
        main_channel : int
            Index of the main channel for hardware sync
        """
        follower_sync_tasks = []
        tasks = []

        hw_sync_manager = self.managers[main_channel]

        for i, manager in enumerate(self.managers):
            if i == main_channel:
                continue

            initiated, result = manager.initiate_hardware_sync_follower_channel(method)
            follower_sync_tasks.append(initiated)
            tasks.append(result)

        await asyncio.gather(*follower_sync_tasks)

        tasks.append(hw_sync_manager.measure(method))

        return tasks
