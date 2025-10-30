import abc
import typing

import clr
import System.Collections
from System import (
    Action_1,
    Array_1,
    Comparison_1,
    Converter_2,
    Exception,
    Func_2,
    Func_3,
    IAsyncDisposable,
    IDisposable,
    Predicate_1,
    ReadOnlySpan_1,
    Span_1,
    SystemException,
)
from System.Collections import (
    ICollection,
    IComparer,
    IDictionary,
    IDictionaryEnumerator,
    IEnumerable,
    IEnumerator,
    IEqualityComparer,
    IList,
)
from System.Collections.ObjectModel import ReadOnlyCollection_1, ReadOnlyDictionary_2
from System.Reflection import MethodBase
from System.Runtime.Serialization import (
    IDeserializationCallback,
    ISerializable,
    SerializationInfo,
    StreamingContext,
)
from System.Threading import CancellationToken
from System.Threading.Tasks import ValueTask_1

class ByteEqualityComparer(EqualityComparer_1[int]):
    def __init__(self) -> None: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...
        @typing.overload
        def __call__(self, x: int, y: int) -> bool: ...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode: GetHashCode_MethodGroup
    class GetHashCode_MethodGroup:
        @typing.overload
        def __call__(self) -> int: ...
        @typing.overload
        def __call__(self, b: int) -> int: ...

class CollectionExtensions(abc.ABC):
    # Skipped AddRange due to it being static, abstract and generic.

    AddRange: AddRange_MethodGroup
    class AddRange_MethodGroup:
        def __getitem__(self, t: typing.Type[AddRange_1_T1]) -> AddRange_1[AddRange_1_T1]: ...

        AddRange_1_T1 = typing.TypeVar('AddRange_1_T1')
        class AddRange_1(typing.Generic[AddRange_1_T1]):
            AddRange_1_T = CollectionExtensions.AddRange_MethodGroup.AddRange_1_T1
            def __call__(
                self, list: List_1[AddRange_1_T], source: ReadOnlySpan_1[AddRange_1_T]
            ) -> None: ...

    # Skipped AsReadOnly due to it being static, abstract and generic.

    AsReadOnly: AsReadOnly_MethodGroup
    class AsReadOnly_MethodGroup:
        @typing.overload
        def __getitem__(
            self, t: typing.Tuple[typing.Type[AsReadOnly_2_T1], typing.Type[AsReadOnly_2_T2]]
        ) -> AsReadOnly_2[AsReadOnly_2_T1, AsReadOnly_2_T2]: ...

        AsReadOnly_2_T1 = typing.TypeVar('AsReadOnly_2_T1')
        AsReadOnly_2_T2 = typing.TypeVar('AsReadOnly_2_T2')
        class AsReadOnly_2(typing.Generic[AsReadOnly_2_T1, AsReadOnly_2_T2]):
            AsReadOnly_2_TKey = CollectionExtensions.AsReadOnly_MethodGroup.AsReadOnly_2_T1
            AsReadOnly_2_TValue = CollectionExtensions.AsReadOnly_MethodGroup.AsReadOnly_2_T2
            def __call__(
                self, dictionary: IDictionary_2[AsReadOnly_2_TKey, AsReadOnly_2_TValue]
            ) -> ReadOnlyDictionary_2[AsReadOnly_2_TKey, AsReadOnly_2_TValue]: ...

        @typing.overload
        def __getitem__(
            self, t: typing.Type[AsReadOnly_1_T1]
        ) -> AsReadOnly_1[AsReadOnly_1_T1]: ...

        AsReadOnly_1_T1 = typing.TypeVar('AsReadOnly_1_T1')
        class AsReadOnly_1(typing.Generic[AsReadOnly_1_T1]):
            AsReadOnly_1_T = CollectionExtensions.AsReadOnly_MethodGroup.AsReadOnly_1_T1
            def __call__(
                self, list: IList_1[AsReadOnly_1_T]
            ) -> ReadOnlyCollection_1[AsReadOnly_1_T]: ...

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo: CopyTo_MethodGroup
    class CopyTo_MethodGroup:
        def __getitem__(self, t: typing.Type[CopyTo_1_T1]) -> CopyTo_1[CopyTo_1_T1]: ...

        CopyTo_1_T1 = typing.TypeVar('CopyTo_1_T1')
        class CopyTo_1(typing.Generic[CopyTo_1_T1]):
            CopyTo_1_T = CollectionExtensions.CopyTo_MethodGroup.CopyTo_1_T1
            def __call__(
                self, list: List_1[CopyTo_1_T], destination: Span_1[CopyTo_1_T]
            ) -> None: ...

    # Skipped GetValueOrDefault due to it being static, abstract and generic.

    GetValueOrDefault: GetValueOrDefault_MethodGroup
    class GetValueOrDefault_MethodGroup:
        def __getitem__(
            self,
            t: typing.Tuple[
                typing.Type[GetValueOrDefault_2_T1], typing.Type[GetValueOrDefault_2_T2]
            ],
        ) -> GetValueOrDefault_2[GetValueOrDefault_2_T1, GetValueOrDefault_2_T2]: ...

        GetValueOrDefault_2_T1 = typing.TypeVar('GetValueOrDefault_2_T1')
        GetValueOrDefault_2_T2 = typing.TypeVar('GetValueOrDefault_2_T2')
        class GetValueOrDefault_2(
            typing.Generic[GetValueOrDefault_2_T1, GetValueOrDefault_2_T2]
        ):
            GetValueOrDefault_2_TKey = (
                CollectionExtensions.GetValueOrDefault_MethodGroup.GetValueOrDefault_2_T1
            )
            GetValueOrDefault_2_TValue = (
                CollectionExtensions.GetValueOrDefault_MethodGroup.GetValueOrDefault_2_T2
            )
            @typing.overload
            def __call__(
                self,
                dictionary: IReadOnlyDictionary_2[
                    GetValueOrDefault_2_TKey, GetValueOrDefault_2_TValue
                ],
                key: GetValueOrDefault_2_TKey,
            ) -> GetValueOrDefault_2_TValue: ...
            @typing.overload
            def __call__(
                self,
                dictionary: IReadOnlyDictionary_2[
                    GetValueOrDefault_2_TKey, GetValueOrDefault_2_TValue
                ],
                key: GetValueOrDefault_2_TKey,
                defaultValue: GetValueOrDefault_2_TValue,
            ) -> GetValueOrDefault_2_TValue: ...

    # Skipped InsertRange due to it being static, abstract and generic.

    InsertRange: InsertRange_MethodGroup
    class InsertRange_MethodGroup:
        def __getitem__(
            self, t: typing.Type[InsertRange_1_T1]
        ) -> InsertRange_1[InsertRange_1_T1]: ...

        InsertRange_1_T1 = typing.TypeVar('InsertRange_1_T1')
        class InsertRange_1(typing.Generic[InsertRange_1_T1]):
            InsertRange_1_T = CollectionExtensions.InsertRange_MethodGroup.InsertRange_1_T1
            def __call__(
                self,
                list: List_1[InsertRange_1_T],
                index: int,
                source: ReadOnlySpan_1[InsertRange_1_T],
            ) -> None: ...

    # Skipped Remove due to it being static, abstract and generic.

    Remove: Remove_MethodGroup
    class Remove_MethodGroup:
        def __getitem__(
            self, t: typing.Tuple[typing.Type[Remove_2_T1], typing.Type[Remove_2_T2]]
        ) -> Remove_2[Remove_2_T1, Remove_2_T2]: ...

        Remove_2_T1 = typing.TypeVar('Remove_2_T1')
        Remove_2_T2 = typing.TypeVar('Remove_2_T2')
        class Remove_2(typing.Generic[Remove_2_T1, Remove_2_T2]):
            Remove_2_TKey = CollectionExtensions.Remove_MethodGroup.Remove_2_T1
            Remove_2_TValue = CollectionExtensions.Remove_MethodGroup.Remove_2_T2
            def __call__(
                self,
                dictionary: IDictionary_2[Remove_2_TKey, Remove_2_TValue],
                key: Remove_2_TKey,
                value: clr.Reference[Remove_2_TValue],
            ) -> bool: ...

    # Skipped TryAdd due to it being static, abstract and generic.

    TryAdd: TryAdd_MethodGroup
    class TryAdd_MethodGroup:
        def __getitem__(
            self, t: typing.Tuple[typing.Type[TryAdd_2_T1], typing.Type[TryAdd_2_T2]]
        ) -> TryAdd_2[TryAdd_2_T1, TryAdd_2_T2]: ...

        TryAdd_2_T1 = typing.TypeVar('TryAdd_2_T1')
        TryAdd_2_T2 = typing.TypeVar('TryAdd_2_T2')
        class TryAdd_2(typing.Generic[TryAdd_2_T1, TryAdd_2_T2]):
            TryAdd_2_TKey = CollectionExtensions.TryAdd_MethodGroup.TryAdd_2_T1
            TryAdd_2_TValue = CollectionExtensions.TryAdd_MethodGroup.TryAdd_2_T2
            def __call__(
                self,
                dictionary: IDictionary_2[TryAdd_2_TKey, TryAdd_2_TValue],
                key: TryAdd_2_TKey,
                value: TryAdd_2_TValue,
            ) -> bool: ...

class Comparer_GenericClasses(abc.ABCMeta):
    Generic_Comparer_GenericClasses_Comparer_1_T = typing.TypeVar(
        'Generic_Comparer_GenericClasses_Comparer_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_Comparer_GenericClasses_Comparer_1_T]
    ) -> typing.Type[Comparer_1[Generic_Comparer_GenericClasses_Comparer_1_T]]: ...

Comparer: Comparer_GenericClasses

Comparer_1_T = typing.TypeVar('Comparer_1_T')

class Comparer_1(typing.Generic[Comparer_1_T], IComparer_1[Comparer_1_T], IComparer, abc.ABC):
    @classmethod
    @property
    def Default(cls) -> Comparer_1[Comparer_1_T]: ...
    @abc.abstractmethod
    def Compare(self, x: Comparer_1_T, y: Comparer_1_T) -> int: ...
    @staticmethod
    def Create(comparison: Comparison_1[Comparer_1_T]) -> Comparer_1[Comparer_1_T]: ...

class Dictionary_GenericClasses(abc.ABCMeta):
    Generic_Dictionary_GenericClasses_Dictionary_2_TKey = typing.TypeVar(
        'Generic_Dictionary_GenericClasses_Dictionary_2_TKey'
    )
    Generic_Dictionary_GenericClasses_Dictionary_2_TValue = typing.TypeVar(
        'Generic_Dictionary_GenericClasses_Dictionary_2_TValue'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[Generic_Dictionary_GenericClasses_Dictionary_2_TKey],
            typing.Type[Generic_Dictionary_GenericClasses_Dictionary_2_TValue],
        ],
    ) -> typing.Type[
        Dictionary_2[
            Generic_Dictionary_GenericClasses_Dictionary_2_TKey,
            Generic_Dictionary_GenericClasses_Dictionary_2_TValue,
        ]
    ]: ...

Dictionary: Dictionary_GenericClasses

Dictionary_2_TKey = typing.TypeVar('Dictionary_2_TKey')
Dictionary_2_TValue = typing.TypeVar('Dictionary_2_TValue')

class Dictionary_2(
    typing.Generic[Dictionary_2_TKey, Dictionary_2_TValue],
    IReadOnlyDictionary_2[Dictionary_2_TKey, Dictionary_2_TValue],
    IDictionary_2[Dictionary_2_TKey, Dictionary_2_TValue],
    IDictionary,
    IDeserializationCallback,
    ISerializable,
):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, capacity: int) -> None: ...
    @typing.overload
    def __init__(
        self, capacity: int, comparer: IEqualityComparer_1[Dictionary_2_TKey]
    ) -> None: ...
    @typing.overload
    def __init__(
        self, collection: IEnumerable_1[KeyValuePair_2[Dictionary_2_TKey, Dictionary_2_TValue]]
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        collection: IEnumerable_1[KeyValuePair_2[Dictionary_2_TKey, Dictionary_2_TValue]],
        comparer: IEqualityComparer_1[Dictionary_2_TKey],
    ) -> None: ...
    @typing.overload
    def __init__(self, comparer: IEqualityComparer_1[Dictionary_2_TKey]) -> None: ...
    @typing.overload
    def __init__(
        self, dictionary: IDictionary_2[Dictionary_2_TKey, Dictionary_2_TValue]
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        dictionary: IDictionary_2[Dictionary_2_TKey, Dictionary_2_TValue],
        comparer: IEqualityComparer_1[Dictionary_2_TKey],
    ) -> None: ...

    Enumerator_GenericClasses_Dictionary_2_TKey = typing.TypeVar(
        'Enumerator_GenericClasses_Dictionary_2_TKey'
    )
    Enumerator_GenericClasses_Dictionary_2_TValue = typing.TypeVar(
        'Enumerator_GenericClasses_Dictionary_2_TValue'
    )
    class Enumerator_GenericClasses(
        typing.Generic[
            Enumerator_GenericClasses_Dictionary_2_TKey,
            Enumerator_GenericClasses_Dictionary_2_TValue,
        ],
        abc.ABCMeta,
    ):
        Enumerator_GenericClasses_Dictionary_2_TKey = (
            Dictionary_2.Enumerator_GenericClasses_Dictionary_2_TKey
        )
        Enumerator_GenericClasses_Dictionary_2_TValue = (
            Dictionary_2.Enumerator_GenericClasses_Dictionary_2_TValue
        )
        def __call__(
            self,
        ) -> Dictionary_2.Enumerator_2[
            Enumerator_GenericClasses_Dictionary_2_TKey,
            Enumerator_GenericClasses_Dictionary_2_TValue,
        ]: ...

    Enumerator: Enumerator_GenericClasses[Dictionary_2_TKey, Dictionary_2_TValue]

    Enumerator_2_TKey = typing.TypeVar('Enumerator_2_TKey')
    Enumerator_2_TValue = typing.TypeVar('Enumerator_2_TValue')
    class Enumerator_2(
        typing.Generic[Enumerator_2_TKey, Enumerator_2_TValue],
        IDictionaryEnumerator,
        IEnumerator_1[KeyValuePair_2[Enumerator_2_TKey, Enumerator_2_TValue]],
    ):
        Enumerator_2_TKey = Dictionary_2.Enumerator_2_TKey
        Enumerator_2_TValue = Dictionary_2.Enumerator_2_TValue
        @property
        def Current(self) -> KeyValuePair_2[Enumerator_2_TKey, Enumerator_2_TValue]: ...
        def Dispose(self) -> None: ...
        def MoveNext(self) -> bool: ...

    KeyCollection_GenericClasses_Dictionary_2_TKey = typing.TypeVar(
        'KeyCollection_GenericClasses_Dictionary_2_TKey'
    )
    KeyCollection_GenericClasses_Dictionary_2_TValue = typing.TypeVar(
        'KeyCollection_GenericClasses_Dictionary_2_TValue'
    )
    class KeyCollection_GenericClasses(
        typing.Generic[
            KeyCollection_GenericClasses_Dictionary_2_TKey,
            KeyCollection_GenericClasses_Dictionary_2_TValue,
        ],
        abc.ABCMeta,
    ):
        KeyCollection_GenericClasses_Dictionary_2_TKey = (
            Dictionary_2.KeyCollection_GenericClasses_Dictionary_2_TKey
        )
        KeyCollection_GenericClasses_Dictionary_2_TValue = (
            Dictionary_2.KeyCollection_GenericClasses_Dictionary_2_TValue
        )
        def __call__(
            self,
        ) -> Dictionary_2.KeyCollection_2[
            KeyCollection_GenericClasses_Dictionary_2_TKey,
            KeyCollection_GenericClasses_Dictionary_2_TValue,
        ]: ...

    KeyCollection: KeyCollection_GenericClasses[Dictionary_2_TKey, Dictionary_2_TValue]

    KeyCollection_2_TKey = typing.TypeVar('KeyCollection_2_TKey')
    KeyCollection_2_TValue = typing.TypeVar('KeyCollection_2_TValue')
    class KeyCollection_2(
        typing.Generic[KeyCollection_2_TKey, KeyCollection_2_TValue],
        IReadOnlyCollection_1[KeyCollection_2_TKey],
        ICollection_1[KeyCollection_2_TKey],
        ICollection,
    ):
        KeyCollection_2_TKey = Dictionary_2.KeyCollection_2_TKey
        KeyCollection_2_TValue = Dictionary_2.KeyCollection_2_TValue
        def __init__(
            self, dictionary: Dictionary_2[KeyCollection_2_TKey, KeyCollection_2_TValue]
        ) -> None: ...

        Enumerator_GenericClasses_KeyCollection_2_TKey = typing.TypeVar(
            'Enumerator_GenericClasses_KeyCollection_2_TKey'
        )
        Enumerator_GenericClasses_KeyCollection_2_TValue = typing.TypeVar(
            'Enumerator_GenericClasses_KeyCollection_2_TValue'
        )
        class Enumerator_GenericClasses(
            typing.Generic[
                Enumerator_GenericClasses_KeyCollection_2_TKey,
                Enumerator_GenericClasses_KeyCollection_2_TValue,
            ],
            abc.ABCMeta,
        ):
            Enumerator_GenericClasses_KeyCollection_2_TKey = (
                Dictionary_2.KeyCollection_2.Enumerator_GenericClasses_KeyCollection_2_TKey
            )
            Enumerator_GenericClasses_KeyCollection_2_TValue = (
                Dictionary_2.KeyCollection_2.Enumerator_GenericClasses_KeyCollection_2_TValue
            )
            def __call__(
                self,
            ) -> Dictionary_2.KeyCollection_2.Enumerator_2[
                Enumerator_GenericClasses_KeyCollection_2_TKey,
                Enumerator_GenericClasses_KeyCollection_2_TValue,
            ]: ...

        Enumerator: Enumerator_GenericClasses[KeyCollection_2_TKey, KeyCollection_2_TValue]

        Enumerator_2_TKey = typing.TypeVar('Enumerator_2_TKey')
        Enumerator_2_TValue = typing.TypeVar('Enumerator_2_TValue')
        class Enumerator_2(
            typing.Generic[Enumerator_2_TKey, Enumerator_2_TValue],
            IEnumerator_1[Enumerator_2_TKey],
        ):
            Enumerator_2_TKey = Dictionary_2.KeyCollection_2.Enumerator_2_TKey
            Enumerator_2_TValue = Dictionary_2.KeyCollection_2.Enumerator_2_TValue
            @property
            def Current(self) -> Enumerator_2_TKey: ...
            def Dispose(self) -> None: ...
            def MoveNext(self) -> bool: ...

        @property
        def Count(self) -> int: ...
        def Contains(self, item: KeyCollection_2_TKey) -> bool: ...
        def CopyTo(self, array: Array_1[KeyCollection_2_TKey], index: int) -> None: ...
        def GetEnumerator(
            self,
        ) -> Dictionary_2.KeyCollection_2.Enumerator_2[
            KeyCollection_2_TKey, KeyCollection_2_TValue
        ]: ...

    ValueCollection_GenericClasses_Dictionary_2_TKey = typing.TypeVar(
        'ValueCollection_GenericClasses_Dictionary_2_TKey'
    )
    ValueCollection_GenericClasses_Dictionary_2_TValue = typing.TypeVar(
        'ValueCollection_GenericClasses_Dictionary_2_TValue'
    )
    class ValueCollection_GenericClasses(
        typing.Generic[
            ValueCollection_GenericClasses_Dictionary_2_TKey,
            ValueCollection_GenericClasses_Dictionary_2_TValue,
        ],
        abc.ABCMeta,
    ):
        ValueCollection_GenericClasses_Dictionary_2_TKey = (
            Dictionary_2.ValueCollection_GenericClasses_Dictionary_2_TKey
        )
        ValueCollection_GenericClasses_Dictionary_2_TValue = (
            Dictionary_2.ValueCollection_GenericClasses_Dictionary_2_TValue
        )
        def __call__(
            self,
        ) -> Dictionary_2.ValueCollection_2[
            ValueCollection_GenericClasses_Dictionary_2_TKey,
            ValueCollection_GenericClasses_Dictionary_2_TValue,
        ]: ...

    ValueCollection: ValueCollection_GenericClasses[Dictionary_2_TKey, Dictionary_2_TValue]

    ValueCollection_2_TKey = typing.TypeVar('ValueCollection_2_TKey')
    ValueCollection_2_TValue = typing.TypeVar('ValueCollection_2_TValue')
    class ValueCollection_2(
        typing.Generic[ValueCollection_2_TKey, ValueCollection_2_TValue],
        IReadOnlyCollection_1[ValueCollection_2_TValue],
        ICollection_1[ValueCollection_2_TValue],
        ICollection,
    ):
        ValueCollection_2_TKey = Dictionary_2.ValueCollection_2_TKey
        ValueCollection_2_TValue = Dictionary_2.ValueCollection_2_TValue
        def __init__(
            self, dictionary: Dictionary_2[ValueCollection_2_TKey, ValueCollection_2_TValue]
        ) -> None: ...

        Enumerator_GenericClasses_ValueCollection_2_TKey = typing.TypeVar(
            'Enumerator_GenericClasses_ValueCollection_2_TKey'
        )
        Enumerator_GenericClasses_ValueCollection_2_TValue = typing.TypeVar(
            'Enumerator_GenericClasses_ValueCollection_2_TValue'
        )
        class Enumerator_GenericClasses(
            typing.Generic[
                Enumerator_GenericClasses_ValueCollection_2_TKey,
                Enumerator_GenericClasses_ValueCollection_2_TValue,
            ],
            abc.ABCMeta,
        ):
            Enumerator_GenericClasses_ValueCollection_2_TKey = (
                Dictionary_2.ValueCollection_2.Enumerator_GenericClasses_ValueCollection_2_TKey
            )
            Enumerator_GenericClasses_ValueCollection_2_TValue = Dictionary_2.ValueCollection_2.Enumerator_GenericClasses_ValueCollection_2_TValue
            def __call__(
                self,
            ) -> Dictionary_2.ValueCollection_2.Enumerator_2[
                Enumerator_GenericClasses_ValueCollection_2_TKey,
                Enumerator_GenericClasses_ValueCollection_2_TValue,
            ]: ...

        Enumerator: Enumerator_GenericClasses[ValueCollection_2_TKey, ValueCollection_2_TValue]

        Enumerator_2_TKey = typing.TypeVar('Enumerator_2_TKey')
        Enumerator_2_TValue = typing.TypeVar('Enumerator_2_TValue')
        class Enumerator_2(
            typing.Generic[Enumerator_2_TKey, Enumerator_2_TValue],
            IEnumerator_1[Enumerator_2_TValue],
        ):
            Enumerator_2_TKey = Dictionary_2.ValueCollection_2.Enumerator_2_TKey
            Enumerator_2_TValue = Dictionary_2.ValueCollection_2.Enumerator_2_TValue
            @property
            def Current(self) -> Enumerator_2_TValue: ...
            def Dispose(self) -> None: ...
            def MoveNext(self) -> bool: ...

        @property
        def Count(self) -> int: ...
        def CopyTo(self, array: Array_1[ValueCollection_2_TValue], index: int) -> None: ...
        def GetEnumerator(
            self,
        ) -> Dictionary_2.ValueCollection_2.Enumerator_2[
            ValueCollection_2_TKey, ValueCollection_2_TValue
        ]: ...

    @property
    def Comparer(self) -> IEqualityComparer_1[Dictionary_2_TKey]: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> Dictionary_2_TValue: ...
    @Item.setter
    def Item(self, value: Dictionary_2_TValue) -> Dictionary_2_TValue: ...
    @property
    def Keys(self) -> KeyCollection_2[Dictionary_2_TKey, Dictionary_2_TValue]: ...
    @property
    def Values(self) -> ValueCollection_2[Dictionary_2_TKey, Dictionary_2_TValue]: ...
    def Add(self, key: Dictionary_2_TKey, value: Dictionary_2_TValue) -> None: ...
    def Clear(self) -> None: ...
    def ContainsKey(self, key: Dictionary_2_TKey) -> bool: ...
    def ContainsValue(self, value: Dictionary_2_TValue) -> bool: ...
    def EnsureCapacity(self, capacity: int) -> int: ...
    def GetEnumerator(
        self,
    ) -> Dictionary_2.Enumerator_2[Dictionary_2_TKey, Dictionary_2_TValue]: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def OnDeserialization(self, sender: typing.Any) -> None: ...
    def TryAdd(self, key: Dictionary_2_TKey, value: Dictionary_2_TValue) -> bool: ...
    def TryGetValue(
        self, key: Dictionary_2_TKey, value: clr.Reference[Dictionary_2_TValue]
    ) -> bool: ...
    # Skipped Remove due to it being static, abstract and generic.

    Remove: Remove_MethodGroup[Dictionary_2_TKey, Dictionary_2_TValue]
    Remove_MethodGroup_Dictionary_2_TKey = typing.TypeVar(
        'Remove_MethodGroup_Dictionary_2_TKey'
    )
    Remove_MethodGroup_Dictionary_2_TValue = typing.TypeVar(
        'Remove_MethodGroup_Dictionary_2_TValue'
    )
    class Remove_MethodGroup(
        typing.Generic[
            Remove_MethodGroup_Dictionary_2_TKey, Remove_MethodGroup_Dictionary_2_TValue
        ]
    ):
        Remove_MethodGroup_Dictionary_2_TKey = Dictionary_2.Remove_MethodGroup_Dictionary_2_TKey
        Remove_MethodGroup_Dictionary_2_TValue = (
            Dictionary_2.Remove_MethodGroup_Dictionary_2_TValue
        )
        @typing.overload
        def __call__(self, key: Remove_MethodGroup_Dictionary_2_TKey) -> bool: ...
        @typing.overload
        def __call__(
            self,
            key: Remove_MethodGroup_Dictionary_2_TKey,
            value: clr.Reference[Remove_MethodGroup_Dictionary_2_TValue],
        ) -> bool: ...

    # Skipped TrimExcess due to it being static, abstract and generic.

    TrimExcess: TrimExcess_MethodGroup[Dictionary_2_TKey, Dictionary_2_TValue]
    TrimExcess_MethodGroup_Dictionary_2_TKey = typing.TypeVar(
        'TrimExcess_MethodGroup_Dictionary_2_TKey'
    )
    TrimExcess_MethodGroup_Dictionary_2_TValue = typing.TypeVar(
        'TrimExcess_MethodGroup_Dictionary_2_TValue'
    )
    class TrimExcess_MethodGroup(
        typing.Generic[
            TrimExcess_MethodGroup_Dictionary_2_TKey, TrimExcess_MethodGroup_Dictionary_2_TValue
        ]
    ):
        TrimExcess_MethodGroup_Dictionary_2_TKey = (
            Dictionary_2.TrimExcess_MethodGroup_Dictionary_2_TKey
        )
        TrimExcess_MethodGroup_Dictionary_2_TValue = (
            Dictionary_2.TrimExcess_MethodGroup_Dictionary_2_TValue
        )
        @typing.overload
        def __call__(self) -> None: ...
        @typing.overload
        def __call__(self, capacity: int) -> None: ...

class EnumEqualityComparer_GenericClasses(abc.ABCMeta):
    Generic_EnumEqualityComparer_GenericClasses_EnumEqualityComparer_1_T = typing.TypeVar(
        'Generic_EnumEqualityComparer_GenericClasses_EnumEqualityComparer_1_T'
    )
    def __getitem__(
        self,
        types: typing.Type[
            Generic_EnumEqualityComparer_GenericClasses_EnumEqualityComparer_1_T
        ],
    ) -> typing.Type[
        EnumEqualityComparer_1[
            Generic_EnumEqualityComparer_GenericClasses_EnumEqualityComparer_1_T
        ]
    ]: ...

EnumEqualityComparer: EnumEqualityComparer_GenericClasses

EnumEqualityComparer_1_T = typing.TypeVar('EnumEqualityComparer_1_T')

class EnumEqualityComparer_1(
    typing.Generic[EnumEqualityComparer_1_T],
    EqualityComparer_1[EnumEqualityComparer_1_T],
    ISerializable,
):
    def __init__(self) -> None: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup[EnumEqualityComparer_1_T]
    Equals_MethodGroup_EnumEqualityComparer_1_T = typing.TypeVar(
        'Equals_MethodGroup_EnumEqualityComparer_1_T'
    )
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_EnumEqualityComparer_1_T]):
        Equals_MethodGroup_EnumEqualityComparer_1_T = (
            EnumEqualityComparer_1.Equals_MethodGroup_EnumEqualityComparer_1_T
        )
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...
        @typing.overload
        def __call__(
            self,
            x: Equals_MethodGroup_EnumEqualityComparer_1_T,
            y: Equals_MethodGroup_EnumEqualityComparer_1_T,
        ) -> bool: ...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode: GetHashCode_MethodGroup[EnumEqualityComparer_1_T]
    GetHashCode_MethodGroup_EnumEqualityComparer_1_T = typing.TypeVar(
        'GetHashCode_MethodGroup_EnumEqualityComparer_1_T'
    )
    class GetHashCode_MethodGroup(
        typing.Generic[GetHashCode_MethodGroup_EnumEqualityComparer_1_T]
    ):
        GetHashCode_MethodGroup_EnumEqualityComparer_1_T = (
            EnumEqualityComparer_1.GetHashCode_MethodGroup_EnumEqualityComparer_1_T
        )
        @typing.overload
        def __call__(self) -> int: ...
        @typing.overload
        def __call__(self, obj: GetHashCode_MethodGroup_EnumEqualityComparer_1_T) -> int: ...

class EqualityComparer_GenericClasses(abc.ABCMeta):
    Generic_EqualityComparer_GenericClasses_EqualityComparer_1_T = typing.TypeVar(
        'Generic_EqualityComparer_GenericClasses_EqualityComparer_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_EqualityComparer_GenericClasses_EqualityComparer_1_T]
    ) -> typing.Type[
        EqualityComparer_1[Generic_EqualityComparer_GenericClasses_EqualityComparer_1_T]
    ]: ...

EqualityComparer: EqualityComparer_GenericClasses

EqualityComparer_1_T = typing.TypeVar('EqualityComparer_1_T')

class EqualityComparer_1(
    typing.Generic[EqualityComparer_1_T],
    IEqualityComparer_1[EqualityComparer_1_T],
    IEqualityComparer,
    abc.ABC,
):
    @classmethod
    @property
    def Default(cls) -> EqualityComparer_1[EqualityComparer_1_T]: ...
    @staticmethod
    def Create(
        equals: Func_3[EqualityComparer_1_T, EqualityComparer_1_T, bool],
        getHashCode: Func_2[EqualityComparer_1_T, int] = ...,
    ) -> EqualityComparer_1[EqualityComparer_1_T]: ...
    @abc.abstractmethod
    def Equals(self, x: EqualityComparer_1_T, y: EqualityComparer_1_T) -> bool: ...
    @abc.abstractmethod
    def GetHashCode(self, obj: EqualityComparer_1_T) -> int: ...

class GenericComparer_GenericClasses(abc.ABCMeta):
    Generic_GenericComparer_GenericClasses_GenericComparer_1_T = typing.TypeVar(
        'Generic_GenericComparer_GenericClasses_GenericComparer_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_GenericComparer_GenericClasses_GenericComparer_1_T]
    ) -> typing.Type[
        GenericComparer_1[Generic_GenericComparer_GenericClasses_GenericComparer_1_T]
    ]: ...

GenericComparer: GenericComparer_GenericClasses

GenericComparer_1_T = typing.TypeVar('GenericComparer_1_T')

class GenericComparer_1(typing.Generic[GenericComparer_1_T], Comparer_1[GenericComparer_1_T]):
    def __init__(self) -> None: ...
    def Compare(self, x: GenericComparer_1_T, y: GenericComparer_1_T) -> int: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...

class GenericEqualityComparer_GenericClasses(abc.ABCMeta):
    Generic_GenericEqualityComparer_GenericClasses_GenericEqualityComparer_1_T = typing.TypeVar(
        'Generic_GenericEqualityComparer_GenericClasses_GenericEqualityComparer_1_T'
    )
    def __getitem__(
        self,
        types: typing.Type[
            Generic_GenericEqualityComparer_GenericClasses_GenericEqualityComparer_1_T
        ],
    ) -> typing.Type[
        GenericEqualityComparer_1[
            Generic_GenericEqualityComparer_GenericClasses_GenericEqualityComparer_1_T
        ]
    ]: ...

GenericEqualityComparer: GenericEqualityComparer_GenericClasses

GenericEqualityComparer_1_T = typing.TypeVar('GenericEqualityComparer_1_T')

class GenericEqualityComparer_1(
    typing.Generic[GenericEqualityComparer_1_T], EqualityComparer_1[GenericEqualityComparer_1_T]
):
    def __init__(self) -> None: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup[GenericEqualityComparer_1_T]
    Equals_MethodGroup_GenericEqualityComparer_1_T = typing.TypeVar(
        'Equals_MethodGroup_GenericEqualityComparer_1_T'
    )
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_GenericEqualityComparer_1_T]):
        Equals_MethodGroup_GenericEqualityComparer_1_T = (
            GenericEqualityComparer_1.Equals_MethodGroup_GenericEqualityComparer_1_T
        )
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...
        @typing.overload
        def __call__(
            self,
            x: Equals_MethodGroup_GenericEqualityComparer_1_T,
            y: Equals_MethodGroup_GenericEqualityComparer_1_T,
        ) -> bool: ...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode: GetHashCode_MethodGroup[GenericEqualityComparer_1_T]
    GetHashCode_MethodGroup_GenericEqualityComparer_1_T = typing.TypeVar(
        'GetHashCode_MethodGroup_GenericEqualityComparer_1_T'
    )
    class GetHashCode_MethodGroup(
        typing.Generic[GetHashCode_MethodGroup_GenericEqualityComparer_1_T]
    ):
        GetHashCode_MethodGroup_GenericEqualityComparer_1_T = (
            GenericEqualityComparer_1.GetHashCode_MethodGroup_GenericEqualityComparer_1_T
        )
        @typing.overload
        def __call__(self) -> int: ...
        @typing.overload
        def __call__(self, obj: GetHashCode_MethodGroup_GenericEqualityComparer_1_T) -> int: ...

class HashSet_GenericClasses(abc.ABCMeta):
    Generic_HashSet_GenericClasses_HashSet_1_T = typing.TypeVar(
        'Generic_HashSet_GenericClasses_HashSet_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_HashSet_GenericClasses_HashSet_1_T]
    ) -> typing.Type[HashSet_1[Generic_HashSet_GenericClasses_HashSet_1_T]]: ...

HashSet: HashSet_GenericClasses

HashSet_1_T = typing.TypeVar('HashSet_1_T')

class HashSet_1(
    typing.Generic[HashSet_1_T],
    IReadOnlySet_1[HashSet_1_T],
    ISet_1[HashSet_1_T],
    IDeserializationCallback,
    ISerializable,
):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, capacity: int) -> None: ...
    @typing.overload
    def __init__(self, capacity: int, comparer: IEqualityComparer_1[HashSet_1_T]) -> None: ...
    @typing.overload
    def __init__(self, collection: IEnumerable_1[HashSet_1_T]) -> None: ...
    @typing.overload
    def __init__(
        self, collection: IEnumerable_1[HashSet_1_T], comparer: IEqualityComparer_1[HashSet_1_T]
    ) -> None: ...
    @typing.overload
    def __init__(self, comparer: IEqualityComparer_1[HashSet_1_T]) -> None: ...

    Enumerator_GenericClasses_HashSet_1_T = typing.TypeVar(
        'Enumerator_GenericClasses_HashSet_1_T'
    )
    class Enumerator_GenericClasses(
        typing.Generic[Enumerator_GenericClasses_HashSet_1_T], abc.ABCMeta
    ):
        Enumerator_GenericClasses_HashSet_1_T = HashSet_1.Enumerator_GenericClasses_HashSet_1_T
        def __call__(self) -> HashSet_1.Enumerator_1[Enumerator_GenericClasses_HashSet_1_T]: ...

    Enumerator: Enumerator_GenericClasses[HashSet_1_T]

    Enumerator_1_T = typing.TypeVar('Enumerator_1_T')
    class Enumerator_1(typing.Generic[Enumerator_1_T], IEnumerator_1[Enumerator_1_T]):
        Enumerator_1_T = HashSet_1.Enumerator_1_T
        @property
        def Current(self) -> Enumerator_1_T: ...
        def Dispose(self) -> None: ...
        def MoveNext(self) -> bool: ...

    @property
    def Comparer(self) -> IEqualityComparer_1[HashSet_1_T]: ...
    @property
    def Count(self) -> int: ...
    def Add(self, item: HashSet_1_T) -> bool: ...
    def Clear(self) -> None: ...
    def Contains(self, item: HashSet_1_T) -> bool: ...
    @staticmethod
    def CreateSetComparer() -> IEqualityComparer_1[HashSet_1[HashSet_1_T]]: ...
    def EnsureCapacity(self, capacity: int) -> int: ...
    def ExceptWith(self, other: IEnumerable_1[HashSet_1_T]) -> None: ...
    def GetEnumerator(self) -> HashSet_1.Enumerator_1[HashSet_1_T]: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def IntersectWith(self, other: IEnumerable_1[HashSet_1_T]) -> None: ...
    def IsProperSubsetOf(self, other: IEnumerable_1[HashSet_1_T]) -> bool: ...
    def IsProperSupersetOf(self, other: IEnumerable_1[HashSet_1_T]) -> bool: ...
    def IsSubsetOf(self, other: IEnumerable_1[HashSet_1_T]) -> bool: ...
    def IsSupersetOf(self, other: IEnumerable_1[HashSet_1_T]) -> bool: ...
    def OnDeserialization(self, sender: typing.Any) -> None: ...
    def Overlaps(self, other: IEnumerable_1[HashSet_1_T]) -> bool: ...
    def Remove(self, item: HashSet_1_T) -> bool: ...
    def RemoveWhere(self, match: Predicate_1[HashSet_1_T]) -> int: ...
    def SetEquals(self, other: IEnumerable_1[HashSet_1_T]) -> bool: ...
    def SymmetricExceptWith(self, other: IEnumerable_1[HashSet_1_T]) -> None: ...
    def TrimExcess(self) -> None: ...
    def TryGetValue(
        self, equalValue: HashSet_1_T, actualValue: clr.Reference[HashSet_1_T]
    ) -> bool: ...
    def UnionWith(self, other: IEnumerable_1[HashSet_1_T]) -> None: ...
    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo: CopyTo_MethodGroup[HashSet_1_T]
    CopyTo_MethodGroup_HashSet_1_T = typing.TypeVar('CopyTo_MethodGroup_HashSet_1_T')
    class CopyTo_MethodGroup(typing.Generic[CopyTo_MethodGroup_HashSet_1_T]):
        CopyTo_MethodGroup_HashSet_1_T = HashSet_1.CopyTo_MethodGroup_HashSet_1_T
        @typing.overload
        def __call__(self, array: Array_1[CopyTo_MethodGroup_HashSet_1_T]) -> None: ...
        @typing.overload
        def __call__(
            self, array: Array_1[CopyTo_MethodGroup_HashSet_1_T], arrayIndex: int
        ) -> None: ...
        @typing.overload
        def __call__(
            self, array: Array_1[CopyTo_MethodGroup_HashSet_1_T], arrayIndex: int, count: int
        ) -> None: ...

class IAsyncEnumerable_GenericClasses(abc.ABCMeta):
    Generic_IAsyncEnumerable_GenericClasses_IAsyncEnumerable_1_T = typing.TypeVar(
        'Generic_IAsyncEnumerable_GenericClasses_IAsyncEnumerable_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_IAsyncEnumerable_GenericClasses_IAsyncEnumerable_1_T]
    ) -> typing.Type[
        IAsyncEnumerable_1[Generic_IAsyncEnumerable_GenericClasses_IAsyncEnumerable_1_T]
    ]: ...

IAsyncEnumerable: IAsyncEnumerable_GenericClasses

IAsyncEnumerable_1_T = typing.TypeVar('IAsyncEnumerable_1_T', covariant=True)

class IAsyncEnumerable_1(typing.Generic[IAsyncEnumerable_1_T], typing.Protocol):
    @abc.abstractmethod
    def GetAsyncEnumerator(
        self, cancellationToken: CancellationToken = ...
    ) -> IAsyncEnumerator_1[IAsyncEnumerable_1_T]: ...

class IAsyncEnumerator_GenericClasses(abc.ABCMeta):
    Generic_IAsyncEnumerator_GenericClasses_IAsyncEnumerator_1_T = typing.TypeVar(
        'Generic_IAsyncEnumerator_GenericClasses_IAsyncEnumerator_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_IAsyncEnumerator_GenericClasses_IAsyncEnumerator_1_T]
    ) -> typing.Type[
        IAsyncEnumerator_1[Generic_IAsyncEnumerator_GenericClasses_IAsyncEnumerator_1_T]
    ]: ...

IAsyncEnumerator: IAsyncEnumerator_GenericClasses

IAsyncEnumerator_1_T = typing.TypeVar('IAsyncEnumerator_1_T', covariant=True)

class IAsyncEnumerator_1(
    typing.Generic[IAsyncEnumerator_1_T], IAsyncDisposable, typing.Protocol
):
    @property
    def Current(self) -> IAsyncEnumerator_1_T: ...
    @abc.abstractmethod
    def MoveNextAsync(self) -> ValueTask_1[bool]: ...

class ICollection_GenericClasses(abc.ABCMeta):
    Generic_ICollection_GenericClasses_ICollection_1_T = typing.TypeVar(
        'Generic_ICollection_GenericClasses_ICollection_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_ICollection_GenericClasses_ICollection_1_T]
    ) -> typing.Type[ICollection_1[Generic_ICollection_GenericClasses_ICollection_1_T]]: ...

ICollection: ICollection_GenericClasses

ICollection_1_T = typing.TypeVar('ICollection_1_T')

class ICollection_1(
    typing.Generic[ICollection_1_T], IEnumerable_1[ICollection_1_T], typing.Protocol
):
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @abc.abstractmethod
    def Add(self, item: ICollection_1_T) -> None: ...
    @abc.abstractmethod
    def Clear(self) -> None: ...
    @abc.abstractmethod
    def Contains(self, item: ICollection_1_T) -> bool: ...
    @abc.abstractmethod
    def CopyTo(self, array: Array_1[ICollection_1_T], arrayIndex: int) -> None: ...
    @abc.abstractmethod
    def Remove(self, item: ICollection_1_T) -> bool: ...

class IComparer_GenericClasses(abc.ABCMeta):
    Generic_IComparer_GenericClasses_IComparer_1_T = typing.TypeVar(
        'Generic_IComparer_GenericClasses_IComparer_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_IComparer_GenericClasses_IComparer_1_T]
    ) -> typing.Type[IComparer_1[Generic_IComparer_GenericClasses_IComparer_1_T]]: ...

IComparer: IComparer_GenericClasses

IComparer_1_T = typing.TypeVar('IComparer_1_T', contravariant=True)

class IComparer_1(typing.Generic[IComparer_1_T], typing.Protocol):
    @abc.abstractmethod
    def Compare(self, x: IComparer_1_T, y: IComparer_1_T) -> int: ...

class IDictionary_GenericClasses(abc.ABCMeta):
    Generic_IDictionary_GenericClasses_IDictionary_2_TKey = typing.TypeVar(
        'Generic_IDictionary_GenericClasses_IDictionary_2_TKey'
    )
    Generic_IDictionary_GenericClasses_IDictionary_2_TValue = typing.TypeVar(
        'Generic_IDictionary_GenericClasses_IDictionary_2_TValue'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[Generic_IDictionary_GenericClasses_IDictionary_2_TKey],
            typing.Type[Generic_IDictionary_GenericClasses_IDictionary_2_TValue],
        ],
    ) -> typing.Type[
        IDictionary_2[
            Generic_IDictionary_GenericClasses_IDictionary_2_TKey,
            Generic_IDictionary_GenericClasses_IDictionary_2_TValue,
        ]
    ]: ...

IDictionary: IDictionary_GenericClasses

IDictionary_2_TKey = typing.TypeVar('IDictionary_2_TKey')
IDictionary_2_TValue = typing.TypeVar('IDictionary_2_TValue')

class IDictionary_2(
    typing.Generic[IDictionary_2_TKey, IDictionary_2_TValue],
    ICollection_1[KeyValuePair_2[IDictionary_2_TKey, IDictionary_2_TValue]],
    typing.Protocol,
):
    @property
    def Item(self) -> IDictionary_2_TValue: ...
    @Item.setter
    def Item(self, value: IDictionary_2_TValue) -> IDictionary_2_TValue: ...
    @property
    def Keys(self) -> ICollection_1[IDictionary_2_TKey]: ...
    @property
    def Values(self) -> ICollection_1[IDictionary_2_TValue]: ...
    @abc.abstractmethod
    def Add(self, key: IDictionary_2_TKey, value: IDictionary_2_TValue) -> None: ...
    @abc.abstractmethod
    def ContainsKey(self, key: IDictionary_2_TKey) -> bool: ...
    @abc.abstractmethod
    def Remove(self, key: IDictionary_2_TKey) -> bool: ...
    @abc.abstractmethod
    def TryGetValue(
        self, key: IDictionary_2_TKey, value: clr.Reference[IDictionary_2_TValue]
    ) -> bool: ...

class IEnumerable_GenericClasses(abc.ABCMeta):
    Generic_IEnumerable_GenericClasses_IEnumerable_1_T = typing.TypeVar(
        'Generic_IEnumerable_GenericClasses_IEnumerable_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_IEnumerable_GenericClasses_IEnumerable_1_T]
    ) -> typing.Type[IEnumerable_1[Generic_IEnumerable_GenericClasses_IEnumerable_1_T]]: ...

IEnumerable: IEnumerable_GenericClasses

IEnumerable_1_T = typing.TypeVar('IEnumerable_1_T', covariant=True)

class IEnumerable_1(typing.Generic[IEnumerable_1_T], IEnumerable, typing.Protocol):
    @abc.abstractmethod
    def GetEnumerator(self) -> IEnumerator_1[IEnumerable_1_T]: ...
    def __iter__(self) -> typing.Iterator[IEnumerable_1_T]: ...

class IEnumerator_GenericClasses(abc.ABCMeta):
    Generic_IEnumerator_GenericClasses_IEnumerator_1_T = typing.TypeVar(
        'Generic_IEnumerator_GenericClasses_IEnumerator_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_IEnumerator_GenericClasses_IEnumerator_1_T]
    ) -> typing.Type[IEnumerator_1[Generic_IEnumerator_GenericClasses_IEnumerator_1_T]]: ...

IEnumerator: IEnumerator_GenericClasses

IEnumerator_1_T = typing.TypeVar('IEnumerator_1_T', covariant=True)

class IEnumerator_1(typing.Generic[IEnumerator_1_T], IEnumerator, IDisposable, typing.Protocol):
    @property
    def Current(self) -> IEnumerator_1_T: ...

class IEqualityComparer_GenericClasses(abc.ABCMeta):
    Generic_IEqualityComparer_GenericClasses_IEqualityComparer_1_T = typing.TypeVar(
        'Generic_IEqualityComparer_GenericClasses_IEqualityComparer_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_IEqualityComparer_GenericClasses_IEqualityComparer_1_T]
    ) -> typing.Type[
        IEqualityComparer_1[Generic_IEqualityComparer_GenericClasses_IEqualityComparer_1_T]
    ]: ...

IEqualityComparer: IEqualityComparer_GenericClasses

IEqualityComparer_1_T = typing.TypeVar('IEqualityComparer_1_T', contravariant=True)

class IEqualityComparer_1(typing.Generic[IEqualityComparer_1_T], typing.Protocol):
    @abc.abstractmethod
    def Equals(self, x: IEqualityComparer_1_T, y: IEqualityComparer_1_T) -> bool: ...
    @abc.abstractmethod
    def GetHashCode(self, obj: IEqualityComparer_1_T) -> int: ...

class IList_GenericClasses(abc.ABCMeta):
    Generic_IList_GenericClasses_IList_1_T = typing.TypeVar(
        'Generic_IList_GenericClasses_IList_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_IList_GenericClasses_IList_1_T]
    ) -> typing.Type[IList_1[Generic_IList_GenericClasses_IList_1_T]]: ...

IList: IList_GenericClasses

IList_1_T = typing.TypeVar('IList_1_T')

class IList_1(typing.Generic[IList_1_T], ICollection_1[IList_1_T], typing.Protocol):
    @property
    def Item(self) -> IList_1_T: ...
    @Item.setter
    def Item(self, value: IList_1_T) -> IList_1_T: ...
    @abc.abstractmethod
    def IndexOf(self, item: IList_1_T) -> int: ...
    @abc.abstractmethod
    def Insert(self, index: int, item: IList_1_T) -> None: ...
    @abc.abstractmethod
    def RemoveAt(self, index: int) -> None: ...

class IReadOnlyCollection_GenericClasses(abc.ABCMeta):
    Generic_IReadOnlyCollection_GenericClasses_IReadOnlyCollection_1_T = typing.TypeVar(
        'Generic_IReadOnlyCollection_GenericClasses_IReadOnlyCollection_1_T'
    )
    def __getitem__(
        self,
        types: typing.Type[Generic_IReadOnlyCollection_GenericClasses_IReadOnlyCollection_1_T],
    ) -> typing.Type[
        IReadOnlyCollection_1[
            Generic_IReadOnlyCollection_GenericClasses_IReadOnlyCollection_1_T
        ]
    ]: ...

IReadOnlyCollection: IReadOnlyCollection_GenericClasses

IReadOnlyCollection_1_T = typing.TypeVar('IReadOnlyCollection_1_T', covariant=True)

class IReadOnlyCollection_1(
    typing.Generic[IReadOnlyCollection_1_T],
    IEnumerable_1[IReadOnlyCollection_1_T],
    typing.Protocol,
):
    @property
    def Count(self) -> int: ...

class IReadOnlyDictionary_GenericClasses(abc.ABCMeta):
    Generic_IReadOnlyDictionary_GenericClasses_IReadOnlyDictionary_2_TKey = typing.TypeVar(
        'Generic_IReadOnlyDictionary_GenericClasses_IReadOnlyDictionary_2_TKey'
    )
    Generic_IReadOnlyDictionary_GenericClasses_IReadOnlyDictionary_2_TValue = typing.TypeVar(
        'Generic_IReadOnlyDictionary_GenericClasses_IReadOnlyDictionary_2_TValue'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[Generic_IReadOnlyDictionary_GenericClasses_IReadOnlyDictionary_2_TKey],
            typing.Type[
                Generic_IReadOnlyDictionary_GenericClasses_IReadOnlyDictionary_2_TValue
            ],
        ],
    ) -> typing.Type[
        IReadOnlyDictionary_2[
            Generic_IReadOnlyDictionary_GenericClasses_IReadOnlyDictionary_2_TKey,
            Generic_IReadOnlyDictionary_GenericClasses_IReadOnlyDictionary_2_TValue,
        ]
    ]: ...

IReadOnlyDictionary: IReadOnlyDictionary_GenericClasses

IReadOnlyDictionary_2_TKey = typing.TypeVar('IReadOnlyDictionary_2_TKey')
IReadOnlyDictionary_2_TValue = typing.TypeVar('IReadOnlyDictionary_2_TValue')

class IReadOnlyDictionary_2(
    typing.Generic[IReadOnlyDictionary_2_TKey, IReadOnlyDictionary_2_TValue],
    IReadOnlyCollection_1[
        KeyValuePair_2[IReadOnlyDictionary_2_TKey, IReadOnlyDictionary_2_TValue]
    ],
    typing.Protocol,
):
    @property
    def Item(self) -> IReadOnlyDictionary_2_TValue: ...
    @property
    def Keys(self) -> IEnumerable_1[IReadOnlyDictionary_2_TKey]: ...
    @property
    def Values(self) -> IEnumerable_1[IReadOnlyDictionary_2_TValue]: ...
    @abc.abstractmethod
    def ContainsKey(self, key: IReadOnlyDictionary_2_TKey) -> bool: ...
    @abc.abstractmethod
    def TryGetValue(
        self,
        key: IReadOnlyDictionary_2_TKey,
        value: clr.Reference[IReadOnlyDictionary_2_TValue],
    ) -> bool: ...

class IReadOnlyList_GenericClasses(abc.ABCMeta):
    Generic_IReadOnlyList_GenericClasses_IReadOnlyList_1_T = typing.TypeVar(
        'Generic_IReadOnlyList_GenericClasses_IReadOnlyList_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_IReadOnlyList_GenericClasses_IReadOnlyList_1_T]
    ) -> typing.Type[
        IReadOnlyList_1[Generic_IReadOnlyList_GenericClasses_IReadOnlyList_1_T]
    ]: ...

IReadOnlyList: IReadOnlyList_GenericClasses

IReadOnlyList_1_T = typing.TypeVar('IReadOnlyList_1_T', covariant=True)

class IReadOnlyList_1(
    typing.Generic[IReadOnlyList_1_T], IReadOnlyCollection_1[IReadOnlyList_1_T], typing.Protocol
):
    @property
    def Item(self) -> IReadOnlyList_1_T: ...

class IReadOnlySet_GenericClasses(abc.ABCMeta):
    Generic_IReadOnlySet_GenericClasses_IReadOnlySet_1_T = typing.TypeVar(
        'Generic_IReadOnlySet_GenericClasses_IReadOnlySet_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_IReadOnlySet_GenericClasses_IReadOnlySet_1_T]
    ) -> typing.Type[IReadOnlySet_1[Generic_IReadOnlySet_GenericClasses_IReadOnlySet_1_T]]: ...

IReadOnlySet: IReadOnlySet_GenericClasses

IReadOnlySet_1_T = typing.TypeVar('IReadOnlySet_1_T')

class IReadOnlySet_1(
    typing.Generic[IReadOnlySet_1_T], IReadOnlyCollection_1[IReadOnlySet_1_T], typing.Protocol
):
    @abc.abstractmethod
    def Contains(self, item: IReadOnlySet_1_T) -> bool: ...
    @abc.abstractmethod
    def IsProperSubsetOf(self, other: IEnumerable_1[IReadOnlySet_1_T]) -> bool: ...
    @abc.abstractmethod
    def IsProperSupersetOf(self, other: IEnumerable_1[IReadOnlySet_1_T]) -> bool: ...
    @abc.abstractmethod
    def IsSubsetOf(self, other: IEnumerable_1[IReadOnlySet_1_T]) -> bool: ...
    @abc.abstractmethod
    def IsSupersetOf(self, other: IEnumerable_1[IReadOnlySet_1_T]) -> bool: ...
    @abc.abstractmethod
    def Overlaps(self, other: IEnumerable_1[IReadOnlySet_1_T]) -> bool: ...
    @abc.abstractmethod
    def SetEquals(self, other: IEnumerable_1[IReadOnlySet_1_T]) -> bool: ...

class ISet_GenericClasses(abc.ABCMeta):
    Generic_ISet_GenericClasses_ISet_1_T = typing.TypeVar(
        'Generic_ISet_GenericClasses_ISet_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_ISet_GenericClasses_ISet_1_T]
    ) -> typing.Type[ISet_1[Generic_ISet_GenericClasses_ISet_1_T]]: ...

ISet: ISet_GenericClasses

ISet_1_T = typing.TypeVar('ISet_1_T')

class ISet_1(typing.Generic[ISet_1_T], ICollection_1[ISet_1_T], typing.Protocol):
    @abc.abstractmethod
    def Add(self, item: ISet_1_T) -> bool: ...
    @abc.abstractmethod
    def ExceptWith(self, other: IEnumerable_1[ISet_1_T]) -> None: ...
    @abc.abstractmethod
    def IntersectWith(self, other: IEnumerable_1[ISet_1_T]) -> None: ...
    @abc.abstractmethod
    def IsProperSubsetOf(self, other: IEnumerable_1[ISet_1_T]) -> bool: ...
    @abc.abstractmethod
    def IsProperSupersetOf(self, other: IEnumerable_1[ISet_1_T]) -> bool: ...
    @abc.abstractmethod
    def IsSubsetOf(self, other: IEnumerable_1[ISet_1_T]) -> bool: ...
    @abc.abstractmethod
    def IsSupersetOf(self, other: IEnumerable_1[ISet_1_T]) -> bool: ...
    @abc.abstractmethod
    def Overlaps(self, other: IEnumerable_1[ISet_1_T]) -> bool: ...
    @abc.abstractmethod
    def SetEquals(self, other: IEnumerable_1[ISet_1_T]) -> bool: ...
    @abc.abstractmethod
    def SymmetricExceptWith(self, other: IEnumerable_1[ISet_1_T]) -> None: ...
    @abc.abstractmethod
    def UnionWith(self, other: IEnumerable_1[ISet_1_T]) -> None: ...

class KeyNotFoundException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, innerException: Exception) -> None: ...
    @property
    def Data(self) -> System.Collections.IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...

class KeyValuePair_GenericClasses(abc.ABCMeta):
    Generic_KeyValuePair_GenericClasses_KeyValuePair_2_TKey = typing.TypeVar(
        'Generic_KeyValuePair_GenericClasses_KeyValuePair_2_TKey'
    )
    Generic_KeyValuePair_GenericClasses_KeyValuePair_2_TValue = typing.TypeVar(
        'Generic_KeyValuePair_GenericClasses_KeyValuePair_2_TValue'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[Generic_KeyValuePair_GenericClasses_KeyValuePair_2_TKey],
            typing.Type[Generic_KeyValuePair_GenericClasses_KeyValuePair_2_TValue],
        ],
    ) -> typing.Type[
        KeyValuePair_2[
            Generic_KeyValuePair_GenericClasses_KeyValuePair_2_TKey,
            Generic_KeyValuePair_GenericClasses_KeyValuePair_2_TValue,
        ]
    ]: ...

class KeyValuePair(KeyValuePair_0, metaclass=KeyValuePair_GenericClasses): ...

class KeyValuePair_0(abc.ABC):
    # Skipped Create due to it being static, abstract and generic.

    Create: Create_MethodGroup
    class Create_MethodGroup:
        def __getitem__(
            self, t: typing.Tuple[typing.Type[Create_2_T1], typing.Type[Create_2_T2]]
        ) -> Create_2[Create_2_T1, Create_2_T2]: ...

        Create_2_T1 = typing.TypeVar('Create_2_T1')
        Create_2_T2 = typing.TypeVar('Create_2_T2')
        class Create_2(typing.Generic[Create_2_T1, Create_2_T2]):
            Create_2_TKey = KeyValuePair_0.Create_MethodGroup.Create_2_T1
            Create_2_TValue = KeyValuePair_0.Create_MethodGroup.Create_2_T2
            def __call__(
                self, key: Create_2_TKey, value: Create_2_TValue
            ) -> KeyValuePair_2[Create_2_TKey, Create_2_TValue]: ...

KeyValuePair_2_TKey = typing.TypeVar('KeyValuePair_2_TKey')
KeyValuePair_2_TValue = typing.TypeVar('KeyValuePair_2_TValue')

class KeyValuePair_2(typing.Generic[KeyValuePair_2_TKey, KeyValuePair_2_TValue]):
    def __init__(self, key: KeyValuePair_2_TKey, value: KeyValuePair_2_TValue) -> None: ...
    @property
    def Key(self) -> KeyValuePair_2_TKey: ...
    @property
    def Value(self) -> KeyValuePair_2_TValue: ...
    def Deconstruct(
        self,
        key: clr.Reference[KeyValuePair_2_TKey],
        value: clr.Reference[KeyValuePair_2_TValue],
    ) -> None: ...
    def ToString(self) -> str: ...

class List_GenericClasses(abc.ABCMeta):
    Generic_List_GenericClasses_List_1_T = typing.TypeVar(
        'Generic_List_GenericClasses_List_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_List_GenericClasses_List_1_T]
    ) -> typing.Type[List_1[Generic_List_GenericClasses_List_1_T]]: ...

List: List_GenericClasses

List_1_T = typing.TypeVar('List_1_T')

class List_1(typing.Generic[List_1_T], IReadOnlyList_1[List_1_T], IList_1[List_1_T], IList):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, capacity: int) -> None: ...
    @typing.overload
    def __init__(self, collection: IEnumerable_1[List_1_T]) -> None: ...

    Enumerator_GenericClasses_List_1_T = typing.TypeVar('Enumerator_GenericClasses_List_1_T')
    class Enumerator_GenericClasses(
        typing.Generic[Enumerator_GenericClasses_List_1_T], abc.ABCMeta
    ):
        Enumerator_GenericClasses_List_1_T = List_1.Enumerator_GenericClasses_List_1_T
        def __call__(self) -> List_1.Enumerator_1[Enumerator_GenericClasses_List_1_T]: ...

    Enumerator: Enumerator_GenericClasses[List_1_T]

    Enumerator_1_T = typing.TypeVar('Enumerator_1_T')
    class Enumerator_1(typing.Generic[Enumerator_1_T], IEnumerator_1[Enumerator_1_T]):
        Enumerator_1_T = List_1.Enumerator_1_T
        @property
        def Current(self) -> Enumerator_1_T: ...
        def Dispose(self) -> None: ...
        def MoveNext(self) -> bool: ...

    @property
    def Capacity(self) -> int: ...
    @Capacity.setter
    def Capacity(self, value: int) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> List_1_T: ...
    @Item.setter
    def Item(self, value: List_1_T) -> List_1_T: ...
    def Add(self, item: List_1_T) -> None: ...
    def AddRange(self, collection: IEnumerable_1[List_1_T]) -> None: ...
    def AsReadOnly(self) -> ReadOnlyCollection_1[List_1_T]: ...
    def Clear(self) -> None: ...
    def Contains(self, item: List_1_T) -> bool: ...
    def EnsureCapacity(self, capacity: int) -> int: ...
    def Exists(self, match: Predicate_1[List_1_T]) -> bool: ...
    def Find(self, match: Predicate_1[List_1_T]) -> List_1_T: ...
    def FindAll(self, match: Predicate_1[List_1_T]) -> List_1[List_1_T]: ...
    def FindLast(self, match: Predicate_1[List_1_T]) -> List_1_T: ...
    def ForEach(self, action: Action_1[List_1_T]) -> None: ...
    def GetEnumerator(self) -> List_1.Enumerator_1[List_1_T]: ...
    def GetRange(self, index: int, count: int) -> List_1[List_1_T]: ...
    def Insert(self, index: int, item: List_1_T) -> None: ...
    def InsertRange(self, index: int, collection: IEnumerable_1[List_1_T]) -> None: ...
    def Remove(self, item: List_1_T) -> bool: ...
    def RemoveAll(self, match: Predicate_1[List_1_T]) -> int: ...
    def RemoveAt(self, index: int) -> None: ...
    def RemoveRange(self, index: int, count: int) -> None: ...
    def Slice(self, start: int, length: int) -> List_1[List_1_T]: ...
    def ToArray(self) -> Array_1[List_1_T]: ...
    def TrimExcess(self) -> None: ...
    def TrueForAll(self, match: Predicate_1[List_1_T]) -> bool: ...
    # Skipped BinarySearch due to it being static, abstract and generic.

    BinarySearch: BinarySearch_MethodGroup[List_1_T]
    BinarySearch_MethodGroup_List_1_T = typing.TypeVar('BinarySearch_MethodGroup_List_1_T')
    class BinarySearch_MethodGroup(typing.Generic[BinarySearch_MethodGroup_List_1_T]):
        BinarySearch_MethodGroup_List_1_T = List_1.BinarySearch_MethodGroup_List_1_T
        @typing.overload
        def __call__(self, item: BinarySearch_MethodGroup_List_1_T) -> int: ...
        @typing.overload
        def __call__(
            self,
            item: BinarySearch_MethodGroup_List_1_T,
            comparer: IComparer_1[BinarySearch_MethodGroup_List_1_T],
        ) -> int: ...
        @typing.overload
        def __call__(
            self,
            index: int,
            count: int,
            item: BinarySearch_MethodGroup_List_1_T,
            comparer: IComparer_1[BinarySearch_MethodGroup_List_1_T],
        ) -> int: ...

    # Skipped ConvertAll due to it being static, abstract and generic.

    ConvertAll: ConvertAll_MethodGroup[List_1_T]
    ConvertAll_MethodGroup_List_1_T = typing.TypeVar('ConvertAll_MethodGroup_List_1_T')
    class ConvertAll_MethodGroup(typing.Generic[ConvertAll_MethodGroup_List_1_T]):
        ConvertAll_MethodGroup_List_1_T = List_1.ConvertAll_MethodGroup_List_1_T
        def __getitem__(
            self, t: typing.Type[ConvertAll_1_T1]
        ) -> ConvertAll_1[ConvertAll_MethodGroup_List_1_T, ConvertAll_1_T1]: ...

        ConvertAll_1_List_1_T = typing.TypeVar('ConvertAll_1_List_1_T')
        ConvertAll_1_T1 = typing.TypeVar('ConvertAll_1_T1')
        class ConvertAll_1(typing.Generic[ConvertAll_1_List_1_T, ConvertAll_1_T1]):
            ConvertAll_1_List_1_T = List_1.ConvertAll_MethodGroup.ConvertAll_1_List_1_T
            ConvertAll_1_TOutput = List_1.ConvertAll_MethodGroup.ConvertAll_1_T1
            def __call__(
                self, converter: Converter_2[ConvertAll_1_List_1_T, ConvertAll_1_TOutput]
            ) -> List_1[ConvertAll_1_TOutput]: ...

    # Skipped CopyTo due to it being static, abstract and generic.

    CopyTo: CopyTo_MethodGroup[List_1_T]
    CopyTo_MethodGroup_List_1_T = typing.TypeVar('CopyTo_MethodGroup_List_1_T')
    class CopyTo_MethodGroup(typing.Generic[CopyTo_MethodGroup_List_1_T]):
        CopyTo_MethodGroup_List_1_T = List_1.CopyTo_MethodGroup_List_1_T
        @typing.overload
        def __call__(self, array: Array_1[CopyTo_MethodGroup_List_1_T]) -> None: ...
        @typing.overload
        def __call__(
            self, array: Array_1[CopyTo_MethodGroup_List_1_T], arrayIndex: int
        ) -> None: ...
        @typing.overload
        def __call__(
            self,
            index: int,
            array: Array_1[CopyTo_MethodGroup_List_1_T],
            arrayIndex: int,
            count: int,
        ) -> None: ...

    # Skipped FindIndex due to it being static, abstract and generic.

    FindIndex: FindIndex_MethodGroup[List_1_T]
    FindIndex_MethodGroup_List_1_T = typing.TypeVar('FindIndex_MethodGroup_List_1_T')
    class FindIndex_MethodGroup(typing.Generic[FindIndex_MethodGroup_List_1_T]):
        FindIndex_MethodGroup_List_1_T = List_1.FindIndex_MethodGroup_List_1_T
        @typing.overload
        def __call__(self, match: Predicate_1[FindIndex_MethodGroup_List_1_T]) -> int: ...
        @typing.overload
        def __call__(
            self, startIndex: int, match: Predicate_1[FindIndex_MethodGroup_List_1_T]
        ) -> int: ...
        @typing.overload
        def __call__(
            self,
            startIndex: int,
            count: int,
            match: Predicate_1[FindIndex_MethodGroup_List_1_T],
        ) -> int: ...

    # Skipped FindLastIndex due to it being static, abstract and generic.

    FindLastIndex: FindLastIndex_MethodGroup[List_1_T]
    FindLastIndex_MethodGroup_List_1_T = typing.TypeVar('FindLastIndex_MethodGroup_List_1_T')
    class FindLastIndex_MethodGroup(typing.Generic[FindLastIndex_MethodGroup_List_1_T]):
        FindLastIndex_MethodGroup_List_1_T = List_1.FindLastIndex_MethodGroup_List_1_T
        @typing.overload
        def __call__(self, match: Predicate_1[FindLastIndex_MethodGroup_List_1_T]) -> int: ...
        @typing.overload
        def __call__(
            self, startIndex: int, match: Predicate_1[FindLastIndex_MethodGroup_List_1_T]
        ) -> int: ...
        @typing.overload
        def __call__(
            self,
            startIndex: int,
            count: int,
            match: Predicate_1[FindLastIndex_MethodGroup_List_1_T],
        ) -> int: ...

    # Skipped IndexOf due to it being static, abstract and generic.

    IndexOf: IndexOf_MethodGroup[List_1_T]
    IndexOf_MethodGroup_List_1_T = typing.TypeVar('IndexOf_MethodGroup_List_1_T')
    class IndexOf_MethodGroup(typing.Generic[IndexOf_MethodGroup_List_1_T]):
        IndexOf_MethodGroup_List_1_T = List_1.IndexOf_MethodGroup_List_1_T
        @typing.overload
        def __call__(self, item: IndexOf_MethodGroup_List_1_T) -> int: ...
        @typing.overload
        def __call__(self, item: IndexOf_MethodGroup_List_1_T, index: int) -> int: ...
        @typing.overload
        def __call__(
            self, item: IndexOf_MethodGroup_List_1_T, index: int, count: int
        ) -> int: ...

    # Skipped LastIndexOf due to it being static, abstract and generic.

    LastIndexOf: LastIndexOf_MethodGroup[List_1_T]
    LastIndexOf_MethodGroup_List_1_T = typing.TypeVar('LastIndexOf_MethodGroup_List_1_T')
    class LastIndexOf_MethodGroup(typing.Generic[LastIndexOf_MethodGroup_List_1_T]):
        LastIndexOf_MethodGroup_List_1_T = List_1.LastIndexOf_MethodGroup_List_1_T
        @typing.overload
        def __call__(self, item: LastIndexOf_MethodGroup_List_1_T) -> int: ...
        @typing.overload
        def __call__(self, item: LastIndexOf_MethodGroup_List_1_T, index: int) -> int: ...
        @typing.overload
        def __call__(
            self, item: LastIndexOf_MethodGroup_List_1_T, index: int, count: int
        ) -> int: ...

    # Skipped Reverse due to it being static, abstract and generic.

    Reverse: Reverse_MethodGroup[List_1_T]
    Reverse_MethodGroup_List_1_T = typing.TypeVar('Reverse_MethodGroup_List_1_T')
    class Reverse_MethodGroup(typing.Generic[Reverse_MethodGroup_List_1_T]):
        Reverse_MethodGroup_List_1_T = List_1.Reverse_MethodGroup_List_1_T
        @typing.overload
        def __call__(self) -> None: ...
        @typing.overload
        def __call__(self, index: int, count: int) -> None: ...

    # Skipped Sort due to it being static, abstract and generic.

    Sort: Sort_MethodGroup[List_1_T]
    Sort_MethodGroup_List_1_T = typing.TypeVar('Sort_MethodGroup_List_1_T')
    class Sort_MethodGroup(typing.Generic[Sort_MethodGroup_List_1_T]):
        Sort_MethodGroup_List_1_T = List_1.Sort_MethodGroup_List_1_T
        @typing.overload
        def __call__(self) -> None: ...
        @typing.overload
        def __call__(self, comparison: Comparison_1[Sort_MethodGroup_List_1_T]) -> None: ...
        @typing.overload
        def __call__(self, comparer: IComparer_1[Sort_MethodGroup_List_1_T]) -> None: ...
        @typing.overload
        def __call__(
            self, index: int, count: int, comparer: IComparer_1[Sort_MethodGroup_List_1_T]
        ) -> None: ...

class NonRandomizedStringEqualityComparer(ISerializable):
    def Equals(self, x: str, y: str) -> bool: ...
    def GetHashCode(self, obj: str) -> int: ...
    @staticmethod
    def GetStringComparer(comparer: typing.Any) -> IEqualityComparer_1[str]: ...
    def GetUnderlyingEqualityComparer(self) -> IEqualityComparer_1[str]: ...

class NullableComparer_GenericClasses(abc.ABCMeta):
    Generic_NullableComparer_GenericClasses_NullableComparer_1_T = typing.TypeVar(
        'Generic_NullableComparer_GenericClasses_NullableComparer_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_NullableComparer_GenericClasses_NullableComparer_1_T]
    ) -> typing.Type[
        NullableComparer_1[Generic_NullableComparer_GenericClasses_NullableComparer_1_T]
    ]: ...

NullableComparer: NullableComparer_GenericClasses

NullableComparer_1_T = typing.TypeVar('NullableComparer_1_T')

class NullableComparer_1(
    typing.Generic[NullableComparer_1_T],
    Comparer_1[typing.Optional[NullableComparer_1_T]],
    ISerializable,
):
    def __init__(self) -> None: ...
    def Compare(
        self, x: typing.Optional[NullableComparer_1_T], y: typing.Optional[NullableComparer_1_T]
    ) -> int: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...

class NullableEqualityComparer_GenericClasses(abc.ABCMeta):
    Generic_NullableEqualityComparer_GenericClasses_NullableEqualityComparer_1_T = (
        typing.TypeVar(
            'Generic_NullableEqualityComparer_GenericClasses_NullableEqualityComparer_1_T'
        )
    )
    def __getitem__(
        self,
        types: typing.Type[
            Generic_NullableEqualityComparer_GenericClasses_NullableEqualityComparer_1_T
        ],
    ) -> typing.Type[
        NullableEqualityComparer_1[
            Generic_NullableEqualityComparer_GenericClasses_NullableEqualityComparer_1_T
        ]
    ]: ...

NullableEqualityComparer: NullableEqualityComparer_GenericClasses

NullableEqualityComparer_1_T = typing.TypeVar('NullableEqualityComparer_1_T')

class NullableEqualityComparer_1(
    typing.Generic[NullableEqualityComparer_1_T],
    EqualityComparer_1[typing.Optional[NullableEqualityComparer_1_T]],
    ISerializable,
):
    def __init__(self) -> None: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup[NullableEqualityComparer_1_T]
    Equals_MethodGroup_NullableEqualityComparer_1_T = typing.TypeVar(
        'Equals_MethodGroup_NullableEqualityComparer_1_T'
    )
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_NullableEqualityComparer_1_T]):
        Equals_MethodGroup_NullableEqualityComparer_1_T = (
            NullableEqualityComparer_1.Equals_MethodGroup_NullableEqualityComparer_1_T
        )
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...
        @typing.overload
        def __call__(
            self,
            x: typing.Optional[Equals_MethodGroup_NullableEqualityComparer_1_T],
            y: typing.Optional[Equals_MethodGroup_NullableEqualityComparer_1_T],
        ) -> bool: ...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode: GetHashCode_MethodGroup[NullableEqualityComparer_1_T]
    GetHashCode_MethodGroup_NullableEqualityComparer_1_T = typing.TypeVar(
        'GetHashCode_MethodGroup_NullableEqualityComparer_1_T'
    )
    class GetHashCode_MethodGroup(
        typing.Generic[GetHashCode_MethodGroup_NullableEqualityComparer_1_T]
    ):
        GetHashCode_MethodGroup_NullableEqualityComparer_1_T = (
            NullableEqualityComparer_1.GetHashCode_MethodGroup_NullableEqualityComparer_1_T
        )
        @typing.overload
        def __call__(self) -> int: ...
        @typing.overload
        def __call__(
            self, obj: typing.Optional[GetHashCode_MethodGroup_NullableEqualityComparer_1_T]
        ) -> int: ...

class ObjectComparer_GenericClasses(abc.ABCMeta):
    Generic_ObjectComparer_GenericClasses_ObjectComparer_1_T = typing.TypeVar(
        'Generic_ObjectComparer_GenericClasses_ObjectComparer_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_ObjectComparer_GenericClasses_ObjectComparer_1_T]
    ) -> typing.Type[
        ObjectComparer_1[Generic_ObjectComparer_GenericClasses_ObjectComparer_1_T]
    ]: ...

ObjectComparer: ObjectComparer_GenericClasses

ObjectComparer_1_T = typing.TypeVar('ObjectComparer_1_T')

class ObjectComparer_1(typing.Generic[ObjectComparer_1_T], Comparer_1[ObjectComparer_1_T]):
    def __init__(self) -> None: ...
    def Compare(self, x: ObjectComparer_1_T, y: ObjectComparer_1_T) -> int: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...

class ObjectEqualityComparer_GenericClasses(abc.ABCMeta):
    Generic_ObjectEqualityComparer_GenericClasses_ObjectEqualityComparer_1_T = typing.TypeVar(
        'Generic_ObjectEqualityComparer_GenericClasses_ObjectEqualityComparer_1_T'
    )
    def __getitem__(
        self,
        types: typing.Type[
            Generic_ObjectEqualityComparer_GenericClasses_ObjectEqualityComparer_1_T
        ],
    ) -> typing.Type[
        ObjectEqualityComparer_1[
            Generic_ObjectEqualityComparer_GenericClasses_ObjectEqualityComparer_1_T
        ]
    ]: ...

ObjectEqualityComparer: ObjectEqualityComparer_GenericClasses

ObjectEqualityComparer_1_T = typing.TypeVar('ObjectEqualityComparer_1_T')

class ObjectEqualityComparer_1(
    typing.Generic[ObjectEqualityComparer_1_T], EqualityComparer_1[ObjectEqualityComparer_1_T]
):
    def __init__(self) -> None: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup[ObjectEqualityComparer_1_T]
    Equals_MethodGroup_ObjectEqualityComparer_1_T = typing.TypeVar(
        'Equals_MethodGroup_ObjectEqualityComparer_1_T'
    )
    class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_ObjectEqualityComparer_1_T]):
        Equals_MethodGroup_ObjectEqualityComparer_1_T = (
            ObjectEqualityComparer_1.Equals_MethodGroup_ObjectEqualityComparer_1_T
        )
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...
        @typing.overload
        def __call__(
            self,
            x: Equals_MethodGroup_ObjectEqualityComparer_1_T,
            y: Equals_MethodGroup_ObjectEqualityComparer_1_T,
        ) -> bool: ...

    # Skipped GetHashCode due to it being static, abstract and generic.

    GetHashCode: GetHashCode_MethodGroup[ObjectEqualityComparer_1_T]
    GetHashCode_MethodGroup_ObjectEqualityComparer_1_T = typing.TypeVar(
        'GetHashCode_MethodGroup_ObjectEqualityComparer_1_T'
    )
    class GetHashCode_MethodGroup(
        typing.Generic[GetHashCode_MethodGroup_ObjectEqualityComparer_1_T]
    ):
        GetHashCode_MethodGroup_ObjectEqualityComparer_1_T = (
            ObjectEqualityComparer_1.GetHashCode_MethodGroup_ObjectEqualityComparer_1_T
        )
        @typing.overload
        def __call__(self) -> int: ...
        @typing.overload
        def __call__(self, obj: GetHashCode_MethodGroup_ObjectEqualityComparer_1_T) -> int: ...

class Queue_GenericClasses(abc.ABCMeta):
    Generic_Queue_GenericClasses_Queue_1_T = typing.TypeVar(
        'Generic_Queue_GenericClasses_Queue_1_T'
    )
    def __getitem__(
        self, types: typing.Type[Generic_Queue_GenericClasses_Queue_1_T]
    ) -> typing.Type[Queue_1[Generic_Queue_GenericClasses_Queue_1_T]]: ...

Queue: Queue_GenericClasses

Queue_1_T = typing.TypeVar('Queue_1_T')

class Queue_1(typing.Generic[Queue_1_T], IReadOnlyCollection_1[Queue_1_T], ICollection):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, capacity: int) -> None: ...
    @typing.overload
    def __init__(self, collection: IEnumerable_1[Queue_1_T]) -> None: ...

    Enumerator_GenericClasses_Queue_1_T = typing.TypeVar('Enumerator_GenericClasses_Queue_1_T')
    class Enumerator_GenericClasses(
        typing.Generic[Enumerator_GenericClasses_Queue_1_T], abc.ABCMeta
    ):
        Enumerator_GenericClasses_Queue_1_T = Queue_1.Enumerator_GenericClasses_Queue_1_T
        def __call__(self) -> Queue_1.Enumerator_1[Enumerator_GenericClasses_Queue_1_T]: ...

    Enumerator: Enumerator_GenericClasses[Queue_1_T]

    Enumerator_1_T = typing.TypeVar('Enumerator_1_T')
    class Enumerator_1(typing.Generic[Enumerator_1_T], IEnumerator_1[Enumerator_1_T]):
        Enumerator_1_T = Queue_1.Enumerator_1_T
        @property
        def Current(self) -> Enumerator_1_T: ...
        def Dispose(self) -> None: ...
        def MoveNext(self) -> bool: ...

    @property
    def Count(self) -> int: ...
    def Clear(self) -> None: ...
    def Contains(self, item: Queue_1_T) -> bool: ...
    def CopyTo(self, array: Array_1[Queue_1_T], arrayIndex: int) -> None: ...
    def Dequeue(self) -> Queue_1_T: ...
    def Enqueue(self, item: Queue_1_T) -> None: ...
    def EnsureCapacity(self, capacity: int) -> int: ...
    def GetEnumerator(self) -> Queue_1.Enumerator_1[Queue_1_T]: ...
    def Peek(self) -> Queue_1_T: ...
    def ToArray(self) -> Array_1[Queue_1_T]: ...
    def TrimExcess(self) -> None: ...
    def TryDequeue(self, result: clr.Reference[Queue_1_T]) -> bool: ...
    def TryPeek(self, result: clr.Reference[Queue_1_T]) -> bool: ...

class ReferenceEqualityComparer(IEqualityComparer, IEqualityComparer_1[typing.Any]):
    @classmethod
    @property
    def Instance(cls) -> ReferenceEqualityComparer: ...
    def Equals(self, x: typing.Any, y: typing.Any) -> bool: ...
    def GetHashCode(self, obj: typing.Any) -> int: ...
