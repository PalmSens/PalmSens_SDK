from __future__ import annotations

import logging

import pytest
import pytest_asyncio
from techniques_test import BaseCP, BaseCV, BaseEIS, BaseMM, BaseMS

import pypalmsens as ps
from pypalmsens._methods import BaseTechnique

logger = logging.getLogger(__name__)


@pytest.mark.asyncio
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


class MeasureAsyncMixin:
    @pytest.mark.instrument
    @pytest.mark.asyncio
    async def _test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = await manager.measure(method)

        self.validate(measurement)


class TestCVAsync(BaseCV, MeasureAsyncMixin): ...


class TestCPAsync(BaseCP, MeasureAsyncMixin): ...


class TestEISAsync(BaseEIS, MeasureAsyncMixin): ...


class TestMSAsync(BaseMS, MeasureAsyncMixin): ...


class TestMMAsync(BaseMM, MeasureAsyncMixin): ...
