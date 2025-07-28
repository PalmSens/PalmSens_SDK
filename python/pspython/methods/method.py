from dataclasses import asdict
from typing import Any

from PalmSens import Method as PSMethod

from . import techniques

ID_TO_PARAMETER_MAPPING = {
    'acv': None,
    'ad': techniques.ChronoAmperometryParameters,
    'cc': None,
    'cp': techniques.ChronopotentiometryParameters,
    'cpot': None,
    'cv': techniques.CyclicVoltammetryParameters,
    'dpv': techniques.DifferentialPulseParameters,
    'eis': techniques.ElectrochemicalImpedanceSpectroscopyParameters,
    'fam': None,
    'fcv': None,
    'fgis': None,
    'fis': None,
    'gis': techniques.GalvanostaticImpedanceSpectroscopyParameters,
    'gs': None,
    'lp': None,
    'lsp': None,
    'lsv': techniques.LinearSweepParameters,
    'ma': None,
    'mm': None,
    'mp': None,
    'mpad': None,
    'ms': techniques.MultiStepAmperometryParameters,
    'npv': None,
    'ocp': techniques.OpenCircuitPotentiometryParameters,
    'pad': None,
    'pot': None,
    'ps': None,
    'scp': None,
    'swv': techniques.SquareWaveParameters,
}


def method_ids() -> list[str]:
    """Return list of all possible method ids."""
    return list(PSMethod.MethodIds)


def method_ids_by_technique_id() -> dict[int, list[str]]:
    """Unique id for method."""

    return {k: list(v) for k, v in dict(PSMethod.MethodIdsByTechniqueId).items()}


class Method:
    def __init__(self, *, psobj):
        self.psobj = psobj

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, id={self.id!r})'

    @property
    def id(self) -> str:
        """Unique id for method."""
        return self.psobj.MethodID

    @property
    def name(self) -> str:
        """Name for the technique."""
        return self.psobj.Name

    @property
    def short_name(self) -> str:
        """Short name for the technique."""
        return self.psobj.ShortName

    @property
    def technique(self) -> int:
        """
        The technique number used in the firmware
        """
        return self.psobj.Technique

    @property
    def notes(self) -> str:
        """
        Some user notes for use with this method
        """
        return self.psobj.Notes

    def to_parameters(self) -> techniques.BaseParameters:
        """Return parameters class."""
        cls = ID_TO_PARAMETER_MAPPING[self.id]
        if not cls:
            raise NotImplementedError(f'Method {self.id} is not implemented yet')
        return cls.from_method(self)

    def to_dict(self) -> dict[str, Any]:
        """Return dictionary with method properties."""
        return self.to_parameters().__dict__
        asdict(self.to_parameters())
