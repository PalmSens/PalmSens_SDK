import abc
import typing

import clr
from System import Array_1
from System.Collections import ICollection, IDictionary, IList
from System.Collections.Generic import (
    ICollection_1,
    IDictionary_2,
    IEnumerator_1,
    IEqualityComparer_1,
    IList_1,
    IReadOnlyCollection_1,
    IReadOnlyDictionary_2,
    IReadOnlyList_1,
    KeyValuePair_2,
)

class Collection_GenericClasses(abc.ABCMeta):
    Generic_Collection_GenericClasses_Collection_1_T = typing.TypeVar(
        'Generic_Collection_GenericClasses_Collection_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_Collection_GenericClasses_Collection_1_T]
    ) -> typing.Type[Collection_1[Generic_Collection_GenericClasses_Collection_1_T]]: ...

Collection: Collection_GenericClasses

Collection_1_T = typing.TypeVar('Collection_1_T')

class Collection_1(
    typing.Generic[Collection_1_T],
    IReadOnlyList_1[Collection_1_T],
    IList_1[Collection_1_T],
    IList,
):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, list: IList_1[Collection_1_T]) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> Collection_1_T: ...
    @Item.setter
    def Item(self, value: Collection_1_T) -> Collection_1_T: ...
    def Add(self, item: Collection_1_T) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, item: Collection_1_T) -> bool: ...
    def CopyTo(self, array: Array_1[Collection_1_T], index: int) -> None: ...
    def GetEnumerator(self) -> IEnumerator_1[Collection_1_T]: ...
    def IndexOf(self, item: Collection_1_T) -> int: ...
    def Insert(self, index: int, item: Collection_1_T) -> None: ...
    def Remove(self, item: Collection_1_T) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...

class KeyedCollection_GenericClasses(abc.ABCMeta):
    Generic_KeyedCollection_GenericClasses_KeyedCollection_2_TKey = typing.TypeVar(
        'Generic_KeyedCollection_GenericClasses_KeyedCollection_2_TKey'
    )
    Generic_KeyedCollection_GenericClasses_KeyedCollection_2_TItem = typing.TypeVar(
        'Generic_KeyedCollection_GenericClasses_KeyedCollection_2_TItem'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[Generic_KeyedCollection_GenericClasses_KeyedCollection_2_TKey],
            typing.Type[Generic_KeyedCollection_GenericClasses_KeyedCollection_2_TItem],
        ],
    ) -> typing.Type[
        KeyedCollection_2[
            Generic_KeyedCollection_GenericClasses_KeyedCollection_2_TKey,
            Generic_KeyedCollection_GenericClasses_KeyedCollection_2_TItem,
        ]
    ]: ...

KeyedCollection: KeyedCollection_GenericClasses

KeyedCollection_2_TKey = typing.TypeVar('KeyedCollection_2_TKey')
KeyedCollection_2_TItem = typing.TypeVar('KeyedCollection_2_TItem')

class KeyedCollection_2(
    typing.Generic[KeyedCollection_2_TKey, KeyedCollection_2_TItem],
    Collection_1[KeyedCollection_2_TItem],
    abc.ABC,
):
    @property
    def Comparer(self) -> IEqualityComparer_1[KeyedCollection_2_TKey]: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> KeyedCollection_2_TItem: ...
    @property
    def Item(self) -> KeyedCollection_2_TItem: ...
    @Item.setter
    def Item(self, value: KeyedCollection_2_TItem) -> KeyedCollection_2_TItem: ...
    def Contains(self, key: KeyedCollection_2_TKey) -> bool: ...
    def Remove(self, key: KeyedCollection_2_TKey) -> bool: ...
    def TryGetValue(
        self, key: KeyedCollection_2_TKey, item: clr.Reference[KeyedCollection_2_TItem]
    ) -> bool: ...

class ReadOnlyCollection_GenericClasses(abc.ABCMeta):
    Generic_ReadOnlyCollection_GenericClasses_ReadOnlyCollection_1_T = typing.TypeVar(
        'Generic_ReadOnlyCollection_GenericClasses_ReadOnlyCollection_1_T'
    )
    def __getitem__(
        self,
        types: typing.Type[Generic_ReadOnlyCollection_GenericClasses_ReadOnlyCollection_1_T],
    ) -> typing.Type[
        ReadOnlyCollection_1[Generic_ReadOnlyCollection_GenericClasses_ReadOnlyCollection_1_T]
    ]: ...

ReadOnlyCollection: ReadOnlyCollection_GenericClasses

ReadOnlyCollection_1_T = typing.TypeVar('ReadOnlyCollection_1_T')

class ReadOnlyCollection_1(
    typing.Generic[ReadOnlyCollection_1_T],
    IReadOnlyList_1[ReadOnlyCollection_1_T],
    IList_1[ReadOnlyCollection_1_T],
    IList,
):
    def __init__(self, list: IList_1[ReadOnlyCollection_1_T]) -> None: ...
    @property
    def Count(self) -> int: ...
    @classmethod
    @property
    def Empty(cls) -> ReadOnlyCollection_1[ReadOnlyCollection_1_T]: ...
    @property
    def Item(self) -> ReadOnlyCollection_1_T: ...
    def Contains(self, value: ReadOnlyCollection_1_T) -> bool: ...
    def CopyTo(self, array: Array_1[ReadOnlyCollection_1_T], index: int) -> None: ...
    def GetEnumerator(self) -> IEnumerator_1[ReadOnlyCollection_1_T]: ...
    def IndexOf(self, value: ReadOnlyCollection_1_T) -> int: ...

class ReadOnlyDictionary_GenericClasses(abc.ABCMeta):
    Generic_ReadOnlyDictionary_GenericClasses_ReadOnlyDictionary_2_TKey = typing.TypeVar(
        'Generic_ReadOnlyDictionary_GenericClasses_ReadOnlyDictionary_2_TKey'
    )
    Generic_ReadOnlyDictionary_GenericClasses_ReadOnlyDictionary_2_TValue = typing.TypeVar(
        'Generic_ReadOnlyDictionary_GenericClasses_ReadOnlyDictionary_2_TValue'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[Generic_ReadOnlyDictionary_GenericClasses_ReadOnlyDictionary_2_TKey],
            typing.Type[Generic_ReadOnlyDictionary_GenericClasses_ReadOnlyDictionary_2_TValue],
        ],
    ) -> typing.Type[
        ReadOnlyDictionary_2[
            Generic_ReadOnlyDictionary_GenericClasses_ReadOnlyDictionary_2_TKey,
            Generic_ReadOnlyDictionary_GenericClasses_ReadOnlyDictionary_2_TValue,
        ]
    ]: ...

ReadOnlyDictionary: ReadOnlyDictionary_GenericClasses

ReadOnlyDictionary_2_TKey = typing.TypeVar('ReadOnlyDictionary_2_TKey')
ReadOnlyDictionary_2_TValue = typing.TypeVar('ReadOnlyDictionary_2_TValue')

class ReadOnlyDictionary_2(
    typing.Generic[ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue],
    IReadOnlyDictionary_2[ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue],
    IDictionary_2[ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue],
    IDictionary,
):
    def __init__(
        self, dictionary: IDictionary_2[ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue]
    ) -> None: ...

    KeyCollection_GenericClasses_ReadOnlyDictionary_2_TKey = typing.TypeVar(
        'KeyCollection_GenericClasses_ReadOnlyDictionary_2_TKey'
    )
    KeyCollection_GenericClasses_ReadOnlyDictionary_2_TValue = typing.TypeVar(
        'KeyCollection_GenericClasses_ReadOnlyDictionary_2_TValue'
    )
    class KeyCollection_GenericClasses(
        typing.Generic[
            KeyCollection_GenericClasses_ReadOnlyDictionary_2_TKey,
            KeyCollection_GenericClasses_ReadOnlyDictionary_2_TValue,
        ],
        abc.ABCMeta,
    ):
        KeyCollection_GenericClasses_ReadOnlyDictionary_2_TKey = (
            ReadOnlyDictionary_2.KeyCollection_GenericClasses_ReadOnlyDictionary_2_TKey
        )
        KeyCollection_GenericClasses_ReadOnlyDictionary_2_TValue = (
            ReadOnlyDictionary_2.KeyCollection_GenericClasses_ReadOnlyDictionary_2_TValue
        )
        def __call__(
            self,
        ) -> ReadOnlyDictionary_2.KeyCollection_2[
            KeyCollection_GenericClasses_ReadOnlyDictionary_2_TKey,
            KeyCollection_GenericClasses_ReadOnlyDictionary_2_TValue,
        ]: ...

    KeyCollection: KeyCollection_GenericClasses[
        ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue
    ]

    KeyCollection_2_TKey = typing.TypeVar('KeyCollection_2_TKey')
    KeyCollection_2_TValue = typing.TypeVar('KeyCollection_2_TValue')
    class KeyCollection_2(
        typing.Generic[KeyCollection_2_TKey, KeyCollection_2_TValue],
        IReadOnlyCollection_1[KeyCollection_2_TKey],
        ICollection_1[KeyCollection_2_TKey],
        ICollection,
    ):
        KeyCollection_2_TKey = ReadOnlyDictionary_2.KeyCollection_2_TKey
        KeyCollection_2_TValue = ReadOnlyDictionary_2.KeyCollection_2_TValue
        @property
        def Count(self) -> int: ...
        def Contains(self, item: KeyCollection_2_TKey) -> bool: ...
        def CopyTo(self, array: Array_1[KeyCollection_2_TKey], arrayIndex: int) -> None: ...
        def GetEnumerator(self) -> IEnumerator_1[KeyCollection_2_TKey]: ...

    ValueCollection_GenericClasses_ReadOnlyDictionary_2_TKey = typing.TypeVar(
        'ValueCollection_GenericClasses_ReadOnlyDictionary_2_TKey'
    )
    ValueCollection_GenericClasses_ReadOnlyDictionary_2_TValue = typing.TypeVar(
        'ValueCollection_GenericClasses_ReadOnlyDictionary_2_TValue'
    )
    class ValueCollection_GenericClasses(
        typing.Generic[
            ValueCollection_GenericClasses_ReadOnlyDictionary_2_TKey,
            ValueCollection_GenericClasses_ReadOnlyDictionary_2_TValue,
        ],
        abc.ABCMeta,
    ):
        ValueCollection_GenericClasses_ReadOnlyDictionary_2_TKey = (
            ReadOnlyDictionary_2.ValueCollection_GenericClasses_ReadOnlyDictionary_2_TKey
        )
        ValueCollection_GenericClasses_ReadOnlyDictionary_2_TValue = (
            ReadOnlyDictionary_2.ValueCollection_GenericClasses_ReadOnlyDictionary_2_TValue
        )
        def __call__(
            self,
        ) -> ReadOnlyDictionary_2.ValueCollection_2[
            ValueCollection_GenericClasses_ReadOnlyDictionary_2_TKey,
            ValueCollection_GenericClasses_ReadOnlyDictionary_2_TValue,
        ]: ...

    ValueCollection: ValueCollection_GenericClasses[
        ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue
    ]

    ValueCollection_2_TKey = typing.TypeVar('ValueCollection_2_TKey')
    ValueCollection_2_TValue = typing.TypeVar('ValueCollection_2_TValue')
    class ValueCollection_2(
        typing.Generic[ValueCollection_2_TKey, ValueCollection_2_TValue],
        IReadOnlyCollection_1[ValueCollection_2_TValue],
        ICollection_1[ValueCollection_2_TValue],
        ICollection,
    ):
        ValueCollection_2_TKey = ReadOnlyDictionary_2.ValueCollection_2_TKey
        ValueCollection_2_TValue = ReadOnlyDictionary_2.ValueCollection_2_TValue
        @property
        def Count(self) -> int: ...
        def CopyTo(self, array: Array_1[ValueCollection_2_TValue], arrayIndex: int) -> None: ...
        def GetEnumerator(self) -> IEnumerator_1[ValueCollection_2_TValue]: ...

    @property
    def Count(self) -> int: ...
    @classmethod
    @property
    def Empty(
        cls,
    ) -> ReadOnlyDictionary_2[ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue]: ...
    @property
    def Item(self) -> ReadOnlyDictionary_2_TValue: ...
    @property
    def Keys(
        self,
    ) -> KeyCollection_2[ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue]: ...
    @property
    def Values(
        self,
    ) -> ValueCollection_2[ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue]: ...
    def ContainsKey(self, key: ReadOnlyDictionary_2_TKey) -> bool: ...
    def GetEnumerator(
        self,
    ) -> IEnumerator_1[
        KeyValuePair_2[ReadOnlyDictionary_2_TKey, ReadOnlyDictionary_2_TValue]
    ]: ...
    def TryGetValue(
        self, key: ReadOnlyDictionary_2_TKey, value: clr.Reference[ReadOnlyDictionary_2_TValue]
    ) -> bool: ...
