import pytest
from PalmSens import AutoRanging, AutoRangingPotential

from pspython.methods import techniques
from pspython.methods._shared import CURRENT_RANGE, POTENTIAL_RANGE


def test_current_range():
    assert CURRENT_RANGE(0).to_psobj().ToString() == '100 pA'
    assert CURRENT_RANGE(30).to_psobj().ToString() == '1 A'
    assert CURRENT_RANGE(26).to_psobj().ToString() == '63 uA'

    with pytest.raises(ValueError):
        CURRENT_RANGE(-1)
        CURRENT_RANGE(100)


def test_potential_range():
    assert POTENTIAL_RANGE.pr_1_mV.to_psobj().ToString() == '1 mV'
    assert POTENTIAL_RANGE.pr_100_mV.to_psobj().ToString() == '100 mV'
    assert POTENTIAL_RANGE.pr_10_mV.to_psobj().ToString() == '1 V'

    with pytest.raises(ValueError):
        POTENTIAL_RANGE(-1)
        POTENTIAL_RANGE(100)


def test_method_current_range():
    crmin = CURRENT_RANGE.cr_100_nA
    crmax = CURRENT_RANGE.cr_1_mA
    crstart = CURRENT_RANGE.cr_100_uA

    method = techniques.CyclicVoltammetryParameters(
        current_range_min=crmin,
        current_range_max=crmax,
        current_range_start=crstart,
    )
    obj = method.to_psobj()

    supported_ranges = obj.Ranging.SupportedCurrentRanges

    assert crmin in supported_ranges
    assert crmax in supported_ranges
    assert crstart in supported_ranges

    assert obj.Ranging.MinimumCurrentRange.Description == '100 nA'
    assert obj.Ranging.MaximumCurrentRange.Description == '1 mA'
    assert obj.Ranging.StartCurrentRange.Description == '100 uA'


def test_method_potential_range():
    potmin = POTENTIAL_RANGE.pr_1_mV
    potmax = POTENTIAL_RANGE.pr_100_mV
    potstart = POTENTIAL_RANGE.pr_10_mV

    method = techniques.ChronopotentiometryParameters(
        potential_range_min=potmin,
        potential_range_max=potmax,
        potential_range_start=potstart,
    )
    obj = method.to_psobj()
    supported_ranges = obj.RangingPotential.SupportedPotentialRanges

    assert potmin in supported_ranges
    assert potmax in supported_ranges
    assert potstart in supported_ranges

    assert obj.RangingPotential.MinimumPotentialRange.Description == '1 mV'
    assert obj.RangingPotential.MaximumPotentialRange.Description == '100 mV'
    assert obj.RangingPotential.StartPotentialRange.Description == '10 mV'


def test_method_current_range_clipping():
    ranging = AutoRanging(
        minRange=CURRENT_RANGE.cr_100_nA.to_psobj(),
        maxRange=CURRENT_RANGE.cr_1_mA.to_psobj(),
        startRange=CURRENT_RANGE.cr_100_uA.to_psobj(),
    )

    cr_outside = CURRENT_RANGE.cr_5_mA.to_psobj()
    assert cr_outside not in ranging.SupportedCurrentRanges

    # Check that start range gets clipped to max range
    ranging.StartCurrentRange = cr_outside
    assert ranging.StartCurrentRange.Description == '1 mA'

    # Check that max range gets clipped to nearest supported range
    ranging.MaximumCurrentRange = cr_outside
    assert ranging.MaximumCurrentRange.Description == '10 mA'


def test_method_potential_range_clipping():
    ranging = AutoRangingPotential(
        minRange=POTENTIAL_RANGE.pr_1_mV.to_psobj(),
        maxRange=POTENTIAL_RANGE.pr_100_mV.to_psobj(),
        startRange=POTENTIAL_RANGE.pr_10_mV.to_psobj(),
    )

    pot_outside = POTENTIAL_RANGE.pr_500_mV.to_psobj()
    assert pot_outside not in ranging.SupportedPotentialRanges

    # Check that start range gets clipped to max range
    ranging.StartPotentialRange = pot_outside
    assert ranging.StartPotentialRange.Description == '100 mV'

    # Check that max range gets clipped to nearest supported range
    ranging.MaximumPotentialRange = pot_outside
    assert ranging.MaximumPotentialRange.Description == '1 V'
