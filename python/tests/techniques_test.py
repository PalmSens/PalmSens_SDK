from __future__ import annotations

import logging
import tempfile
from pathlib import Path

import pytest
import System

import pypalmsens as ps
from pypalmsens._methods import BaseTechnique

logger = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def manager():
    with ps.connect() as mgr:
        logger.warning('Connected to %s' % mgr.instrument.id)
        yield mgr


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
    id = 'cv'
    kwargs = {
        'begin_potential': -1,
        'vertex1_potential': -1,
        'vertex2_potential': 1,
        'step_potential': 0.25,
        'scanrate': 5,
        'n_scans': 2,
        'current_range': {'max': 7, 'min': 3, 'start': 6},
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)

        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        assert measurement.method.psmethod.nScans == 2

        dataset = measurement.dataset
        assert len(dataset) == 7
        assert list(dataset.keys()) == [
            'Time',
            'Potential_1',
            'Current_1',
            'Charge_1',
            'Potential_2',
            'Current_2',
            'Charge_2',
        ]
        assert dataset.array_names == {'scan1', 'scan2', 'time'}
        assert dataset.array_quantities == {'Charge', 'Current', 'Potential', 'Time'}


class TestFCV:
    id = 'fcv'
    kwargs = {
        'begin_potential': -1,
        'vertex1_potential': -1,
        'vertex2_potential': 1,
        'step_potential': 0.25,
        'scanrate': 500,
        'n_scans': 3,
        'n_avg_scans': 2,
        'n_equil_scans': 2,
        'current_range': 5,
    }

    @pytest.mark.xfail(raises=AssertionError, reason='FCV only returns 1 scan with nScans>1')
    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)

        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        assert measurement.method.psmethod.nScans == 3
        assert measurement.method.psmethod.nAvgScans == 2
        assert measurement.method.psmethod.nEqScans == 2

        dataset = measurement.dataset

        assert len(dataset) == 10
        assert list(dataset.keys()) == [
            'Time',
            'Potential_1',
            'Current_1',
            'Charge_1',
            'Potential_2',
            'Current_2',
            'Charge_2',
            'Potential_3',
            'Current_3',
            'Charge_3',
        ]
        assert dataset.array_names == {'scan1', 'scan2', 'scan3', 'time'}
        assert dataset.array_quantities == {'Charge', 'Current', 'Potential', 'Time'}


class TestLSV:
    id = 'lsv'
    kwargs = {
        'begin_potential': -1.0,
        'end_potential': 1.0,
        'step_potential': 0.1,
        'scanrate': 2.0,
        'current_range': {'max': 7, 'min': 3, 'start': 6},
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)

        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {'charge', 'potential', 'current', 'time'}
        assert dataset.array_quantities == {'Charge', 'Current', 'Potential', 'Time'}


class TestACV:
    id = 'acv'
    kwargs = {
        'begin_potential': -0.15,
        'end_potential': 0.15,
        'step_potential': 0.05,
        'ac_potential': 0.25,
        'frequency': 200.0,
        'scanrate': 0.2,
        'current_range': {'max': 7, 'min': 3, 'start': 6},
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 8

        assert dataset.array_names == {
            'Applied E DC',
            'E AC RMS',
            'E DC',
            "Y'",
            "Y''",
            'i AC RMS',
            'i DC',
            'time',
        }
        assert dataset.array_quantities == {'Current', 'Potential', 'Time', "Y'", "Y''"}


class TestSWV:
    id = 'swv'
    kwargs = {
        'equilibration_time': 0.0,
        'begin_potential': -0.5,
        'end_potential': 0.5,
        'step_potential': 0.1,
        'frequency': 10.0,
        'amplitude': 0.05,
        'record_forward_and_reverse_currents': True,
        'current_range': {'max': 7, 'min': 3, 'start': 6},
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        assert measurement.method.psmethod.nScans == 1

        dataset = measurement.dataset
        assert len(dataset) == 5

        assert dataset.array_names == {'potential', 'current', 'time', 'reverse', 'forward'}
        assert dataset.array_quantities == {'Current', 'Potential', 'Time'}


class TestCP:
    id = 'pot'
    kwargs = {
        'current': 0.0,
        'applied_current_range': ps.settings.CURRENT_RANGE.cr_100_uA,
        'interval_time': 0.1,
        'run_time': 1.0,
        'potential_range': {'max': 7, 'min': 1, 'start': 7},
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)

        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {'potential', 'current', 'time', 'charge'}
        assert dataset.array_quantities == {'Current', 'Potential', 'Time', 'Charge'}


class TestSCP:
    id = 'scp'
    kwargs = {
        'current': 0.1,
        'applied_current_range': ps.settings.CURRENT_RANGE.cr_100_uA,
        'measurement_time': 0.2,
        'potential_range': {'max': 7, 'min': 1, 'start': 7},
    }

    @pytest.mark.xfail(
        raises=System.NotImplementedException,
        reason='Not all devices support SCP.',
    )
    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {'potential', 'current', 'time', 'charge'}
        assert dataset.array_quantities == {'Current', 'Potential', 'Time', 'Charge'}


class TestLSP:
    id = 'lsp'
    kwargs = {
        'applied_current_range': ps.settings.CURRENT_RANGE.cr_100_uA,
        'current_step': 0.1,
        'scan_rate': 8.0,
        'potential_range': {'max': 7, 'min': 1, 'start': 7},
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {'potential', 'current', 'time', 'charge'}
        assert dataset.array_quantities == {'Current', 'Potential', 'Time', 'Charge'}


class TestOCP:
    id = 'ocp'
    kwargs = {
        'interval_time': 0.1,
        'run_time': 1.0,
        'potential_range': {'max': 7, 'min': 1, 'start': 7},
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 2

        assert dataset.array_names == {'potential', 'time'}
        assert dataset.array_quantities == {'Potential', 'Time'}


class TestCA:
    id = 'ad'
    kwargs = {
        'interval_time': 0.1,
        'run_time': 1.0,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {'potential', 'time', 'charge', 'current'}
        assert dataset.array_quantities == {'Potential', 'Time', 'Charge', 'Current'}


class TestFAM:
    id = 'fam'
    kwargs = {
        'interval_time': 0.1,
        'run_time': 1.0,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {'potential', 'time', 'charge', 'current'}
        assert dataset.array_quantities == {'Potential', 'Time', 'Charge', 'Current'}


class TestDPV:
    id = 'dpv'
    kwargs = {
        'begin_potential': -0.4,
        'end_potential': 0.4,
        'step_potential': 0.15,
        'pulse_potential': 0.10,
        'pulse_time': 0.1,
        'scan_rate': 0.5,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 3

        assert dataset.array_names == {'potential', 'time', 'current'}
        assert dataset.array_quantities == {'Potential', 'Time', 'Current'}


class TestPAD:
    id = 'pad'
    kwargs = {
        'potential': 0.5,
        'pulse_potential': 1.0,
        'pulse_time': 0.1,
        'mode': 'pulse',
        'run_time': 1.0,
        'interval_time': 0.2,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 3

        assert dataset.array_names == {'potential', 'time', 'current'}
        assert dataset.array_quantities == {'Potential', 'Time', 'Current'}


class TestMPAD:
    id = 'mpad'
    kwargs = {
        'run_time': 2.5,
        'potential_1': 0.1,
        'potential_2': 0.1,
        'potential_3': 0.1,
        'duration_1': 0.15,
        'duration_2': 0.15,
        'duration_3': 0.15,
    }

    @pytest.mark.xfail(
        raises=ValueError,
        reason='Not all devices support MPAD.',
    )
    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 3

        assert dataset.array_names == {'potential', 'time', 'current'}
        assert dataset.array_quantities == {'Potential', 'Time', 'Current'}


class TestNPV:
    id = 'npv'
    kwargs = {
        'begin_potential': -0.4,
        'end_potential': 0.4,
        'step_potential': 0.15,
        'pulse_time': 0.1,
        'scan_rate': 0.5,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 3

        assert dataset.array_names == {'potential', 'time', 'current'}
        assert dataset.array_quantities == {'Potential', 'Time', 'Current'}


class TestMA:
    id = 'ma'
    kwargs = {
        'equilibration_time': 0.0,
        'interval_time': 0.01,
        'n_cycles': 2,
        'levels': [
            {'level': 0.5, 'duration': 0.1},
            {'level': 0.3, 'duration': 0.2},
        ],
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {
            'potential',
            'time',
            'current',
            'charge',
        }
        assert dataset.array_quantities == {'Charge', 'Potential', 'Time', 'Current'}


class TestMP:
    id = 'mp'
    kwargs = {
        'interval_time': 0.01,
        'n_cycles': 2,
        'levels': [
            {'level': 0.5, 'duration': 0.1},
            {'level': 0.3, 'duration': 0.2},
        ],
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)

        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {
            'potential',
            'time',
            'current',
            'charge',
        }
        assert dataset.array_quantities == {'Charge', 'Potential', 'Time', 'Current'}


class TestCC:
    id = 'cc'
    kwargs = {
        'equilibration_time': 0.0,
        'interval_time': 0.01,
        'step1_run_time': 0.1,
        'step2_run_time': 0.2,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 4

        assert dataset.array_names == {
            'potential',
            'time',
            'current',
            'charge',
        }
        assert dataset.array_quantities == {'Charge', 'Potential', 'Time', 'Current'}


class TestEIS:
    id = 'eis'
    kwargs = {
        'n_frequencies': 7,
        'max_frequency': 1e5,
        'min_frequency': 1e3,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 18

        assert dataset.array_names == {
            "Capacitance'",
            "Capacitance''",
            'Capacitance',
            'Eac',
            'Frequency',
            'Iac',
            'Idc',
            'Phase',
            'Y',
            'YIm',
            'YRe',
            'Z',
            'ZIm',
            'ZRe',
            'mEdc',
            'miDC',
            'potential',
            'time',
        }
        assert dataset.array_quantities == {
            "-C''",
            '-Phase',
            "-Z''",
            'C',
            "C'",
            'Current',
            'Frequency',
            'Potential',
            'Time',
            'Y',
            "Y'",
            "Y''",
            'Z',
            "Z'",
        }


class TestFIS:
    id = 'fis'
    kwargs = {
        'frequency': 40000,
        'run_time': 0.5,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 18

        assert dataset.array_names == {
            "Capacitance'",
            "Capacitance''",
            'Capacitance',
            'Eac',
            'Frequency',
            'Iac',
            'Idc',
            'Phase',
            'Y',
            'YIm',
            'YRe',
            'Z',
            'ZIm',
            'ZRe',
            'mEdc',
            'miDC',
            'potential',
            'time',
        }
        assert dataset.array_quantities == {
            "-C''",
            '-Phase',
            "-Z''",
            'C',
            "C'",
            'Current',
            'Frequency',
            'Potential',
            'Time',
            'Y',
            "Y'",
            "Y''",
            'Z',
            "Z'",
        }


class TestGIS:
    id = 'gis'
    kwargs = {
        'applied_current_range': 5,
        'equilibration_time': 0.0,
        'n_frequencies': 7,
        'max_frequency': 1e5,
        'min_frequency': 1e3,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 18

        assert dataset.array_names == {
            "Capacitance'",
            "Capacitance''",
            'Capacitance',
            'Eac',
            'Frequency',
            'Iac',
            'Idc',
            'Phase',
            'Y',
            'YIm',
            'YRe',
            'Z',
            'ZIm',
            'ZRe',
            'mEdc',
            'miDC',
            'potential',
            'time',
        }
        assert dataset.array_quantities == {
            "-C''",
            '-Phase',
            "-Z''",
            'C',
            "C'",
            'Current',
            'Frequency',
            'Potential',
            'Time',
            'Y',
            "Y'",
            "Y''",
            'Z',
            "Z'",
        }


class TestFGIS:
    id = 'fgis'
    kwargs = {
        'applied_current_range': 5,
        'run_time': 0.3,
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 18

        assert dataset.array_names == {
            "Capacitance'",
            "Capacitance''",
            'Capacitance',
            'Eac',
            'Frequency',
            'Iac',
            'Idc',
            'Phase',
            'Y',
            'YIm',
            'YRe',
            'Z',
            'ZIm',
            'ZRe',
            'mEdc',
            'miDC',
            'potential',
            'time',
        }
        assert dataset.array_quantities == {
            "-C''",
            '-Phase',
            "-Z''",
            'C',
            "C'",
            'Current',
            'Frequency',
            'Potential',
            'Time',
            'Y',
            "Y'",
            "Y''",
            'Z',
            "Z'",
        }


class TestMS:
    id = 'ms'
    kwargs = {
        'script': (
            'e\n'  # must start with e
            'var p\n'
            'var c\n'
            'set_pgstat_chan 0\n'
            'set_pgstat_mode 2\n'
            'cell_on\n'
            'meas_loop_ca p c 100m 200m 1000m\n'
            '    pck_start\n'
            '    pck_add p\n'
            '    pck_add c\n'
            '    pck_end\n'
            'endloop\n'
            '\n'  # must end with 2 newlines
        )
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset
        assert len(dataset) == 2

        assert dataset.array_names == {'AppliedPotential1_1', 'Current1_1'}
        assert dataset.array_quantities == {'Current', 'Potential'}


class TestMM:
    id = 'mm'
    kwargs = {
        'cycles': 2,
        'interval_time': 0.02,
        'stages': [
            {
                'type': 'ConstantE',
                'current_limits': {'max': 10.0, 'min': 1},
                'potential': 0.5,
                'run_time': 0.1,
            },
            {
                'type': 'ConstantI',
                'potential_limits': {'max': 1, 'min': -1},
                'current': 1.0,
                'applied_current_range': 3,
                'run_time': 0.1,
            },
            {
                'type': 'SweepE',
                'begin_potential': -0.5,
                'end_potential': 0.5,
                'step_potential': 0.25,
                'scanrate': 20.0,
            },
            {'type': 'OpenCircuit', 'run_time': 0.1},
            {
                'type': 'Impedance',
                'run_time': 0.1,
                'dc_potential': 0.0,
                'ac_potential': 0.01,
                'min_sampling_time': 0.0,
                'max_equilibration_time': 5.0,
            },
        ],
    }

    @pytest.mark.instrument
    def test_measurement(self, manager):
        method = BaseTechnique._registry[self.id].from_dict(self.kwargs)
        measurement = manager.measure(method)

        assert measurement
        assert isinstance(measurement, ps.data.Measurement)

        for curve in measurement.curves:
            assert curve.n_points > 1

        dataset = measurement.dataset

        assert len(dataset) == 4

        assert dataset.array_names == {'charge', 'current', 'potential', 'time'}
        assert dataset.array_quantities == {'Charge', 'Current', 'Potential', 'Time'}

        eis = measurement.eis_data
        assert len(eis) == 2

        eis_dataset = eis[0].dataset

        assert eis_dataset.array_names == {
            'Capacitance',
            "Capacitance'",
            "Capacitance''",
            'Eac',
            'Frequency',
            'Iac',
            'Idc',
            'Phase',
            'Y',
            'YIm',
            'YRe',
            'Z',
            'ZIm',
            'ZRe',
            'mEdc',
            'miDC',
            'potential',
            'time',
        }
        assert eis_dataset.array_quantities == {
            "-C''",
            '-Phase',
            "-Z''",
            'C',
            "C'",
            'Current',
            'Frequency',
            'Potential',
            'Time',
            'Y',
            "Y'",
            "Y''",
            'Z',
            "Z'",
        }


@pytest.mark.parametrize(
    'method',
    (
        TestCV,
        TestFCV,
        TestLSV,
        TestACV,
        TestSWV,
        TestCP,
        TestSCP,
        TestLSP,
        TestOCP,
        TestCA,
        TestFAM,
        TestDPV,
        TestPAD,
        TestMPAD,
        TestNPV,
        TestMA,
        TestMP,
        TestCC,
        TestEIS,
        TestFIS,
        TestGIS,
        TestFGIS,
        TestMS,
        TestMM,
    ),
)
def test_params_round_trip(method):
    params = BaseTechnique._registry[method.id].from_dict(method.kwargs)

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, f'{method.id}.psmethod')
        ps.save_method_file(path, params)
        new_params = ps.load_method_file(path)

    assert new_params == params
