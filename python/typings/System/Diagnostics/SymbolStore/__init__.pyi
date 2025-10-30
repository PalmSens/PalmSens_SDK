import abc
import typing

from System import Array_1, Guid

class ISymbolDocumentWriter(typing.Protocol):
    @abc.abstractmethod
    def SetCheckSum(self, algorithmId: Guid, checkSum: Array_1[int]) -> None: ...
    @abc.abstractmethod
    def SetSource(self, source: Array_1[int]) -> None: ...
