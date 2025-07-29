from dataclasses import asdict
from typing import Any

from PalmSens import Method as PSMethod

from . import techniques


def _method_ids() -> list[str]:
    """Return list of all possible method ids."""
    return list(PSMethod.MethodIds)


def _method_ids_by_technique_id() -> dict[int, list[str]]:
    """Unique id for method."""
    return {k: list(v) for k, v in dict(PSMethod.MethodIdsByTechniqueId).items()}


class Method:
    def __init__(self, *, psmethod):
        self.psmethod = psmethod

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, id={self.id!r})'

    @property
    def id(self) -> str:
        """Unique id for method."""
        return self.psmethod.MethodID

    @property
    def name(self) -> str:
        """Name for the technique."""
        return self.psmethod.Name

    @property
    def short_name(self) -> str:
        """Short name for the technique."""
        return self.psmethod.ShortName

    @property
    def technique_number(self) -> int:
        """The technique number used in the firmware."""
        return self.psmethod.Technique

    def to_parameters(self):
        """Extract techniques parameters as dataclass."""
        return techniques.psmethod_to_parameters(psmethod=self.psmethod)

    def to_dict(self) -> dict[str, Any]:
        """Return dictionary with technique parameters."""
        return asdict(self.to_parameters())
