from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Awaitable, Callable

from .._methods import MethodSettings
from ._common import Instrument
from .instrument_manager_async import InstrumentManagerAsync

if TYPE_CHECKING:
    from .._data.measurement import Measurement


class InstrumentPoolAsync:
    """Manages a set of instrument.

    Parameters
    ----------
    devices_or_managers : list[Instrument | InstrumentManagerAsync]
        List of devices or managers.
    callback : Callable, optional
        Optional callable to set on instrument managers
    """

    def __init__(
        self,
        devices_or_managers: list[Instrument],
        *,
        callback: None | Callable = None,
    ):
        self.managers = []
        """List of instruments managers in the pool."""

        for item in devices_or_managers:
            if isinstance(item, Instrument):
                self.managers.append(InstrumentManagerAsync(item, callback=callback))
            else:
                if callback:
                    item.callback = callback
                self.managers.append(item)

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        return await self.disconnect()

    def __iter__(self):
        yield from self.managers

    async def connect(self) -> None:
        """Connect all instrument managers in the pool."""
        tasks = []
        for manager in self.managers:
            tasks.append(manager.connect())
        await asyncio.gather(*tasks)

    async def disconnect(self) -> None:
        """Disconnect all instrument managers in the pool."""
        tasks = []
        for manager in self.managers:
            tasks.append(manager.disconnect())
        await asyncio.gather(*tasks)

    def is_connected(self) -> bool:
        """Return true if all managers in the pool are connected."""
        return all(manager.is_connected for manager in self.managers)

    def is_disconnected(self) -> bool:
        """Return true if all managers in the pool are disconnected."""
        return not any(manager.is_connected for manager in self.managers)

    async def remove(self, manager: InstrumentManagerAsync) -> None:
        """Close and remove manager from pool.

        Parameters
        ----------
        manager : InstrumentManagerAsync
            Instance of an instrument manager.
        """
        self.managers.remove(manager)
        await manager.disconnect()

    async def add(self, manager: InstrumentManagerAsync) -> None:
        """Open and add manager to the pool.

        Parameters
        ----------
        manager : InstrumentManagerAsync
            Instance of an instrument manager.
        """
        await manager.connect()
        self.managers.append(manager)

    async def measure(self, method: MethodSettings) -> list[Awaitable[Measurement]]:
        """Concurrently start measurement on all managers in the pool.

        Parameters
        ----------
        method : MethodSettings
            Method parameters for measurement.
        """
        tasks: list[Awaitable[Measurement]] = []
        for manager in self.managers:
            tasks.append(manager.measure(method))
        return tasks

    async def submit(self, func: Callable, **kwargs: Any) -> list[Awaitable[Any]]:
        """Concurrently start measurement on all managers in the pool.

        Parameters
        ----------
        func : Callable
            This function gets called with an instance of
            `InstrumentManagerAsync` as the argument.
        **kwargs
            These keyword arguments are passed on to the submitted function.
        """
        tasks: list[Awaitable[Any]] = []
        for manager in self.managers:
            tasks.append(func(manager, **kwargs))
        return tasks

    async def measure_hw_sync(
        self,
        method: MethodSettings,
        *,
        main_channel: None | int = None,
        main_serial: None | str = None,
        main_manager: None | InstrumentManagerAsync,
    ) -> list[Awaitable[Measurement]]:
        """Concurrently start measurement on all managers in the pool.

        All instruments are prepared and put in a waiting state.
        The measurements are started via a hardware sync trigger.

        If no main channel/serial/manager is provided, the first manager
        in the pool is taken as the main hardware sync manager.

        Parameters
        ----------
        method : MethodSettings
            Method parameters for measurement.
        main_channel : int
            Index of the main channel for hardware sync
        main_serial : int
            Serial number of the main channel for hardware sync
        main_manager : int
            Instance of the manager to use for hardware sync.
            Does not have to be part of the pool.
        """
        follower_sync_tasks = []
        tasks = []

        if main_channel:
            for manager in self.managers:
                if manager.get_channel_index() == main_channel:
                    hw_sync_manager = manager
                    break
            else:
                raise IndexError(f'Unknown channel: {main_channel}')
        elif main_serial:
            for manager in self.managers:
                if await manager.get_instrument_serial() == main_serial:
                    hw_sync_manager = manager
                    break
            else:
                raise IndexError(f'Unknown serial: {main_serial}')
        elif main_manager:
            hw_sync_manager = main_manager
        else:
            hw_sync_manager = self.managers[0]

        for manager in self.managers:
            if manager is hw_sync_manager:
                continue

            initiated, result = manager.initiate_hardware_sync_follower_channel(method)
            follower_sync_tasks.append(initiated)
            tasks.append(result)

        await asyncio.gather(*follower_sync_tasks)

        tasks.append(hw_sync_manager.measure(method))

        return tasks
