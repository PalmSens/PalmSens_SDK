from __future__ import annotations

import logging

import pytest
import pytest_asyncio
from techniques_test import CP, CV, EIS, MM, MS

import pypalmsens as ps
from pypalmsens._methods import BaseTechnique

logger = logging.getLogger(__name__)


@pytest_asyncio.fixture(scope='module')
async def manager():
    instruments = ps.discover()
    async with await ps.connect_async(instruments[0]) as mgr:
        logger.warning('Connected to %s' % mgr.instrument.id)
        yield mgr


@pytest.mark.instrument
@pytest.mark.asyncio
async def test_get_instrument_serial(manager):
    val = await manager.get_instrument_serial()
    assert isinstance(val, str)


@pytest.mark.instrument
@pytest.mark.asyncio
async def test_read_current(manager):
    val = await manager.read_current()
    assert isinstance(val, float)


@pytest.mark.instrument
@pytest.mark.asyncio
async def test_read_potential(manager):
    val = await manager.read_potential()
    assert isinstance(val, float)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'method',
    (
        CV,
        CP,
        EIS,
        MS,
        MM,
    ),
)
async def test_measure(manager, method):
    params = BaseTechnique._registry[method.id].from_dict(method.kwargs)
    measurement = await manager.measure(params)

    method.validate(measurement)
