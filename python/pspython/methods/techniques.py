from dataclasses import dataclass

from PalmSens import Techniques

from ._shared import multi_step_amperometry_level
from .settings import (
    AutorangingCurrentSettings,
    BaseParameters,
    BipotSettings,
    CurrentLimitSettings,
    FilterSettings,
    IrDropCompensationSettings,
    MultiplexerSettings,
    OtherSettings,
    PostMeasurementSettings,
    PretreatmentSettings,
    TriggerAtEquilibrationSettings,
    TriggerAtMeasurementSettings,
    VersusOcpSettings,
)


@dataclass
class CyclicVoltammetryParameters(
    BaseParameters,
    AutorangingCurrentSettings,
    PretreatmentSettings,
    VersusOcpSettings,
    PostMeasurementSettings,
    CurrentLimitSettings,
    IrDropCompensationSettings,
    TriggerAtEquilibrationSettings,
    TriggerAtMeasurementSettings,
    FilterSettings,
    OtherSettings,
):
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
    _PSMethod = Techniques.CyclicVoltammetry

    def add_to_object(self, *, obj):
        """Update method with cyclic voltammetry settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.BeginPotential = self.begin_potential
        obj.Vtx1Potential = self.vertex1_potential
        obj.Vtx2Potential = self.vertex2_potential
        obj.StepPotential = self.step_potential
        obj.Scanrate = self.scanrate
        obj.nScans = self.n_scans


@dataclass
class LinearSweepParameters(
    BaseParameters,
    AutorangingCurrentSettings,
    PretreatmentSettings,
    VersusOcpSettings,
    BipotSettings,
    PostMeasurementSettings,
    CurrentLimitSettings,
    IrDropCompensationSettings,
    TriggerAtEquilibrationSettings,
    TriggerAtMeasurementSettings,
    FilterSettings,
    MultiplexerSettings,
    OtherSettings,
):
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
    """

    # linear sweep voltammetry settings
    begin_potential: float = -0.5  # potential (V)
    end_potential: float = 0.5  # potential (V)
    step_potential: float = 0.1  # potential (V)
    scanrate: float = 1.0  # potential/time (V/s)
    _PSMethod = Techniques.LinearSweep

    def add_to_object(self, *, obj):
        """Update method with linear sweep settings."""
        obj.BeginPotential = self.begin_potential
        obj.EndPotential = self.end_potential
        obj.StepPotential = self.step_potential
        obj.Scanrate = self.scanrate


@dataclass
class SquareWaveParameters(
    BaseParameters,
    AutorangingCurrentSettings,
    PretreatmentSettings,
    VersusOcpSettings,
    BipotSettings,
    PostMeasurementSettings,
    IrDropCompensationSettings,
    TriggerAtEquilibrationSettings,
    TriggerAtMeasurementSettings,
    FilterSettings,
    MultiplexerSettings,
    OtherSettings,
):
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
    record_forward_and_reverse_currents : bool
        Record forward and reverse currents (default: False)
    """

    # square wave voltammetry settings
    equilibration_time: float = 0.0
    begin_potential: float = -0.5
    end_potential: float = 0.5
    step_potential: float = 0.1
    frequency: float = 10.0
    amplitude: float = 0.05
    record_forward_and_reverse_currents: bool = False
    _PSMethod = Techniques.SquareWave

    def add_to_object(self, *, obj):
        """Update method with linear sweep settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.BeginPotential = self.begin_potential
        obj.EndPotential = self.end_potential
        obj.StepPotential = self.step_potential
        obj.Frequency = self.frequency
        obj.PulseAmplitude = self.amplitude

        # if self.record_forward_and_reverse_currents:
        #     extra_values = int(obj.ExtraValueMsk) | int(ExtraValueMask.IForwardReverse)
        #     obj.ExtraValueMsk = ExtraValueMask(extra_values)


@dataclass
class DifferentialPulseParameters(
    BaseParameters,
    AutorangingCurrentSettings,
    PretreatmentSettings,
    VersusOcpSettings,
    BipotSettings,
    PostMeasurementSettings,
    IrDropCompensationSettings,
    TriggerAtEquilibrationSettings,
    TriggerAtMeasurementSettings,
    FilterSettings,
    MultiplexerSettings,
    OtherSettings,
):
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
    """

    # differential pulse voltammetry settings
    equilibration_time: float = 0.0  # Time (s)
    begin_potential: float = -0.5  # potential (V)
    end_potential: float = 0.5  # potential (V)
    step_potential: float = 0.1  # potential (V)
    pulse_potential: float = 0.05  # potential (V)
    pulse_time: float = 0.01  # time (s)
    scan_rate: float = 1.0  # potential/time (V/s)
    _PSMethod = Techniques.SquareWave

    def add_to_object(self, *, obj):
        """Update method with linear sweep settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.BeginPotential = self.begin_potential
        obj.EndPotential = self.end_potential
        obj.StepPotential = self.step_potential
        obj.PulsePotential = self.pulse_potential
        obj.PulseTime = self.pulse_time
        obj.Scanrate = self.scan_rate


@dataclass
class ChronoAmperometryParameters(
    BaseParameters,
    AutorangingCurrentSettings,
    PretreatmentSettings,
    VersusOcpSettings,
    BipotSettings,
    PostMeasurementSettings,
    CurrentLimitSettings,
    IrDropCompensationSettings,
    TriggerAtEquilibrationSettings,
    TriggerAtMeasurementSettings,
    FilterSettings,
    MultiplexerSettings,
    OtherSettings,
):
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
    """

    equilibration_time: float = 0.0
    interval_time: float = 0.1
    potential: float = 0.0
    run_time: float = 1.0
    _PSMethod = Techniques.AmperometricDetection

    def add_to_object(self, *, obj):
        """Update method with chrono amperometry settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.IntervalTime = self.interval_time
        obj.Potential = self.potential
        obj.RunTime = self.run_time

        # set_extra_value_mask(
        #     dotnet_method,
        #     enable_bipot_current=self.enable_bipot_current,
        #     record_auxiliary_input=self.record_auxiliary_input,
        #     record_cell_potential=self.record_cell_potential,
        #     record_we_potential=self.record_we_potential,
        # )


@dataclass
class MultiStepAmperometryParameters(
    BaseParameters,
    AutorangingCurrentSettings,
    PretreatmentSettings,
    BipotSettings,
    PostMeasurementSettings,
    CurrentLimitSettings,
    IrDropCompensationSettings,
    FilterSettings,
    MultiplexerSettings,
    OtherSettings,
):
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
        List of levels (default: [multi_step_amperometry_level()].
        Use multi_step_amperometry_level() to create levels.
    """

    equilibration_time: float = 0.0  # Time (s)
    interval_time: float = 0.1  # Time (s)
    n_cycles: float = 1  # Number of cycles
    levels: list[Techniques.ELevel] = [multi_step_amperometry_level()]
    _PSMethod = Techniques.MultistepAmperometry

    def add_to_object(self, *, obj):
        """Update method with chrono amperometry settings."""
        obj.EquilibrationTime = self.equilibration_time
        obj.IntervalTime = self.interval_time
        obj.nCycles = self.n_cycles
        obj.Levels.Clear()

        if len(self.levels) == 0:
            raise ValueError('At least one level must be specified.')

        use_partial_record = False
        use_level_limits = False

        for level in self.levels:
            if level.Record:
                use_partial_record = True
            if level.UseMaxLimit or level.UseMinLimit:
                use_level_limits = True

            obj.Levels.Add(level)

        obj.UseSelectiveRecord = use_partial_record
        obj.UseLimits = use_level_limits
