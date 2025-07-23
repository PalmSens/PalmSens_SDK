from dataclasses import dataclass

from PalmSens import Techniques

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
