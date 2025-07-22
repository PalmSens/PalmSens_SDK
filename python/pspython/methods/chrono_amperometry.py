from dataclasses import dataclass

from PalmSens.Techniques import AmperometricDetection as PSAmperometricDetection

from ._shared import (
    set_extra_value_mask,
)
from .time_method import TimeMethodParameters


@dataclass
class ChronoAmperometryParameters(TimeMethodParameters):
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

    # chronoamperometry settings
    equilibration_time: float = 0.0
    interval_time: float = 0.1
    potential: float = 0.0
    run_time: float = 1.0

    # Limit settings
    use_limit_charge_max: bool = False
    limit_charge_max: float = 0.0  # in µC
    use_limit_charge_min: bool = False
    limit_charge_min: float = 0.0  # in µC

    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_potential: bool = False

    def update_dotnet_method(self, *, dotnet_method):
        """Update method with chrono amperometry settings."""
        super().update_dotnet_method(dotnet_method=dotnet_method)

        dotnet_method.EquilibrationTime = self.equilibration_time
        dotnet_method.IntervalTime = self.interval_time
        dotnet_method.Potential = self.potential
        dotnet_method.RunTime = self.run_time

        dotnet_method.UseChargeLimitMax = self.use_limit_charge_max
        dotnet_method.ChargeLimitMax = self.limit_charge_max
        dotnet_method.UseChargeLimitMin = self.use_limit_charge_min
        dotnet_method.ChargeLimitMin = self.limit_charge_min

        set_extra_value_mask(
            dotnet_method,
            enable_bipot_current=self.enable_bipot_current,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_potential=self.record_we_potential,
        )

    def to_dotnet_method(self):
        """Convert parameters to dotnet method."""
        obj = PSAmperometricDetection()

        self.update_dotnet_method(dotnet_method=obj)

        return obj


def chronoamperometry(**kwargs):
    """Alias for Potentiometry for backwards compatibility"""
    cp = ChronoAmperometryParameters(**kwargs)
    return cp.to_dotnet_method()
