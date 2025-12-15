from __future__ import annotations

import PalmSens

import pypalmsens as ps
from pypalmsens._methods.techniques2 import CurrentRange, CyclicVoltammetry


def test_cv():
    cv = CyclicVoltammetry()

    m = cv._to_psmethod()
    assert isinstance(m, PalmSens.Method)
    assert m.MethodID == 'cv'


def test_cv_current_range():
    cv = CyclicVoltammetry(
        current_range={
            'min': ps.settings.CURRENT_RANGE.cr_10_uA,
            'max': ps.settings.CURRENT_RANGE.cr_10_mA,
            'start': ps.settings.CURRENT_RANGE.cr_1_mA,
        }
    )

    assert isinstance(cv.current_range, CurrentRange)
    assert cv.current_range.min.name == 'cr_10_uA'
    assert cv.current_range.max.name == 'cr_10_mA'
    assert cv.current_range.start.name == 'cr_1_mA'

    m = cv._to_psmethod()

    assert m.Ranging.MinimumCurrentRange.ToString() == '10 uA'
    assert m.Ranging.MaximumCurrentRange.ToString() == '10 mA'
    assert m.Ranging.StartCurrentRange.ToString() == '1 mA'
