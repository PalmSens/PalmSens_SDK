from dataclasses import dataclass

from PalmSens import Method as PSMethod

from ._shared import (
    convert_bool_list_to_base2,
    set_extra_value_mask,
)
from .scan_method import ScanMethodParameters


@dataclass
class PotentialMethodParameters(ScanMethodParameters):
    """Create a Potential method parameters.

    Attributes
    ----------
    record_auxiliary_input: bool
        Record auxiliary input (default: False)
    record_cell_potential: bool
        Record cell potential (default: False) [counter electrode vs ground]
    record_we_potential: bool
        Record applied working electrode potential (default: False) [reference electrode vs ground]

    use_limit_current_max: bool
        Use limit current max (default: False).
        This will reverse the scan instead of aborting measurement
    limit_current_max: float
        Limit current max in µA (default: 0.0)
    use_limit_current_min: bool
        Use limit current min (default: False)
        This will reverse the scan instead of aborting measurement
    limit_current_min: float
        Limit current min in µA (default: 0.0)

    use_ir_compensation: bool
        Enable iR compensation
    ir_compensation: float
        Set the iR compensation in Ω (default: 0.0)

    trigger_at_equilibration: bool
        Enable trigger at equilibration (default: False)
    trigger_at_equilibration_lines: tuple[bool, bool, bool, bool]
        Enable trigger at equilibration lines (default: [False, False, False, False])
        Line order: d0 high, d1 high, d2 high, d3 high
    trigger_at_measurement: bool
        Enable trigger at measurement (default: False)
    trigger_at_measurement_lines: tuple[bool, bool, bool, bool]
        Enable trigger at measurement lines (default: [False, False, False, False])
        Line order: d0 high, d1 high, d2 high, d3 high

    """

    # record extra value settings
    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_potential: bool = False

    # limit settings
    use_limit_current_max: bool = False
    limit_current_max: float = 0.0  # µA
    use_limit_current_min: bool = False
    limit_current_min: float = 0.0  # µA

    # iR compensation settings
    use_ir_compensation: bool = False
    ir_compensation: float = 0.0  # Ω

    # set trigger settings
    trigger_at_equilibration: bool = False
    trigger_at_equilibration_lines: tuple[bool, bool, bool, bool] = (False, False, False, False)

    def update_dotnet_method(self, *, dotnet_method):
        super().update_dotnet_method(dotnet_method=dotnet_method)

        # Set the versus OCP settings for a given method
        dotnet_method.OCPmode = self.versus_ocp_mode
        dotnet_method.OCPMaxOCPTime = self.versus_ocp_max_ocp_time
        dotnet_method.OCPStabilityCriterion = self.versus_ocp_stability_criterion

        # Set the bipot settings for a given method
        dotnet_method.BiPotModePS = PSMethod.EnumPalmSensBipotMode(self.bipot_mode)
        dotnet_method.BiPotPotential = self.bipot_potential

        # Set the autoranging bipot current for a given method
        dotnet_method.BipotRanging.MaximumCurrentRange = self.bipot_current_range_max
        dotnet_method.BipotRanging.MinimumCurrentRange = self.bipot_current_range_min
        dotnet_method.BipotRanging.StartCurrentRange = self.bipot_current_range_start

        set_extra_value_mask(
            dotnet_method,
            enable_bipot_current=self.enable_bipot_current,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_potential=self.record_we_potential,
        )

        # Set the post measurement settings for a given method
        dotnet_method.CellOnAfterMeasurement = self.cell_on_after_measurement
        dotnet_method.StandbyPotential = self.cell_on_after_measurement_potential

        # Set the limit settings for a given method
        dotnet_method.UseLimitMaxValue = self.use_limit_current_max
        dotnet_method.LimitMaxValue = self.limit_current_max
        dotnet_method.UseLimitMinValue = self.use_limit_current_min
        dotnet_method.LimitMinValue = self.limit_current_min

        # Set the iR drop compensation settings for a given method
        dotnet_method.UseIRDropComp = self.use_ir_compensation
        dotnet_method.IRDropCompRes = self.ir_compensation

        # Set the trigger at equilibration settings for a given method
        dotnet_method.UseTriggerOnEquil = self.trigger_at_equilibration
        dotnet_method.TriggerValueOnEquil = convert_bool_list_to_base2(
            self.trigger_at_equilibration_lines
        )

        # Set the trigger at measurement settings for a given method
        dotnet_method.UseTriggerOnStart = self.trigger_at_measurement
        dotnet_method.TriggerValueOnStart = convert_bool_list_to_base2(
            self.trigger_at_measurement_lines
        )

    def to_dotnet_method(self):
        """Convert parameters to dotnet method."""
        raise NotImplementedError
