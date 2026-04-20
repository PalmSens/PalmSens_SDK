from __future__ import annotations

from ._methods.corrosion import (
    CorrosionPotential,
    CyclicPolarization,
    Galvanostatic,
    LinearPolarization,
    Potentiostatic,
)
from ._methods.techniques import ElectrochemicalImpedanceSpectroscopy

__all__ = [
    'Potentiostatic',
    'CorrosionPotential',
    'CyclicPolarization',
    'LinearPolarization',
    'Galvanostatic',
    'ElectrochemicalImpedanceSpectroscopy',  # alias EIS for completeness
]
