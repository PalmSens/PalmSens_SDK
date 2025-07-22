from dataclasses import dataclass

import PalmSens
from PalmSens import Method as PSMethod
from PalmSens.Techniques import CyclicVoltammetry as PSCyclicVoltammetry

from ._shared import get_current_range
from .potential_method import PotentialMethodParameters


@dataclass
class AutorangingCurrentSettings:
    """Set the autoranging current for a given method.

    Attributes
    ----------
    current_range_max: int
        Maximum current range (default: 10 mA).
        Use `get_current_range()` to get the range.
    current_range_min: int
        Minimum current range (default: 1 µA).
        Use `get_current_range()` to get the range.
    current_range_start: int
         Start current range (default: 100 µA).
         Use `get_current_range()` to get the range.
    """

    current_range_max: int = get_current_range(8)
    current_range_min: int = get_current_range(4)
    current_range_start: int = get_current_range(6)

    def add_to_object(self, obj):
        obj.Ranging.MaximumCurrentRange = self.current_range_max
        obj.Ranging.MinimumCurrentRange = self.current_range_min
        obj.Ranging.StartCurrentRange = self.current_range_start


@dataclass
class AutorangingBipotCurrentSettings:
    """Set the autoranging bipot current for a given method.

    Attributes
    ----------

    """


@dataclass
class AutorangingPotentialSettings: ...


@dataclass
class PretreatmentSettings:
    """Set the pretreatment settings for a given method.

    Attributes
    ----------
    deposition_potential: float
        Deposition potential in V (default: 0.0)
    deposition_time: float
        Deposition time in s (default: 0.0)
    conditioning_potential: float
        Conditioning potential in V (default: 0.0)
    conditioning_time: float
        Conditioning time in s (default: 0.0)
    """

    deposition_potential: float = 0.0
    deposition_time: float = 0.0
    conditioning_potential: float = 0.0
    conditioning_time: float = 0.0

    def add_to_object(self, obj):
        obj.DepositionPotential = self.deposition_potential
        obj.DepositionTime = self.deposition_time
        obj.ConditioningPotential = self.conditioning_potential
        obj.ConditioningTime = self.conditioning_time


@dataclass
class VersusOcpSettings:
    """Set the versus OCP settings for a given method.

    Attributes
    ----------
    versus_ocp_mode: int
        Set versus OCP mode.
            0 = disable versus OCP
            1 = vertex 1 potential
            2 = vertex 2 potential
            3 = vertex 1 & 2 potential
            4 = begin potential
            5 = begin & vertex 1 potential
            6 = begin & vertex 2 potential
            7 = begin & vertex 1 & 2 potential
    versus_ocp_max_ocp_time: int
        Maximum OCP time in s (default: 20.0)
    versus_ocp_stability_criterion: int = 0
        Stability criterion in mV/s (default: 0.0)
            0 = no stability criterion
            > 0 is stability threshold potential/time (mV/s)
    """

    versus_ocp_mode: int = 0
    versus_ocp_max_ocp_time: float = 20.0  # Time (s)
    versus_ocp_stability_criterion: int = 0

    def add_to_object(self, *, obj):
        obj.OCPmode = self.versus_ocp_mode
        obj.OCPMaxOCPTime = self.versus_ocp_max_ocp_time
        obj.OCPStabilityCriterion = self.versus_ocp_stability_criterion


@dataclass
class BipotSettings:
    """Set the bipot settings for a given method.

    Attributes
    ----------
    enable_bipot_current: bool
        Enable bipotential current (default: False)
    bipot_mode: int
        Set the bipotential mode, 0 = constant, 1 = offset (default: 0)
    bipot_potential: float
        Set the bipotential in V (default: 0.0)
    bipot_current_range_max: int
        Maximum bipotential current range (default: 10 mA).
        Use `get_current_range()` to get the range.
    bipot_current_range_min: int
        Minimum bipotential current range (default: 1 µA).
        Use `get_current_range()` to get the range.
    bipot_current_range_start: int
        Start bipotential current range (default: 100 µA).
        Use `get_current_range()` to get the range.
    """

    enable_bipot_current: bool = False
    bipot_mode: int = 0
    bipot_potential: float = 0.0  # V
    bipot_current_range_max: int = get_current_range(8)
    bipot_current_range_min: int = get_current_range(4)
    bipot_current_range_start: int = get_current_range(6)

    def add_to_object(self, obj):
        obj.BiPotModePS = PalmSens.Method.EnumPalmSensBipotMode(self.bipot_mode)
        obj.BiPotPotential = self.bipot_potential
        obj.BipotRanging.MaximumCurrentRange = self.bipot_current_range_max
        obj.BipotRanging.MinimumCurrentRange = self.bipot_current_range_min
        obj.BipotRanging.StartCurrentRange = self.bipot_current_range_start


@dataclass
class ExtraValueMask: ...


@dataclass
class PostMeasurementSettings:
    """Set the post measurement settings for a given method.

    Attributes
    ----------
    cell_on_after_measurement: bool
        Cell on after measurement (default: False)
    cell_on_after_measurement_potential: float
        Cell on after measurement potential in V (default: 0.0)
    """

    cell_on_after_measurement: bool = False
    cell_on_after_measurement_potential: float = 0.0  # V

    def add_to_object(self, obj):
        obj.CellOnAfterMeasurement = self.cell_on_after_measurement
        obj.StandbyPotential = self.cell_on_after_measurement_potential


@dataclass
class CurrentLimitSettings:
    """Set the limit settings for a given method.

    Attributes
    ----------
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

    """

    use_limit_current_max: bool = False
    limit_current_max: float = 0.0  # µA
    use_limit_current_min: bool = False
    limit_current_min: float = 0.0  # µA

    def add_to_object(self, obj):
        obj.UseLimitMaxValue = self.use_limit_current_max
        obj.LimitMaxValue = self.limit_current_max
        obj.UseLimitMinValue = self.use_limit_current_min
        obj.LimitMinValue = self.limit_current_min


@dataclass
class PotentialLimitSettings:
    """Set the limit settings for a given method.

    Attributes
    ----------
    use_limit_potential_max: bool
        Use limit potential max (default: False).
    limit_potential_max: float
        Limit potential max in V (default: 0.0)
    use_limit_potential_min: bool
        Use limit potential min (default: False)
    limit_potential_min: float
        Limit potential min in V (default: 0.0)

    """

    use_limit_potential_max: bool = False
    limit_potential_max: float = 0.0  # V
    use_limit_potential_min: bool = False
    limit_potential_min: float = 0.0  # V

    def add_to_object(self, obj):
        obj.UseLimitMaxValue = self.use_limit_potential_max
        obj.LimitMaxValue = self.limit_potential_max
        obj.UseLimitMinValue = self.use_limit_potential_min
        obj.LimitMinValue = self.limit_potential_min


@dataclass
class ChargeLimitSettings:
    """Set the charge limit settings for a given method.

    Attributes
    ----------
    use_limit_charge_max: bool
        Use limit charge max (default: False).
    limit_charge_max: float
        Limit charge max in µC (default: 0.0)
    use_limit_charge_min: bool
        Use limit charge min (default: False)
    limit_charge_min: float
        Limit charge min in µC (default: 0.0)

    """

    use_limit_charge_max: bool = False
    limit_charge_max: float = 0.0  # in µC
    use_limit_charge_min: bool = False
    limit_charge_min: float = 0.0  # in µC

    def add_to_object(self, obj):
        obj.UseChargeLimitMax = self.use_limit_charge_max
        obj.ChargeLimitMax = self.limit_charge_max
        obj.UseChargeLimitMin = self.use_limit_charge_min
        obj.ChargeLimitMin = self.limit_charge_min


@dataclass
class IrDropCompensationSettings:
    """Set the iR drop compensation settings for a given method.

    Attributes
    ----------
    use_ir_compensation: bool
        Enable iR compensation
    ir_compensation: float
        Set the iR compensation in Ω (default: 0.0)

    """

    use_ir_compensation: bool = False
    ir_compensation: float = 0.0  # Ω

    def add_to_object(self, obj):
        obj.UseIRDropComp = self.use_ir_compensation
        obj.IRDropCompRes = self.ir_compensation


@dataclass
class TriggerAtEquilibrationSettings:
    """Set the trigger at equilibration settings for a given method.

    Attributes
    ----------
    trigger_at_equilibration: bool
        Enable trigger at equilibration (default: False)
    trigger_at_equilibration_lines: tuple[bool, bool, bool, bool]
        Enable trigger at equilibration lines (default: [False, False, False, False])
        Line order: d0 high, d1 high, d2 high, d3 high

    """

    trigger_at_equilibration: bool = False
    trigger_at_equilibration_lines: tuple[bool, bool, bool, bool] = (False, False, False, False)

    def add_to_object(self, obj):
        obj.UseTriggerOnEquil = self.trigger_at_equilibration
        lines = 0
        for i, set_high in enumerate(self.trigger_at_equilibration_lines):
            if set_high:
                lines = lines | (1 << i)
        obj.TriggerValueOnEquil = lines


@dataclass
class TriggerAtMeasurementSettings:
    """Set the trigger at measurement settings for a given method.

    Attributes
    ----------
    trigger_at_measurement: bool
        Enable trigger at measurement (default: False)
    trigger_at_measurement_lines: tuple[bool, bool, bool, bool]
        Enable trigger at measurement lines (default: [False, False, False, False])
        Line order: d0 high, d1 high, d2 high, d3 high

    """

    trigger_at_measurement: bool = False
    trigger_at_measurement_lines: tuple[bool, bool, bool, bool] = (False, False, False, False)

    def add_to_object(self, obj):
        obj.UseTriggerOnStart = self.trigger_at_measurement
        lines = 0
        for i, set_high in enumerate(self.trigger_at_measurement_lines):
            if set_high:
                lines = lines | (1 << i)
        obj.TriggerValueOnStart = lines


@dataclass
class MultiplexerSettings: ...


@dataclass
class FilterSettings: ...


@dataclass
class CyclicVoltammetryParameters(PotentialMethodParameters):
    """Create cyclic voltammetry method parameters.

    Attributes
    ----------
    equilibration_time : float
        Equilibration time in s (default: 0.0)
    begin_potential: float
        Begin potential in V (default: -0.5)
    vertex1_potential: float
        Vertex 1 potential in V (default: 0.5)
    vertex2_potential: float
        Vertex 2 potential in V (default: -0.5)
    step_potential: float
        Step potential in V (default: 0.1)
    scanrate: float
        Scan rate in V/s (default: 1.0)
    n_scans: float
        Number of scans (default: 1)
    """

    # cyclic voltammetry settings
    equilibration_time: float = 0.0  # Time (s)
    begin_potential: float = -0.5  # potential (V)
    vertex1_potential: float = 0.5  # potential (V)
    vertex2_potential: float = -0.5  # potential (V)
    step_potential: float = 0.1  # potential (V)
    scanrate: float = 1.0  # potential/time (V/s)
    n_scans: float = 1  # number of cycles

    def update_dotnet_method(self, *, dotnet_method):
        """Update method with cyclic voltammetry settings."""
        super().update_dotnet_method(dotnet_method=dotnet_method)

        dotnet_method.BeginPotential = self.begin_potential
        dotnet_method.Vtx1Potential = self.vertex1_potential
        dotnet_method.Vtx2Potential = self.vertex2_potential
        dotnet_method.StepPotential = self.step_potential
        dotnet_method.Scanrate = self.scanrate
        dotnet_method.nScans = self.n_scans

    def to_dotnet_method(self):
        """Convert parameters to dotnet method."""
        obj = PSCyclicVoltammetry()

        self.update_dotnet_method(dotnet_method=obj)

        return obj

    @classmethod
    def from_dotnet_method(cls, dotnet_method: PSMethod) -> 'CyclicVoltammetryParameters':
        """Generate parameters from dotnet method."""
        raise NotImplementedError


def cyclic_voltammetry(**kwargs):
    """Alias for CyclicVoltammetry for backwards compatibility"""
    cv = CyclicVoltammetryParameters(**kwargs)
    return cv.to_dotnet_method()
