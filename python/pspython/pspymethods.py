from PalmSens.Techniques import (  # type: ignore
    MethodScriptSandbox,
)

from .methods import (
    chronoamperometry,
    chronopotentiometry,
    cyclic_voltammetry,
    differential_pulse_voltammetry,
    electrochemical_impedance_spectroscopy,
    galvanostatic_impedance_spectroscopy,
    linear_sweep_voltammetry,
    multi_step_amperometry,
    multi_step_amperometry_level,
    open_circuit_potentiometry,
    square_wave_voltammetry,
)


def method_script_sandbox(method_script: str) -> MethodScriptSandbox:
    """Create a method script sandbox object.

    Parameters
    ----------
    method_script : str
        Method script
    """
    method_script_sandbox = MethodScriptSandbox()
    method_script_sandbox.MethodScript = method_script
    return method_script_sandbox


__all__ = [
    'chronoamperometry',
    'chronopotentiometry',
    'cyclic_voltammetry',
    'differential_pulse_voltammetry',
    'electrochemical_impedance_spectroscopy',
    'galvanostatic_impedance_spectroscopy',
    'linear_sweep_voltammetry',
    'multi_step_amperometry',
    'multi_step_amperometry_level',
    'open_circuit_potentiometry',
    'square_wave_voltammetry',
    'method_script_sandbox',
]
