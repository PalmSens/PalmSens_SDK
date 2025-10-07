from __future__ import annotations

import sys

# Load dotnet platform dependencies and init SDK
if sys.platform == 'win32':
    from ._lib.windows import sdk_version
else:
    from ._lib.mono import sdk_version

__version__ = '1.1.0'
__sdk_version__ = sdk_version

from . import data, fitting, settings
from ._instruments.instrument_manager import (
    InstrumentManager,
    connect,
    discover,
)
from ._instruments.instrument_manager_async import (
    InstrumentManagerAsync,
    connect_async,
    discover_async,
)
from ._instruments.instrument_pool import InstrumentPool
from ._instruments.instrument_pool_async import InstrumentPoolAsync
from ._io import load_method_file, load_session_file, save_method_file, save_session_file
from ._methods.techniques import (
    ACVoltammetry,
    ChronoAmperometry,
    ChronoCoulometry,
    ChronoPotentiometry,
    CyclicVoltammetry,
    DifferentialPulseVoltammetry,
    ElectrochemicalImpedanceSpectroscopy,
    FastAmperometry,
    FastCyclicVoltammetry,
    GalvanostaticImpedanceSpectroscopy,
    LinearSweepPotentiometry,
    LinearSweepVoltammetry,
    MethodScript,
    MultiStepAmperometry,
    MultiStepPotentiometry,
    NormalPulseVoltammetry,
    OpenCircuitPotentiometry,
    PulsedAmperometricDetection,
    SquareWaveVoltammetry,
    StrippingChronoPotentiometry,
)

__all__ = [
    'settings',
    'data',
    'fitting',
    'connect',
    'connect_async',
    'discover',
    'discover_async',
    'load_method_file',
    'load_session_file',
    'save_method_file',
    'save_session_file',
    'InstrumentManager',
    'FastAmperometry',
    'InstrumentManagerAsync',
    'InstrumentPool',
    'InstrumentPoolAsync',
    'ACVoltammetry',
    'ChronoAmperometry',
    'ChronoPotentiometry',
    'CyclicVoltammetry',
    'LinearSweepPotentiometry',
    'MultiStepPotentiometry',
    'StrippingChronoPotentiometry',
    'DifferentialPulseVoltammetry',
    'ElectrochemicalImpedanceSpectroscopy',
    'FastCyclicVoltammetry',
    'GalvanostaticImpedanceSpectroscopy',
    'LinearSweepVoltammetry',
    'ChronoCoulometry',
    'MethodScript',
    'MultiStepAmperometry',
    'NormalPulseVoltammetry',
    'OpenCircuitPotentiometry',
    'PulsedAmperometricDetection',
    'SquareWaveVoltammetry',
]
