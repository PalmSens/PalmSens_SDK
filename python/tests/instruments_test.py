import logging

import pytest

from pspython import pspyinstruments, pspymethods
from pspython.data.measurement import Measurement

logger = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def manager():
    mgr = pspyinstruments.InstrumentManager()

    available_instruments = pspyinstruments.discover_instruments()
    logger.info('Connecting to %s' % available_instruments[0].name)
    success = mgr.connect(available_instruments[0])
    assert success

    yield mgr

    success = mgr.disconnect()
    assert success


def test_get_instrument_serial(manager):
    val = manager.get_instrument_serial()
    assert val
    assert isinstance(val, str)


def test_read_current(manager):
    val = manager.read_current()
    assert val
    assert isinstance(val, float)


def test_read_potential(manager):
    val = manager.read_current()
    assert val
    assert isinstance(val, float)


def test_cv(manager):
    method = pspymethods.cyclic_voltammetry(
        current_range_max=pspymethods.get_current_range(30),  # 1A range
        current_range_min=pspymethods.get_current_range(4),  # 1µA range
        current_range_start=pspymethods.get_current_range(8),  # 1mA range
        equilibration_time=0,  # seconds
        begin_potential=-1,  # V
        vertex1_potential=-1,  # V
        vertex2_potential=1,  # V
        step_potential=0.25,  # V
        scanrate=20,  # V/s
        n_scans=2,  # number of scans
    )

    measurement = manager.measure(method)

    assert measurement
    assert isinstance(measurement, Measurement)
    assert measurement.method.dotnet_method.nScans == 2

    dataset = measurement.dataset
    assert len(dataset) == 7
    assert dataset.array_names == {'scan1', 'scan2', 'time'}
    assert dataset.array_quantities == {'Charge', 'Current', 'Potential', 'Time'}
