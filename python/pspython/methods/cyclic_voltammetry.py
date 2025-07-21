from dataclasses import dataclass, field
from typing import Optional

import PalmSens
from PalmSens.Techniques import CyclicVoltammetry as PSCyclicVoltammetry

from ._shared import (
    get_current_range,
    set_autoranging_current,
    set_bipot_settings,
    set_extra_value_mask,
    set_filter_settings,
    set_ir_drop_compensation,
    set_limit_settings,
    set_multiplexer_settings,
    set_post_measurement_settings,
    set_pretreatment,
    set_trigger_at_equilibration_settings,
    set_trigger_at_measurement_settings,
    set_versus_ocp,
)
from .method import MethodParameters


@dataclass
class CyclicVoltammetry(MethodParameters):
    """Create a cyclic voltammetry method parameters.

    Attributes
    ----------
    current_range_max: int
        Maximum current range (default: 10 mA) [use get_current_range() to get the range]
    current_range_min: int
        Minimum current range (default: 1 µA) [use get_current_range() to get the range]
    current_range_start: int
         Start current range (default: 100 µA) [use get_current_range() to get the range]
    deposition_potential: float
        Deposition potential in V (default: 0.0)
    deposition_time: float
        Deposition time in s (default: 0.0)
    conditioning_potential: float
        Conditioning potential in V (default: 0.0)
    conditioning_time: float
        Conditioning time in s (default: 0.0)
    equilibration_time: float
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
    enable_bipot_current: bool
        Enable bipotential current (default: False)
    bipot_mode: int
        Set the bipotential mode, 0 = constant, 1 = offset (default: 0)
    bipot_potential: float
        Set the bipotential in V (default: 0.0)
    bipot_current_range_max: int
        Maximum bipotential current range (default: 10 mA) [use get_current_range() to get the range]
    bipot_current_range_min: int
        Minimum bipotential current range (default: 1 µA) [use get_current_range() to get the range]
    bipot_current_range_start: int
        Start bipotential current range (default: 100 µA) [use get_current_range() to get the range]

    record_auxiliary_input: bool
        Record auxiliary input (default: False)
    record_cell_potential: bool
        Record cell potential (default: False) [counter electrode vs ground]
    record_we_potential: bool
        Record applied working electrode potential (default: False) [reference electrode vs ground]

    cell_on_after_measurement: bool
        Cell on after measurement (default: False)
    cell_on_after_measurement_potential: float
        Cell on after measurement potential in V (default: 0.0)

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

    dc_mains_filter: int
        Set the DC mains filter in Hz. Set to 50 Hz or 60 Hz depending on your region (default: 50).
    default_curve_post_processing_filter: int = 0
        Set the default curve post processing filter (default: 0)
           -1 = no filter
            0 = spike rejection
            1 = spike rejection + Savitsky-golay window 5
            2 = spike rejection + Savitsky-golay window 9
            3 = spike rejection + Savitsky-golay window 15
            4 = spike rejection + Savitsky-golay window 25

    set_mux_mode: int = -1
        Set multiplexer mode
           -1 = No multiplexer (disable)
            0 = Consecutive
            1 = Alternate
    set_mux_channels: list[bool]
        Set multiplexer channels as a list of bools for each channel (channel 1, channel 2, ..., channel 128).
        In consecutive mode all selections are valid.
        In alternating mode the first channel must be selected and all other
        channels should be consequtive i.e. (channel 1, channel 2, channel 3 and so on).
    set_mux8r2_settings: Optional[PalmSens.Method.MuxSettings]
        Initialize the settings for the MUX8R2 multiplexer (default: None).
        use get_mux8r2_settings() to create the settings.

    save_on_internal_storage: bool
        Save on internal storage (default: False)

    use_hardware_sync: bool
        Use hardware synchronization with other channels/instruments (default: False)
    """

    # autoranging
    current_range_max: int = get_current_range(8)
    current_range_min: int = get_current_range(4)
    current_range_start: int = get_current_range(6)

    # pretreatment
    deposition_potential: float = 0.0
    deposition_time: float = 0.0
    conditioning_potential: float = 0.0
    conditioning_time: float = 0.0
    equilibration_time: float = 0.0  # Time (s)

    # cyclic voltammetry settings
    begin_potential: float = -0.5  # potential (V)
    vertex1_potential: float = 0.5  # potential (V)
    vertex2_potential: float = -0.5  # potential (V)
    step_potential: float = 0.1  # potential (V)
    scanrate: float = 1.0  # potential/time (V/s)
    n_scans: float = 1  # number of cycles

    # advanced settings
    versus_ocp_mode: int = 0
    versus_ocp_max_ocp_time: float = 20.0  # Time (s)
    versus_ocp_stability_criterion: int = 0

    # bipot settings
    enable_bipot_current: bool = False
    bipot_mode: int = 0
    bipot_potential: float = 0.0  # V
    bipot_current_range_max: int = get_current_range(8)
    bipot_current_range_min: int = get_current_range(4)
    bipot_current_range_start: int = get_current_range(6)

    # record extra value settings
    record_auxiliary_input: bool = False
    record_cell_potential: bool = False
    record_we_potential: bool = False

    # post measurement settings
    cell_on_after_measurement: bool = False
    cell_on_after_measurement_potential: float = 0.0  # V

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
    # d0 high, d1 high, d2 high, d3 high
    trigger_at_equilibration_lines: tuple[bool, bool, bool, bool] = (False, False, False, False)
    trigger_at_measurement: bool = False
    # d0 high, d1 high, d2 high, d3 high
    trigger_at_measurement_lines: tuple[bool, bool, bool, bool] = (False, False, False, False)

    # set filter settings
    dc_mains_filter: int = 50  # Hz
    default_curve_post_processing_filter: int = 0

    # multiplexer settings
    set_mux_mode: int = -1
    set_mux_channels: list[bool] = field(
        default_factory=lambda: [False, False, False, False, False, False, False, False]
    )
    set_mux8r2_settings: Optional[PalmSens.Method.MuxSettings] = None

    # internal storage
    save_on_internal_storage: bool = False

    # use hardware synchronization with other channels/instruments
    use_hardware_sync: bool = False

    def to_dotnet_method(self):
        obj = PSCyclicVoltammetry()

        set_autoranging_current(
            obj,
            current_range_max=self.current_range_max,
            current_range_min=self.current_range_min,
            current_range_start=self.current_range_start,
        )

        set_pretreatment(
            obj,
            deposition_potential=self.deposition_potential,
            deposition_time=self.deposition_time,
            conditioning_potential=self.conditioning_potential,
            conditioning_time=self.conditioning_time,
        )
        obj.EquilibrationTime = self.equilibration_time

        # cyclic voltammetry settings
        obj.BeginPotential = self.begin_potential
        obj.Vtx1Potential = self.vertex1_potential
        obj.Vtx2Potential = self.vertex2_potential
        obj.StepPotential = self.step_potential
        obj.Scanrate = self.scanrate
        obj.nScans = self.n_scans

        set_versus_ocp(
            obj,
            versus_ocp_mode=self.versus_ocp_mode,
            versus_ocp_max_ocp_time=self.versus_ocp_max_ocp_time,
            versus_ocp_stability_criterion=self.versus_ocp_stability_criterion,
        )

        set_bipot_settings(
            obj,
            bipot_mode=self.bipot_mode,
            bipot_potential=self.bipot_potential,
            bipot_current_range_max=self.bipot_current_range_max,
            bipot_current_range_min=self.bipot_current_range_min,
            bipot_current_range_start=self.bipot_current_range_start,
        )

        set_extra_value_mask(
            obj,
            enable_bipot_current=self.enable_bipot_current,
            record_auxiliary_input=self.record_auxiliary_input,
            record_cell_potential=self.record_cell_potential,
            record_we_potential=self.record_we_potential,
        )

        set_post_measurement_settings(
            obj,
            cell_on_after_measurement=self.cell_on_after_measurement,
            cell_on_after_measurement_potential=self.cell_on_after_measurement_potential,
        )

        set_limit_settings(
            obj,
            use_limit_max=self.use_limit_current_max,
            limit_max=self.limit_current_max,
            use_limit_min=self.use_limit_current_min,
            limit_min=self.limit_current_min,
        )

        set_ir_drop_compensation(
            obj,
            use_ir_compensation=self.use_ir_compensation,
            ir_compensation=self.ir_compensation,
        )

        set_trigger_at_equilibration_settings(
            obj,
            trigger_at_equilibration=self.trigger_at_equilibration,
            trigger_at_equilibration_lines=self.trigger_at_equilibration_lines,
        )
        set_trigger_at_measurement_settings(
            obj,
            trigger_at_measurement=self.trigger_at_measurement,
            trigger_at_measurement_lines=self.trigger_at_measurement_lines,
        )

        set_filter_settings(
            obj,
            dc_mains_filter=self.dc_mains_filter,
            default_curve_post_processing_filter=self.default_curve_post_processing_filter,
        )

        set_multiplexer_settings(
            obj,
            set_mux_mode=self.set_mux_mode,
            set_mux_channels=self.set_mux_channels,
            set_mux8r2_settings=self.set_mux8r2_settings,
        )

        obj.SaveOnDevice = self.save_on_internal_storage
        obj.UseHWSync = self.use_hardware_sync

        return obj


def cyclic_voltammetry(**kwargs):
    """Alias for CyclicVoltammetry for backwards compatibility"""
    cyclic_voltammetry = CyclicVoltammetry(**kwargs)
    return cyclic_voltammetry.to_dotnet_method()
