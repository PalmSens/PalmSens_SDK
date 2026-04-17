from __future__ import annotations

from typing import Literal

from . import techniques


class CorrosionPotential(techniques.OpenCircuitPotentiometry):
    """Thin wrapper around OCP."""

    id: Literal['cpot'] = 'cpot'  # type: ignore
    """Unique method identifier."""


class CyclicPolarization(techniques.CyclicVoltammetry):
    """Thin wrapper around CV."""

    id: Literal['cp'] = 'cp'  # type: ignore
    """Unique method identifier."""


class Galvanostatic(techniques.ChronoPotentiometry):
    """Thin wrapper around CP."""

    id: Literal['gs'] = 'gs'  # type: ignore
    """Unique method identifier."""


class LinearPolarization(techniques.LinearSweepVoltammetry):
    """Thin wrapper around LSV."""

    id: Literal['lp'] = 'lp'  # type: ignore
    """Unique method identifier."""


class Potentiostatic(techniques.ChronoAmperometry):
    """Thin wrapper around CA."""

    id: Literal['ps'] = 'ps'  # type: ignore
    """Unique method identifier."""
