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

        self._update_psmethod(psmethod=psmethod)
        self._update_psmethod_nested(psmethod=psmethod)
        return psmethod

    def _update_psmethod_nested(self, *, psmethod):
        """Convert and set field parameters on dotnet method."""
        for field in self.__attrs_attrs__:
            attribute = getattr(self, field.name)
            try:
                # Update parameters if attribute has the `update_params` method
                attribute._update_psmethod(obj=psmethod)
            except AttributeError:
                pass

        return psmethod

    @classmethod
    def from_method_id(cls, id: str) -> BaseTechnique:
        """Create new instance of appropriate technique from method ID."""
        new = cls._registry[id]
        return new()

    @classmethod
    def _from_psmethod(cls, psmethod: PSMethod) -> BaseTechnique:
        """Generate parameters from dotnet method object."""
        new = cls.from_method_id(psmethod.MethodID)
        new._update_params(psmethod=psmethod)
        new._update_params_nested(psmethod=psmethod)
        return new

    def _update_params_nested(self, *, psmethod):
        """Retrieve and convert dotnet method for nested field parameters."""
        for field in self.__attrs_attrs__:
            attribute = getattr(self, field.name)
            try:
                # Update parameters if attribute has the `update_params` method
                attribute._update_params(obj=psmethod)
            except AttributeError:
                pass

    @abstractmethod
    def _update_psmethod(self, *, psmethod: PSMethod) -> None: ...

    @abstractmethod
    def _update_params(self, *, psmethod: PSMethod) -> None: ...
