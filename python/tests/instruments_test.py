import logging

import pytest
from PalmSens.Techniques import CyclicVoltammetry as PSCyclicVoltammetry
from PalmSens.Techniques import LinearSweep as PSLinearSweep
from PalmSens.Techniques import Potentiometry as PSPotentiometry
from PalmSens.Techniques import SquareWave as PSSquareWave

from pspython import pspyinstruments
from pspython.data.measurement import Measurement
from pspython.methods._shared import get_current_range, get_potential_range
from pspython.methods.cyclic_voltammetry import CyclicVoltammetryParameters, cyclic_voltammetry
from pspython.methods.linear_sweep import LinearSweepParameters, linear_sweep_voltammetry
from pspython.methods.potentiometry import PotentiometryParameters, chronopotentiometry
from pspython.methods.squarewave import SquareWaveParameters, square_wave_voltammetry

logger = logging.getLogger(__name__)


pytestmark = pytest.mark.instrument


@pytest.fixture(scope='module')
def manager():
    mgr = pspyinstruments.InstrumentManager()

    available_instruments = pspyinstruments.discover_instruments()
    logger.warning('Connecting to %s' % available_instruments[0].name)
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
    kwargs = {
        'current_range_max': get_current_range(30),
        'current_range_min': get_current_range(4),
        'current_range_start': get_current_range(8),
        'begin_potential': -1,
        'vertex1_potential': -1,
        'vertex2_potential': 1,
        'step_potential': 0.25,
        'scanrate': 5,
        'n_scans': 2,
    }
    method_old = cyclic_voltammetry(**kwargs)
    assert isinstance(method_old, PSCyclicVoltammetry)

    method = CyclicVoltammetryParameters(**kwargs)
    measurement = manager.measure(method.to_dotnet_method())

    assert measurement
    assert isinstance(measurement, Measurement)
    assert measurement.method.dotnet_method.nScans == 2

    dataset = measurement.dataset
    assert len(dataset) == 7
    assert dataset.array_names == {'scan1', 'scan2', 'time'}
    assert dataset.array_quantities == {'Charge', 'Current', 'Potential', 'Time'}


def test_lsv(manager):
    kwargs = {
        'current_range_max': get_current_range(30),
        'current_range_min': get_current_range(4),
        'current_range_start': get_current_range(8),
        'begin_potential': -1.0,
        'end_potential': 1.0,
        'step_potential': 0.1,
        'scanrate': 2.0,
    }

    method_old = linear_sweep_voltammetry(**kwargs)
    assert isinstance(method_old, PSLinearSweep)

    method = LinearSweepParameters(**kwargs)
    measurement = manager.measure(method.to_dotnet_method())

    assert measurement
    assert isinstance(measurement, Measurement)
    assert measurement.method.dotnet_method.nScans == 1

    dataset = measurement.dataset
    assert len(dataset) == 4

    assert dataset.array_names == {'charge', 'potential', 'current', 'time'}
    assert dataset.array_quantities == {'Charge', 'Current', 'Potential', 'Time'}


def test_swv(manager):
    kwargs = {
        'current_range_max': get_current_range(30),
        'current_range_min': get_current_range(4),
        'current_range_start': get_current_range(8),
        'equilibration_time': 0.0,
        'begin_potential': -0.5,
        'end_potential': 0.5,
        'step_potential': 0.1,
        'frequency': 10.0,
        'amplitude': 0.05,
        'record_forward_and_reverse_currents': True,
    }

    method_old = square_wave_voltammetry(**kwargs)
    assert isinstance(method_old, PSSquareWave)

    method = SquareWaveParameters(**kwargs)
    measurement = manager.measure(method.to_dotnet_method())

    assert measurement
    assert isinstance(measurement, Measurement)
    assert measurement.method.dotnet_method.nScans == 1

    dataset = measurement.dataset
    assert len(dataset) == 5

    assert dataset.array_names == {'potential', 'current', 'time', 'Reverse', 'Forward'}
    assert dataset.array_quantities == {'Current', 'Potential', 'Time'}


def test_cp(manager):
    kwargs = {
        'potential_range_max': get_potential_range(7),
        'potential_range_min': get_potential_range(1),
        'potential_range_start': get_potential_range(7),
        'current': 0.0,
        'applied_current_range': get_current_range(6),
        'interval_time': 0.1,
        'run_time': 1.0,
    }

    method_old = chronopotentiometry(**kwargs)
    assert isinstance(method_old, PSPotentiometry)

    method = PotentiometryParameters(**kwargs)
    measurement = manager.measure(method.to_dotnet_method())

    assert measurement
    assert isinstance(measurement, Measurement)
    assert measurement.method.dotnet_method.nScans == 1

    dataset = measurement.dataset
    assert len(dataset) == 5

    assert dataset.array_names == {'potential', 'current', 'time', 'Reverse', 'Forward'}
    assert dataset.array_quantities == {'Current', 'Potential', 'Time'}
