from __future__ import annotations

import asyncio

import pytest
import pytest_asyncio

import pypalmsens
from pypalmsens._data.measurement import Measurement


@pytest_asyncio.fixture
async def pool():
    instruments = await pypalmsens.discover_async()
    assert len(instruments) >= 0

    async with pypalmsens.InstrumentPoolAsync(instruments) as pool:
        yield pool

    assert pool.is_disconnected() is True


@pytest.mark.asyncio
@pytest.mark.instrument
async def test_pool(pool):
    assert pool.is_connected() is True

    n = len(pool.managers)

    assert pool.managers
    manager = pool.managers[0]

    await pool.remove(manager)

    assert manager not in pool.managers

    await pool.add(manager)
    assert len(pool.managers) == n
    assert manager in pool.managers


@pytest.mark.asyncio
@pytest.mark.instrument
async def test_pool_measure(pool):
    method = pypalmsens.LinearSweepVoltammetry(
        end_potential=-0.5,
        begin_potential=0.5,
        step_potential=0.1,
        scanrate=8.0,
    )

    tasks = await pool.measure(method)
    results = await asyncio.gather(*tasks)

    assert len(results) == len(pool.managers)
    assert all(isinstance(item, Measurement) for item in results)


@pytest.mark.asyncio
@pytest.mark.instrument
async def test_pool_submit(pool):
    async def my_func(manager, value):
        assert value == 1
        serial = await manager.get_instrument_serial()
        return serial

    tasks = await pool.submit(my_func, value=1)
    results = await asyncio.gather(*tasks)

    assert len(results) == len(pool.managers)
    assert all(isinstance(item, str) for item in results)


@pytest.mark.asyncio
@pytest.mark.instrument
async def test_pool_hw_sync(pool):
    method = pypalmsens.LinearSweepVoltammetry(
        end_potential=-0.5,
        begin_potential=0.5,
        step_potential=0.1,
        scanrate=8.0,
        general=pypalmsens.settings.General(use_hardware_sync=True),
    )

    tasks = await pool.measure_hw_sync(method)
    results = await asyncio.gather(*tasks)

    assert len(results) == len(pool.managers)
    assert all(isinstance(item, Measurement) for item in results)


def test_pool_instrument():
    device = pypalmsens._instruments.Instrument(name='test', connection='test', device=None)
    mgr = pypalmsens.InstrumentManagerAsync(device)
    pool = pypalmsens.InstrumentPoolAsync([mgr])
    assert pool.managers
