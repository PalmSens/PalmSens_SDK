from __future__ import annotations

from abc import abstractmethod
from typing import ClassVar, Protocol, Type, runtime_checkable

import attrs
from PalmSens import Method as PSMethod


@runtime_checkable
class BaseTechnique(Protocol):
    """Protocol to provide base methods for method classes."""

    __attrs_attrs__: ClassVar[list[attrs.Attribute]] = []
    _id: str
    _registry: dict[str, Type[BaseTechnique]] = {}

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls._registry[cls._id] = cls

    def _to_psmethod(self) -> PSMethod:
        """Convert parameters to dotnet method."""
        psmethod = PSMethod.FromMethodID(self._id)

        self._update_psmethod(obj=psmethod)

        for field in self.__attrs_attrs__:
            attribute = getattr(self, field.name)
            try:
                # Update parameters if attribute has the `update_params` method
                attribute._update_psmethod(obj=psmethod)
            except AttributeError:
                pass

        return psmethod

    @staticmethod
    def _from_psmethod(psmethod: PSMethod) -> BaseTechnique:
        """Generate parameters from dotnet method object."""
        id = psmethod.MethodID

        # cls = ID_TO_PARAMETER_MAPPING[id]
        cls = BaseTechnique._registry[id]

        if cls is None:
            raise NotImplementedError(f'Mapping of {id} parameters is not implemented yet')

        new: BaseTechnique = cls()

        new._update_params(obj=psmethod)

        # new._update_own_params(obj=psmethod)
        # new._update_field_params(obj=psmethod)

        for field in new.__attrs_attrs__:
            attribute = getattr(new, field.name)
            try:
                # Update parameters if attribute has the `update_params` method
                attribute._update_params(obj=psmethod)
            except AttributeError:
                pass

        return new

    @abstractmethod
    def _update_psmethod(self, *, obj: PSMethod) -> None: ...

    @abstractmethod
    def _update_params(self, *, obj: PSMethod) -> None: ...
