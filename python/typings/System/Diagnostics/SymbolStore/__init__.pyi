import typing, abc
from System import Guid, Array_1

class ISymbolDocumentWriter(typing.Protocol):
    @abc.abstractmethod
    def SetCheckSum(self, algorithmId: Guid, checkSum: Array_1[int]) -> None: ...
    @abc.abstractmethod
    def SetSource(self, source: Array_1[int]) -> None: ...
