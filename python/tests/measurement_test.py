from pathlib import Path

import pytest

from pspython.data.curve import Curve
from pspython.data.peak import Peak
from pspython.pspyfiles import load_session_file

DATA_FILE = Path(__file__).parents[1] / 'Demo CV DPV EIS IS-C electrode.pssession'


@pytest.fixture
def measurements():
    return load_session_file(
        str(DATA_FILE),
    )


def test_measurement_arrays(measurements):
    m = measurements[0]

    assert len(m.current_arrays[0]) == 219
    assert len(m.potential_arrays[0]) == 219
    assert len(m.time_arrays[0]) == 219

    assert len(m.freq_arrays) == 0
    assert len(m.zre_arrays) == 0
    assert len(m.zim_arrays) == 0
    assert len(m.aux_input_arrays) == 0

    peaks = m.peaks
    assert len(peaks) == 1
    assert isinstance(peaks[0], Peak)

    assert len(m.eis_fit) == 0

    curves = m.curves
    assert len(curves) == 1
    assert isinstance(curves[0], Curve)


def test_measurement_properties(measurements):
    m = measurements[0]

    assert m.title == 'Differential Pulse Voltammetry'
    assert isinstance(m.timestamp, str)

    breakpoint()
