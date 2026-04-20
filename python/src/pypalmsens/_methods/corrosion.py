from __future__ import annotations

from typing import Literal

from . import techniques


class CorrosionPotential(techniques.BaseOpenCircuitPotentiometry):
    """Create corrosion potential method parameters.

    Thin wrapper around OCP."""

    id: Literal['cpot'] = 'cpot'
    """Unique method identifier."""


class CyclicPolarization(techniques.BaseCyclicVoltammetry):
    """Create cyclic polarization method parameters.

    Thin wrapper around CV."""

    id: Literal['cp'] = 'cp'
    """Unique method identifier."""


class Galvanostatic(techniques.BaseChronoPotentiometry):
    """Create galvanostatic method parameters.

    Thin wrapper around CP."""

    id: Literal['gs'] = 'gs'
    """Unique method identifier."""


class LinearPolarization(techniques.BaseLinearSweepVoltammetry):
    """Create linear polarization method parameters.

    Thin wrapper around LSV."""

    id: Literal['lp'] = 'lp'
    """Unique method identifier."""


class Potentiostatic(techniques.BaseChronoAmperometry):
    """Create potentiostatic method parameters.

    Thin wrapper around CA."""

    id: Literal['ps'] = 'ps'
    """Unique method identifier."""
