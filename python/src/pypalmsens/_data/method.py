from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Union

import PalmSens

from .._methods.techniques import BaseTechnique


@dataclass(frozen=True)
class Material:
    """Dataclass for material information."""

    surface_area: float
    """Surface area of the sample in cm2."""

    weight: float
    """Equivalent mass of one mole of the sample material in g/mol."""

    density: float
    """Density of the sample in g/cm3."""

    b_anodic: float
    """B anodic in V/dec."""

    b_cathodic: float
    """B cathodic in V/dec."""

    @classmethod
    def _from_psmethod(cls, obj: PalmSens.Method) -> Material:
        """Construct material dataclass from method object."""
        return cls(
            surface_area=obj.Area,
            weight=obj.Weight,
            density=obj.Density,
            b_anodic=obj.Ba,
            b_cathodic=obj.Bc,
        )


class Method:
    """Wrapper for PalmSens.Method."""

    def __init__(self, *, psmethod: PalmSens.Method):
        self._psmethod = psmethod

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, id={self.id!r})'

    @property
    def id(self) -> str:
        """Unique id for method."""
        return self._psmethod.MethodID

    @property
    def name(self) -> str:
        """Name for the technique."""
        return self._psmethod.Name

    @property
    def short_name(self) -> str:
        """Short name for the technique."""
        return self._psmethod.ShortName

    @property
    def filename(self) -> Union[Path, None]:
        """Filename for the method if applicable."""
        fn = self._psmethod.MethodFilename
        if fn:
            return Path(fn)
        return None

    @property
    def material(self) -> Material:
        """Return dataclass with material information used for corrosion measurements."""
        return Material._from_psmethod(self._psmethod)

    def get_estimated_duration(self, *, instrument_manager=None):
        """Get the estimated duration for this method.

        Parameters
        ----------
        instrument_manager : InstrumentManager
            Specifies the instrument manager to get the connected instruments capabilities from,
            If not specified it will use the PalmSens4 capabilities to determine the estimated duration.
        """
        if instrument_manager is None or instrument_manager.__comm is None:
            instrument_capabilities = PalmSens.Devices.PalmSens4Capabilities()
        else:
            instrument_capabilities = instrument_manager.__comm.Capabilities
        return self._psmethod.GetMinimumEstimatedMeasurementDuration(instrument_capabilities)

    @property
    def technique_number(self) -> int:
        """The technique number used in the firmware."""
        return self._psmethod.Technique

    def to_settings(self) -> BaseTechnique:
        """Extract techniques parameters as dataclass."""
        return BaseTechnique._from_psmethod(self._psmethod)

    def to_dict(self) -> dict[str, Any]:
        """Return dictionary with technique parameters."""
        return self.to_settings().model_dump()
