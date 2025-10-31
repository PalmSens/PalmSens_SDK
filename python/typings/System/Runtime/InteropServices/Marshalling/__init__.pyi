import abc
import typing

import clr
from System import Array_1, Attribute, ReadOnlySpan_1, Span_1

class AnsiStringMarshaller(abc.ABC):
    class ManagedToUnmanagedIn:
        @classmethod
        @property
        def BufferSize(cls) -> int: ...
        def Free(self) -> None: ...
        def FromManaged(self, managed: str, buffer: Span_1[int]) -> None: ...
        def ToUnmanaged(self) -> clr.Reference[int]: ...

    @staticmethod
    def ConvertToManaged(unmanaged: clr.Reference[int]) -> str: ...
    @staticmethod
    def ConvertToUnmanaged(managed: str) -> clr.Reference[int]: ...
    @staticmethod
    def Free(unmanaged: clr.Reference[int]) -> None: ...

class ArrayMarshaller_GenericClasses(abc.ABCMeta):
    Generic_ArrayMarshaller_GenericClasses_ArrayMarshaller_2_T = typing.TypeVar(
        'Generic_ArrayMarshaller_GenericClasses_ArrayMarshaller_2_T'
    )
    Generic_ArrayMarshaller_GenericClasses_ArrayMarshaller_2_TUnmanagedElement = typing.TypeVar(
        'Generic_ArrayMarshaller_GenericClasses_ArrayMarshaller_2_TUnmanagedElement'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[Generic_ArrayMarshaller_GenericClasses_ArrayMarshaller_2_T],
            typing.Type[
                Generic_ArrayMarshaller_GenericClasses_ArrayMarshaller_2_TUnmanagedElement
            ],
        ],
    ) -> typing.Type[
        ArrayMarshaller_2[
            Generic_ArrayMarshaller_GenericClasses_ArrayMarshaller_2_T,
            Generic_ArrayMarshaller_GenericClasses_ArrayMarshaller_2_TUnmanagedElement,
        ]
    ]: ...

ArrayMarshaller: ArrayMarshaller_GenericClasses

ArrayMarshaller_2_T = typing.TypeVar('ArrayMarshaller_2_T')
ArrayMarshaller_2_TUnmanagedElement = typing.TypeVar('ArrayMarshaller_2_TUnmanagedElement')

class ArrayMarshaller_2(
    typing.Generic[ArrayMarshaller_2_T, ArrayMarshaller_2_TUnmanagedElement], abc.ABC
):
    ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_T = typing.TypeVar(
        'ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_T'
    )
    ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_TUnmanagedElement = typing.TypeVar(
        'ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_TUnmanagedElement'
    )
    class ManagedToUnmanagedIn_GenericClasses(
        typing.Generic[
            ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_T,
            ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_TUnmanagedElement,
        ],
        abc.ABCMeta,
    ):
        ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_T = (
            ArrayMarshaller_2.ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_T
        )
        ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_TUnmanagedElement = ArrayMarshaller_2.ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_TUnmanagedElement
        def __call__(
            self,
        ) -> ArrayMarshaller_2.ManagedToUnmanagedIn_2[
            ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_T,
            ManagedToUnmanagedIn_GenericClasses_ArrayMarshaller_2_TUnmanagedElement,
        ]: ...

    ManagedToUnmanagedIn: ManagedToUnmanagedIn_GenericClasses[
        ArrayMarshaller_2_T, ArrayMarshaller_2_TUnmanagedElement
    ]

    ManagedToUnmanagedIn_2_T = typing.TypeVar('ManagedToUnmanagedIn_2_T')
    ManagedToUnmanagedIn_2_TUnmanagedElement = typing.TypeVar(
        'ManagedToUnmanagedIn_2_TUnmanagedElement'
    )
    class ManagedToUnmanagedIn_2(
        typing.Generic[ManagedToUnmanagedIn_2_T, ManagedToUnmanagedIn_2_TUnmanagedElement]
    ):
        ManagedToUnmanagedIn_2_T = ArrayMarshaller_2.ManagedToUnmanagedIn_2_T
        ManagedToUnmanagedIn_2_TUnmanagedElement = (
            ArrayMarshaller_2.ManagedToUnmanagedIn_2_TUnmanagedElement
        )
        @classmethod
        @property
        def BufferSize(cls) -> int: ...
        def Free(self) -> None: ...
        def FromManaged(
            self,
            array: Array_1[ManagedToUnmanagedIn_2_T],
            buffer: Span_1[ManagedToUnmanagedIn_2_TUnmanagedElement],
        ) -> None: ...
        def GetManagedValuesSource(self) -> ReadOnlySpan_1[ManagedToUnmanagedIn_2_T]: ...
        def GetUnmanagedValuesDestination(
            self,
        ) -> Span_1[ManagedToUnmanagedIn_2_TUnmanagedElement]: ...
        def ToUnmanaged(self) -> clr.Reference[ManagedToUnmanagedIn_2_TUnmanagedElement]: ...
        # Skipped GetPinnableReference due to it being static, abstract and generic.

        GetPinnableReference: GetPinnableReference_MethodGroup[
            ManagedToUnmanagedIn_2_T, ManagedToUnmanagedIn_2_TUnmanagedElement
        ]
        GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T = typing.TypeVar(
            'GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T'
        )
        GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement = (
            typing.TypeVar(
                'GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement'
            )
        )
        class GetPinnableReference_MethodGroup(
            typing.Generic[
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T,
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement,
            ]
        ):
            GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T = ArrayMarshaller_2.ManagedToUnmanagedIn_2.GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T
            GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement = ArrayMarshaller_2.ManagedToUnmanagedIn_2.GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement
            @typing.overload
            def __call__(
                self,
            ) -> clr.Reference[
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement
            ]: ...
            @typing.overload
            def __call__(
                self, array: Array_1[GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T]
            ) -> clr.Reference[GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T]: ...

    @staticmethod
    def AllocateContainerForManagedElements(
        unmanaged: clr.Reference[ArrayMarshaller_2_TUnmanagedElement], numElements: int
    ) -> Array_1[ArrayMarshaller_2_T]: ...
    @staticmethod
    def AllocateContainerForUnmanagedElements(
        managed: Array_1[ArrayMarshaller_2_T], numElements: clr.Reference[int]
    ) -> clr.Reference[ArrayMarshaller_2_TUnmanagedElement]: ...
    @staticmethod
    def Free(unmanaged: clr.Reference[ArrayMarshaller_2_TUnmanagedElement]) -> None: ...
    @staticmethod
    def GetManagedValuesDestination(
        managed: Array_1[ArrayMarshaller_2_T],
    ) -> Span_1[ArrayMarshaller_2_T]: ...
    @staticmethod
    def GetManagedValuesSource(
        managed: Array_1[ArrayMarshaller_2_T],
    ) -> ReadOnlySpan_1[ArrayMarshaller_2_T]: ...
    @staticmethod
    def GetUnmanagedValuesDestination(
        unmanaged: clr.Reference[ArrayMarshaller_2_TUnmanagedElement], numElements: int
    ) -> Span_1[ArrayMarshaller_2_TUnmanagedElement]: ...
    @staticmethod
    def GetUnmanagedValuesSource(
        unmanagedValue: clr.Reference[ArrayMarshaller_2_TUnmanagedElement], numElements: int
    ) -> ReadOnlySpan_1[ArrayMarshaller_2_TUnmanagedElement]: ...

class BStrStringMarshaller(abc.ABC):
    class ManagedToUnmanagedIn:
        @classmethod
        @property
        def BufferSize(cls) -> int: ...
        def Free(self) -> None: ...
        def FromManaged(self, managed: str, buffer: Span_1[int]) -> None: ...
        def ToUnmanaged(self) -> clr.Reference[int]: ...

    @staticmethod
    def ConvertToManaged(unmanaged: clr.Reference[int]) -> str: ...
    @staticmethod
    def ConvertToUnmanaged(managed: str) -> clr.Reference[int]: ...
    @staticmethod
    def Free(unmanaged: clr.Reference[int]) -> None: ...

class ContiguousCollectionMarshallerAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

class CustomMarshallerAttribute(Attribute):
    def __init__(
        self,
        managedType: typing.Type[typing.Any],
        marshalMode: MarshalMode,
        marshallerType: typing.Type[typing.Any],
    ) -> None: ...

    class GenericPlaceholder:
        pass

    @property
    def ManagedType(self) -> typing.Type[typing.Any]: ...
    @property
    def MarshallerType(self) -> typing.Type[typing.Any]: ...
    @property
    def MarshalMode(self) -> MarshalMode: ...
    @property
    def TypeId(self) -> typing.Any: ...

class MarshalMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Default: MarshalMode  # 0
    ManagedToUnmanagedIn: MarshalMode  # 1
    ManagedToUnmanagedRef: MarshalMode  # 2
    ManagedToUnmanagedOut: MarshalMode  # 3
    UnmanagedToManagedIn: MarshalMode  # 4
    UnmanagedToManagedRef: MarshalMode  # 5
    UnmanagedToManagedOut: MarshalMode  # 6
    ElementIn: MarshalMode  # 7
    ElementRef: MarshalMode  # 8
    ElementOut: MarshalMode  # 9

class MarshalUsingAttribute(Attribute):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, nativeType: typing.Type[typing.Any]) -> None: ...
    ReturnsCountValue: str
    @property
    def ConstantElementCount(self) -> int: ...
    @ConstantElementCount.setter
    def ConstantElementCount(self, value: int) -> int: ...
    @property
    def CountElementName(self) -> str: ...
    @CountElementName.setter
    def CountElementName(self, value: str) -> str: ...
    @property
    def ElementIndirectionDepth(self) -> int: ...
    @ElementIndirectionDepth.setter
    def ElementIndirectionDepth(self, value: int) -> int: ...
    @property
    def NativeType(self) -> typing.Type[typing.Any]: ...
    @property
    def TypeId(self) -> typing.Any: ...

class NativeMarshallingAttribute(Attribute):
    def __init__(self, nativeType: typing.Type[typing.Any]) -> None: ...
    @property
    def NativeType(self) -> typing.Type[typing.Any]: ...
    @property
    def TypeId(self) -> typing.Any: ...

class PointerArrayMarshaller_GenericClasses(abc.ABCMeta):
    Generic_PointerArrayMarshaller_GenericClasses_PointerArrayMarshaller_2_T = typing.TypeVar(
        'Generic_PointerArrayMarshaller_GenericClasses_PointerArrayMarshaller_2_T'
    )
    Generic_PointerArrayMarshaller_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement = typing.TypeVar(
        'Generic_PointerArrayMarshaller_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[
                Generic_PointerArrayMarshaller_GenericClasses_PointerArrayMarshaller_2_T
            ],
            typing.Type[
                Generic_PointerArrayMarshaller_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement
            ],
        ],
    ) -> typing.Type[
        PointerArrayMarshaller_2[
            Generic_PointerArrayMarshaller_GenericClasses_PointerArrayMarshaller_2_T,
            Generic_PointerArrayMarshaller_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement,
        ]
    ]: ...

PointerArrayMarshaller: PointerArrayMarshaller_GenericClasses

PointerArrayMarshaller_2_T = typing.TypeVar('PointerArrayMarshaller_2_T')
PointerArrayMarshaller_2_TUnmanagedElement = typing.TypeVar(
    'PointerArrayMarshaller_2_TUnmanagedElement'
)

class PointerArrayMarshaller_2(
    typing.Generic[PointerArrayMarshaller_2_T, PointerArrayMarshaller_2_TUnmanagedElement],
    abc.ABC,
):
    ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_T = typing.TypeVar(
        'ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_T'
    )
    ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement = (
        typing.TypeVar(
            'ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement'
        )
    )
    class ManagedToUnmanagedIn_GenericClasses(
        typing.Generic[
            ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_T,
            ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement,
        ],
        abc.ABCMeta,
    ):
        ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_T = PointerArrayMarshaller_2.ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_T
        ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement = PointerArrayMarshaller_2.ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement
        def __call__(
            self,
        ) -> PointerArrayMarshaller_2.ManagedToUnmanagedIn_2[
            ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_T,
            ManagedToUnmanagedIn_GenericClasses_PointerArrayMarshaller_2_TUnmanagedElement,
        ]: ...

    ManagedToUnmanagedIn: ManagedToUnmanagedIn_GenericClasses[
        PointerArrayMarshaller_2_T, PointerArrayMarshaller_2_TUnmanagedElement
    ]

    ManagedToUnmanagedIn_2_T = typing.TypeVar('ManagedToUnmanagedIn_2_T')
    ManagedToUnmanagedIn_2_TUnmanagedElement = typing.TypeVar(
        'ManagedToUnmanagedIn_2_TUnmanagedElement'
    )
    class ManagedToUnmanagedIn_2(
        typing.Generic[ManagedToUnmanagedIn_2_T, ManagedToUnmanagedIn_2_TUnmanagedElement]
    ):
        ManagedToUnmanagedIn_2_T = PointerArrayMarshaller_2.ManagedToUnmanagedIn_2_T
        ManagedToUnmanagedIn_2_TUnmanagedElement = (
            PointerArrayMarshaller_2.ManagedToUnmanagedIn_2_TUnmanagedElement
        )
        @classmethod
        @property
        def BufferSize(cls) -> int: ...
        def Free(self) -> None: ...
        def FromManaged(
            self,
            array: Array_1[clr.Reference[ManagedToUnmanagedIn_2_T]],
            buffer: Span_1[ManagedToUnmanagedIn_2_TUnmanagedElement],
        ) -> None: ...
        def GetManagedValuesSource(self) -> ReadOnlySpan_1[int]: ...
        def GetUnmanagedValuesDestination(
            self,
        ) -> Span_1[ManagedToUnmanagedIn_2_TUnmanagedElement]: ...
        def ToUnmanaged(self) -> clr.Reference[ManagedToUnmanagedIn_2_TUnmanagedElement]: ...
        # Skipped GetPinnableReference due to it being static, abstract and generic.

        GetPinnableReference: GetPinnableReference_MethodGroup[
            ManagedToUnmanagedIn_2_T, ManagedToUnmanagedIn_2_TUnmanagedElement
        ]
        GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T = typing.TypeVar(
            'GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T'
        )
        GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement = (
            typing.TypeVar(
                'GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement'
            )
        )
        class GetPinnableReference_MethodGroup(
            typing.Generic[
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T,
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement,
            ]
        ):
            GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T = PointerArrayMarshaller_2.ManagedToUnmanagedIn_2.GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T
            GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement = PointerArrayMarshaller_2.ManagedToUnmanagedIn_2.GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement
            @typing.overload
            def __call__(
                self,
            ) -> clr.Reference[
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement
            ]: ...
            @typing.overload
            def __call__(
                self,
                array: Array_1[
                    clr.Reference[GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T]
                ],
            ) -> clr.Reference[int]: ...

    @staticmethod
    def AllocateContainerForManagedElements(
        unmanaged: clr.Reference[PointerArrayMarshaller_2_TUnmanagedElement], numElements: int
    ) -> Array_1[clr.Reference[PointerArrayMarshaller_2_T]]: ...
    @staticmethod
    def AllocateContainerForUnmanagedElements(
        managed: Array_1[clr.Reference[PointerArrayMarshaller_2_T]],
        numElements: clr.Reference[int],
    ) -> clr.Reference[PointerArrayMarshaller_2_TUnmanagedElement]: ...
    @staticmethod
    def Free(unmanaged: clr.Reference[PointerArrayMarshaller_2_TUnmanagedElement]) -> None: ...
    @staticmethod
    def GetManagedValuesDestination(
        managed: Array_1[clr.Reference[PointerArrayMarshaller_2_T]],
    ) -> Span_1[int]: ...
    @staticmethod
    def GetManagedValuesSource(
        managed: Array_1[clr.Reference[PointerArrayMarshaller_2_T]],
    ) -> ReadOnlySpan_1[int]: ...
    @staticmethod
    def GetUnmanagedValuesDestination(
        unmanaged: clr.Reference[PointerArrayMarshaller_2_TUnmanagedElement], numElements: int
    ) -> Span_1[PointerArrayMarshaller_2_TUnmanagedElement]: ...
    @staticmethod
    def GetUnmanagedValuesSource(
        unmanagedValue: clr.Reference[PointerArrayMarshaller_2_TUnmanagedElement],
        numElements: int,
    ) -> ReadOnlySpan_1[PointerArrayMarshaller_2_TUnmanagedElement]: ...

class ReadOnlySpanMarshaller_GenericClasses(abc.ABCMeta):
    Generic_ReadOnlySpanMarshaller_GenericClasses_ReadOnlySpanMarshaller_2_T = typing.TypeVar(
        'Generic_ReadOnlySpanMarshaller_GenericClasses_ReadOnlySpanMarshaller_2_T'
    )
    Generic_ReadOnlySpanMarshaller_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement = typing.TypeVar(
        'Generic_ReadOnlySpanMarshaller_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[
                Generic_ReadOnlySpanMarshaller_GenericClasses_ReadOnlySpanMarshaller_2_T
            ],
            typing.Type[
                Generic_ReadOnlySpanMarshaller_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement
            ],
        ],
    ) -> typing.Type[
        ReadOnlySpanMarshaller_2[
            Generic_ReadOnlySpanMarshaller_GenericClasses_ReadOnlySpanMarshaller_2_T,
            Generic_ReadOnlySpanMarshaller_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement,
        ]
    ]: ...

ReadOnlySpanMarshaller: ReadOnlySpanMarshaller_GenericClasses

ReadOnlySpanMarshaller_2_T = typing.TypeVar('ReadOnlySpanMarshaller_2_T')
ReadOnlySpanMarshaller_2_TUnmanagedElement = typing.TypeVar(
    'ReadOnlySpanMarshaller_2_TUnmanagedElement'
)

class ReadOnlySpanMarshaller_2(
    typing.Generic[ReadOnlySpanMarshaller_2_T, ReadOnlySpanMarshaller_2_TUnmanagedElement],
    abc.ABC,
):
    ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_T = typing.TypeVar(
        'ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_T'
    )
    ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement = (
        typing.TypeVar(
            'ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement'
        )
    )
    class ManagedToUnmanagedIn_GenericClasses(
        typing.Generic[
            ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_T,
            ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement,
        ],
        abc.ABCMeta,
    ):
        ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_T = ReadOnlySpanMarshaller_2.ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_T
        ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement = ReadOnlySpanMarshaller_2.ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement
        def __call__(
            self,
        ) -> ReadOnlySpanMarshaller_2.ManagedToUnmanagedIn_2[
            ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_T,
            ManagedToUnmanagedIn_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement,
        ]: ...

    ManagedToUnmanagedIn: ManagedToUnmanagedIn_GenericClasses[
        ReadOnlySpanMarshaller_2_T, ReadOnlySpanMarshaller_2_TUnmanagedElement
    ]

    ManagedToUnmanagedIn_2_T = typing.TypeVar('ManagedToUnmanagedIn_2_T')
    ManagedToUnmanagedIn_2_TUnmanagedElement = typing.TypeVar(
        'ManagedToUnmanagedIn_2_TUnmanagedElement'
    )
    class ManagedToUnmanagedIn_2(
        typing.Generic[ManagedToUnmanagedIn_2_T, ManagedToUnmanagedIn_2_TUnmanagedElement]
    ):
        ManagedToUnmanagedIn_2_T = ReadOnlySpanMarshaller_2.ManagedToUnmanagedIn_2_T
        ManagedToUnmanagedIn_2_TUnmanagedElement = (
            ReadOnlySpanMarshaller_2.ManagedToUnmanagedIn_2_TUnmanagedElement
        )
        @classmethod
        @property
        def BufferSize(cls) -> int: ...
        def Free(self) -> None: ...
        def FromManaged(
            self,
            managed: ReadOnlySpan_1[ManagedToUnmanagedIn_2_T],
            buffer: Span_1[ManagedToUnmanagedIn_2_TUnmanagedElement],
        ) -> None: ...
        def GetManagedValuesSource(self) -> ReadOnlySpan_1[ManagedToUnmanagedIn_2_T]: ...
        def GetUnmanagedValuesDestination(
            self,
        ) -> Span_1[ManagedToUnmanagedIn_2_TUnmanagedElement]: ...
        def ToUnmanaged(self) -> clr.Reference[ManagedToUnmanagedIn_2_TUnmanagedElement]: ...
        # Skipped GetPinnableReference due to it being static, abstract and generic.

        GetPinnableReference: GetPinnableReference_MethodGroup[
            ManagedToUnmanagedIn_2_T, ManagedToUnmanagedIn_2_TUnmanagedElement
        ]
        GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T = typing.TypeVar(
            'GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T'
        )
        GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement = (
            typing.TypeVar(
                'GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement'
            )
        )
        class GetPinnableReference_MethodGroup(
            typing.Generic[
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T,
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement,
            ]
        ):
            GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T = ReadOnlySpanMarshaller_2.ManagedToUnmanagedIn_2.GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T
            GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement = ReadOnlySpanMarshaller_2.ManagedToUnmanagedIn_2.GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement
            @typing.overload
            def __call__(
                self,
            ) -> clr.Reference[
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement
            ]: ...
            @typing.overload
            def __call__(
                self,
                managed: ReadOnlySpan_1[
                    GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T
                ],
            ) -> clr.Reference[GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T]: ...

    UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_T = typing.TypeVar(
        'UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_T'
    )
    UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement = (
        typing.TypeVar(
            'UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement'
        )
    )
    class UnmanagedToManagedOut_GenericClasses(
        typing.Generic[
            UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_T,
            UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement,
        ],
        abc.ABCMeta,
    ):
        UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_T = ReadOnlySpanMarshaller_2.UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_T
        UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement = ReadOnlySpanMarshaller_2.UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement
        def __call__(
            self,
        ) -> ReadOnlySpanMarshaller_2.UnmanagedToManagedOut_2[
            UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_T,
            UnmanagedToManagedOut_GenericClasses_ReadOnlySpanMarshaller_2_TUnmanagedElement,
        ]: ...

    UnmanagedToManagedOut: UnmanagedToManagedOut_GenericClasses[
        ReadOnlySpanMarshaller_2_T, ReadOnlySpanMarshaller_2_TUnmanagedElement
    ]

    UnmanagedToManagedOut_2_T = typing.TypeVar('UnmanagedToManagedOut_2_T')
    UnmanagedToManagedOut_2_TUnmanagedElement = typing.TypeVar(
        'UnmanagedToManagedOut_2_TUnmanagedElement'
    )
    class UnmanagedToManagedOut_2(
        typing.Generic[UnmanagedToManagedOut_2_T, UnmanagedToManagedOut_2_TUnmanagedElement],
        abc.ABC,
    ):
        UnmanagedToManagedOut_2_T = ReadOnlySpanMarshaller_2.UnmanagedToManagedOut_2_T
        UnmanagedToManagedOut_2_TUnmanagedElement = (
            ReadOnlySpanMarshaller_2.UnmanagedToManagedOut_2_TUnmanagedElement
        )
        @staticmethod
        def AllocateContainerForUnmanagedElements(
            managed: ReadOnlySpan_1[UnmanagedToManagedOut_2_T], numElements: clr.Reference[int]
        ) -> clr.Reference[UnmanagedToManagedOut_2_TUnmanagedElement]: ...
        @staticmethod
        def GetManagedValuesSource(
            managed: ReadOnlySpan_1[UnmanagedToManagedOut_2_T],
        ) -> ReadOnlySpan_1[UnmanagedToManagedOut_2_T]: ...
        @staticmethod
        def GetUnmanagedValuesDestination(
            unmanaged: clr.Reference[UnmanagedToManagedOut_2_TUnmanagedElement],
            numElements: int,
        ) -> Span_1[UnmanagedToManagedOut_2_TUnmanagedElement]: ...

class SafeHandleMarshaller_GenericClasses(abc.ABCMeta):
    Generic_SafeHandleMarshaller_GenericClasses_SafeHandleMarshaller_1_T = typing.TypeVar(
        'Generic_SafeHandleMarshaller_GenericClasses_SafeHandleMarshaller_1_T'
    )
    def __getitem__(
        self,
        types: typing.Type[
            Generic_SafeHandleMarshaller_GenericClasses_SafeHandleMarshaller_1_T
        ],
    ) -> typing.Type[
        SafeHandleMarshaller_1[
            Generic_SafeHandleMarshaller_GenericClasses_SafeHandleMarshaller_1_T
        ]
    ]: ...

SafeHandleMarshaller: SafeHandleMarshaller_GenericClasses

SafeHandleMarshaller_1_T = typing.TypeVar('SafeHandleMarshaller_1_T')

class SafeHandleMarshaller_1(typing.Generic[SafeHandleMarshaller_1_T], abc.ABC):
    ManagedToUnmanagedIn_GenericClasses_SafeHandleMarshaller_1_T = typing.TypeVar(
        'ManagedToUnmanagedIn_GenericClasses_SafeHandleMarshaller_1_T'
    )
    class ManagedToUnmanagedIn_GenericClasses(
        typing.Generic[ManagedToUnmanagedIn_GenericClasses_SafeHandleMarshaller_1_T],
        abc.ABCMeta,
    ):
        ManagedToUnmanagedIn_GenericClasses_SafeHandleMarshaller_1_T = (
            SafeHandleMarshaller_1.ManagedToUnmanagedIn_GenericClasses_SafeHandleMarshaller_1_T
        )
        def __call__(
            self,
        ) -> SafeHandleMarshaller_1.ManagedToUnmanagedIn_1[
            ManagedToUnmanagedIn_GenericClasses_SafeHandleMarshaller_1_T
        ]: ...

    ManagedToUnmanagedIn: ManagedToUnmanagedIn_GenericClasses[SafeHandleMarshaller_1_T]

    ManagedToUnmanagedIn_1_T = typing.TypeVar('ManagedToUnmanagedIn_1_T')
    class ManagedToUnmanagedIn_1(typing.Generic[ManagedToUnmanagedIn_1_T]):
        ManagedToUnmanagedIn_1_T = SafeHandleMarshaller_1.ManagedToUnmanagedIn_1_T
        def Free(self) -> None: ...
        def FromManaged(self, handle: ManagedToUnmanagedIn_1_T) -> None: ...
        def ToUnmanaged(self) -> int: ...

    ManagedToUnmanagedOut_GenericClasses_SafeHandleMarshaller_1_T = typing.TypeVar(
        'ManagedToUnmanagedOut_GenericClasses_SafeHandleMarshaller_1_T'
    )
    class ManagedToUnmanagedOut_GenericClasses(
        typing.Generic[ManagedToUnmanagedOut_GenericClasses_SafeHandleMarshaller_1_T],
        abc.ABCMeta,
    ):
        ManagedToUnmanagedOut_GenericClasses_SafeHandleMarshaller_1_T = (
            SafeHandleMarshaller_1.ManagedToUnmanagedOut_GenericClasses_SafeHandleMarshaller_1_T
        )
        def __call__(
            self,
        ) -> SafeHandleMarshaller_1.ManagedToUnmanagedOut_1[
            ManagedToUnmanagedOut_GenericClasses_SafeHandleMarshaller_1_T
        ]: ...

    ManagedToUnmanagedOut: ManagedToUnmanagedOut_GenericClasses[SafeHandleMarshaller_1_T]

    ManagedToUnmanagedOut_1_T = typing.TypeVar('ManagedToUnmanagedOut_1_T')
    class ManagedToUnmanagedOut_1(typing.Generic[ManagedToUnmanagedOut_1_T]):
        ManagedToUnmanagedOut_1_T = SafeHandleMarshaller_1.ManagedToUnmanagedOut_1_T
        def __init__(self) -> None: ...
        def Free(self) -> None: ...
        def FromUnmanaged(self, value: int) -> None: ...
        def ToManaged(self) -> ManagedToUnmanagedOut_1_T: ...

    ManagedToUnmanagedRef_GenericClasses_SafeHandleMarshaller_1_T = typing.TypeVar(
        'ManagedToUnmanagedRef_GenericClasses_SafeHandleMarshaller_1_T'
    )
    class ManagedToUnmanagedRef_GenericClasses(
        typing.Generic[ManagedToUnmanagedRef_GenericClasses_SafeHandleMarshaller_1_T],
        abc.ABCMeta,
    ):
        ManagedToUnmanagedRef_GenericClasses_SafeHandleMarshaller_1_T = (
            SafeHandleMarshaller_1.ManagedToUnmanagedRef_GenericClasses_SafeHandleMarshaller_1_T
        )
        def __call__(
            self,
        ) -> SafeHandleMarshaller_1.ManagedToUnmanagedRef_1[
            ManagedToUnmanagedRef_GenericClasses_SafeHandleMarshaller_1_T
        ]: ...

    ManagedToUnmanagedRef: ManagedToUnmanagedRef_GenericClasses[SafeHandleMarshaller_1_T]

    ManagedToUnmanagedRef_1_T = typing.TypeVar('ManagedToUnmanagedRef_1_T')
    class ManagedToUnmanagedRef_1(typing.Generic[ManagedToUnmanagedRef_1_T]):
        ManagedToUnmanagedRef_1_T = SafeHandleMarshaller_1.ManagedToUnmanagedRef_1_T
        def __init__(self) -> None: ...
        def Free(self) -> None: ...
        def FromManaged(self, handle: ManagedToUnmanagedRef_1_T) -> None: ...
        def FromUnmanaged(self, value: int) -> None: ...
        def OnInvoked(self) -> None: ...
        def ToManagedFinally(self) -> ManagedToUnmanagedRef_1_T: ...
        def ToUnmanaged(self) -> int: ...

class SpanMarshaller_GenericClasses(abc.ABCMeta):
    Generic_SpanMarshaller_GenericClasses_SpanMarshaller_2_T = typing.TypeVar(
        'Generic_SpanMarshaller_GenericClasses_SpanMarshaller_2_T'
    )
    Generic_SpanMarshaller_GenericClasses_SpanMarshaller_2_TUnmanagedElement = typing.TypeVar(
        'Generic_SpanMarshaller_GenericClasses_SpanMarshaller_2_TUnmanagedElement'
    )
    def __getitem__(
        self,
        types: typing.Tuple[
            typing.Type[Generic_SpanMarshaller_GenericClasses_SpanMarshaller_2_T],
            typing.Type[
                Generic_SpanMarshaller_GenericClasses_SpanMarshaller_2_TUnmanagedElement
            ],
        ],
    ) -> typing.Type[
        SpanMarshaller_2[
            Generic_SpanMarshaller_GenericClasses_SpanMarshaller_2_T,
            Generic_SpanMarshaller_GenericClasses_SpanMarshaller_2_TUnmanagedElement,
        ]
    ]: ...

SpanMarshaller: SpanMarshaller_GenericClasses

SpanMarshaller_2_T = typing.TypeVar('SpanMarshaller_2_T')
SpanMarshaller_2_TUnmanagedElement = typing.TypeVar('SpanMarshaller_2_TUnmanagedElement')

class SpanMarshaller_2(
    typing.Generic[SpanMarshaller_2_T, SpanMarshaller_2_TUnmanagedElement], abc.ABC
):
    ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_T = typing.TypeVar(
        'ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_T'
    )
    ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_TUnmanagedElement = typing.TypeVar(
        'ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_TUnmanagedElement'
    )
    class ManagedToUnmanagedIn_GenericClasses(
        typing.Generic[
            ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_T,
            ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_TUnmanagedElement,
        ],
        abc.ABCMeta,
    ):
        ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_T = (
            SpanMarshaller_2.ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_T
        )
        ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_TUnmanagedElement = SpanMarshaller_2.ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_TUnmanagedElement
        def __call__(
            self,
        ) -> SpanMarshaller_2.ManagedToUnmanagedIn_2[
            ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_T,
            ManagedToUnmanagedIn_GenericClasses_SpanMarshaller_2_TUnmanagedElement,
        ]: ...

    ManagedToUnmanagedIn: ManagedToUnmanagedIn_GenericClasses[
        SpanMarshaller_2_T, SpanMarshaller_2_TUnmanagedElement
    ]

    ManagedToUnmanagedIn_2_T = typing.TypeVar('ManagedToUnmanagedIn_2_T')
    ManagedToUnmanagedIn_2_TUnmanagedElement = typing.TypeVar(
        'ManagedToUnmanagedIn_2_TUnmanagedElement'
    )
    class ManagedToUnmanagedIn_2(
        typing.Generic[ManagedToUnmanagedIn_2_T, ManagedToUnmanagedIn_2_TUnmanagedElement]
    ):
        ManagedToUnmanagedIn_2_T = SpanMarshaller_2.ManagedToUnmanagedIn_2_T
        ManagedToUnmanagedIn_2_TUnmanagedElement = (
            SpanMarshaller_2.ManagedToUnmanagedIn_2_TUnmanagedElement
        )
        @classmethod
        @property
        def BufferSize(cls) -> int: ...
        def Free(self) -> None: ...
        def FromManaged(
            self,
            managed: Span_1[ManagedToUnmanagedIn_2_T],
            buffer: Span_1[ManagedToUnmanagedIn_2_TUnmanagedElement],
        ) -> None: ...
        def GetManagedValuesSource(self) -> ReadOnlySpan_1[ManagedToUnmanagedIn_2_T]: ...
        def GetUnmanagedValuesDestination(
            self,
        ) -> Span_1[ManagedToUnmanagedIn_2_TUnmanagedElement]: ...
        def ToUnmanaged(self) -> clr.Reference[ManagedToUnmanagedIn_2_TUnmanagedElement]: ...
        # Skipped GetPinnableReference due to it being static, abstract and generic.

        GetPinnableReference: GetPinnableReference_MethodGroup[
            ManagedToUnmanagedIn_2_T, ManagedToUnmanagedIn_2_TUnmanagedElement
        ]
        GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T = typing.TypeVar(
            'GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T'
        )
        GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement = (
            typing.TypeVar(
                'GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement'
            )
        )
        class GetPinnableReference_MethodGroup(
            typing.Generic[
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T,
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement,
            ]
        ):
            GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T = SpanMarshaller_2.ManagedToUnmanagedIn_2.GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T
            GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement = SpanMarshaller_2.ManagedToUnmanagedIn_2.GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement
            @typing.overload
            def __call__(
                self,
            ) -> clr.Reference[
                GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_TUnmanagedElement
            ]: ...
            @typing.overload
            def __call__(
                self, managed: Span_1[GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T]
            ) -> clr.Reference[GetPinnableReference_MethodGroup_ManagedToUnmanagedIn_2_T]: ...

    @staticmethod
    def AllocateContainerForManagedElements(
        unmanaged: clr.Reference[SpanMarshaller_2_TUnmanagedElement], numElements: int
    ) -> Span_1[SpanMarshaller_2_T]: ...
    @staticmethod
    def AllocateContainerForUnmanagedElements(
        managed: Span_1[SpanMarshaller_2_T], numElements: clr.Reference[int]
    ) -> clr.Reference[SpanMarshaller_2_TUnmanagedElement]: ...
    @staticmethod
    def Free(unmanaged: clr.Reference[SpanMarshaller_2_TUnmanagedElement]) -> None: ...
    @staticmethod
    def GetManagedValuesDestination(
        managed: Span_1[SpanMarshaller_2_T],
    ) -> Span_1[SpanMarshaller_2_T]: ...
    @staticmethod
    def GetManagedValuesSource(
        managed: Span_1[SpanMarshaller_2_T],
    ) -> ReadOnlySpan_1[SpanMarshaller_2_T]: ...
    @staticmethod
    def GetUnmanagedValuesDestination(
        unmanaged: clr.Reference[SpanMarshaller_2_TUnmanagedElement], numElements: int
    ) -> Span_1[SpanMarshaller_2_TUnmanagedElement]: ...
    @staticmethod
    def GetUnmanagedValuesSource(
        unmanaged: clr.Reference[SpanMarshaller_2_TUnmanagedElement], numElements: int
    ) -> ReadOnlySpan_1[SpanMarshaller_2_TUnmanagedElement]: ...

class Utf16StringMarshaller(abc.ABC):
    @staticmethod
    def ConvertToManaged(unmanaged: clr.Reference[int]) -> str: ...
    @staticmethod
    def ConvertToUnmanaged(managed: str) -> clr.Reference[int]: ...
    @staticmethod
    def Free(unmanaged: clr.Reference[int]) -> None: ...
    @staticmethod
    def GetPinnableReference(str: str) -> clr.Reference[str]: ...

class Utf8StringMarshaller(abc.ABC):
    class ManagedToUnmanagedIn:
        @classmethod
        @property
        def BufferSize(cls) -> int: ...
        def Free(self) -> None: ...
        def FromManaged(self, managed: str, buffer: Span_1[int]) -> None: ...
        def ToUnmanaged(self) -> clr.Reference[int]: ...

    @staticmethod
    def ConvertToManaged(unmanaged: clr.Reference[int]) -> str: ...
    @staticmethod
    def ConvertToUnmanaged(managed: str) -> clr.Reference[int]: ...
    @staticmethod
    def Free(unmanaged: clr.Reference[int]) -> None: ...
