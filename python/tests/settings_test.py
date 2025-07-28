from dataclasses import asdict

from PalmSens import Techniques

from pspython.methods import settings
from pspython.methods._shared import (
    get_current_range,
    get_extra_value_mask,
    get_mux8r2_settings,
    get_potential_range,
    set_extra_value_mask,
)


def test_set_extra_value_mask():
    obj = Techniques.CyclicVoltammetry()
    assert obj.ExtraValueMsk.value__ == 0

    set_extra_value_mask(
        obj=obj,
        record_auxiliary_input=True,
        record_cell_potential=True,
        record_we_potential=True,
    )
    assert obj.ExtraValueMsk.value__ == 274

    dct = get_extra_value_mask(obj)

    assert dct['record_auxiliary_input']
    assert dct['record_cell_potential']
    assert dct['record_we_potential']
    assert not dct['enable_bipot_current']
    assert not dct['record_forward_and_reverse_currents']
    assert not dct['record_we_current']

    set_extra_value_mask(
        obj=obj,
        enable_bipot_current=True,
        record_forward_and_reverse_currents=True,
        record_we_current=True,
        record_we_current_range=get_current_range(1),
    )
    assert obj.ExtraValueMsk.value__ == 101

    dct = get_extra_value_mask(obj)

    assert dct['enable_bipot_current']
    assert dct['record_forward_and_reverse_currents']
    assert dct['record_we_current']
    assert not dct['record_auxiliary_input']
    assert not dct['record_cell_potential']
    assert not dct['record_we_potential']

    # this is not an extra value mask property
    assert 'record_we_current_range' not in dct


def test_AutorangingCurrentSettings():
    obj = Techniques.CyclicVoltammetry()
    params = settings.AutorangingCurrentSettings(
        current_range_max=get_current_range(6),
        current_range_min=get_current_range(3),
        current_range_start=get_current_range(5),
    )
    params.update_psobj(obj=obj)

    assert obj.Ranging.MaximumCurrentRange.Description == '100 uA'
    assert obj.Ranging.MinimumCurrentRange.Description == '100 nA'
    assert obj.Ranging.StartCurrentRange.Description == '10 uA'

    new_params = settings.AutorangingCurrentSettings()
    new_params.update_params(obj=obj)

    assert new_params.current_range_max == get_current_range(6)
    assert new_params.current_range_min == get_current_range(3)
    assert new_params.current_range_start == get_current_range(5)


def test_AutorangingPotentialSettings():
    obj = Techniques.Potentiometry()
    params = settings.AutorangingPotentialSettings(
        potential_range_max=get_potential_range(4),
        potential_range_min=get_potential_range(0),
        potential_range_start=get_potential_range(1),
    )
    params.update_psobj(obj=obj)
    assert obj.RangingPotential.MaximumPotentialRange.Description == '100 mV'
    assert obj.RangingPotential.MinimumPotentialRange.Description == '1 mV'
    assert obj.RangingPotential.StartPotentialRange.Description == '10 mV'

    new_params = settings.AutorangingPotentialSettings()
    new_params.update_params(obj=obj)

    assert new_params.potential_range_max == get_potential_range(4)
    assert new_params.potential_range_min == get_potential_range(0)
    assert new_params.potential_range_start == get_potential_range(1)


def test_PretreatmentSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'deposition_potential': 12,
        'deposition_time': 34,
        'conditioning_potential': 56,
        'conditioning_time': 78,
    }

    params = settings.PretreatmentSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.DepositionPotential == 12
    assert obj.DepositionTime == 34
    assert obj.ConditioningPotential == 56
    assert obj.ConditioningTime == 78

    new_params = settings.PretreatmentSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_VersusOcpSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'versus_ocp_mode': 7,
        'versus_ocp_max_ocp_time': 200.0,
        'versus_ocp_stability_criterion': 123,
    }

    params = settings.VersusOcpSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.OCPmode == 7
    assert obj.OCPMaxOCPTime == 200
    assert obj.OCPStabilityCriterion == 123

    new_params = settings.VersusOcpSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_BipotSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'bipot_mode': 1,
        'bipot_potential': 10.0,
        'bipot_current_range_max': get_current_range(6),
        'bipot_current_range_min': get_current_range(2),
        'bipot_current_range_start': get_current_range(5),
    }

    params = settings.BipotSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.BiPotModePS == Techniques.CyclicVoltammetry.EnumPalmSensBipotMode(1)
    assert obj.BiPotPotential == 10.0
    assert obj.BipotRanging.MaximumCurrentRange.Description == '100 uA'
    assert obj.BipotRanging.MinimumCurrentRange.Description == '10 nA'
    assert obj.BipotRanging.StartCurrentRange.Description == '10 uA'

    new_params = settings.BipotSettings()
    new_params.update_params(obj=obj)

    assert new_params.bipot_mode == 1
    assert new_params.bipot_potential == 10.0
    assert new_params.bipot_current_range_max == get_current_range(6)
    assert new_params.bipot_current_range_min == get_current_range(2)
    assert new_params.bipot_current_range_start == get_current_range(5)


def test_PostMeasurementSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'cell_on_after_measurement': True,
        'cell_on_after_measurement_potential': 123,
    }

    params = settings.PostMeasurementSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.CellOnAfterMeasurement is True
    assert obj.StandbyPotential == 123

    new_params = settings.PostMeasurementSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_CurrentLimitSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'use_limit_current_max': True,
        'limit_current_max': 123.0,
        'use_limit_current_min': True,
        'limit_current_min': 678.0,
    }

    params = settings.CurrentLimitSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.UseLimitMaxValue is True
    assert obj.LimitMaxValue == 123.0
    assert obj.UseLimitMinValue is True
    assert obj.LimitMinValue == 678.0

    new_params = settings.CurrentLimitSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_PotentialLimitSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'use_limit_potential_max': True,
        'limit_potential_max': 123.0,
        'use_limit_potential_min': True,
        'limit_potential_min': 678.0,
    }

    params = settings.PotentialLimitSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.UseLimitMaxValue is True
    assert obj.LimitMaxValue == 123.0
    assert obj.UseLimitMinValue is True
    assert obj.LimitMinValue == 678.0

    new_params = settings.PotentialLimitSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_ChargeLimitSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'use_limit_charge_max': True,
        'limit_charge_max': 123.0,
        'use_limit_charge_min': True,
        'limit_charge_min': 678.0,
    }

    params = settings.ChargeLimitSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.UseChargeLimitMax is True
    assert obj.ChargeLimitMax == 123.0
    assert obj.UseChargeLimitMin is True
    assert obj.ChargeLimitMin == 678.0

    new_params = settings.ChargeLimitSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_IrDropCompensationSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'use_ir_compensation': True,
        'ir_compensation': 123.0,
    }

    params = settings.IrDropCompensationSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.UseIRDropComp is True
    assert obj.IRDropCompRes == 123

    new_params = settings.IrDropCompensationSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_TriggerAtEquilibrationSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'trigger_at_equilibration': True,
        'trigger_at_equilibration_lines': (True, False, True, True),
    }

    params = settings.TriggerAtEquilibrationSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.UseTriggerOnEquil is True
    assert obj.TriggerValueOnEquil == 13

    new_params = settings.TriggerAtEquilibrationSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_TriggerAtMeasurementSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'trigger_at_measurement': True,
        'trigger_at_measurement_lines': (True, True, False, True),
    }

    params = settings.TriggerAtMeasurementSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.UseTriggerOnStart is True
    assert obj.TriggerValueOnStart == 11

    new_params = settings.TriggerAtMeasurementSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_MultiplexerSettings():
    obj = Techniques.CyclicVoltammetry()

    mux_kwargs = {
        'connect_sense_to_working_electrode': True,
        'combine_reference_and_counter_electrodes': True,
        'use_channel_1_reference_and_counter_electrodes': True,
        'set_unselected_channel_working_electrode': 1,
    }

    kwargs = {
        'set_mux_mode': 0,
        'set_mux_channels': [True, False, True, False, True],
        'set_mux8r2_settings': get_mux8r2_settings(**mux_kwargs),
    }

    params = settings.MultiplexerSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert int(obj.MuxMethod) == 0
    for i, v in enumerate([True, False, True, False, True]):
        assert obj.UseMuxChannel[i] is v

    assert obj.MuxSett.ConnSEWE is True
    assert obj.MuxSett.ConnectCERE is True
    assert obj.MuxSett.CommonCERE is True
    assert int(obj.MuxSett.UnselWE) == 1

    new_params = settings.MultiplexerSettings()
    new_params.update_params(obj=obj)

    assert new_params.set_mux_mode == 0
    assert new_params.set_mux_channels == [True, False, True, False, True]
    assert new_params.set_mux8r2_settings == mux_kwargs


def test_FilterSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'dc_mains_filter': 60,
        'default_curve_post_processing_filter': 1,
    }

    params = settings.FilterSettings(**kwargs)
    params.update_psobj(obj=obj)

    assert obj.DCMainsFilter == 60
    assert obj.DefaultCurvePostProcessingFilter == 1

    new_params = settings.FilterSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs


def test_OtherSettings():
    obj = Techniques.CyclicVoltammetry()

    kwargs = {
        'save_on_internal_storage': True,
        'use_hardware_sync': True,
    }

    params = settings.OtherSettings(**kwargs)
    params.update_psobj(obj=obj)

    obj.SaveOnDevice = True
    obj.UseHWSync = True

    new_params = settings.OtherSettings()
    new_params.update_params(obj=obj)

    assert asdict(new_params) == kwargs
