from dataclasses import dataclass

from PalmSens.Techniques import SquareWave as PSSquareWave

from .potential_method import PotentialMethodParameters


@dataclass
class SquareWaveParameters(PotentialMethodParameters):
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

    def update_dotnet_method(self, *, dotnet_method):
        """Update method with linear sweep settings."""
        dotnet_method.EquilibrationTime = self.equilibration_time
        dotnet_method.BeginPotential = self.begin_potential
        dotnet_method.EndPotential = self.end_potential
        dotnet_method.StepPotential = self.step_potential
        dotnet_method.Frequency = self.frequency
        dotnet_method.PulseAmplitude = self.amplitude

        # breakpoint()

        # set_extra_value_mask(
        #     record_forward_and_reverse_currents=record_forward_and_reverse_currents,
        # )

    def to_dotnet_method(self):
        """Convert parameters to dotnet method."""
        obj = PSSquareWave()

        super().update_dotnet_method(dotnet_method=obj)
        self.update_dotnet_method(dotnet_method=obj)

        return obj


def square_wave_voltammetry(**kwargs) -> PSSquareWave:
    """Alias for LinearSweep for backwards compatibility"""
    square_wave = SquareWaveParameters(**kwargs)
    return square_wave.to_dotnet_method()
