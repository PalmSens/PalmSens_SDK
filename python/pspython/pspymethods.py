from PalmSens.Techniques import MethodScriptSandbox

from .methods._shared import (
    CURRENT_RANGE,
    POTENTIAL_RANGE,
    ELevel,
    get_method_estimated_duration,
    set_extra_value_mask,
)
from .methods.techniques_old import (
    chronoamperometry,
    chronopotentiometry,
    cyclic_voltammetry,
    differential_pulse_voltammetry,
    electrochemical_impedance_spectroscopy,
    galvanostatic_impedance_spectroscopy,
    linear_sweep_voltammetry,
    multi_step_amperometry,
    open_circuit_potentiometry,
    square_wave_voltammetry,
)


def method_script_sandbox(method_script: str) -> MethodScriptSandbox:
    """Create a method script sandbox object.

    Parameters
    ----------
    method_script : str
        Method script

    Returns
    -------
    sandbox : MethodScriptSandbox
    """
    sandbox = MethodScriptSandbox()
    sandbox.MethodScript = method_script
    return sandbox


__all__ = [
    'chronoamperometry',
    'chronopotentiometry',
    'cyclic_voltammetry',
    'differential_pulse_voltammetry',
    'electrochemical_impedance_spectroscopy',
    'galvanostatic_impedance_spectroscopy',
    'linear_sweep_voltammetry',
    'multi_step_amperometry',
    'ELevel',
    'open_circuit_potentiometry',
    'square_wave_voltammetry',
    'method_script_sandbox',
    'CURRENT_RANGE',
    'POTENTIAL_RANGE',
    'set_extra_value_mask',
    'get_method_estimated_duration',
]
