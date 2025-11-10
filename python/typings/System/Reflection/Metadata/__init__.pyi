import typing, clr, abc
from System.Reflection import Assembly
from System import Attribute, ReadOnlySpan_1

class AssemblyExtensions(abc.ABC):
    @staticmethod
    def TryGetRawMetadata(assembly: Assembly, blob: clr.Reference[clr.Reference[int]], length: clr.Reference[int]) -> bool: ...


class MetadataUpdateHandlerAttribute(Attribute):
    def __init__(self, handlerType: typing.Type[typing.Any]) -> None: ...
    @property
    def HandlerType(self) -> typing.Type[typing.Any]: ...
    @property
    def TypeId(self) -> typing.Any: ...


class MetadataUpdater(abc.ABC):
    @classmethod
    @property
    def IsSupported(cls) -> bool: ...
    @staticmethod
    def ApplyUpdate(assembly: Assembly, metadataDelta: ReadOnlySpan_1[int], ilDelta: ReadOnlySpan_1[int], pdbDelta: ReadOnlySpan_1[int]) -> None: ...
