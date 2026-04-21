from __future__ import annotations

from typing import Literal

from . import techniques


class CorrosionPotential(techniques.BaseOpenCircuitPotentiometry):
    """Create corrosion potential method parameters.

    The method is equivalent to Open Circuit Potentiometry."""

    id: Literal['cpot'] = 'cpot'
    """Unique method identifier."""


class CyclicPolarization(techniques.BaseCyclicVoltammetry):
    """Create cyclic polarization method parameters.

    The method is equivalent to Cyclic Voltammetry."""

    id: Literal['cp'] = 'cp'
    """Unique method identifier."""


class Galvanostatic(techniques.BaseChronoPotentiometry):
    """Create galvanostatic method parameters.

    The method is equivalent to Chronopotentiometry."""

    id: Literal['gs'] = 'gs'
    """Unique method identifier."""


class LinearPolarization(techniques.BaseLinearSweepVoltammetry):
    """Create linear polarization method parameters.

    Linear polarization is typically used to study the corrosion response of metallic coatings.
    The method is equivalent to Linear Sweep Voltammetry.
    """

    id: Literal['lp'] = 'lp'
    """Unique method identifier."""


class Potentiostatic(techniques.BaseChronoAmperometry):
    """Create potentiostatic method parameters.

    The method is equivalent to Chronoamperometry."""

    id: Literal['ps'] = 'ps'
    """Unique method identifier."""


class ImpedanceSpectroscopy(techniques.ElectrochemicalImpedanceSpectroscopy):
    """Create Impedance Specroscopy method parameters.

    Electrochemical Impedance Spectroscopy (EIS) can be used to study corrosion and the effects
    of a wide range of coatings. For example, anodized coatings (anodized aluminium), conversion
    coatings (Chromate conversion coating), or organic coatings (paint). The corrosion rate and
    the pitting/disbanding of coatings are studied by fitting equivalent circuit models on the EIS
    measurement.

    The method is equivalent to Electrochemical Impedance Spectroscopy.
    """

    id: Literal['ps'] = 'ps'
    """Unique method identifier."""
