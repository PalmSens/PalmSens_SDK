from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, ClassVar, Protocol, Type, runtime_checkable

import attrs
from PalmSens import Method as PSMethod
from PalmSens.Techniques.Impedance import enumFrequencyType, enumScanType

from . import settings
from ._shared import (
    CURRENT_RANGE,
    ELevel,
    get_extra_value_mask,
    set_extra_value_mask,
)
from .settings import (
    AutorangingCurrentSettings,
    AutorangingPotentialSettings,
    BipotSettings,
    ChargeLimitSettings,
    CommonSettings,
    CurrentLimitSettings,
    IrDropCompensationSettings,
    MultiplexerSettings,
    PeakSettings,
    PostMeasurementSettings,
    PotentialLimitSettings,
    PretreatmentSettings,
    SettingsType,
    TriggerAtEquilibrationSettings,
    TriggerAtMeasurementSettings,
    VersusOcpSettings,
)

if TYPE_CHECKING:
    from .method import Method


@runtime_checkable
class BaseConfig(Protocol):
    """Protocol to provide generic methods for parameters."""

    __attrs_attrs__: ClassVar[list[attrs.Attribute]] = []

    def to_psmethod(self):
        return parameters_to_psmethod(self)

    @staticmethod
    def from_psmethod(obj: PSMethod) -> BaseConfig:
        return psmethod_to_parameters(obj)

    @abstractmethod
    def update_psmethod(self, *, obj: PSMethod) -> None: ...

    @abstractmethod
    def update_params(self, *, obj: PSMethod) -> None: ...


def parameters_to_psmethod(params) -> Method:
    """Convert parameters to dotnet method."""
    psmethod = PSMethod.FromMethodID(params._id)

    params.update_psmethod(obj=psmethod)

    for attrib in attrs.fields(params):
        if isinstance(attrib.type, SettingsType):
            sett = getattr(params, attrib.name)
            sett.update_psmethod(obj=psmethod)

    return psmethod


def psmethod_to_parameters(psmethod: PSMethod) -> BaseConfig:
    """Generate parameters from dotnet method object."""
    id = psmethod.MethodID

    cls = ID_TO_PARAMETER_MAPPING[id]

    if cls is None:
        raise NotImplementedError(f'Mapping of {id} parameters is not implemented yet')

    new = cls()

    for attrib in new.__attrs_attrs__:
        if isinstance(attrib.type, SettingsType):
            sett = getattr(new, attrib.name)
            sett.update_params(obj=psmethod)

    return new


@attrs.define
class CyclicVoltammetry(BaseConfig):
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
    enable_bipot_current: bool
        Enable bipot current (default: False)
    record_auxiliary_input : bool
        Record auxiliary input (default: False)
    record_cell_potential : bool
        Record cell potential (default: False)
        Counter electrode vs ground.
    record_we_potential : bool
        Record applied working electrode potential (default: False)
        Reference electrode vs ground.
    """

    _id = 'cv'

    equilibration_time: float = 0.0
    begin_potential: float = -0.5
    vertex1_potential: float = 0.5
    vertex2_potential: float = -0.5
    step_potential: float = 0.1
    scanrate: float = 1.0
    n_scans: float = 1

    enable_bipot_current: bool = False
    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_potential: bool = False

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    versus_ocp: VersusOcpSettings = attrs.field(
        factory=VersusOcpSettings, converter=settings.to_VersusOcpSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    current_limits: CurrentLimitSettings = attrs.field(
        factory=CurrentLimitSettings, converter=settings.to_CurrentLimitSettings
    )
    ir_drop_compensation: IrDropCompensationSettings = attrs.field(
        factory=IrDropCompensationSettings, converter=settings.to_IrDropCompensationSettings
    )
    equilibrion_triggers: TriggerAtEquilibrationSettings = attrs.field(
        factory=TriggerAtEquilibrationSettings,
        converter=settings.to_TriggerAtEquilibrationSettings,
    )
    measurement_triggers: TriggerAtMeasurementSettings = attrs.field(
        factory=TriggerAtMeasurementSettings, converter=settings.to_TriggerAtMeasurementSettings
    )
    peaks: PeakSettings = attrs.field(factory=PeakSettings, converter=settings.to_PeakSettings)
    general: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with cyclic voltammetry settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.BeginPotential = self.begin_potential
        obj.Vtx1Potential = self.vertex1_potential
        obj.Vtx2Potential = self.vertex2_potential
        obj.StepPotential = self.step_potential
        obj.Scanrate = self.scanrate
        obj.nScans = self.n_scans

        set_extra_value_mask(
            obj=obj,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_potential=self.record_we_potential,
            enable_bipot_current=self.enable_bipot_current,
        )

    def update_params(self, *, obj):
        self.equilibration_time = obj.EquilibrationTime
        self.begin_potential = obj.BeginPotential
        self.vertex1_potential = obj.Vtx1Potential
        self.vertex2_potential = obj.Vtx2Potential
        self.step_potential = obj.StepPotential
        self.scanrate = obj.Scanrate
        self.n_scans = obj.nScans

        msk = get_extra_value_mask(obj)

        for key in (
            'record_auxiliary_input',
            'record_cell_potential',
            'record_we_potential',
            'enable_bipot_current',
        ):
            setattr(self, key, msk[key])


@attrs.define
class LinearSweepVoltammetry(BaseConfig):
    """Create linear sweep method parameters.

    Attributes
    ----------
    begin_potential : float
        Begin potential in V (default: -0.5)
    end_potential : float
        End potential in V (default: 0.5)
    step_potential : float
        Step potential in V (default: 0.1)
    scanrate : float
        Scan rate in V/s (default: 1.0)
    enable_bipot_current: bool
        Enable bipot current (default: False)
    record_auxiliary_input : bool
        Record auxiliary input (default: False)
    record_cell_potential : bool
        Record cell potential (default: False)
        Counter electrode vs ground.
    record_we_potential : bool
        Record applied working electrode potential (default: False)
        Reference electrode vs ground.
    """

    _id = 'lsv'

    begin_potential: float = -0.5
    end_potential: float = 0.5
    step_potential: float = 0.1
    scanrate: float = 1.0

    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_potential: bool = False
    enable_bipot_current: bool = False

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    versus_ocp: VersusOcpSettings = attrs.field(
        factory=VersusOcpSettings, converter=settings.to_VersusOcpSettings
    )
    bipot: BipotSettings = attrs.field(
        factory=BipotSettings, converter=settings.to_BipotSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    current_limits: CurrentLimitSettings = attrs.field(
        factory=CurrentLimitSettings, converter=settings.to_CurrentLimitSettings
    )
    ir_drop: IrDropCompensationSettings = attrs.field(
        factory=IrDropCompensationSettings, converter=settings.to_IrDropCompensationSettings
    )
    equilibration_triggers: TriggerAtEquilibrationSettings = attrs.field(
        factory=TriggerAtEquilibrationSettings,
        converter=settings.to_TriggerAtEquilibrationSettings,
    )
    measurement_triggers: TriggerAtMeasurementSettings = attrs.field(
        factory=TriggerAtMeasurementSettings, converter=settings.to_TriggerAtMeasurementSettings
    )
    peaks: PeakSettings = attrs.field(factory=PeakSettings, converter=settings.to_PeakSettings)
    multiplexer: MultiplexerSettings = attrs.field(
        factory=MultiplexerSettings, converter=settings.to_MultiplexerSettings
    )
    common: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with linear sweep settings."""
        obj.BeginPotential = self.begin_potential
        obj.EndPotential = self.end_potential
        obj.StepPotential = self.step_potential
        obj.Scanrate = self.scanrate

        set_extra_value_mask(
            obj=obj,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_potential=self.record_we_potential,
            enable_bipot_current=self.enable_bipot_current,
        )

    def update_params(self, *, obj):
        self.begin_potential = obj.BeginPotential
        self.end_potential = obj.EndPotential
        self.step_potential = obj.StepPotential
        self.scanrate = obj.Scanrate

        msk = get_extra_value_mask(obj)

        for key in (
            'record_auxiliary_input',
            'record_cell_potential',
            'record_we_potential',
            'enable_bipot_current',
        ):
            setattr(self, key, msk[key])


@attrs.define
class SquareWaveVoltammetry(BaseConfig):
    """Create square wave method parameters.

    Attributes
    ----------
    equilibration_time : float
        Equilibration time in s (default: 0.0)
    begin_potential : float
        Begin potential in V (default: -0.5)
    end_potential : float
        End potential in V (default: 0.5)
    step_potential : float
        Step potential in V (default: 0.1)
    frequency : float
        Frequency in Hz (default: 10.0)
    amplitude : float
        Amplitude in V as half peak-to-peak value (default: 0.05).
    enable_bipot_current: bool
        Enable bipot current (default: False)
    record_auxiliary_input : bool
        Record auxiliary input (default: False)
    record_cell_potential : bool
        Record cell potential (default: False)
        Counter electrode vs ground.
    record_we_potential : bool
        Record applied working electrode potential (default: False)
        Reference electrode vs ground.
    record_forward_and_reverse_currents : bool
        Record forward and reverse currents (default: False)
    """

    _id = 'swv'

    equilibration_time: float = 0.0
    begin_potential: float = -0.5
    end_potential: float = 0.5
    step_potential: float = 0.1
    frequency: float = 10.0
    amplitude: float = 0.05

    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_potential: bool = False
    enable_bipot_current: bool = False
    record_forward_and_reverse_currents: bool = False

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    versus_ocp: VersusOcpSettings = attrs.field(
        factory=VersusOcpSettings, converter=settings.to_VersusOcpSettings
    )
    bipot: BipotSettings = attrs.field(
        factory=BipotSettings, converter=settings.to_BipotSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    ir_drop: IrDropCompensationSettings = attrs.field(
        factory=IrDropCompensationSettings, converter=settings.to_IrDropCompensationSettings
    )
    equilibration_triggers: TriggerAtEquilibrationSettings = attrs.field(
        factory=TriggerAtEquilibrationSettings,
        converter=settings.to_TriggerAtEquilibrationSettings,
    )
    measurement_triggers: TriggerAtMeasurementSettings = attrs.field(
        factory=TriggerAtMeasurementSettings, converter=settings.to_TriggerAtMeasurementSettings
    )
    peaks: PeakSettings = attrs.field(factory=PeakSettings, converter=settings.to_PeakSettings)
    multiplexer: MultiplexerSettings = attrs.field(
        factory=MultiplexerSettings, converter=settings.to_MultiplexerSettings
    )
    common: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with linear sweep settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.BeginPotential = self.begin_potential
        obj.EndPotential = self.end_potential
        obj.StepPotential = self.step_potential
        obj.Frequency = self.frequency
        obj.PulseAmplitude = self.amplitude

        set_extra_value_mask(
            obj=obj,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_potential=self.record_we_potential,
            enable_bipot_current=self.enable_bipot_current,
            record_forward_and_reverse_currents=self.record_forward_and_reverse_currents,
        )

    def update_params(self, *, obj):
        self.equilibration_time = obj.EquilibrationTime
        self.begin_potential = obj.BeginPotential
        self.end_potential = obj.EndPotential
        self.step_potential = obj.StepPotential
        self.frequency = obj.Frequency
        self.amplitude = obj.PulseAmplitude

        msk = get_extra_value_mask(obj)

        for key in (
            'record_auxiliary_input',
            'record_cell_potential',
            'record_we_potential',
            'enable_bipot_current',
            'record_forward_and_reverse_currents',
        ):
            setattr(self, key, msk[key])


@attrs.define
class DifferentialPulseVoltammetry(BaseConfig):
    """Create square wave method parameters.

    Attributes
    ----------
    equilibration_time : float
        Equilibration time in s (default: 0.0)
    begin_potential : float
        Begin potential in V (default: -0.5)
    end_potential : float
        End potential in V (default: 0.5)
    step_potential : float
        Step potential in V (default: 0.1)
    pulse_potential : float
        Pulse potential in V (default: 0.05)
    pulse_time : float
        Pulse time in s (default: 0.01)
    scanrate : float
        Scan rate in V/s (default: 1.0)
    enable_bipot_current: bool
        Enable bipot current (default: False)
    record_auxiliary_input : bool
        Record auxiliary input (default: False)
    record_cell_potential : bool
        Record cell potential (default: False)
        Counter electrode vs ground.
    record_we_potential : bool
        Record applied working electrode potential (default: False)
        Reference electrode vs ground.
    """

    _id = 'dpv'

    equilibration_time: float = 0.0  # Time (s)
    begin_potential: float = -0.5  # potential (V)
    end_potential: float = 0.5  # potential (V)
    step_potential: float = 0.1  # potential (V)
    pulse_potential: float = 0.05  # potential (V)
    pulse_time: float = 0.01  # time (s)
    scan_rate: float = 1.0  # potential/time (V/s)

    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_potential: bool = False
    enable_bipot_current: bool = False

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    versus_ocp: VersusOcpSettings = attrs.field(
        factory=VersusOcpSettings, converter=settings.to_VersusOcpSettings
    )
    bipot: BipotSettings = attrs.field(
        factory=BipotSettings, converter=settings.to_BipotSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    ir_drop: IrDropCompensationSettings = attrs.field(
        factory=IrDropCompensationSettings, converter=settings.to_IrDropCompensationSettings
    )
    equilibration_triggers: TriggerAtEquilibrationSettings = attrs.field(
        factory=TriggerAtEquilibrationSettings,
        converter=settings.to_TriggerAtEquilibrationSettings,
    )
    measurement_triggers: TriggerAtMeasurementSettings = attrs.field(
        factory=TriggerAtMeasurementSettings, converter=settings.to_TriggerAtMeasurementSettings
    )
    peaks: PeakSettings = attrs.field(factory=PeakSettings, converter=settings.to_PeakSettings)
    multiplexer: MultiplexerSettings = attrs.field(
        factory=MultiplexerSettings, converter=settings.to_MultiplexerSettings
    )
    common: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with linear sweep settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.BeginPotential = self.begin_potential
        obj.EndPotential = self.end_potential
        obj.StepPotential = self.step_potential
        obj.PulsePotential = self.pulse_potential
        obj.PulseTime = self.pulse_time
        obj.Scanrate = self.scan_rate

        set_extra_value_mask(
            obj=obj,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_potential=self.record_we_potential,
            enable_bipot_current=self.enable_bipot_current,
        )

    def update_params(self, *, obj):
        self.equilibration_time = obj.EquilibrationTime
        self.begin_potential = obj.BeginPotential
        self.end_potential = obj.EndPotential
        self.step_potential = obj.StepPotential
        self.pulse_potential = obj.PulsePotential
        self.pulse_time = obj.PulseTime
        self.scan_rate = obj.Scanrate

        msk = get_extra_value_mask(obj)

        for key in (
            'record_auxiliary_input',
            'record_cell_potential',
            'record_we_potential',
            'enable_bipot_current',
        ):
            setattr(self, key, msk[key])


@attrs.define
class ChronoAmperometry(BaseConfig):
    """Create chrono amperometry method parameters.

    Attributes
    ----------
    equilibration_time : float
        Equilibration time in s (default: 0.0)
    interval_time : float
        Interval time in s (default: 0.1)
    potential : float
        Potential in V (default: 0.0)
    run_time : float
        Run time in s (default: 1.0)
    enable_bipot_current: bool
        Enable bipot current (default: False)
    record_auxiliary_input : bool
        Record auxiliary input (default: False)
    record_cell_potential : bool
        Record cell potential (default: False)
        Counter electrode vs ground.
    record_we_potential : bool
        Record applied working electrode potential (default: False)
        Reference electrode vs ground.
    """

    _id = 'ad'

    equilibration_time: float = 0.0
    interval_time: float = 0.1
    potential: float = 0.0
    run_time: float = 1.0

    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_potential: bool = False
    enable_bipot_current: bool = False

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    versus_ocp: VersusOcpSettings = attrs.field(
        factory=VersusOcpSettings, converter=settings.to_VersusOcpSettings
    )
    bipot: BipotSettings = attrs.field(
        factory=BipotSettings, converter=settings.to_BipotSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    current_limits: CurrentLimitSettings = attrs.field(
        factory=CurrentLimitSettings, converter=settings.to_CurrentLimitSettings
    )
    charge_limits: ChargeLimitSettings = attrs.field(
        factory=ChargeLimitSettings, converter=settings.to_ChargeLimitSettings
    )
    ir_drop: IrDropCompensationSettings = attrs.field(
        factory=IrDropCompensationSettings, converter=settings.to_IrDropCompensationSettings
    )
    equilibration_triggers: TriggerAtEquilibrationSettings = attrs.field(
        factory=TriggerAtEquilibrationSettings,
        converter=settings.to_TriggerAtEquilibrationSettings,
    )
    measurement_triggers: TriggerAtMeasurementSettings = attrs.field(
        factory=TriggerAtMeasurementSettings, converter=settings.to_TriggerAtMeasurementSettings
    )
    peaks: PeakSettings = attrs.field(factory=PeakSettings, converter=settings.to_PeakSettings)
    multiplexer: MultiplexerSettings = attrs.field(
        factory=MultiplexerSettings, converter=settings.to_MultiplexerSettings
    )
    common: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with chrono amperometry settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.IntervalTime = self.interval_time
        obj.Potential = self.potential
        obj.RunTime = self.run_time

        set_extra_value_mask(
            obj=obj,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_potential=self.record_we_potential,
            enable_bipot_current=self.enable_bipot_current,
        )

    def update_params(self, *, obj):
        self.equilibration_time = obj.EquilibrationTime
        self.interval_time = obj.IntervalTime
        self.potential = obj.Potential
        self.run_time = obj.RunTime

        msk = get_extra_value_mask(obj)

        for key in (
            'record_auxiliary_input',
            'record_cell_potential',
            'record_we_potential',
            'enable_bipot_current',
        ):
            setattr(self, key, msk[key])


@attrs.define
class MultiStepAmperometry(BaseConfig):
    """Create multi-step amperometry method parameters.

    Attributes
    ----------
    equilibration_time : float
        Equilibration time in s (default: 0.0)
    interval_time : float
        Interval time in s (default: 0.1)
    n_cycles : int
        Number of cycles (default: 1)
    levels : list
        List of levels (default: [ELevel()].
        Use ELevel() to create levels.
    enable_bipot_current: bool
        Enable bipot current (default: False)
    record_auxiliary_input : bool
        Record auxiliary input (default: False)
    record_cell_potential : bool
        Record cell potential (default: False)
        Counter electrode vs ground.
    record_we_potential : bool
        Record applied working electrode potential (default: False)
        Reference electrode vs ground.
    """

    _id = 'ma'

    equilibration_time: float = 0.0
    interval_time: float = 0.1
    n_cycles: float = 1
    levels: list[ELevel] = attrs.field(factory=lambda: [ELevel()])

    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_potential: bool = False
    enable_bipot_current: bool = False

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    bipot: BipotSettings = attrs.field(
        factory=BipotSettings, converter=settings.to_BipotSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    current_limits: CurrentLimitSettings = attrs.field(
        factory=CurrentLimitSettings, converter=settings.to_CurrentLimitSettings
    )
    ir_drop: IrDropCompensationSettings = attrs.field(
        factory=IrDropCompensationSettings, converter=settings.to_IrDropCompensationSettings
    )
    peaks: PeakSettings = attrs.field(factory=PeakSettings, converter=settings.to_PeakSettings)
    multiplexer: MultiplexerSettings = attrs.field(
        factory=MultiplexerSettings, converter=settings.to_MultiplexerSettings
    )
    common: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with chrono amperometry settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.IntervalTime = self.interval_time
        obj.nCycles = self.n_cycles
        obj.Levels.Clear()

        if not self.levels:
            raise ValueError('At least one level must be specified.')

        for level in self.levels:
            obj.Levels.Add(level.to_psobj())

        obj.UseSelectiveRecord = any(level.record for level in self.levels)
        obj.UseLimits = any(
            (level.use_limit_current_min or level.use_limit_current_max)
            for level in self.levels
        )

        set_extra_value_mask(
            obj=obj,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_potential=self.record_we_potential,
            enable_bipot_current=self.enable_bipot_current,
        )

    def update_params(self, *, obj):
        self.equilibration_time = obj.EquilibrationTime
        self.interval_time = obj.IntervalTime
        self.n_cycles = obj.nCycles

        self.levels = [ELevel.from_psobj(pslevel) for pslevel in obj.Levels]

        msk = get_extra_value_mask(obj)

        for key in (
            'record_auxiliary_input',
            'record_cell_potential',
            'record_we_potential',
            'enable_bipot_current',
        ):
            setattr(self, key, msk[key])


@attrs.define
class OpenCircuitPotentiometry(BaseConfig):
    """Create open circuit potentiometry method parameters.

    Attributes
    ----------
    interval_time : float
        Interval time in s (default: 0.1)
    run_time : float
        Run time in s (default: 1.0)
    enable_bipot_current: bool
        Enable bipot current (default: False)
    record_auxiliary_input : bool
        Record auxiliary input (default: False)
    record_we_current: bool
        Record working electrode current (default: False)
    record_we_current_range: int
        Record working electrode current range (default: 1 µA)
        Use `CURRENT_RANGE` to define the range.
    """

    _id = 'ocp'

    interval_time: float = 0.1  # Time (s)
    run_time: float = 1.0  # Time (s)

    record_auxiliary_input: bool = False
    record_we_current: bool = False
    record_we_current_range: CURRENT_RANGE = CURRENT_RANGE.cr_1_uA

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    potential_ranges: AutorangingPotentialSettings = attrs.field(
        factory=AutorangingPotentialSettings, converter=settings.to_AutorangingPotentialSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    potential_limits: PotentialLimitSettings = attrs.field(
        factory=PotentialLimitSettings, converter=settings.to_PotentialLimitSettings
    )
    measurement_triggers: TriggerAtMeasurementSettings = attrs.field(
        factory=TriggerAtMeasurementSettings, converter=settings.to_TriggerAtMeasurementSettings
    )
    peaks: PeakSettings = attrs.field(factory=PeakSettings, converter=settings.to_PeakSettings)
    multiplexer: MultiplexerSettings = attrs.field(
        factory=MultiplexerSettings, converter=settings.to_MultiplexerSettings
    )
    common: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with open circuit potentiometry settings."""
        obj.IntervalTime = self.interval_time
        obj.RunTime = self.run_time
        obj.AppliedCurrentRange = self.record_we_current_range.to_psobj()

        set_extra_value_mask(
            obj=obj,
            record_auxiliary_input=self.record_auxiliary_input,
            record_we_current=self.record_we_current,
        )

    def update_params(self, *, obj):
        self.interval_time = obj.IntervalTime
        self.run_time = obj.RunTime
        self.record_we_current_range = CURRENT_RANGE.from_psobj(obj.AppliedCurrentRange)

        msk = get_extra_value_mask(obj)

        for key in (
            'record_auxiliary_input',
            'record_we_current',
        ):
            setattr(self, key, msk[key])


@attrs.define
class ChronoPotentiometry(BaseConfig):
    """Create potentiometry method parameters.

    Attributes
    ----------
    current : float
        The current to apply. The unit of the value is the applied current range. So if 10 uA is the applied current range and 1.5 is given as value, the applied current will be 15 uA. (default: 0.0)
    applied_current_range : PalmSens.CurrentRange
        Applied current range (default: 100 µA).
        Use `CURRENT_RANGE` to define the range.
    interval_time : float
        Interval time in s (default: 0.1)
    run_time : float
        Run time in s (default: 1.0)
    record_auxiliary_input : bool
        Record auxiliary input (default: False)
    record_cell_potential : bool
        Record cell potential (default: False) [counter electrode vs ground]
    record_we_current : bool
        Record working electrode current (default: False)
    """

    _id = 'pot'

    current: float = 0.0
    applied_current_range: CURRENT_RANGE = CURRENT_RANGE.cr_100_uA
    interval_time: float = 0.1
    run_time: float = 1.0

    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_current: bool = False

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    potential_ranges: AutorangingPotentialSettings = attrs.field(
        factory=AutorangingPotentialSettings, converter=settings.to_AutorangingPotentialSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    potential_limits: PotentialLimitSettings = attrs.field(
        factory=PotentialLimitSettings, converter=settings.to_PotentialLimitSettings
    )
    measurement_triggers: TriggerAtMeasurementSettings = attrs.field(
        factory=TriggerAtMeasurementSettings, converter=settings.to_TriggerAtMeasurementSettings
    )
    peaks: PeakSettings = attrs.field(factory=PeakSettings, converter=settings.to_PeakSettings)
    multiplexer: MultiplexerSettings = attrs.field(
        factory=MultiplexerSettings, converter=settings.to_MultiplexerSettings
    )
    common: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with potentiometry settings."""
        obj.Current = self.current
        obj.AppliedCurrentRange = self.applied_current_range.to_psobj()
        obj.IntervalTime = self.interval_time
        obj.RunTime = self.run_time

        obj.AppliedCurrentRange = self.applied_current_range.to_psobj()

        set_extra_value_mask(
            obj=obj,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_current=self.record_we_current,
        )

    def update_params(self, *, obj):
        self.current = obj.Current
        self.applied_current_range = CURRENT_RANGE.from_psobj(obj.AppliedCurrentRange)
        self.interval_time = obj.IntervalTime
        self.run_time = obj.RunTime

        msk = get_extra_value_mask(obj)

        for key in (
            'record_auxiliary_input',
            'record_cell_potential',
            'record_we_current',
        ):
            setattr(self, key, msk[key])


@attrs.define
class ElectrochemicalImpedanceSpectroscopy(BaseConfig):
    """Create potentiometry method parameters.

    Attributes
    ----------
    equilibration_time : float
        Equilibration time in s (default: 0.0)
    dc_potential : float
        DC potential in V (default: 0.0)
    ac_potential : float
        AC potential in V RMS (default: 0.01)
    n_frequencies : int
        Number of frequencies (default: 11)
    max_frequency : float
        Maximum frequency in Hz (default: 1e5)
    min_frequency : float
        Minimum frequency in Hz (default: 1e3)
    """

    _id = 'eis'

    equilibration_time: float = 0.0
    dc_potential: float = 0.0
    ac_potential: float = 0.01
    n_frequencies: int = 11
    max_frequency: float = 1e5
    min_frequency: float = 1e3

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    potential_ranges: AutorangingPotentialSettings = attrs.field(
        factory=AutorangingPotentialSettings, converter=settings.to_AutorangingPotentialSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    versus_ocp: VersusOcpSettings = attrs.field(
        factory=VersusOcpSettings, converter=settings.to_VersusOcpSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    equilibration_triggers: TriggerAtMeasurementSettings = attrs.field(
        factory=TriggerAtMeasurementSettings, converter=settings.to_TriggerAtMeasurementSettings
    )
    measurement_triggers: TriggerAtEquilibrationSettings = attrs.field(
        factory=TriggerAtEquilibrationSettings,
        converter=settings.to_TriggerAtEquilibrationSettings,
    )
    multiplexer: MultiplexerSettings = attrs.field(
        factory=MultiplexerSettings, converter=settings.to_MultiplexerSettings
    )
    common: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with potentiometry settings."""
        obj.ScanType = enumScanType.Fixed
        obj.FreqType = enumFrequencyType.Scan
        obj.EquilibrationTime = self.equilibration_time
        obj.Potential = self.dc_potential
        obj.Eac = self.ac_potential
        obj.nFrequencies = self.n_frequencies
        obj.MaxFrequency = self.max_frequency
        obj.MinFrequency = self.min_frequency

    def update_params(self, *, obj):
        self.equilibration_time = obj.EquilibrationTime
        self.dc_potential = obj.Potential
        self.ac_potential = obj.Eac
        self.n_frequencies = obj.nFrequencies
        self.max_frequency = obj.MaxFrequency
        self.min_frequency = obj.MinFrequency


@attrs.define
class GalvanostaticImpedanceSpectroscopy(BaseConfig):
    """Create potentiometry method parameters.

    Attributes
    ----------
    applied_current_range : PalmSens.CurrentRange
        Applied current range (default: 100 µA)
        Use `CURRENT_RANGE` to define the range.
    ac_current : float
        AC current in applied current range RMS (default: 0.01)
    dc_current : float
        DC current in applied current range (default: 0.0)
    n_frequencies : int
        Number of frequencies (default: 11)
    max_frequency : float
        Maximum frequency in Hz (default: 1e5)
    min_frequency : float
        Minimum frequency in Hz (default: 1e3)
    """

    _id = 'gis'

    applied_current_range: CURRENT_RANGE = CURRENT_RANGE.cr_100_uA
    equilibration_time: float = 0.0
    ac_current: float = 0.01
    dc_current: float = 0.0
    n_frequencies: int = 11
    max_frequency: float = 1e5
    min_frequency: float = 1e3

    current_ranges: AutorangingCurrentSettings = attrs.field(
        factory=AutorangingCurrentSettings, converter=settings.to_AutorangingCurrentSettings
    )
    potential_ranges: AutorangingPotentialSettings = attrs.field(
        factory=AutorangingPotentialSettings, converter=settings.to_AutorangingPotentialSettings
    )
    pretreatment: PretreatmentSettings = attrs.field(
        factory=PretreatmentSettings, converter=settings.to_PretreatmentSettings
    )
    post_measurement: PostMeasurementSettings = attrs.field(
        factory=PostMeasurementSettings, converter=settings.to_PostMeasurementSettings
    )
    equilibration_triggers: TriggerAtEquilibrationSettings = attrs.field(
        factory=TriggerAtEquilibrationSettings,
        converter=settings.to_TriggerAtEquilibrationSettings,
    )
    measurement_triggers: TriggerAtMeasurementSettings = attrs.field(
        factory=TriggerAtMeasurementSettings, converter=settings.to_TriggerAtMeasurementSettings
    )
    multiplexer: MultiplexerSettings = attrs.field(
        factory=MultiplexerSettings, converter=settings.to_MultiplexerSettings
    )
    common: CommonSettings = attrs.field(
        factory=CommonSettings, converter=settings.to_CommonSettings
    )

    def update_psmethod(self, *, obj):
        """Update method with potentiometry settings."""

        obj.ScanType = enumScanType.Fixed
        obj.FreqType = enumFrequencyType.Scan
        obj.AppliedCurrentRange = self.applied_current_range.to_psobj()
        obj.EquilibrationTime = self.equilibration_time
        obj.Iac = self.ac_current
        obj.Idc = self.dc_current
        obj.nFrequencies = self.n_frequencies
        obj.MaxFrequency = self.max_frequency
        obj.MinFrequency = self.min_frequency

    def update_params(self, *, obj):
        self.applied_current_range = CURRENT_RANGE.from_psobj(obj.AppliedCurrentRange)
        self.equilibration_time = obj.EquilibrationTime
        self.ac_current = obj.Iac
        self.dc_current = obj.Idc
        self.n_frequencies = obj.nFrequencies
        self.max_frequency = obj.MaxFrequency
        self.min_frequency = obj.MinFrequency


@attrs.define
class MethodScript(BaseConfig):
    """Create a method script sandbox object.

    Attributes
    ----------
    script : str
        Method script, see https://www.palmsens.com/methodscript/ for more information.
    """

    _id = 'ms'

    script: str = """e
wait 100m
if 1 < 2
    send_string "Hello world"
endif

"""

    def update_psmethod(self, *, obj):
        """Update method with MethodScript."""
        obj.MethodScript = self.script

    def update_params(self, *, obj):
        self.script = obj.MethodScript


ID_TO_PARAMETER_MAPPING: dict[str, Type[BaseConfig] | None] = {
    'acv': None,
    'ad': ChronoAmperometry,
    'cc': None,
    'cp': ChronoPotentiometry,
    'cpot': None,
    'cv': CyclicVoltammetry,
    'dpv': DifferentialPulseVoltammetry,
    'eis': ElectrochemicalImpedanceSpectroscopy,
    'fam': None,
    'fcv': None,
    'fgis': None,
    'fis': None,
    'gis': GalvanostaticImpedanceSpectroscopy,
    'gs': None,
    'lp': None,
    'lsp': None,
    'lsv': LinearSweepVoltammetry,
    'ma': MultiStepAmperometry,
    'mm': None,
    'mp': None,
    'mpad': None,
    'ms': MethodScript,
    'npv': None,
    'ocp': OpenCircuitPotentiometry,
    'pad': None,
    'pot': None,
    'ps': None,
    'scp': None,
    'swv': SquareWaveVoltammetry,
}
