import abc
import typing

from System import Array_1
from System.Collections.Generic import IEnumerable_1, IList_1
from System.Collections.ObjectModel import ReadOnlyCollection_1
from System.Linq.Expressions import Expression, ExpressionType, LabelTarget, ParameterExpression
from System.Runtime.CompilerServices import CallSiteBinder

class BinaryOperationBinder(DynamicMetaObjectBinder):
    @property
    def Operation(self) -> ExpressionType: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackBinaryOperation due to it being static, abstract and generic.

    FallbackBinaryOperation: FallbackBinaryOperation_MethodGroup
    class FallbackBinaryOperation_MethodGroup:
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, arg: DynamicMetaObject
        ) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self,
            target: DynamicMetaObject,
            arg: DynamicMetaObject,
            errorSuggestion: DynamicMetaObject,
        ) -> DynamicMetaObject: ...

class BindingRestrictions(abc.ABC):
    Empty: BindingRestrictions
    @staticmethod
    def Combine(contributingObjects: IList_1[DynamicMetaObject]) -> BindingRestrictions: ...
    @staticmethod
    def GetExpressionRestriction(expression: Expression) -> BindingRestrictions: ...
    @staticmethod
    def GetInstanceRestriction(
        expression: Expression, instance: typing.Any
    ) -> BindingRestrictions: ...
    @staticmethod
    def GetTypeRestriction(
        expression: Expression, type: typing.Type[typing.Any]
    ) -> BindingRestrictions: ...
    def Merge(self, restrictions: BindingRestrictions) -> BindingRestrictions: ...
    def ToExpression(self) -> Expression: ...

class CallInfo:
    @typing.overload
    def __init__(self, argCount: int, argNames: Array_1[str]) -> None: ...
    @typing.overload
    def __init__(self, argCount: int, argNames: IEnumerable_1[str]) -> None: ...
    @property
    def ArgumentCount(self) -> int: ...
    @property
    def ArgumentNames(self) -> ReadOnlyCollection_1[str]: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...

class ConvertBinder(DynamicMetaObjectBinder):
    @property
    def Explicit(self) -> bool: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    @property
    def Type(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackConvert due to it being static, abstract and generic.

    FallbackConvert: FallbackConvert_MethodGroup
    class FallbackConvert_MethodGroup:
        @typing.overload
        def __call__(self, target: DynamicMetaObject) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
        ) -> DynamicMetaObject: ...

class CreateInstanceBinder(DynamicMetaObjectBinder):
    @property
    def CallInfo(self) -> CallInfo: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackCreateInstance due to it being static, abstract and generic.

    FallbackCreateInstance: FallbackCreateInstance_MethodGroup
    class FallbackCreateInstance_MethodGroup:
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
        ) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self,
            target: DynamicMetaObject,
            args: Array_1[DynamicMetaObject],
            errorSuggestion: DynamicMetaObject,
        ) -> DynamicMetaObject: ...

class DeleteIndexBinder(DynamicMetaObjectBinder):
    @property
    def CallInfo(self) -> CallInfo: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackDeleteIndex due to it being static, abstract and generic.

    FallbackDeleteIndex: FallbackDeleteIndex_MethodGroup
    class FallbackDeleteIndex_MethodGroup:
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, indexes: Array_1[DynamicMetaObject]
        ) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self,
            target: DynamicMetaObject,
            indexes: Array_1[DynamicMetaObject],
            errorSuggestion: DynamicMetaObject,
        ) -> DynamicMetaObject: ...

class DeleteMemberBinder(DynamicMetaObjectBinder):
    @property
    def IgnoreCase(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackDeleteMember due to it being static, abstract and generic.

    FallbackDeleteMember: FallbackDeleteMember_MethodGroup
    class FallbackDeleteMember_MethodGroup:
        @typing.overload
        def __call__(self, target: DynamicMetaObject) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
        ) -> DynamicMetaObject: ...

class DynamicMetaObject:
    @typing.overload
    def __init__(self, expression: Expression, restrictions: BindingRestrictions) -> None: ...
    @typing.overload
    def __init__(
        self, expression: Expression, restrictions: BindingRestrictions, value: typing.Any
    ) -> None: ...
    EmptyMetaObjects: Array_1[DynamicMetaObject]
    @property
    def Expression(self) -> Expression: ...
    @property
    def HasValue(self) -> bool: ...
    @property
    def LimitType(self) -> typing.Type[typing.Any]: ...
    @property
    def Restrictions(self) -> BindingRestrictions: ...
    @property
    def RuntimeType(self) -> typing.Type[typing.Any]: ...
    @property
    def Value(self) -> typing.Any: ...
    def BindBinaryOperation(
        self, binder: BinaryOperationBinder, arg: DynamicMetaObject
    ) -> DynamicMetaObject: ...
    def BindConvert(self, binder: ConvertBinder) -> DynamicMetaObject: ...
    def BindCreateInstance(
        self, binder: CreateInstanceBinder, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    def BindDeleteIndex(
        self, binder: DeleteIndexBinder, indexes: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    def BindDeleteMember(self, binder: DeleteMemberBinder) -> DynamicMetaObject: ...
    def BindGetIndex(
        self, binder: GetIndexBinder, indexes: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    def BindGetMember(self, binder: GetMemberBinder) -> DynamicMetaObject: ...
    def BindInvoke(
        self, binder: InvokeBinder, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    def BindInvokeMember(
        self, binder: InvokeMemberBinder, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    def BindSetIndex(
        self,
        binder: SetIndexBinder,
        indexes: Array_1[DynamicMetaObject],
        value: DynamicMetaObject,
    ) -> DynamicMetaObject: ...
    def BindSetMember(
        self, binder: SetMemberBinder, value: DynamicMetaObject
    ) -> DynamicMetaObject: ...
    def BindUnaryOperation(self, binder: UnaryOperationBinder) -> DynamicMetaObject: ...
    @staticmethod
    def Create(value: typing.Any, expression: Expression) -> DynamicMetaObject: ...
    def GetDynamicMemberNames(self) -> IEnumerable_1[str]: ...

class DynamicMetaObjectBinder(CallSiteBinder):
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def GetUpdateExpression(self, type: typing.Type[typing.Any]) -> Expression: ...
    # Skipped Bind due to it being static, abstract and generic.

    Bind: Bind_MethodGroup
    class Bind_MethodGroup:
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
        ) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self,
            args: Array_1[typing.Any],
            parameters: ReadOnlyCollection_1[ParameterExpression],
            returnLabel: LabelTarget,
        ) -> Expression: ...

    # Skipped Defer due to it being static, abstract and generic.

    Defer: Defer_MethodGroup
    class Defer_MethodGroup:
        @typing.overload
        def __call__(self, args: Array_1[DynamicMetaObject]) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
        ) -> DynamicMetaObject: ...

class GetIndexBinder(DynamicMetaObjectBinder):
    @property
    def CallInfo(self) -> CallInfo: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackGetIndex due to it being static, abstract and generic.

    FallbackGetIndex: FallbackGetIndex_MethodGroup
    class FallbackGetIndex_MethodGroup:
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, indexes: Array_1[DynamicMetaObject]
        ) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self,
            target: DynamicMetaObject,
            indexes: Array_1[DynamicMetaObject],
            errorSuggestion: DynamicMetaObject,
        ) -> DynamicMetaObject: ...

class GetMemberBinder(DynamicMetaObjectBinder):
    @property
    def IgnoreCase(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackGetMember due to it being static, abstract and generic.

    FallbackGetMember: FallbackGetMember_MethodGroup
    class FallbackGetMember_MethodGroup:
        @typing.overload
        def __call__(self, target: DynamicMetaObject) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
        ) -> DynamicMetaObject: ...

class IDynamicMetaObjectProvider(typing.Protocol):
    @abc.abstractmethod
    def GetMetaObject(self, parameter: Expression) -> DynamicMetaObject: ...

class InvokeBinder(DynamicMetaObjectBinder):
    @property
    def CallInfo(self) -> CallInfo: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackInvoke due to it being static, abstract and generic.

    FallbackInvoke: FallbackInvoke_MethodGroup
    class FallbackInvoke_MethodGroup:
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
        ) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self,
            target: DynamicMetaObject,
            args: Array_1[DynamicMetaObject],
            errorSuggestion: DynamicMetaObject,
        ) -> DynamicMetaObject: ...

class InvokeMemberBinder(DynamicMetaObjectBinder):
    @property
    def CallInfo(self) -> CallInfo: ...
    @property
    def IgnoreCase(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    @abc.abstractmethod
    def FallbackInvoke(
        self,
        target: DynamicMetaObject,
        args: Array_1[DynamicMetaObject],
        errorSuggestion: DynamicMetaObject,
    ) -> DynamicMetaObject: ...
    # Skipped FallbackInvokeMember due to it being static, abstract and generic.

    FallbackInvokeMember: FallbackInvokeMember_MethodGroup
    class FallbackInvokeMember_MethodGroup:
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
        ) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self,
            target: DynamicMetaObject,
            args: Array_1[DynamicMetaObject],
            errorSuggestion: DynamicMetaObject,
        ) -> DynamicMetaObject: ...

class SetIndexBinder(DynamicMetaObjectBinder):
    @property
    def CallInfo(self) -> CallInfo: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackSetIndex due to it being static, abstract and generic.

    FallbackSetIndex: FallbackSetIndex_MethodGroup
    class FallbackSetIndex_MethodGroup:
        @typing.overload
        def __call__(
            self,
            target: DynamicMetaObject,
            indexes: Array_1[DynamicMetaObject],
            value: DynamicMetaObject,
        ) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self,
            target: DynamicMetaObject,
            indexes: Array_1[DynamicMetaObject],
            value: DynamicMetaObject,
            errorSuggestion: DynamicMetaObject,
        ) -> DynamicMetaObject: ...

class SetMemberBinder(DynamicMetaObjectBinder):
    @property
    def IgnoreCase(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackSetMember due to it being static, abstract and generic.

    FallbackSetMember: FallbackSetMember_MethodGroup
    class FallbackSetMember_MethodGroup:
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, value: DynamicMetaObject
        ) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self,
            target: DynamicMetaObject,
            value: DynamicMetaObject,
            errorSuggestion: DynamicMetaObject,
        ) -> DynamicMetaObject: ...

class UnaryOperationBinder(DynamicMetaObjectBinder):
    @property
    def Operation(self) -> ExpressionType: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    def Bind(
        self, target: DynamicMetaObject, args: Array_1[DynamicMetaObject]
    ) -> DynamicMetaObject: ...
    # Skipped FallbackUnaryOperation due to it being static, abstract and generic.

    FallbackUnaryOperation: FallbackUnaryOperation_MethodGroup
    class FallbackUnaryOperation_MethodGroup:
        @typing.overload
        def __call__(self, target: DynamicMetaObject) -> DynamicMetaObject: ...
        @typing.overload
        def __call__(
            self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject
        ) -> DynamicMetaObject: ...
