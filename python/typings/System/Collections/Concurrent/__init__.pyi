import abc
import typing

import clr
from System import Array_1
from System.Collections import ICollection
from System.Collections.Generic import IEnumerable_1, IEnumerator_1, IReadOnlyCollection_1

class ConcurrentQueue_GenericClasses(abc.ABCMeta):
    Generic_ConcurrentQueue_GenericClasses_ConcurrentQueue_1_T = typing.TypeVar(
        'Generic_ConcurrentQueue_GenericClasses_ConcurrentQueue_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_ConcurrentQueue_GenericClasses_ConcurrentQueue_1_T]
    ) -> typing.Type[
        ConcurrentQueue_1[Generic_ConcurrentQueue_GenericClasses_ConcurrentQueue_1_T]
    ]: ...

ConcurrentQueue: ConcurrentQueue_GenericClasses

ConcurrentQueue_1_T = typing.TypeVar('ConcurrentQueue_1_T')

class ConcurrentQueue_1(
    typing.Generic[ConcurrentQueue_1_T],
    IReadOnlyCollection_1[ConcurrentQueue_1_T],
    IProducerConsumerCollection_1[ConcurrentQueue_1_T],
):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, collection: IEnumerable_1[ConcurrentQueue_1_T]) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    def Clear(self) -> None: ...
    def CopyTo(self, array: Array_1[ConcurrentQueue_1_T], index: int) -> None: ...
    def Enqueue(self, item: ConcurrentQueue_1_T) -> None: ...
    def GetEnumerator(self) -> IEnumerator_1[ConcurrentQueue_1_T]: ...
    def ToArray(self) -> Array_1[ConcurrentQueue_1_T]: ...
    def TryDequeue(self, result: clr.Reference[ConcurrentQueue_1_T]) -> bool: ...
    def TryPeek(self, result: clr.Reference[ConcurrentQueue_1_T]) -> bool: ...

class IProducerConsumerCollection_GenericClasses(abc.ABCMeta):
    Generic_IProducerConsumerCollection_GenericClasses_IProducerConsumerCollection_1_T = (
        typing.TypeVar(
            'Generic_IProducerConsumerCollection_GenericClasses_IProducerConsumerCollection_1_T'
        )
    )
    def __getitem__(
        self,
        types: typing.Type[
            Generic_IProducerConsumerCollection_GenericClasses_IProducerConsumerCollection_1_T
        ],
    ) -> typing.Type[
        IProducerConsumerCollection_1[
            Generic_IProducerConsumerCollection_GenericClasses_IProducerConsumerCollection_1_T
        ]
    ]: ...

IProducerConsumerCollection: IProducerConsumerCollection_GenericClasses

IProducerConsumerCollection_1_T = typing.TypeVar('IProducerConsumerCollection_1_T')

class IProducerConsumerCollection_1(
    typing.Generic[IProducerConsumerCollection_1_T],
    ICollection,
    IEnumerable_1[IProducerConsumerCollection_1_T],
    typing.Protocol,
):
    @abc.abstractmethod
    def CopyTo(self, array: Array_1[IProducerConsumerCollection_1_T], index: int) -> None: ...
    @abc.abstractmethod
    def ToArray(self) -> Array_1[IProducerConsumerCollection_1_T]: ...
    @abc.abstractmethod
    def TryAdd(self, item: IProducerConsumerCollection_1_T) -> bool: ...
    @abc.abstractmethod
    def TryTake(self, item: clr.Reference[IProducerConsumerCollection_1_T]) -> bool: ...
