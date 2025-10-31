import abc
import typing

import clr
from System import (
    Array_1,
    Delegate,
    Guid,
    IEquatable_1,
    ModuleHandle,
    RuntimeFieldHandle,
    RuntimeMethodHandle,
    RuntimeTypeHandle,
)
from System.Collections.Generic import IEnumerable_1
from System.Globalization import CultureInfo
from System.IO import FileStream, Stream
from System.Reflection import (
    Assembly,
    AssemblyName,
    Binder,
    BindingFlags,
    CallingConventions,
    ConstructorInfo,
    CustomAttributeData,
    EventAttributes,
    EventInfo,
    FieldAttributes,
    FieldInfo,
    GenericParameterAttributes,
    ICustomAttributeProvider,
    LocalVariableInfo,
    ManifestResourceInfo,
    MemberInfo,
    MemberTypes,
    MethodAttributes,
    MethodBase,
    MethodImplAttributes,
    MethodInfo,
    Module,
    ParameterAttributes,
    ParameterInfo,
    PropertyAttributes,
    PropertyInfo,
    TypeAttributes,
    TypeInfo,
)
from System.Runtime.InteropServices import CallingConvention, CharSet, StructLayoutAttribute
from System.Security import SecurityRuleSet

class AssemblyBuilder(Assembly):
    @property
    def CodeBase(self) -> str: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DefinedTypes(self) -> IEnumerable_1[TypeInfo]: ...
    @property
    def EntryPoint(self) -> MethodInfo: ...
    @property
    def EscapedCodeBase(self) -> str: ...
    @property
    def ExportedTypes(self) -> IEnumerable_1[typing.Type[typing.Any]]: ...
    @property
    def FullName(self) -> str: ...
    @property
    def GlobalAssemblyCache(self) -> bool: ...
    @property
    def HostContext(self) -> int: ...
    @property
    def ImageRuntimeVersion(self) -> str: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsDynamic(self) -> bool: ...
    @property
    def IsFullyTrusted(self) -> bool: ...
    @property
    def Location(self) -> str: ...
    @property
    def ManifestModule(self) -> Module: ...
    @property
    def Modules(self) -> IEnumerable_1[Module]: ...
    @property
    def ReflectionOnly(self) -> bool: ...
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet: ...
    def DefineDynamicModule(self, name: str) -> ModuleBuilder: ...
    def GetDynamicModule(self, name: str) -> ModuleBuilder: ...
    def GetExportedTypes(self) -> Array_1[typing.Type[typing.Any]]: ...
    def GetFile(self, name: str) -> FileStream: ...
    def GetFiles(self, getResourceModules: bool) -> Array_1[FileStream]: ...
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo: ...
    def GetManifestResourceNames(self) -> Array_1[str]: ...
    # Skipped DefineDynamicAssembly due to it being static, abstract and generic.

    DefineDynamicAssembly: DefineDynamicAssembly_MethodGroup
    class DefineDynamicAssembly_MethodGroup:
        @typing.overload
        def __call__(
            self, name: AssemblyName, access: AssemblyBuilderAccess
        ) -> AssemblyBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: AssemblyName,
            access: AssemblyBuilderAccess,
            assemblyAttributes: IEnumerable_1[CustomAttributeBuilder],
        ) -> AssemblyBuilder: ...

    # Skipped GetManifestResourceStream due to it being static, abstract and generic.

    GetManifestResourceStream: GetManifestResourceStream_MethodGroup
    class GetManifestResourceStream_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> Stream: ...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], name: str) -> Stream: ...

    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class AssemblyBuilderAccess(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Run: AssemblyBuilderAccess  # 1
    RunAndCollect: AssemblyBuilderAccess  # 9

class ConstructorBuilder(ConstructorInfo):
    @property
    def Attributes(self) -> MethodAttributes: ...
    @property
    def CallingConvention(self) -> CallingConventions: ...
    @property
    def ContainsGenericParameters(self) -> bool: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DeclaringType(self) -> typing.Type[typing.Any]: ...
    @property
    def InitLocals(self) -> bool: ...
    @InitLocals.setter
    def InitLocals(self, value: bool) -> bool: ...
    @property
    def IsAbstract(self) -> bool: ...
    @property
    def IsAssembly(self) -> bool: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsConstructedGenericMethod(self) -> bool: ...
    @property
    def IsConstructor(self) -> bool: ...
    @property
    def IsFamily(self) -> bool: ...
    @property
    def IsFamilyAndAssembly(self) -> bool: ...
    @property
    def IsFamilyOrAssembly(self) -> bool: ...
    @property
    def IsFinal(self) -> bool: ...
    @property
    def IsGenericMethod(self) -> bool: ...
    @property
    def IsGenericMethodDefinition(self) -> bool: ...
    @property
    def IsHideBySig(self) -> bool: ...
    @property
    def IsPrivate(self) -> bool: ...
    @property
    def IsPublic(self) -> bool: ...
    @property
    def IsSecurityCritical(self) -> bool: ...
    @property
    def IsSecuritySafeCritical(self) -> bool: ...
    @property
    def IsSecurityTransparent(self) -> bool: ...
    @property
    def IsSpecialName(self) -> bool: ...
    @property
    def IsStatic(self) -> bool: ...
    @property
    def IsVirtual(self) -> bool: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> str: ...
    @property
    def ReflectedType(self) -> typing.Type[typing.Any]: ...
    def DefineParameter(
        self, iSequence: int, attributes: ParameterAttributes, strParamName: str
    ) -> ParameterBuilder: ...
    def SetImplementationFlags(self, attributes: MethodImplAttributes) -> None: ...
    # Skipped GetILGenerator due to it being static, abstract and generic.

    GetILGenerator: GetILGenerator_MethodGroup
    class GetILGenerator_MethodGroup:
        @typing.overload
        def __call__(self) -> ILGenerator: ...
        @typing.overload
        def __call__(self, streamSize: int) -> ILGenerator: ...

    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class CustomAttributeBuilder:
    @typing.overload
    def __init__(self, con: ConstructorInfo, constructorArgs: Array_1[typing.Any]) -> None: ...
    @typing.overload
    def __init__(
        self,
        con: ConstructorInfo,
        constructorArgs: Array_1[typing.Any],
        namedFields: Array_1[FieldInfo],
        fieldValues: Array_1[typing.Any],
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        con: ConstructorInfo,
        constructorArgs: Array_1[typing.Any],
        namedProperties: Array_1[PropertyInfo],
        propertyValues: Array_1[typing.Any],
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        con: ConstructorInfo,
        constructorArgs: Array_1[typing.Any],
        namedProperties: Array_1[PropertyInfo],
        propertyValues: Array_1[typing.Any],
        namedFields: Array_1[FieldInfo],
        fieldValues: Array_1[typing.Any],
    ) -> None: ...

class DynamicILInfo:
    @property
    def DynamicMethod(self) -> DynamicMethod: ...
    # Skipped GetTokenFor due to it being static, abstract and generic.

    GetTokenFor: GetTokenFor_MethodGroup
    class GetTokenFor_MethodGroup:
        @typing.overload
        def __call__(self, signature: Array_1[int]) -> int: ...
        @typing.overload
        def __call__(self, method: DynamicMethod) -> int: ...
        @typing.overload
        def __call__(self, field: RuntimeFieldHandle) -> int: ...
        @typing.overload
        def __call__(self, literal: str) -> int: ...
        @typing.overload
        def __call__(self, method: RuntimeMethodHandle) -> int: ...
        @typing.overload
        def __call__(self, type: RuntimeTypeHandle) -> int: ...
        @typing.overload
        def __call__(
            self, field: RuntimeFieldHandle, contextType: RuntimeTypeHandle
        ) -> int: ...
        @typing.overload
        def __call__(
            self, method: RuntimeMethodHandle, contextType: RuntimeTypeHandle
        ) -> int: ...

    # Skipped SetCode due to it being static, abstract and generic.

    SetCode: SetCode_MethodGroup
    class SetCode_MethodGroup:
        @typing.overload
        def __call__(self, code: Array_1[int], maxStackSize: int) -> None: ...
        @typing.overload
        def __call__(
            self, code: clr.Reference[int], codeSize: int, maxStackSize: int
        ) -> None: ...

    # Skipped SetExceptions due to it being static, abstract and generic.

    SetExceptions: SetExceptions_MethodGroup
    class SetExceptions_MethodGroup:
        @typing.overload
        def __call__(self, exceptions: Array_1[int]) -> None: ...
        @typing.overload
        def __call__(self, exceptions: clr.Reference[int], exceptionsSize: int) -> None: ...

    # Skipped SetLocalSignature due to it being static, abstract and generic.

    SetLocalSignature: SetLocalSignature_MethodGroup
    class SetLocalSignature_MethodGroup:
        @typing.overload
        def __call__(self, localSignature: Array_1[int]) -> None: ...
        @typing.overload
        def __call__(self, localSignature: clr.Reference[int], signatureSize: int) -> None: ...

class DynamicMethod(MethodInfo):
    @typing.overload
    def __init__(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: typing.Type[typing.Any],
        parameterTypes: Array_1[typing.Type[typing.Any]],
        m: Module,
        skipVisibility: bool,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        name: str,
        attributes: MethodAttributes,
        callingConvention: CallingConventions,
        returnType: typing.Type[typing.Any],
        parameterTypes: Array_1[typing.Type[typing.Any]],
        owner: typing.Type[typing.Any],
        skipVisibility: bool,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        name: str,
        returnType: typing.Type[typing.Any],
        parameterTypes: Array_1[typing.Type[typing.Any]],
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        name: str,
        returnType: typing.Type[typing.Any],
        parameterTypes: Array_1[typing.Type[typing.Any]],
        m: Module,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        name: str,
        returnType: typing.Type[typing.Any],
        parameterTypes: Array_1[typing.Type[typing.Any]],
        m: Module,
        skipVisibility: bool,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        name: str,
        returnType: typing.Type[typing.Any],
        parameterTypes: Array_1[typing.Type[typing.Any]],
        owner: typing.Type[typing.Any],
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        name: str,
        returnType: typing.Type[typing.Any],
        parameterTypes: Array_1[typing.Type[typing.Any]],
        owner: typing.Type[typing.Any],
        skipVisibility: bool,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        name: str,
        returnType: typing.Type[typing.Any],
        parameterTypes: Array_1[typing.Type[typing.Any]],
        restrictedSkipVisibility: bool,
    ) -> None: ...
    @property
    def Attributes(self) -> MethodAttributes: ...
    @property
    def CallingConvention(self) -> CallingConventions: ...
    @property
    def ContainsGenericParameters(self) -> bool: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DeclaringType(self) -> typing.Type[typing.Any]: ...
    @property
    def InitLocals(self) -> bool: ...
    @InitLocals.setter
    def InitLocals(self, value: bool) -> bool: ...
    @property
    def IsAbstract(self) -> bool: ...
    @property
    def IsAssembly(self) -> bool: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsConstructedGenericMethod(self) -> bool: ...
    @property
    def IsConstructor(self) -> bool: ...
    @property
    def IsFamily(self) -> bool: ...
    @property
    def IsFamilyAndAssembly(self) -> bool: ...
    @property
    def IsFamilyOrAssembly(self) -> bool: ...
    @property
    def IsFinal(self) -> bool: ...
    @property
    def IsGenericMethod(self) -> bool: ...
    @property
    def IsGenericMethodDefinition(self) -> bool: ...
    @property
    def IsHideBySig(self) -> bool: ...
    @property
    def IsPrivate(self) -> bool: ...
    @property
    def IsPublic(self) -> bool: ...
    @property
    def IsSecurityCritical(self) -> bool: ...
    @property
    def IsSecuritySafeCritical(self) -> bool: ...
    @property
    def IsSecurityTransparent(self) -> bool: ...
    @property
    def IsSpecialName(self) -> bool: ...
    @property
    def IsStatic(self) -> bool: ...
    @property
    def IsVirtual(self) -> bool: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> str: ...
    @property
    def ReflectedType(self) -> typing.Type[typing.Any]: ...
    @property
    def ReturnParameter(self) -> ParameterInfo: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    def DefineParameter(
        self, position: int, attributes: ParameterAttributes, parameterName: str
    ) -> ParameterBuilder: ...
    def GetBaseDefinition(self) -> MethodInfo: ...
    def GetDynamicILInfo(self) -> DynamicILInfo: ...
    def GetMethodImplementationFlags(self) -> MethodImplAttributes: ...
    def GetParameters(self) -> Array_1[ParameterInfo]: ...
    def Invoke(
        self,
        obj: typing.Any,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array_1[typing.Any],
        culture: CultureInfo,
    ) -> typing.Any: ...
    def IsDefined(self, attributeType: typing.Type[typing.Any], inherit: bool) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped CreateDelegate due to it being static, abstract and generic.

    CreateDelegate: CreateDelegate_MethodGroup
    class CreateDelegate_MethodGroup:
        @typing.overload
        def __call__(self, delegateType: typing.Type[typing.Any]) -> Delegate: ...
        @typing.overload
        def __call__(
            self, delegateType: typing.Type[typing.Any], target: typing.Any
        ) -> Delegate: ...

    # Skipped GetCustomAttributes due to it being static, abstract and generic.

    GetCustomAttributes: GetCustomAttributes_MethodGroup
    class GetCustomAttributes_MethodGroup:
        @typing.overload
        def __call__(self, inherit: bool) -> Array_1[typing.Any]: ...
        @typing.overload
        def __call__(
            self, attributeType: typing.Type[typing.Any], inherit: bool
        ) -> Array_1[typing.Any]: ...

    # Skipped GetILGenerator due to it being static, abstract and generic.

    GetILGenerator: GetILGenerator_MethodGroup
    class GetILGenerator_MethodGroup:
        @typing.overload
        def __call__(self) -> ILGenerator: ...
        @typing.overload
        def __call__(self, streamSize: int) -> ILGenerator: ...

class EnumBuilder(TypeInfo):
    @property
    def Assembly(self) -> Assembly: ...
    @property
    def AssemblyQualifiedName(self) -> str: ...
    @property
    def Attributes(self) -> TypeAttributes: ...
    @property
    def BaseType(self) -> typing.Type[typing.Any]: ...
    @property
    def ContainsGenericParameters(self) -> bool: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DeclaredConstructors(self) -> IEnumerable_1[ConstructorInfo]: ...
    @property
    def DeclaredEvents(self) -> IEnumerable_1[EventInfo]: ...
    @property
    def DeclaredFields(self) -> IEnumerable_1[FieldInfo]: ...
    @property
    def DeclaredMembers(self) -> IEnumerable_1[MemberInfo]: ...
    @property
    def DeclaredMethods(self) -> IEnumerable_1[MethodInfo]: ...
    @property
    def DeclaredNestedTypes(self) -> IEnumerable_1[TypeInfo]: ...
    @property
    def DeclaredProperties(self) -> IEnumerable_1[PropertyInfo]: ...
    @property
    def DeclaringMethod(self) -> MethodBase: ...
    @property
    def DeclaringType(self) -> typing.Type[typing.Any]: ...
    @property
    def FullName(self) -> str: ...
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    @property
    def GenericParameterPosition(self) -> int: ...
    @property
    def GenericTypeArguments(self) -> Array_1[typing.Type[typing.Any]]: ...
    @property
    def GenericTypeParameters(self) -> Array_1[typing.Type[typing.Any]]: ...
    @property
    def GUID(self) -> Guid: ...
    @property
    def HasElementType(self) -> bool: ...
    @property
    def ImplementedInterfaces(self) -> IEnumerable_1[typing.Type[typing.Any]]: ...
    @property
    def IsAbstract(self) -> bool: ...
    @property
    def IsAnsiClass(self) -> bool: ...
    @property
    def IsArray(self) -> bool: ...
    @property
    def IsAutoClass(self) -> bool: ...
    @property
    def IsAutoLayout(self) -> bool: ...
    @property
    def IsByRef(self) -> bool: ...
    @property
    def IsByRefLike(self) -> bool: ...
    @property
    def IsClass(self) -> bool: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsCOMObject(self) -> bool: ...
    @property
    def IsConstructedGenericType(self) -> bool: ...
    @property
    def IsContextful(self) -> bool: ...
    @property
    def IsEnum(self) -> bool: ...
    @property
    def IsExplicitLayout(self) -> bool: ...
    @property
    def IsFunctionPointer(self) -> bool: ...
    @property
    def IsGenericMethodParameter(self) -> bool: ...
    @property
    def IsGenericParameter(self) -> bool: ...
    @property
    def IsGenericType(self) -> bool: ...
    @property
    def IsGenericTypeDefinition(self) -> bool: ...
    @property
    def IsGenericTypeParameter(self) -> bool: ...
    @property
    def IsImport(self) -> bool: ...
    @property
    def IsInterface(self) -> bool: ...
    @property
    def IsLayoutSequential(self) -> bool: ...
    @property
    def IsMarshalByRef(self) -> bool: ...
    @property
    def IsNested(self) -> bool: ...
    @property
    def IsNestedAssembly(self) -> bool: ...
    @property
    def IsNestedFamANDAssem(self) -> bool: ...
    @property
    def IsNestedFamily(self) -> bool: ...
    @property
    def IsNestedFamORAssem(self) -> bool: ...
    @property
    def IsNestedPrivate(self) -> bool: ...
    @property
    def IsNestedPublic(self) -> bool: ...
    @property
    def IsNotPublic(self) -> bool: ...
    @property
    def IsPointer(self) -> bool: ...
    @property
    def IsPrimitive(self) -> bool: ...
    @property
    def IsPublic(self) -> bool: ...
    @property
    def IsSealed(self) -> bool: ...
    @property
    def IsSecurityCritical(self) -> bool: ...
    @property
    def IsSecuritySafeCritical(self) -> bool: ...
    @property
    def IsSecurityTransparent(self) -> bool: ...
    @property
    def IsSerializable(self) -> bool: ...
    @property
    def IsSignatureType(self) -> bool: ...
    @property
    def IsSpecialName(self) -> bool: ...
    @property
    def IsSZArray(self) -> bool: ...
    @property
    def IsTypeDefinition(self) -> bool: ...
    @property
    def IsUnicodeClass(self) -> bool: ...
    @property
    def IsUnmanagedFunctionPointer(self) -> bool: ...
    @property
    def IsValueType(self) -> bool: ...
    @property
    def IsVariableBoundArray(self) -> bool: ...
    @property
    def IsVisible(self) -> bool: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> str: ...
    @property
    def Namespace(self) -> str: ...
    @property
    def ReflectedType(self) -> typing.Type[typing.Any]: ...
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute: ...
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    @property
    def TypeInitializer(self) -> ConstructorInfo: ...
    @property
    def UnderlyingField(self) -> FieldBuilder: ...
    @property
    def UnderlyingSystemType(self) -> typing.Type[typing.Any]: ...
    def CreateType(self) -> typing.Type[typing.Any]: ...
    def CreateTypeInfo(self) -> TypeInfo: ...
    def DefineLiteral(self, literalName: str, literalValue: typing.Any) -> FieldBuilder: ...
    def MakeByRefType(self) -> typing.Type[typing.Any]: ...
    def MakePointerType(self) -> typing.Type[typing.Any]: ...
    # Skipped MakeArrayType due to it being static, abstract and generic.

    MakeArrayType: MakeArrayType_MethodGroup
    class MakeArrayType_MethodGroup:
        @typing.overload
        def __call__(self) -> typing.Type[typing.Any]: ...
        @typing.overload
        def __call__(self, rank: int) -> typing.Type[typing.Any]: ...

    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class EventBuilder(abc.ABC):
    def AddOtherMethod(self, mdBuilder: MethodBuilder) -> None: ...
    def SetAddOnMethod(self, mdBuilder: MethodBuilder) -> None: ...
    def SetRaiseMethod(self, mdBuilder: MethodBuilder) -> None: ...
    def SetRemoveOnMethod(self, mdBuilder: MethodBuilder) -> None: ...
    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class FieldBuilder(FieldInfo):
    @property
    def Attributes(self) -> FieldAttributes: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DeclaringType(self) -> typing.Type[typing.Any]: ...
    @property
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    @property
    def FieldType(self) -> typing.Type[typing.Any]: ...
    @property
    def IsAssembly(self) -> bool: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsFamily(self) -> bool: ...
    @property
    def IsFamilyAndAssembly(self) -> bool: ...
    @property
    def IsFamilyOrAssembly(self) -> bool: ...
    @property
    def IsInitOnly(self) -> bool: ...
    @property
    def IsLiteral(self) -> bool: ...
    @property
    def IsNotSerialized(self) -> bool: ...
    @property
    def IsPinvokeImpl(self) -> bool: ...
    @property
    def IsPrivate(self) -> bool: ...
    @property
    def IsPublic(self) -> bool: ...
    @property
    def IsSecurityCritical(self) -> bool: ...
    @property
    def IsSecuritySafeCritical(self) -> bool: ...
    @property
    def IsSecurityTransparent(self) -> bool: ...
    @property
    def IsSpecialName(self) -> bool: ...
    @property
    def IsStatic(self) -> bool: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> str: ...
    @property
    def ReflectedType(self) -> typing.Type[typing.Any]: ...
    def SetConstant(self, defaultValue: typing.Any) -> None: ...
    def SetOffset(self, iOffset: int) -> None: ...
    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class FlowControl(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Branch: FlowControl  # 0
    Break: FlowControl  # 1
    Call: FlowControl  # 2
    Cond_Branch: FlowControl  # 3
    Meta: FlowControl  # 4
    Next: FlowControl  # 5
    Phi: FlowControl  # 6
    Return: FlowControl  # 7
    Throw: FlowControl  # 8

class GenericTypeParameterBuilder(TypeInfo):
    @property
    def Assembly(self) -> Assembly: ...
    @property
    def AssemblyQualifiedName(self) -> str: ...
    @property
    def Attributes(self) -> TypeAttributes: ...
    @property
    def BaseType(self) -> typing.Type[typing.Any]: ...
    @property
    def ContainsGenericParameters(self) -> bool: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DeclaredConstructors(self) -> IEnumerable_1[ConstructorInfo]: ...
    @property
    def DeclaredEvents(self) -> IEnumerable_1[EventInfo]: ...
    @property
    def DeclaredFields(self) -> IEnumerable_1[FieldInfo]: ...
    @property
    def DeclaredMembers(self) -> IEnumerable_1[MemberInfo]: ...
    @property
    def DeclaredMethods(self) -> IEnumerable_1[MethodInfo]: ...
    @property
    def DeclaredNestedTypes(self) -> IEnumerable_1[TypeInfo]: ...
    @property
    def DeclaredProperties(self) -> IEnumerable_1[PropertyInfo]: ...
    @property
    def DeclaringMethod(self) -> MethodBase: ...
    @property
    def DeclaringType(self) -> typing.Type[typing.Any]: ...
    @property
    def FullName(self) -> str: ...
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    @property
    def GenericParameterPosition(self) -> int: ...
    @property
    def GenericTypeArguments(self) -> Array_1[typing.Type[typing.Any]]: ...
    @property
    def GenericTypeParameters(self) -> Array_1[typing.Type[typing.Any]]: ...
    @property
    def GUID(self) -> Guid: ...
    @property
    def HasElementType(self) -> bool: ...
    @property
    def ImplementedInterfaces(self) -> IEnumerable_1[typing.Type[typing.Any]]: ...
    @property
    def IsAbstract(self) -> bool: ...
    @property
    def IsAnsiClass(self) -> bool: ...
    @property
    def IsArray(self) -> bool: ...
    @property
    def IsAutoClass(self) -> bool: ...
    @property
    def IsAutoLayout(self) -> bool: ...
    @property
    def IsByRef(self) -> bool: ...
    @property
    def IsByRefLike(self) -> bool: ...
    @property
    def IsClass(self) -> bool: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsCOMObject(self) -> bool: ...
    @property
    def IsConstructedGenericType(self) -> bool: ...
    @property
    def IsContextful(self) -> bool: ...
    @property
    def IsEnum(self) -> bool: ...
    @property
    def IsExplicitLayout(self) -> bool: ...
    @property
    def IsFunctionPointer(self) -> bool: ...
    @property
    def IsGenericMethodParameter(self) -> bool: ...
    @property
    def IsGenericParameter(self) -> bool: ...
    @property
    def IsGenericType(self) -> bool: ...
    @property
    def IsGenericTypeDefinition(self) -> bool: ...
    @property
    def IsGenericTypeParameter(self) -> bool: ...
    @property
    def IsImport(self) -> bool: ...
    @property
    def IsInterface(self) -> bool: ...
    @property
    def IsLayoutSequential(self) -> bool: ...
    @property
    def IsMarshalByRef(self) -> bool: ...
    @property
    def IsNested(self) -> bool: ...
    @property
    def IsNestedAssembly(self) -> bool: ...
    @property
    def IsNestedFamANDAssem(self) -> bool: ...
    @property
    def IsNestedFamily(self) -> bool: ...
    @property
    def IsNestedFamORAssem(self) -> bool: ...
    @property
    def IsNestedPrivate(self) -> bool: ...
    @property
    def IsNestedPublic(self) -> bool: ...
    @property
    def IsNotPublic(self) -> bool: ...
    @property
    def IsPointer(self) -> bool: ...
    @property
    def IsPrimitive(self) -> bool: ...
    @property
    def IsPublic(self) -> bool: ...
    @property
    def IsSealed(self) -> bool: ...
    @property
    def IsSecurityCritical(self) -> bool: ...
    @property
    def IsSecuritySafeCritical(self) -> bool: ...
    @property
    def IsSecurityTransparent(self) -> bool: ...
    @property
    def IsSerializable(self) -> bool: ...
    @property
    def IsSignatureType(self) -> bool: ...
    @property
    def IsSpecialName(self) -> bool: ...
    @property
    def IsSZArray(self) -> bool: ...
    @property
    def IsTypeDefinition(self) -> bool: ...
    @property
    def IsUnicodeClass(self) -> bool: ...
    @property
    def IsUnmanagedFunctionPointer(self) -> bool: ...
    @property
    def IsValueType(self) -> bool: ...
    @property
    def IsVariableBoundArray(self) -> bool: ...
    @property
    def IsVisible(self) -> bool: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> str: ...
    @property
    def Namespace(self) -> str: ...
    @property
    def ReflectedType(self) -> typing.Type[typing.Any]: ...
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute: ...
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    @property
    def TypeInitializer(self) -> ConstructorInfo: ...
    @property
    def UnderlyingSystemType(self) -> typing.Type[typing.Any]: ...
    def SetBaseTypeConstraint(self, baseTypeConstraint: typing.Type[typing.Any]) -> None: ...
    def SetGenericParameterAttributes(
        self, genericParameterAttributes: GenericParameterAttributes
    ) -> None: ...
    def SetInterfaceConstraints(
        self, interfaceConstraints: Array_1[typing.Type[typing.Any]]
    ) -> None: ...
    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class ILGenerator(abc.ABC):
    @property
    def ILOffset(self) -> int: ...
    @abc.abstractmethod
    def BeginCatchBlock(self, exceptionType: typing.Type[typing.Any]) -> None: ...
    @abc.abstractmethod
    def BeginExceptFilterBlock(self) -> None: ...
    @abc.abstractmethod
    def BeginExceptionBlock(self) -> Label: ...
    @abc.abstractmethod
    def BeginFaultBlock(self) -> None: ...
    @abc.abstractmethod
    def BeginFinallyBlock(self) -> None: ...
    @abc.abstractmethod
    def BeginScope(self) -> None: ...
    @abc.abstractmethod
    def DefineLabel(self) -> Label: ...
    @abc.abstractmethod
    def EmitCall(
        self,
        opcode: OpCode,
        methodInfo: MethodInfo,
        optionalParameterTypes: Array_1[typing.Type[typing.Any]],
    ) -> None: ...
    @abc.abstractmethod
    def EndExceptionBlock(self) -> None: ...
    @abc.abstractmethod
    def EndScope(self) -> None: ...
    @abc.abstractmethod
    def MarkLabel(self, loc: Label) -> None: ...
    def ThrowException(self, excType: typing.Type[typing.Any]) -> None: ...
    @abc.abstractmethod
    def UsingNamespace(self, usingNamespace: str) -> None: ...
    # Skipped DeclareLocal due to it being static, abstract and generic.

    DeclareLocal: DeclareLocal_MethodGroup
    class DeclareLocal_MethodGroup:
        @typing.overload
        def __call__(self, localType: typing.Type[typing.Any]) -> LocalBuilder: ...
        @typing.overload
        def __call__(
            self, localType: typing.Type[typing.Any], pinned: bool
        ) -> LocalBuilder: ...

    # Skipped Emit due to it being static, abstract and generic.

    Emit: Emit_MethodGroup
    class Emit_MethodGroup:
        @typing.overload
        def __call__(self, opcode: OpCode) -> None: ...
        @typing.overload
        def __call__(self, opcode: OpCode, arg: float) -> None: ...
        # Method Emit(opcode : OpCode, arg : Double) was skipped since it collides with above method
        # Method Emit(opcode : OpCode, arg : Byte) was skipped since it collides with above method
        # Method Emit(opcode : OpCode, arg : Int16) was skipped since it collides with above method
        # Method Emit(opcode : OpCode, arg : Int64) was skipped since it collides with above method
        # Method Emit(opcode : OpCode, arg : Int32) was skipped since it collides with above method
        # Method Emit(opcode : OpCode, arg : SByte) was skipped since it collides with above method
        @typing.overload
        def __call__(self, opcode: OpCode, labels: Array_1[Label]) -> None: ...
        @typing.overload
        def __call__(self, opcode: OpCode, con: ConstructorInfo) -> None: ...
        @typing.overload
        def __call__(self, opcode: OpCode, meth: MethodInfo) -> None: ...
        @typing.overload
        def __call__(self, opcode: OpCode, cls: typing.Type[typing.Any]) -> None: ...
        @typing.overload
        def __call__(self, opcode: OpCode, field: FieldInfo) -> None: ...
        @typing.overload
        def __call__(self, opcode: OpCode, label: Label) -> None: ...
        @typing.overload
        def __call__(self, opcode: OpCode, local: LocalBuilder) -> None: ...
        @typing.overload
        def __call__(self, opcode: OpCode, str: str) -> None: ...
        @typing.overload
        def __call__(self, opcode: OpCode, signature: SignatureHelper) -> None: ...

    # Skipped EmitCalli due to it being static, abstract and generic.

    EmitCalli: EmitCalli_MethodGroup
    class EmitCalli_MethodGroup:
        @typing.overload
        def __call__(
            self,
            opcode: OpCode,
            unmanagedCallConv: CallingConvention,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> None: ...
        @typing.overload
        def __call__(
            self,
            opcode: OpCode,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            optionalParameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> None: ...

    # Skipped EmitWriteLine due to it being static, abstract and generic.

    EmitWriteLine: EmitWriteLine_MethodGroup
    class EmitWriteLine_MethodGroup:
        @typing.overload
        def __call__(self, fld: FieldInfo) -> None: ...
        @typing.overload
        def __call__(self, localBuilder: LocalBuilder) -> None: ...
        @typing.overload
        def __call__(self, value: str) -> None: ...

class Label(IEquatable_1[Label]):
    def GetHashCode(self) -> int: ...
    def __eq__(self, a: Label, b: Label) -> bool: ...
    def __ne__(self, a: Label, b: Label) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: Label) -> bool: ...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...

class LocalBuilder(LocalVariableInfo):
    @property
    def IsPinned(self) -> bool: ...
    @property
    def LocalIndex(self) -> int: ...
    @property
    def LocalType(self) -> typing.Type[typing.Any]: ...

class MethodBuilder(MethodInfo):
    @property
    def Attributes(self) -> MethodAttributes: ...
    @property
    def CallingConvention(self) -> CallingConventions: ...
    @property
    def ContainsGenericParameters(self) -> bool: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DeclaringType(self) -> typing.Type[typing.Any]: ...
    @property
    def InitLocals(self) -> bool: ...
    @InitLocals.setter
    def InitLocals(self, value: bool) -> bool: ...
    @property
    def IsAbstract(self) -> bool: ...
    @property
    def IsAssembly(self) -> bool: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsConstructedGenericMethod(self) -> bool: ...
    @property
    def IsConstructor(self) -> bool: ...
    @property
    def IsFamily(self) -> bool: ...
    @property
    def IsFamilyAndAssembly(self) -> bool: ...
    @property
    def IsFamilyOrAssembly(self) -> bool: ...
    @property
    def IsFinal(self) -> bool: ...
    @property
    def IsGenericMethod(self) -> bool: ...
    @property
    def IsGenericMethodDefinition(self) -> bool: ...
    @property
    def IsHideBySig(self) -> bool: ...
    @property
    def IsPrivate(self) -> bool: ...
    @property
    def IsPublic(self) -> bool: ...
    @property
    def IsSecurityCritical(self) -> bool: ...
    @property
    def IsSecuritySafeCritical(self) -> bool: ...
    @property
    def IsSecurityTransparent(self) -> bool: ...
    @property
    def IsSpecialName(self) -> bool: ...
    @property
    def IsStatic(self) -> bool: ...
    @property
    def IsVirtual(self) -> bool: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> str: ...
    @property
    def ReflectedType(self) -> typing.Type[typing.Any]: ...
    @property
    def ReturnParameter(self) -> ParameterInfo: ...
    @property
    def ReturnType(self) -> typing.Type[typing.Any]: ...
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    def DefineGenericParameters(
        self, names: Array_1[str]
    ) -> Array_1[GenericTypeParameterBuilder]: ...
    def DefineParameter(
        self, position: int, attributes: ParameterAttributes, strParamName: str
    ) -> ParameterBuilder: ...
    def SetImplementationFlags(self, attributes: MethodImplAttributes) -> None: ...
    def SetParameters(self, parameterTypes: Array_1[typing.Type[typing.Any]]) -> None: ...
    def SetReturnType(self, returnType: typing.Type[typing.Any]) -> None: ...
    def SetSignature(
        self,
        returnType: typing.Type[typing.Any],
        returnTypeRequiredCustomModifiers: Array_1[typing.Type[typing.Any]],
        returnTypeOptionalCustomModifiers: Array_1[typing.Type[typing.Any]],
        parameterTypes: Array_1[typing.Type[typing.Any]],
        parameterTypeRequiredCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
        parameterTypeOptionalCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
    ) -> None: ...
    # Skipped GetILGenerator due to it being static, abstract and generic.

    GetILGenerator: GetILGenerator_MethodGroup
    class GetILGenerator_MethodGroup:
        @typing.overload
        def __call__(self) -> ILGenerator: ...
        @typing.overload
        def __call__(self, size: int) -> ILGenerator: ...

    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class ModuleBuilder(Module):
    @property
    def Assembly(self) -> Assembly: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def FullyQualifiedName(self) -> str: ...
    @property
    def MDStreamVersion(self) -> int: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def ModuleHandle(self) -> ModuleHandle: ...
    @property
    def ModuleVersionId(self) -> Guid: ...
    @property
    def Name(self) -> str: ...
    @property
    def ScopeName(self) -> str: ...
    def CreateGlobalFunctions(self) -> None: ...
    def DefineEnum(
        self, name: str, visibility: TypeAttributes, underlyingType: typing.Type[typing.Any]
    ) -> EnumBuilder: ...
    def DefineInitializedData(
        self, name: str, data: Array_1[int], attributes: FieldAttributes
    ) -> FieldBuilder: ...
    def DefineUninitializedData(
        self, name: str, size: int, attributes: FieldAttributes
    ) -> FieldBuilder: ...
    def GetArrayMethod(
        self,
        arrayClass: typing.Type[typing.Any],
        methodName: str,
        callingConvention: CallingConventions,
        returnType: typing.Type[typing.Any],
        parameterTypes: Array_1[typing.Type[typing.Any]],
    ) -> MethodInfo: ...
    @abc.abstractmethod
    def GetFieldMetadataToken(self, field: FieldInfo) -> int: ...
    @abc.abstractmethod
    def GetSignatureMetadataToken(self, signature: SignatureHelper) -> int: ...
    @abc.abstractmethod
    def GetStringMetadataToken(self, stringConstant: str) -> int: ...
    @abc.abstractmethod
    def GetTypeMetadataToken(self, type: typing.Type[typing.Any]) -> int: ...
    # Skipped DefineGlobalMethod due to it being static, abstract and generic.

    DefineGlobalMethod: DefineGlobalMethod_MethodGroup
    class DefineGlobalMethod_MethodGroup:
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: MethodAttributes,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> MethodBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> MethodBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            requiredReturnTypeCustomModifiers: Array_1[typing.Type[typing.Any]],
            optionalReturnTypeCustomModifiers: Array_1[typing.Type[typing.Any]],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            requiredParameterTypeCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
            optionalParameterTypeCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
        ) -> MethodBuilder: ...

    # Skipped DefinePInvokeMethod due to it being static, abstract and generic.

    DefinePInvokeMethod: DefinePInvokeMethod_MethodGroup
    class DefinePInvokeMethod_MethodGroup:
        @typing.overload
        def __call__(
            self,
            name: str,
            dllName: str,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            nativeCallConv: CallingConvention,
            nativeCharSet: CharSet,
        ) -> MethodBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            dllName: str,
            entryName: str,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            nativeCallConv: CallingConvention,
            nativeCharSet: CharSet,
        ) -> MethodBuilder: ...

    # Skipped DefineType due to it being static, abstract and generic.

    DefineType: DefineType_MethodGroup
    class DefineType_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> TypeBuilder: ...
        @typing.overload
        def __call__(self, name: str, attr: TypeAttributes) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self, name: str, attr: TypeAttributes, parent: typing.Type[typing.Any]
        ) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attr: TypeAttributes,
            parent: typing.Type[typing.Any],
            typesize: int,
        ) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attr: TypeAttributes,
            parent: typing.Type[typing.Any],
            interfaces: Array_1[typing.Type[typing.Any]],
        ) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attr: TypeAttributes,
            parent: typing.Type[typing.Any],
            packsize: PackingSize,
        ) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attr: TypeAttributes,
            parent: typing.Type[typing.Any],
            packingSize: PackingSize,
            typesize: int,
        ) -> TypeBuilder: ...

    # Skipped GetMethodMetadataToken due to it being static, abstract and generic.

    GetMethodMetadataToken: GetMethodMetadataToken_MethodGroup
    class GetMethodMetadataToken_MethodGroup:
        @typing.overload
        def __call__(self, constructor: ConstructorInfo) -> int: ...
        @typing.overload
        def __call__(self, method: MethodInfo) -> int: ...

    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class OpCode(IEquatable_1[OpCode]):
    @property
    def FlowControl(self) -> FlowControl: ...
    @property
    def Name(self) -> str: ...
    @property
    def OpCodeType(self) -> OpCodeType: ...
    @property
    def OperandType(self) -> OperandType: ...
    @property
    def Size(self) -> int: ...
    @property
    def StackBehaviourPop(self) -> StackBehaviour: ...
    @property
    def StackBehaviourPush(self) -> StackBehaviour: ...
    @property
    def Value(self) -> int: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, a: OpCode, b: OpCode) -> bool: ...
    def __ne__(self, a: OpCode, b: OpCode) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, obj: OpCode) -> bool: ...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...

class OpCodes:
    Add: OpCode
    Add_Ovf: OpCode
    Add_Ovf_Un: OpCode
    And: OpCode
    Arglist: OpCode
    Beq: OpCode
    Beq_S: OpCode
    Bge: OpCode
    Bge_S: OpCode
    Bge_Un: OpCode
    Bge_Un_S: OpCode
    Bgt: OpCode
    Bgt_S: OpCode
    Bgt_Un: OpCode
    Bgt_Un_S: OpCode
    Ble: OpCode
    Ble_S: OpCode
    Ble_Un: OpCode
    Ble_Un_S: OpCode
    Blt: OpCode
    Blt_S: OpCode
    Blt_Un: OpCode
    Blt_Un_S: OpCode
    Bne_Un: OpCode
    Bne_Un_S: OpCode
    Box: OpCode
    Br: OpCode
    Br_S: OpCode
    Break: OpCode
    Brfalse: OpCode
    Brfalse_S: OpCode
    Brtrue: OpCode
    Brtrue_S: OpCode
    Call: OpCode
    Calli: OpCode
    Callvirt: OpCode
    Castclass: OpCode
    Ceq: OpCode
    Cgt: OpCode
    Cgt_Un: OpCode
    Ckfinite: OpCode
    Clt: OpCode
    Clt_Un: OpCode
    Constrained: OpCode
    Conv_I: OpCode
    Conv_I1: OpCode
    Conv_I2: OpCode
    Conv_I4: OpCode
    Conv_I8: OpCode
    Conv_Ovf_I: OpCode
    Conv_Ovf_I_Un: OpCode
    Conv_Ovf_I1: OpCode
    Conv_Ovf_I1_Un: OpCode
    Conv_Ovf_I2: OpCode
    Conv_Ovf_I2_Un: OpCode
    Conv_Ovf_I4: OpCode
    Conv_Ovf_I4_Un: OpCode
    Conv_Ovf_I8: OpCode
    Conv_Ovf_I8_Un: OpCode
    Conv_Ovf_U: OpCode
    Conv_Ovf_U_Un: OpCode
    Conv_Ovf_U1: OpCode
    Conv_Ovf_U1_Un: OpCode
    Conv_Ovf_U2: OpCode
    Conv_Ovf_U2_Un: OpCode
    Conv_Ovf_U4: OpCode
    Conv_Ovf_U4_Un: OpCode
    Conv_Ovf_U8: OpCode
    Conv_Ovf_U8_Un: OpCode
    Conv_R_Un: OpCode
    Conv_R4: OpCode
    Conv_R8: OpCode
    Conv_U: OpCode
    Conv_U1: OpCode
    Conv_U2: OpCode
    Conv_U4: OpCode
    Conv_U8: OpCode
    Cpblk: OpCode
    Cpobj: OpCode
    Div: OpCode
    Div_Un: OpCode
    Dup: OpCode
    Endfilter: OpCode
    Endfinally: OpCode
    Initblk: OpCode
    Initobj: OpCode
    Isinst: OpCode
    Jmp: OpCode
    Ldarg: OpCode
    Ldarg_0: OpCode
    Ldarg_1: OpCode
    Ldarg_2: OpCode
    Ldarg_3: OpCode
    Ldarg_S: OpCode
    Ldarga: OpCode
    Ldarga_S: OpCode
    Ldc_I4: OpCode
    Ldc_I4_0: OpCode
    Ldc_I4_1: OpCode
    Ldc_I4_2: OpCode
    Ldc_I4_3: OpCode
    Ldc_I4_4: OpCode
    Ldc_I4_5: OpCode
    Ldc_I4_6: OpCode
    Ldc_I4_7: OpCode
    Ldc_I4_8: OpCode
    Ldc_I4_M1: OpCode
    Ldc_I4_S: OpCode
    Ldc_I8: OpCode
    Ldc_R4: OpCode
    Ldc_R8: OpCode
    Ldelem: OpCode
    Ldelem_I: OpCode
    Ldelem_I1: OpCode
    Ldelem_I2: OpCode
    Ldelem_I4: OpCode
    Ldelem_I8: OpCode
    Ldelem_R4: OpCode
    Ldelem_R8: OpCode
    Ldelem_Ref: OpCode
    Ldelem_U1: OpCode
    Ldelem_U2: OpCode
    Ldelem_U4: OpCode
    Ldelema: OpCode
    Ldfld: OpCode
    Ldflda: OpCode
    Ldftn: OpCode
    Ldind_I: OpCode
    Ldind_I1: OpCode
    Ldind_I2: OpCode
    Ldind_I4: OpCode
    Ldind_I8: OpCode
    Ldind_R4: OpCode
    Ldind_R8: OpCode
    Ldind_Ref: OpCode
    Ldind_U1: OpCode
    Ldind_U2: OpCode
    Ldind_U4: OpCode
    Ldlen: OpCode
    Ldloc: OpCode
    Ldloc_0: OpCode
    Ldloc_1: OpCode
    Ldloc_2: OpCode
    Ldloc_3: OpCode
    Ldloc_S: OpCode
    Ldloca: OpCode
    Ldloca_S: OpCode
    Ldnull: OpCode
    Ldobj: OpCode
    Ldsfld: OpCode
    Ldsflda: OpCode
    Ldstr: OpCode
    Ldtoken: OpCode
    Ldvirtftn: OpCode
    Leave: OpCode
    Leave_S: OpCode
    Localloc: OpCode
    Mkrefany: OpCode
    Mul: OpCode
    Mul_Ovf: OpCode
    Mul_Ovf_Un: OpCode
    Neg: OpCode
    Newarr: OpCode
    Newobj: OpCode
    Nop: OpCode
    Not: OpCode
    Or: OpCode
    Pop: OpCode
    Prefix1: OpCode
    Prefix2: OpCode
    Prefix3: OpCode
    Prefix4: OpCode
    Prefix5: OpCode
    Prefix6: OpCode
    Prefix7: OpCode
    Prefixref: OpCode
    Readonly: OpCode
    Refanytype: OpCode
    Refanyval: OpCode
    Rem: OpCode
    Rem_Un: OpCode
    Ret: OpCode
    Rethrow: OpCode
    Shl: OpCode
    Shr: OpCode
    Shr_Un: OpCode
    Sizeof: OpCode
    Starg: OpCode
    Starg_S: OpCode
    Stelem: OpCode
    Stelem_I: OpCode
    Stelem_I1: OpCode
    Stelem_I2: OpCode
    Stelem_I4: OpCode
    Stelem_I8: OpCode
    Stelem_R4: OpCode
    Stelem_R8: OpCode
    Stelem_Ref: OpCode
    Stfld: OpCode
    Stind_I: OpCode
    Stind_I1: OpCode
    Stind_I2: OpCode
    Stind_I4: OpCode
    Stind_I8: OpCode
    Stind_R4: OpCode
    Stind_R8: OpCode
    Stind_Ref: OpCode
    Stloc: OpCode
    Stloc_0: OpCode
    Stloc_1: OpCode
    Stloc_2: OpCode
    Stloc_3: OpCode
    Stloc_S: OpCode
    Stobj: OpCode
    Stsfld: OpCode
    Sub: OpCode
    Sub_Ovf: OpCode
    Sub_Ovf_Un: OpCode
    Switch: OpCode
    Tailcall: OpCode
    Throw: OpCode
    Unaligned: OpCode
    Unbox: OpCode
    Unbox_Any: OpCode
    Volatile: OpCode
    Xor: OpCode
    @staticmethod
    def TakesSingleByteArgument(inst: OpCode) -> bool: ...

class OpCodeType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Annotation: OpCodeType  # 0
    Macro: OpCodeType  # 1
    Nternal: OpCodeType  # 2
    Objmodel: OpCodeType  # 3
    Prefix: OpCodeType  # 4
    Primitive: OpCodeType  # 5

class OperandType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    InlineBrTarget: OperandType  # 0
    InlineField: OperandType  # 1
    InlineI: OperandType  # 2
    InlineI8: OperandType  # 3
    InlineMethod: OperandType  # 4
    InlineNone: OperandType  # 5
    InlinePhi: OperandType  # 6
    InlineR: OperandType  # 7
    InlineSig: OperandType  # 9
    InlineString: OperandType  # 10
    InlineSwitch: OperandType  # 11
    InlineTok: OperandType  # 12
    InlineType: OperandType  # 13
    InlineVar: OperandType  # 14
    ShortInlineBrTarget: OperandType  # 15
    ShortInlineI: OperandType  # 16
    ShortInlineR: OperandType  # 17
    ShortInlineVar: OperandType  # 18

class PackingSize(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Unspecified: PackingSize  # 0
    Size1: PackingSize  # 1
    Size2: PackingSize  # 2
    Size4: PackingSize  # 4
    Size8: PackingSize  # 8
    Size16: PackingSize  # 16
    Size32: PackingSize  # 32
    Size64: PackingSize  # 64
    Size128: PackingSize  # 128

class ParameterBuilder(abc.ABC):
    @property
    def Attributes(self) -> int: ...
    @property
    def IsIn(self) -> bool: ...
    @property
    def IsOptional(self) -> bool: ...
    @property
    def IsOut(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Position(self) -> int: ...
    def SetConstant(self, defaultValue: typing.Any) -> None: ...
    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class PEFileKinds(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Dll: PEFileKinds  # 1
    ConsoleApplication: PEFileKinds  # 2
    WindowApplication: PEFileKinds  # 3

class PropertyBuilder(PropertyInfo):
    @property
    def Attributes(self) -> PropertyAttributes: ...
    @property
    def CanRead(self) -> bool: ...
    @property
    def CanWrite(self) -> bool: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DeclaringType(self) -> typing.Type[typing.Any]: ...
    @property
    def GetMethod(self) -> MethodInfo: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsSpecialName(self) -> bool: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> str: ...
    @property
    def PropertyType(self) -> typing.Type[typing.Any]: ...
    @property
    def ReflectedType(self) -> typing.Type[typing.Any]: ...
    @property
    def SetMethod(self) -> MethodInfo: ...
    def AddOtherMethod(self, mdBuilder: MethodBuilder) -> None: ...
    def SetConstant(self, defaultValue: typing.Any) -> None: ...
    def SetGetMethod(self, mdBuilder: MethodBuilder) -> None: ...
    def SetSetMethod(self, mdBuilder: MethodBuilder) -> None: ...
    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...

class SignatureHelper:
    def AddArguments(
        self,
        arguments: Array_1[typing.Type[typing.Any]],
        requiredCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
        optionalCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
    ) -> None: ...
    def AddSentinel(self) -> None: ...
    def Equals(self, obj: typing.Any) -> bool: ...
    @staticmethod
    def GetFieldSigHelper(mod: Module) -> SignatureHelper: ...
    def GetHashCode(self) -> int: ...
    def GetSignature(self) -> Array_1[int]: ...
    def ToString(self) -> str: ...
    # Skipped AddArgument due to it being static, abstract and generic.

    AddArgument: AddArgument_MethodGroup
    class AddArgument_MethodGroup:
        @typing.overload
        def __call__(self, clsArgument: typing.Type[typing.Any]) -> None: ...
        @typing.overload
        def __call__(self, argument: typing.Type[typing.Any], pinned: bool) -> None: ...
        @typing.overload
        def __call__(
            self,
            argument: typing.Type[typing.Any],
            requiredCustomModifiers: Array_1[typing.Type[typing.Any]],
            optionalCustomModifiers: Array_1[typing.Type[typing.Any]],
        ) -> None: ...

    # Skipped GetLocalVarSigHelper due to it being static, abstract and generic.

    GetLocalVarSigHelper: GetLocalVarSigHelper_MethodGroup
    class GetLocalVarSigHelper_MethodGroup:
        @typing.overload
        def __call__(self) -> SignatureHelper: ...
        @typing.overload
        def __call__(self, mod: Module) -> SignatureHelper: ...

    # Skipped GetMethodSigHelper due to it being static, abstract and generic.

    GetMethodSigHelper: GetMethodSigHelper_MethodGroup
    class GetMethodSigHelper_MethodGroup:
        @typing.overload
        def __call__(
            self, callingConvention: CallingConventions, returnType: typing.Type[typing.Any]
        ) -> SignatureHelper: ...
        @typing.overload
        def __call__(
            self,
            mod: Module,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
        ) -> SignatureHelper: ...
        @typing.overload
        def __call__(
            self,
            mod: Module,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> SignatureHelper: ...

    # Skipped GetPropertySigHelper due to it being static, abstract and generic.

    GetPropertySigHelper: GetPropertySigHelper_MethodGroup
    class GetPropertySigHelper_MethodGroup:
        @typing.overload
        def __call__(
            self,
            mod: Module,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> SignatureHelper: ...
        @typing.overload
        def __call__(
            self,
            mod: Module,
            returnType: typing.Type[typing.Any],
            requiredReturnTypeCustomModifiers: Array_1[typing.Type[typing.Any]],
            optionalReturnTypeCustomModifiers: Array_1[typing.Type[typing.Any]],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            requiredParameterTypeCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
            optionalParameterTypeCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
        ) -> SignatureHelper: ...
        @typing.overload
        def __call__(
            self,
            mod: Module,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            requiredReturnTypeCustomModifiers: Array_1[typing.Type[typing.Any]],
            optionalReturnTypeCustomModifiers: Array_1[typing.Type[typing.Any]],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            requiredParameterTypeCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
            optionalParameterTypeCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
        ) -> SignatureHelper: ...

class StackBehaviour(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Pop0: StackBehaviour  # 0
    Pop1: StackBehaviour  # 1
    Pop1_pop1: StackBehaviour  # 2
    Popi: StackBehaviour  # 3
    Popi_pop1: StackBehaviour  # 4
    Popi_popi: StackBehaviour  # 5
    Popi_popi8: StackBehaviour  # 6
    Popi_popi_popi: StackBehaviour  # 7
    Popi_popr4: StackBehaviour  # 8
    Popi_popr8: StackBehaviour  # 9
    Popref: StackBehaviour  # 10
    Popref_pop1: StackBehaviour  # 11
    Popref_popi: StackBehaviour  # 12
    Popref_popi_popi: StackBehaviour  # 13
    Popref_popi_popi8: StackBehaviour  # 14
    Popref_popi_popr4: StackBehaviour  # 15
    Popref_popi_popr8: StackBehaviour  # 16
    Popref_popi_popref: StackBehaviour  # 17
    Push0: StackBehaviour  # 18
    Push1: StackBehaviour  # 19
    Push1_push1: StackBehaviour  # 20
    Pushi: StackBehaviour  # 21
    Pushi8: StackBehaviour  # 22
    Pushr4: StackBehaviour  # 23
    Pushr8: StackBehaviour  # 24
    Pushref: StackBehaviour  # 25
    Varpop: StackBehaviour  # 26
    Varpush: StackBehaviour  # 27
    Popref_popi_pop1: StackBehaviour  # 28

class TypeBuilder(TypeInfo):
    UnspecifiedTypeSize: int
    @property
    def Assembly(self) -> Assembly: ...
    @property
    def AssemblyQualifiedName(self) -> str: ...
    @property
    def Attributes(self) -> TypeAttributes: ...
    @property
    def BaseType(self) -> typing.Type[typing.Any]: ...
    @property
    def ContainsGenericParameters(self) -> bool: ...
    @property
    def CustomAttributes(self) -> IEnumerable_1[CustomAttributeData]: ...
    @property
    def DeclaredConstructors(self) -> IEnumerable_1[ConstructorInfo]: ...
    @property
    def DeclaredEvents(self) -> IEnumerable_1[EventInfo]: ...
    @property
    def DeclaredFields(self) -> IEnumerable_1[FieldInfo]: ...
    @property
    def DeclaredMembers(self) -> IEnumerable_1[MemberInfo]: ...
    @property
    def DeclaredMethods(self) -> IEnumerable_1[MethodInfo]: ...
    @property
    def DeclaredNestedTypes(self) -> IEnumerable_1[TypeInfo]: ...
    @property
    def DeclaredProperties(self) -> IEnumerable_1[PropertyInfo]: ...
    @property
    def DeclaringMethod(self) -> MethodBase: ...
    @property
    def DeclaringType(self) -> typing.Type[typing.Any]: ...
    @property
    def FullName(self) -> str: ...
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes: ...
    @property
    def GenericParameterPosition(self) -> int: ...
    @property
    def GenericTypeArguments(self) -> Array_1[typing.Type[typing.Any]]: ...
    @property
    def GenericTypeParameters(self) -> Array_1[typing.Type[typing.Any]]: ...
    @property
    def GUID(self) -> Guid: ...
    @property
    def HasElementType(self) -> bool: ...
    @property
    def ImplementedInterfaces(self) -> IEnumerable_1[typing.Type[typing.Any]]: ...
    @property
    def IsAbstract(self) -> bool: ...
    @property
    def IsAnsiClass(self) -> bool: ...
    @property
    def IsArray(self) -> bool: ...
    @property
    def IsAutoClass(self) -> bool: ...
    @property
    def IsAutoLayout(self) -> bool: ...
    @property
    def IsByRef(self) -> bool: ...
    @property
    def IsByRefLike(self) -> bool: ...
    @property
    def IsClass(self) -> bool: ...
    @property
    def IsCollectible(self) -> bool: ...
    @property
    def IsCOMObject(self) -> bool: ...
    @property
    def IsConstructedGenericType(self) -> bool: ...
    @property
    def IsContextful(self) -> bool: ...
    @property
    def IsEnum(self) -> bool: ...
    @property
    def IsExplicitLayout(self) -> bool: ...
    @property
    def IsFunctionPointer(self) -> bool: ...
    @property
    def IsGenericMethodParameter(self) -> bool: ...
    @property
    def IsGenericParameter(self) -> bool: ...
    @property
    def IsGenericType(self) -> bool: ...
    @property
    def IsGenericTypeDefinition(self) -> bool: ...
    @property
    def IsGenericTypeParameter(self) -> bool: ...
    @property
    def IsImport(self) -> bool: ...
    @property
    def IsInterface(self) -> bool: ...
    @property
    def IsLayoutSequential(self) -> bool: ...
    @property
    def IsMarshalByRef(self) -> bool: ...
    @property
    def IsNested(self) -> bool: ...
    @property
    def IsNestedAssembly(self) -> bool: ...
    @property
    def IsNestedFamANDAssem(self) -> bool: ...
    @property
    def IsNestedFamily(self) -> bool: ...
    @property
    def IsNestedFamORAssem(self) -> bool: ...
    @property
    def IsNestedPrivate(self) -> bool: ...
    @property
    def IsNestedPublic(self) -> bool: ...
    @property
    def IsNotPublic(self) -> bool: ...
    @property
    def IsPointer(self) -> bool: ...
    @property
    def IsPrimitive(self) -> bool: ...
    @property
    def IsPublic(self) -> bool: ...
    @property
    def IsSealed(self) -> bool: ...
    @property
    def IsSecurityCritical(self) -> bool: ...
    @property
    def IsSecuritySafeCritical(self) -> bool: ...
    @property
    def IsSecurityTransparent(self) -> bool: ...
    @property
    def IsSerializable(self) -> bool: ...
    @property
    def IsSignatureType(self) -> bool: ...
    @property
    def IsSpecialName(self) -> bool: ...
    @property
    def IsSZArray(self) -> bool: ...
    @property
    def IsTypeDefinition(self) -> bool: ...
    @property
    def IsUnicodeClass(self) -> bool: ...
    @property
    def IsUnmanagedFunctionPointer(self) -> bool: ...
    @property
    def IsValueType(self) -> bool: ...
    @property
    def IsVariableBoundArray(self) -> bool: ...
    @property
    def IsVisible(self) -> bool: ...
    @property
    def MemberType(self) -> MemberTypes: ...
    @property
    def MetadataToken(self) -> int: ...
    @property
    def Module(self) -> Module: ...
    @property
    def Name(self) -> str: ...
    @property
    def Namespace(self) -> str: ...
    @property
    def PackingSize(self) -> PackingSize: ...
    @property
    def ReflectedType(self) -> typing.Type[typing.Any]: ...
    @property
    def Size(self) -> int: ...
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute: ...
    @property
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    @property
    def TypeInitializer(self) -> ConstructorInfo: ...
    @property
    def UnderlyingSystemType(self) -> typing.Type[typing.Any]: ...
    def AddInterfaceImplementation(self, interfaceType: typing.Type[typing.Any]) -> None: ...
    def CreateType(self) -> typing.Type[typing.Any]: ...
    def CreateTypeInfo(self) -> TypeInfo: ...
    def DefineDefaultConstructor(self, attributes: MethodAttributes) -> ConstructorBuilder: ...
    def DefineEvent(
        self, name: str, attributes: EventAttributes, eventtype: typing.Type[typing.Any]
    ) -> EventBuilder: ...
    def DefineGenericParameters(
        self, names: Array_1[str]
    ) -> Array_1[GenericTypeParameterBuilder]: ...
    def DefineInitializedData(
        self, name: str, data: Array_1[int], attributes: FieldAttributes
    ) -> FieldBuilder: ...
    def DefineMethodOverride(
        self, methodInfoBody: MethodInfo, methodInfoDeclaration: MethodInfo
    ) -> None: ...
    def DefineTypeInitializer(self) -> ConstructorBuilder: ...
    def DefineUninitializedData(
        self, name: str, size: int, attributes: FieldAttributes
    ) -> FieldBuilder: ...
    @staticmethod
    def GetConstructor(
        type: typing.Type[typing.Any], constructor: ConstructorInfo
    ) -> ConstructorInfo: ...
    @staticmethod
    def GetField(type: typing.Type[typing.Any], field: FieldInfo) -> FieldInfo: ...
    @staticmethod
    def GetMethod(type: typing.Type[typing.Any], method: MethodInfo) -> MethodInfo: ...
    def IsCreated(self) -> bool: ...
    def MakeByRefType(self) -> typing.Type[typing.Any]: ...
    def MakeGenericType(
        self, typeArguments: Array_1[typing.Type[typing.Any]]
    ) -> typing.Type[typing.Any]: ...
    def MakePointerType(self) -> typing.Type[typing.Any]: ...
    def SetParent(self, parent: typing.Type[typing.Any]) -> None: ...
    # Skipped DefineConstructor due to it being static, abstract and generic.

    DefineConstructor: DefineConstructor_MethodGroup
    class DefineConstructor_MethodGroup:
        @typing.overload
        def __call__(
            self,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> ConstructorBuilder: ...
        @typing.overload
        def __call__(
            self,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            parameterTypes: Array_1[typing.Type[typing.Any]],
            requiredCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
            optionalCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
        ) -> ConstructorBuilder: ...

    # Skipped DefineField due to it being static, abstract and generic.

    DefineField: DefineField_MethodGroup
    class DefineField_MethodGroup:
        @typing.overload
        def __call__(
            self, fieldName: str, type: typing.Type[typing.Any], attributes: FieldAttributes
        ) -> FieldBuilder: ...
        @typing.overload
        def __call__(
            self,
            fieldName: str,
            type: typing.Type[typing.Any],
            requiredCustomModifiers: Array_1[typing.Type[typing.Any]],
            optionalCustomModifiers: Array_1[typing.Type[typing.Any]],
            attributes: FieldAttributes,
        ) -> FieldBuilder: ...

    # Skipped DefineMethod due to it being static, abstract and generic.

    DefineMethod: DefineMethod_MethodGroup
    class DefineMethod_MethodGroup:
        @typing.overload
        def __call__(self, name: str, attributes: MethodAttributes) -> MethodBuilder: ...
        @typing.overload
        def __call__(
            self, name: str, attributes: MethodAttributes, callingConvention: CallingConventions
        ) -> MethodBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: MethodAttributes,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> MethodBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> MethodBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            returnTypeRequiredCustomModifiers: Array_1[typing.Type[typing.Any]],
            returnTypeOptionalCustomModifiers: Array_1[typing.Type[typing.Any]],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            parameterTypeRequiredCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
            parameterTypeOptionalCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
        ) -> MethodBuilder: ...

    # Skipped DefineNestedType due to it being static, abstract and generic.

    DefineNestedType: DefineNestedType_MethodGroup
    class DefineNestedType_MethodGroup:
        @typing.overload
        def __call__(self, name: str) -> TypeBuilder: ...
        @typing.overload
        def __call__(self, name: str, attr: TypeAttributes) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self, name: str, attr: TypeAttributes, parent: typing.Type[typing.Any]
        ) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attr: TypeAttributes,
            parent: typing.Type[typing.Any],
            typeSize: int,
        ) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attr: TypeAttributes,
            parent: typing.Type[typing.Any],
            interfaces: Array_1[typing.Type[typing.Any]],
        ) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attr: TypeAttributes,
            parent: typing.Type[typing.Any],
            packSize: PackingSize,
        ) -> TypeBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attr: TypeAttributes,
            parent: typing.Type[typing.Any],
            packSize: PackingSize,
            typeSize: int,
        ) -> TypeBuilder: ...

    # Skipped DefinePInvokeMethod due to it being static, abstract and generic.

    DefinePInvokeMethod: DefinePInvokeMethod_MethodGroup
    class DefinePInvokeMethod_MethodGroup:
        @typing.overload
        def __call__(
            self,
            name: str,
            dllName: str,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            nativeCallConv: CallingConvention,
            nativeCharSet: CharSet,
        ) -> MethodBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            dllName: str,
            entryName: str,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            nativeCallConv: CallingConvention,
            nativeCharSet: CharSet,
        ) -> MethodBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            dllName: str,
            entryName: str,
            attributes: MethodAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            returnTypeRequiredCustomModifiers: Array_1[typing.Type[typing.Any]],
            returnTypeOptionalCustomModifiers: Array_1[typing.Type[typing.Any]],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            parameterTypeRequiredCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
            parameterTypeOptionalCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
            nativeCallConv: CallingConvention,
            nativeCharSet: CharSet,
        ) -> MethodBuilder: ...

    # Skipped DefineProperty due to it being static, abstract and generic.

    DefineProperty: DefineProperty_MethodGroup
    class DefineProperty_MethodGroup:
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: PropertyAttributes,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> PropertyBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: PropertyAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            parameterTypes: Array_1[typing.Type[typing.Any]],
        ) -> PropertyBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: PropertyAttributes,
            returnType: typing.Type[typing.Any],
            returnTypeRequiredCustomModifiers: Array_1[typing.Type[typing.Any]],
            returnTypeOptionalCustomModifiers: Array_1[typing.Type[typing.Any]],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            parameterTypeRequiredCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
            parameterTypeOptionalCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
        ) -> PropertyBuilder: ...
        @typing.overload
        def __call__(
            self,
            name: str,
            attributes: PropertyAttributes,
            callingConvention: CallingConventions,
            returnType: typing.Type[typing.Any],
            returnTypeRequiredCustomModifiers: Array_1[typing.Type[typing.Any]],
            returnTypeOptionalCustomModifiers: Array_1[typing.Type[typing.Any]],
            parameterTypes: Array_1[typing.Type[typing.Any]],
            parameterTypeRequiredCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
            parameterTypeOptionalCustomModifiers: Array_1[Array_1[typing.Type[typing.Any]]],
        ) -> PropertyBuilder: ...

    # Skipped MakeArrayType due to it being static, abstract and generic.

    MakeArrayType: MakeArrayType_MethodGroup
    class MakeArrayType_MethodGroup:
        @typing.overload
        def __call__(self) -> typing.Type[typing.Any]: ...
        @typing.overload
        def __call__(self, rank: int) -> typing.Type[typing.Any]: ...

    # Skipped SetCustomAttribute due to it being static, abstract and generic.

    SetCustomAttribute: SetCustomAttribute_MethodGroup
    class SetCustomAttribute_MethodGroup:
        @typing.overload
        def __call__(self, customBuilder: CustomAttributeBuilder) -> None: ...
        @typing.overload
        def __call__(self, con: ConstructorInfo, binaryAttribute: Array_1[int]) -> None: ...
