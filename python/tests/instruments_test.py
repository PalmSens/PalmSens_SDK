import logging

import pytest
from PalmSens import Techniques
from pytest import approx

from pspython import pspyinstruments
from pspython.data.measurement import Measurement
from pspython.methods import techniques
from pspython.methods._shared import (
    CURRENT_RANGE,
    POTENTIAL_RANGE,
    ELevel,
)
from pspython.methods.techniques_old import (
    chronoamperometry,
    chronopotentiometry,
    cyclic_voltammetry,
    differential_pulse_voltammetry,
    electrochemical_impedance_spectroscopy,
    galvanostatic_impedance_spectroscopy,
    linear_sweep_voltammetry,
    method_script_sandbox,
    multi_step_amperometry,
    open_circuit_potentiometry,
    square_wave_voltammetry,
)

logger = logging.getLogger(__name__)


def assert_params_match_kwargs(params, *, kwargs):
    for key, exp in kwargs.items():
        ret = getattr(params, key)
        if isinstance(exp, float):
            assert ret == approx(exp), f'{key}: expected {exp}, got {ret}'
        else:
            assert ret == exp, f'{key}: expected {exp}, got {ret}'


def assert_params_round_trip_equal(*, pscls, pycls, kwargs):
    obj = pscls()

    params = pycls(**kwargs)
    params.update_psmethod(obj=obj)

    new_params = pycls()
    new_params.update_params(obj=obj)

    assert_params_match_kwargs(new_params, kwargs=kwargs)


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


@pytest.mark.instrument
def test_get_instrument_serial(manager):
    val = manager.get_instrument_serial()
    assert val
    assert isinstance(val, str)


@pytest.mark.instrument
def test_read_current(manager):
    val = manager.read_current()
    assert val
    assert isinstance(val, float)


@pytest.mark.instrument
def test_read_potential(manager):
    val = manager.read_current()
    assert val
    assert isinstance(val, float)


class TestCV:
    kwargs = {
        'begin_potential': -1,
        'vertex1_potential': -1,
        'vertex2_potential': 1,
        'step_potential': 0.25,
        'scanrate': 5,
        'n_scans': 2,
    }
    pycls = techniques.CyclicVoltammetryParameters
    pscls = Techniques.CyclicVoltammetry

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = cyclic_voltammetry(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(
            current_range_max=CURRENT_RANGE.cr_1_mA,
            current_range_min=CURRENT_RANGE.cr_100_nA,
            current_range_start=CURRENT_RANGE.cr_100_uA,
            **self.kwargs,
        )
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)
        assert measurement.method.psobj.nScans == 2

        dataset = measurement.dataset
        assert len(dataset) == 7
        assert dataset.array_names == {'scan1', 'scan2', 'time'}
        assert dataset.array_quantities == {'Charge', 'Current', 'Potential', 'Time'}


class TestLSV:
    kwargs = {
        'begin_potential': -1.0,
        'end_potential': 1.0,
        'step_potential': 0.1,
        'scanrate': 2.0,
    }
    pycls = techniques.LinearSweepParameters
    pscls = Techniques.LinearSweep

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = linear_sweep_voltammetry(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(
            current_range_max=CURRENT_RANGE.cr_1_mA,
            current_range_min=CURRENT_RANGE.cr_100_nA,
            current_range_start=CURRENT_RANGE.cr_100_uA,
            **self.kwargs,
        )
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)
        assert measurement.method.psobj.nScans == 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {'charge', 'potential', 'current', 'time'}
        assert dataset.array_quantities == {'Charge', 'Current', 'Potential', 'Time'}


class TestSWV:
    kwargs = {
        'equilibration_time': 0.0,
        'begin_potential': -0.5,
        'end_potential': 0.5,
        'step_potential': 0.1,
        'frequency': 10.0,
        'amplitude': 0.05,
        'record_forward_and_reverse_currents': True,
    }
    pycls = techniques.SquareWaveParameters
    pscls = Techniques.SquareWave

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = square_wave_voltammetry(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(
            current_range_max=CURRENT_RANGE.cr_1_mA,
            current_range_min=CURRENT_RANGE.cr_100_nA,
            current_range_start=CURRENT_RANGE.cr_100_uA,
            **self.kwargs,
        )
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)
        assert measurement.method.psobj.nScans == 1

        dataset = measurement.dataset
        assert len(dataset) == 5

        assert dataset.array_names == {'potential', 'current', 'time', 'reverse', 'forward'}
        assert dataset.array_quantities == {'Current', 'Potential', 'Time'}


class TestCP:
    kwargs = {
        'current': 0.0,
        'applied_current_range': CURRENT_RANGE.cr_100_uA,
        'interval_time': 0.1,
        'run_time': 1.0,
    }
    pycls = techniques.ChronopotentiometryParameters
    pscls = Techniques.Potentiometry

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = chronopotentiometry(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(
            potential_range_max=POTENTIAL_RANGE.pr_1_V,
            potential_range_min=POTENTIAL_RANGE.pr_10_mV,
            potential_range_start=POTENTIAL_RANGE.pr_1_V,
            **self.kwargs,
        )
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {'potential', 'current', 'time', 'charge'}
        assert dataset.array_quantities == {'Current', 'Potential', 'Time', 'Charge'}


class TestOCP:
    kwargs = {
        'interval_time': 0.1,
        'run_time': 1.0,
    }
    pycls = techniques.OpenCircuitPotentiometryParameters
    pscls = Techniques.OpenCircuitPotentiometry

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = open_circuit_potentiometry(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(
            potential_range_max=POTENTIAL_RANGE.pr_1_V,
            potential_range_min=POTENTIAL_RANGE.pr_10_mV,
            potential_range_start=POTENTIAL_RANGE.pr_1_V,
            **self.kwargs,
        )
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)

        dataset = measurement.dataset
        assert len(dataset) == 2

        assert dataset.array_names == {'potential', 'time'}
        assert dataset.array_quantities == {'Potential', 'Time'}


class TestCA:
    kwargs = {
        'interval_time': 0.1,
        'run_time': 1.0,
    }
    pycls = techniques.ChronoAmperometryParameters
    pscls = Techniques.AmperometricDetection

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = chronoamperometry(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(**self.kwargs)
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {'potential', 'time', 'charge', 'current'}
        assert dataset.array_quantities == {'Potential', 'Time', 'Charge', 'Current'}


class TestDP:
    kwargs = {
        'begin_potential': -0.4,
        'end_potential': 0.4,
        'step_potential': 0.15,
        'pulse_potential': 0.10,
        'pulse_time': 0.1,
        'scan_rate': 0.5,
    }
    pycls = techniques.DifferentialPulseParameters
    pscls = Techniques.DifferentialPulse

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = differential_pulse_voltammetry(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(**self.kwargs)
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)

        dataset = measurement.dataset
        assert len(dataset) == 3

        assert dataset.array_names == {'potential', 'time', 'current'}
        assert dataset.array_quantities == {'Potential', 'Time', 'Current'}


class TestMSA:
    kwargs = {
        'equilibration_time': 0.0,
        'interval_time': 0.01,
        'n_cycles': 2,
        'levels': [
            ELevel(level=0.5, duration=0.1),
            ELevel(level=0.3, duration=0.2),
        ],
    }
    pycls = techniques.MultiStepAmperometryParameters
    pscls = Techniques.MultistepAmperometry

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = multi_step_amperometry(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(**self.kwargs)
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)

        dataset = measurement.dataset
        assert len(dataset) == 5

        assert dataset.array_names == {
            'potential',
            'time',
            'current',
            'charge',
            'MeasuredStepStartIndex',
        }
        assert dataset.array_quantities == {'', 'Charge', 'Potential', 'Time', 'Current'}


class TestEIS:
    kwargs = {
        'n_frequencies': 7,
        'max_frequency': 1e5,
        'min_frequency': 1e3,
    }
    pycls = techniques.ElectrochemicalImpedanceSpectroscopyParameters
    pscls = Techniques.ImpedimetricMethod

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = electrochemical_impedance_spectroscopy(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(**self.kwargs)
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)

        dataset = measurement.dataset
        assert len(dataset) == 22

        assert dataset.array_names == {
            'Capacitance',
            "Capacitance'",
            "Capacitance''",
            'Eac',
            'Frequency',
            'Iac',
            'Idc',
            'miDC',
            'nPointsAC',
            'potential',
            'realtintac',
            'time',
            'ymean',
            'Phase',
            'Y',
            'YIm',
            'YRe',
            'Z',
            'ZIm',
            'ZRe',
            'debugtext',
            'mEdc',
        }
        assert dataset.array_quantities == {
            "-C''",
            '-Phase',
            "-Z''",
            'C',
            "C'",
            'Current',
            'Frequency',
            None,
            'Potential',
            'Time',
            'Y',
            "Y'",
            "Y''",
            'Z',
            "Z'",
        }


class TestGIS:
    kwargs = {
        'applied_current_range': CURRENT_RANGE.cr_10_uA,
        'equilibration_time': 0.0,
        'n_frequencies': 7,
        'max_frequency': 1e5,
        'min_frequency': 1e3,
    }
    pycls = techniques.GalvanostaticImpedanceSpectroscopyParameters
    pscls = Techniques.ImpedimetricGstatMethod

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = galvanostatic_impedance_spectroscopy(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(**self.kwargs)
        measurement = manager.measure(method.to_psmethod())

        assert measurement
        assert isinstance(measurement, Measurement)

        dataset = measurement.dataset
        assert len(dataset) == 22

        assert dataset.array_names == {
            'Capacitance',
            "Capacitance'",
            "Capacitance''",
            'Eac',
            'Frequency',
            'Iac',
            'Idc',
            'miDC',
            'nPointsAC',
            'potential',
            'realtintac',
            'time',
            'ymean',
            'Phase',
            'Y',
            'YIm',
            'YRe',
            'Z',
            'ZIm',
            'ZRe',
            'debugtext',
            'mEdc',
        }
        assert dataset.array_quantities == {
            "-C''",
            '-Phase',
            "-Z''",
            'C',
            "C'",
            'Current',
            'Frequency',
            None,
            'Potential',
            'Time',
            'Y',
            "Y'",
            "Y''",
            'Z',
            "Z'",
        }


class TestMS:
    kwargs = {'method_script': ''}
    pycls = techniques.MethodScriptParameters
    pscls = Techniques.MethodScriptSandbox

    def test_params_round_trip(self):
        assert_params_round_trip_equal(
            pscls=self.pscls,
            pycls=self.pycls,
            kwargs=self.kwargs,
        )

    def test_old_interface(self):
        method_old = method_script_sandbox(**self.kwargs)
        assert isinstance(method_old, self.pscls)

    @pytest.mark.xfail(
        reason='Not fully implemented yet: https://github.com/PalmSens/PalmSens_SDK/issues/47.'
    )
    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = self.pycls(**self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, Measurement)
