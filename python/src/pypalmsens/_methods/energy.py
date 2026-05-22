from __future__ import annotations

import PalmSens
from pydantic import BaseModel, Field

from .techniques import MethodScript

TEMPLATE = """e
#############
# MethodSCRIPT example for potentiostats by PalmSens BV - www.palmsens.com
# This example includes detailed explanation of each element in the code, either preceding or appearing in the same line.
#
# Description:  With Chronopotentiometry and Chronoamperometry charge a cell and a Constant current followed by Constant Coltage (CC-CV).
#				With Chronopotentiometry discharge the cell at a constant current (CC).
#               Store the amount of charge transferred during each charge and discharge step.
#               Send live I-V verus time. Send the capacity per charge - discharge step.
#				The charge values are absolute and are converted to mAh.
#
# MethodSCRIPT version: 1.9
# Last modified: May 2026
# Applies to: EmStat4 (adapted from Nexus)
# Go to www.palmsens.com/msmanual for the MethodSCRIPT Manual
#
#############
#
# Initialize variables. All variables must be declared before first use.
var potential_max
var potential_min
var current_charge
var current_discharge
var current_min
var cycles
var interval
var max_time
var cycle
var current
var potential
var time
var q
var qchg
var qdis
var delta_v
var delta_i
var delta_t
var prev_potential
var meas_delta_v
var acc_delta_v
var prev_current
var meas_delta_i
var acc_delta_i
var acc_t
var bandwidth
# The arrays below are used to store the charge data.
array capacity_charge 10000i
array capacity_discharge 10000i
store_var cycle 1i ja # defines which cycle will be the first. Sufix "i" after the number assign it as a floating point.
# Set technique parameters
store_var potential_max {model.potential_max}m ab # Maximum potential to charge to.
store_var current_min {model.current_min}u ba # Minimum current to stop the CV charge step.
store_var potential_min {model.potential_min}m ab # Minimum potential to discharge to.
store_var current_charge {model.current_charge}u ba # Constant current to charge with.
store_var current_discharge {model.current_discharge}u ba # Constant current to discharge with.
store_var cycles {model.cycles}i ja # Amount of charge and discharge cycles.
store_var interval {model.interval}m eb # Interval time of each measurement point.
store_var max_time {model.max_time} eb # Maximum duration of each step (if the cut-off is not met).
store_var delta_v {model.delta_v}u ia # Minimum potential variation required for plotting data in CC steps. Leave it as a positive value.
store_var delta_i {model.delta_i}n ha # Minimum current variation required for plotting data in the CV step. Leave it as a positive value.
store_var delta_t {model.delta_t}m eb # Maximum time without plotting data.
# General instrument settings
store_var bandwidth 5850535u dc # Recommended bandwidth per each 1 s time interval.
div_var bandwidth interval # Calculate the bandwidth to be applied based on the provided time interval.
set_pgstat_chan 0 # Use the main channel.
meas 100m potential ab # Measure the OCP to be used in the first Cell ON.
# Charge/discharge loop
timer_start # Start the time counting (t=0).
loop cycle <= cycles # Repeat until last cycle.
    # Constant Current (CC) charge step.
	set_pgstat_mode 6 # Set galvanostat mode.
	set_max_bandwidth bandwidth # Set the maximum bandwidth to the recommended setting. Must be declared after every pgstat_mode command.
	set_acquisition_frac_autoadjust 50 # Equivalent to mains filter, change it to 60 if your mains is 60 Hz.
	set_range_minmax ab potential_min potential_max # Set the range for voltage reading.
	set_autoranging ab potential_min potential_max # Set automatic range switching for voltage reading.
	set_range db current_charge # Set the range for applied current.
	cell_on # option disabled for ES4 # ocp(potential) # Turns cell ON with the measured OCP.
    meas_loop_cp potential current current_charge interval max_time # CC experiment with the previously declared parameters.
		copy_var prev_potential meas_delta_v # Get the previous potential to calculate its variation (delta)
		sub_var meas_delta_v potential # Calculate potential variation.
		if meas_delta_v < 0 # Make delta_v absolute.
			mul_var meas_delta_v -1
		endif
		add_var acc_delta_v meas_delta_v # Accumulate delta_v.
        copy_var current q # Copy obtained current to calculate the charge.
        mul_var q interval # Multiply the current with the time and store the result (Coulombs) in variable q.
        div_var q 3600m # Convert the charge from Coulombs to mAh.
        add_var capacity_charge[cycle] q # Adds the charge to the array.
		if acc_delta_v >= delta_v # Plot a data point if the accumulated delta_v is reached.
			set_script_output 1 # Enable data sending (because it is disabled elsewhere for concatenating plots).
			timer_get time # Get the elapsed time and store it in the variable time.
			pck_start # Start sending data package.
				pck_add time # Plot time. First data package becomes X axis in PSTrace.
				pck_add potential # Plot measured potential.
				pck_add current # Plot applied current.
			pck_end # Finish data package sending.
			store_var acc_delta_v 0 ia # Reset accumulated delta_v after plotted point.
			store_var acc_t 0 eb # Reset accumulated time after plotted point.
			# Update the status bar with measured values (code below):
			send_string f"Cycle {{cycle}}/{{cycles}}    |    E = {{potential}} V    |    I = {{current}} A    |    Qchg = {{capacity_charge[cycle]}} mAh   |    Qdis = {{capacity_discharge[cycle]}} mAh   |   t = {{time}} s"
			set_script_output 0 # Disable data sending to concatenated charge and discharge steps.
		elseif acc_t > delta_t # If the delta_v condition is not met, test the delta time condition.
			add_var acc_delta_v delta_v # This trick forces the point plotting using the next delta-v condition.
		else # If none of the conditions are met.
			add_var acc_t interval # Store the accumulated time without plotting.
		endif
		copy_var potential prev_potential # Copy the measured potential to be used in the next measurement point.
        if potential >= potential_max # Cut-off limit for the charging step.
            breakloop # If the limit is reached, break this loop and proceed to the next step.
        endif # Finish the "if" condition.
    endloop # Finish the CC charge step.
	# Constant Voltage (CV) charge step. Many codes are similar to the CC charge step.
	set_pgstat_mode 3 # Set potentiostatic mode.
	set_max_bandwidth bandwidth
	set_acquisition_frac_autoadjust 50
	set_range da potential_max # Set the range for applied voltage.
	set_range_minmax ba current_min current_charge # Set the range for current reading.
	set_autoranging ba current_min current_charge # Set automatic range switching for current reading.
	set_e potential_max # Set the starting voltage before cell ON.
	cell_on
    meas_loop_ca potential current potential_max interval max_time # CV experiment with the previously declared parameters
		copy_var prev_current meas_delta_i
		sub_var meas_delta_i current
		if meas_delta_i < 0
			mul_var meas_delta_i -1
		endif
		add_var acc_delta_i meas_delta_i
        copy_var current q
        mul_var q interval
        div_var q 3600m
        add_var capacity_charge[cycle] q
		if acc_delta_i >= delta_i
			set_script_output 1
			timer_get time
			pck_start
				pck_add time
				pck_add potential
				pck_add current
			pck_end
			store_var acc_delta_i 0 ha
			store_var acc_t 0 eb
			send_string f"Cycle {{cycle}}/{{cycles}}    |    E = {{potential}} V    |    I = {{current}} A    |    Qchg = {{capacity_charge[cycle]}} mAh   |    Qdis = {{capacity_discharge[cycle]}} mAh   |   t = {{time}} s"
			set_script_output 0
		elseif acc_t > delta_t
			add_var acc_delta_i delta_i
		else
			add_var acc_t interval
		endif
		copy_var current prev_current
        if current <= current_min
            breakloop
        endif
    endloop
    # Constant current discharge. Codes below are almost the same as for the CC charge step.
	set_pgstat_mode 6
	set_max_bandwidth bandwidth
	set_acquisition_frac_autoadjust 50
	set_range_minmax ab potential_min potential_max
	set_autoranging ab potential_min potential_max
	set_range db current_discharge
	cell_on # option disabled for ES4 # ocp(potential)
    meas_loop_cp potential current current_discharge interval max_time
		copy_var prev_potential meas_delta_v
		sub_var meas_delta_v potential
		if meas_delta_v < 0
			mul_var meas_delta_v -1
		endif
		add_var acc_delta_v meas_delta_v
        copy_var current q
        mul_var q interval
        div_var q -3600m
        add_var capacity_discharge[cycle] q
		if acc_delta_v >= delta_v
			set_script_output 1
			timer_get time
			pck_start
				pck_add time
				pck_add potential
				pck_add current
			pck_end
			store_var acc_delta_v 0 ia
			store_var acc_t 0 eb
			send_string f"Cycle {{cycle}}/{{cycles}}    |    E = {{potential}} V    |    I = {{current}} A    |    Qchg = {{capacity_charge[cycle]}} mAh   |    Qdis = {{capacity_discharge[cycle]}} mAh   |   t = {{time}} s"
        elseif acc_t > delta_t
			add_var acc_delta_v delta_v
		else
			add_var acc_t interval
		endif
		copy_var potential prev_potential
		if potential <= potential_min
            breakloop
        endif
	endloop # Finish the CC discharge step.
    # Send cycle number and charged and discharged capacity.
	alter_vartype cycle at # Define cycle value as AT type, enabling custom axis name in PSTrace.
    alter_vartype capacity_charge[cycle] as # Define charge value as AS type, enabling custom axis name in PSTrace.
    alter_vartype capacity_discharge[cycle] as # Define discharge value as AS type, enabling custom axis name in PSTrace.
    pck_start # Plot passed charge/discharge versus cycle number.
        pck_add cycle # Plot cycle number. First data package becomes X axis in PSTrace
        pck_add capacity_charge[cycle] # Plot passed charge in the charge step.
        pck_add capacity_discharge[cycle] # PLot passed charge in the discharge step.
    pck_end # Finish data package sending.
    add_var cycle 1i # Add one cycle count.
endloop # Finish outer loop.
on_finished: # Define what to do when the experiment is finisehd or aborted.
    cell_off # Switch the cell OFF when finished.

"""


class BatteryCycling(BaseModel):
    potential_max: float = 4300
    """Maximum potential to charge to (units: mV)."""

    current_min: float = 5
    """Minimum current to stop the CV charge step (units: μA)."""

    potential_min: float = 2500
    """Minimum potential to discharge to (units: mV)."""

    current_charge: float = 100
    """Constant current to charge with (units: μA)."""

    current_discharge: float = -100
    """Constant current to discharge with (units: μA)."""

    cycles: int = 100
    """Number of charge and discharge cycles."""

    interval: float = 10
    """Interval time of each measurement point (units: s)."""

    max_time: float = 3
    """Maximum duration of each step (if the cut-off is not met) (units: s)."""

    delta_v: float = Field(100, gt=0)
    """Minimum potential variation required for plotting data in CC steps (units: μV)."""

    delta_i: float = Field(500, gt=0)
    """Minimum current variation reuqired for plotting data in the CV step (units: nA)."""

    delta_t: float = 100
    """Maximum time without plotting data (units: ms)."""

    def render(self) -> str:
        return TEMPLATE.format(model=self)

    def to_methodscript(self) -> MethodScript:
        script = self.render()
        return MethodScript(script=script)

    def _to_psmethod(self) -> PalmSens.Method:
        method = self.to_methodscript()
        return method._to_psmethod()
