from typing import Any

from PalmSens import Method as PSMethod


def method_ids() -> list[str]:
    """Return list of all possible method ids."""
    return list(PSMethod.MethodIds)


def method_ids_by_technique_id() -> dict[int, list[str]]:
    """Unique id for method."""

    return {k: list(v) for k, v in dict(PSMethod.MethodIdsByTechniqueId).items()}


class Method:
    def __init__(self, *, dotnet_method):
        self.dotnet_method = dotnet_method

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name}, id={self.id!r})'

    def id(self) -> str:
        """Unique id for method."""
        return self.dotnet_method.MethodID

    def name(self) -> str:
        """Name for the technique."""
        return self.dotnet_method.Name

    def short_name(self) -> str:
        """Short name for the technique."""
        return self.dotnet_method.Name

    def properties(self) -> dict[str, Any]:
        """Return dictionary with method properties."""
        obj = self.dotnet_method
        return {
            'analyte_name': list(obj.AnalyteName),
            'analyte_peak_autodetect': list(obj.AnalytePeakAutodetect),
            'area': obj.Area,
            'ba': obj.Ba,
            'bandwidth': obj.Bandwidth,
            'bc': obj.Bc,
            'begin_potential': obj.BeginPotential,
            'bipot_cr': obj.BiPotCR,
            'bipot_potential': obj.BiPotPotential,
            'bipot_mode_ps': obj.BipotModePS,
            'bipot_ranging': obj.BipotRanging,  # object
            'blank_type': obj.BlankType,
            'cell_on_after_measurement': obj.CellOnAfterMeasurement,
            'cell_volume': obj.CellVolume,
            'concentration_unit': obj.ConcentrationUnit,
            'conditioning_potential': obj.ConditioningPotential,
            'conditioning_time': obj.ConditioningTime,
            'default_bandwidth': obj.DefaultBandwidth,
            'default_x_array_type_bipot_potential': obj.DefaultXArrayTypeBipotPotential,
            'default_x_axis': obj.DefaultXAxis,
            'default_x_unit': obj.DefaultXUnit,
            'default_y_axis': obj.DefaultYAxis,
            'default_y_unit': obj.DefaultYUnit,
            'density': obj.Density,
            'deposition_potential': obj.DepositionPotential,
            'deposition_time': obj.DepositionTime,
            'determination': obj.Determination,
            'e_peak_left': list(obj.EPeakLeft),
            'e_peak_right': list(obj.EPeakRight),
            'e_peaks': list(obj.EPeaks),
            'e_pretreat': list(obj.EPretreat),
            'end_potential': obj.EndPotential,
            'enum_palm_sens_bipot_mode': obj.EnumPalmSensBipotMode,
            'equilibration_time': obj.EquilibrationTime,
            'extra_value_msk': obj.ExtraValueMsk,
            'ir_drop_comp_res': obj.IRDropCompRes,
            'is_main_we': obj.IsMainWE,
            'is_versus_ocp': obj.IsVersusOCP,
            'limit_max_value': obj.LimitMaxValue,
            'limit_min_value': obj.LimitMinValue,
            'max_mux_channel_selected': obj.MaxMuxChannelSelected,
            'method_filename': obj.MethodFilename,
            'method_id': obj.MethodID,
            'method_is_galvanostatic': obj.MethodIsGalvanostatic,
            'min_peak_height': obj.MinPeakHeight,
            'min_peak_width': obj.MinPeakWidth,
            'multiplex_cycles': obj.MultiplexCycles,
            'mux_method': obj.MuxMethod,
            'mux_no_time_reset_for_next_channel': obj.MuxNoTimeResetForNextChannel,
            'mux_settings': str(obj.MuxSett),  # object
            'name': obj.Name,
            'note': obj.Note,
            'ocp_max_ocp_time': obj.OCPMaxOCPTime,
            'ocp_stability_criterion': obj.OCPStabilityCriterion,
            'ocp_mode': obj.OCPmode,
            'override_bandwidth': obj.OverrideBandwidth,
            'override_pg_stat_mode': obj.OverridePGStatMode,
            'override_potential_range': obj.OverridePotentialRange,
            'override_potential_range_max': obj.OverridePotentialRangeMax,
            'override_potential_range_min': obj.OverridePotentialRangeMin,
            'override': obj.Override,
            'pg_stat_mode': obj.PGStatMode,
            'peak_overlap': obj.PeakOverlap,
            'peak_value': obj.PeakValue,
            'peak_window': obj.PeakWindow,
            'poly_em_stat': obj.PolyEmStat,  # object
            'poly_stat_mode': obj.PolyStatMode,
            'power_freq': obj.PowerFreq,
            'power_line_period': obj.PowerLinePeriod,
            'pret_limit_max_value': obj.PretLimitMaxValue,
            'pret_limit_min_value': obj.PretLimitMinValue,
            'pretreatment_duration': obj.PretreatmentDuration,
            'ranging': obj.Ranging,  # object
            'ranging_potential': obj.RangingPotential,  # object
            'ranging_type': str(obj.RangingType),
            'record_ce': obj.RecordCE,
            'reference_electrode_name': obj.ReferenceElectrodeName,
            'reference_electrode_offset': obj.ReferenceElectrodeOffset,
            'se_2_extra_value_channel_names': {
                row.Key: row.Value for row in obj.SE2ExtraValueChannelNames
            },
            'se_2_versus_x_channel_names': {
                row.Key: row.Value for row in obj.SE2VersusXChannelNames
            },
            'se_2_vs_x_channel': obj.SE2vsXChannel,
            'sample_volume': obj.SampleVolume,
            'scanrate': obj.Scanrate,
            'selected_potentiostat_channel': str(obj.SelectedPotentiostatChannel),
            'short_name': obj.ShortName,
            'smooth_level': obj.SmoothLevel,
            'solution_nr': list(obj.SolutionNr),
            'standard_concentration': list(obj.StandardConcentration),
            'standards_values': str(obj.StandardsValues),
            'standby_potential': obj.StandbyPotential,
            'standby_time': obj.StandbyTime,
            'step_potential': obj.StepPotential,
            'supports_corrosion': obj.SupportsCorrosion,
            'supports_determination': obj.SupportsDetermination,
            'supports_hold_during_measurement': obj.SupportsHoldDuringMeasurement,
            'supports_ir_drop_comp': obj.SupportsIRDropComp,
            'technique_number': obj.TechniqueNumber,
            'trigger_delay_period': obj.TriggerDelayPeriod,
            'trigger_value_on_delay': obj.TriggerValueOnDelay,
            'trigger_value_on_equil': obj.TriggerValueOnEquil,
            'trigger_value_on_start': obj.TriggerValueOnStart,
            # 'use_alternative_signal_train': obj.UseAlternativeSignalTrain,  # not availabe for CV
            'use_hw_sync': obj.UseHWSync,
            'use_ir_drop_comp': obj.UseIRDropComp,
            'use_limit_max_value': obj.UseLimitMaxValue,
            'use_limit_min_value': obj.UseLimitMinValue,
            'use_mux_channel': list(obj.UseMuxChannel),
            'use_pret_limit_max_value': obj.UsePretLimitMaxValue,
            'use_pret_limit_min_value': obj.UsePretLimitMinValue,
            'use_stirrer': obj.UseStirrer,
            'use_trigger_on_delay': obj.UseTriggerOnDelay,
            'use_trigger_on_equil': obj.UseTriggerOnEquil,
            'use_trigger_on_start': obj.UseTriggerOnStart,
            'versus_ocp_begin_potential': obj.VersusOCPBeginPotential,
            'versus_ocp_end_potential': obj.VersusOCPEndPotential,
            'versus_ocp_vtx_1_potential': obj.VersusOCPVtx1Potential,
            'versus_ocp_vtx_2_potential': obj.VersusOCPVtx2Potential,
            'view_bottom': obj.ViewBottom,
            'view_left': obj.ViewLeft,
            'view_right': obj.ViewRight,
            'view_top': obj.ViewTop,
            'volume_concentration': list(obj.VolumeConcentration),
            'vs_prev_ei': obj.VsPrevEI,
            'vtx_1_potential': obj.Vtx1Potential,
            'vtx_2_potential': obj.Vtx2Potential,
            'weight': obj.Weight,
            'x_direction': str(obj.XDirection),
            'x_left': obj.XLeft,
            'x_right': obj.XRight,
            'y_bottom': obj.YBottom,
            'y_direction': str(obj.YDirection),
            'y_top': obj.YTop,
            'n_avg_scans': obj.nAvgScans,
            'n_eq_scans': obj.nEqScans,
            'n_oc_pparameters': obj.nOCPparameters,
            'n_points': obj.nPoints,
            'n_scans': obj.nScans,
            't_pretreat': list(obj.tPretreat),
        }
