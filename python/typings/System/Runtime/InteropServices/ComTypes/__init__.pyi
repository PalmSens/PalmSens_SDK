import typing, clr, abc
from System import Guid, Array_1

class BIND_OPTS:
    cbStruct : int
    dwTickCountDeadline : int
    grfFlags : int
    grfMode : int


class BINDPTR:
    lpfuncdesc : int
    lptcomp : int
    lpvardesc : int


class CALLCONV(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    CC_CDECL : CALLCONV # 1
    CC_MSCPASCAL : CALLCONV # 2
    CC_PASCAL : CALLCONV # 2
    CC_MACPASCAL : CALLCONV # 3
    CC_STDCALL : CALLCONV # 4
    CC_RESERVED : CALLCONV # 5
    CC_SYSCALL : CALLCONV # 6
    CC_MPWCDECL : CALLCONV # 7
    CC_MPWPASCAL : CALLCONV # 8
    CC_MAX : CALLCONV # 9


class CONNECTDATA:
    dwCookie : int
    pUnk : typing.Any


class DESCKIND(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    DESCKIND_NONE : DESCKIND # 0
    DESCKIND_FUNCDESC : DESCKIND # 1
    DESCKIND_VARDESC : DESCKIND # 2
    DESCKIND_TYPECOMP : DESCKIND # 3
    DESCKIND_IMPLICITAPPOBJ : DESCKIND # 4
    DESCKIND_MAX : DESCKIND # 5


class DISPPARAMS:
    cArgs : int
    cNamedArgs : int
    rgdispidNamedArgs : int
    rgvarg : int


class ELEMDESC:

    class DESCUNION:
        idldesc : IDLDESC
        paramdesc : PARAMDESC

    desc : ELEMDESC.DESCUNION
    tdesc : TYPEDESC


class EXCEPINFO:
    bstrDescription : str
    bstrHelpFile : str
    bstrSource : str
    dwHelpContext : int
    pfnDeferredFillIn : int
    pvReserved : int
    scode : int
    wCode : int
    wReserved : int


class FILETIME:
    dwHighDateTime : int
    dwLowDateTime : int


class FUNCDESC:
    callconv : CALLCONV
    cParams : int
    cParamsOpt : int
    cScodes : int
    elemdescFunc : ELEMDESC
    funckind : FUNCKIND
    invkind : INVOKEKIND
    lprgelemdescParam : int
    lprgscode : int
    memid : int
    oVft : int
    wFuncFlags : int


class FUNCFLAGS(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    FUNCFLAG_FRESTRICTED : FUNCFLAGS # 1
    FUNCFLAG_FSOURCE : FUNCFLAGS # 2
    FUNCFLAG_FBINDABLE : FUNCFLAGS # 4
    FUNCFLAG_FREQUESTEDIT : FUNCFLAGS # 8
    FUNCFLAG_FDISPLAYBIND : FUNCFLAGS # 16
    FUNCFLAG_FDEFAULTBIND : FUNCFLAGS # 32
    FUNCFLAG_FHIDDEN : FUNCFLAGS # 64
    FUNCFLAG_FUSESGETLASTERROR : FUNCFLAGS # 128
    FUNCFLAG_FDEFAULTCOLLELEM : FUNCFLAGS # 256
    FUNCFLAG_FUIDEFAULT : FUNCFLAGS # 512
    FUNCFLAG_FNONBROWSABLE : FUNCFLAGS # 1024
    FUNCFLAG_FREPLACEABLE : FUNCFLAGS # 2048
    FUNCFLAG_FIMMEDIATEBIND : FUNCFLAGS # 4096


class FUNCKIND(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    FUNC_VIRTUAL : FUNCKIND # 0
    FUNC_PUREVIRTUAL : FUNCKIND # 1
    FUNC_NONVIRTUAL : FUNCKIND # 2
    FUNC_STATIC : FUNCKIND # 3
    FUNC_DISPATCH : FUNCKIND # 4


class IBindCtx(typing.Protocol):
    @abc.abstractmethod
    def EnumObjectParam(self, ppenum: clr.Reference[IEnumString]) -> None: ...
    @abc.abstractmethod
    def GetBindOptions(self, pbindopts: clr.Reference[BIND_OPTS]) -> None: ...
    @abc.abstractmethod
    def GetObjectParam(self, pszKey: str, ppunk: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def GetRunningObjectTable(self, pprot: clr.Reference[IRunningObjectTable]) -> None: ...
    @abc.abstractmethod
    def RegisterObjectBound(self, punk: typing.Any) -> None: ...
    @abc.abstractmethod
    def RegisterObjectParam(self, pszKey: str, punk: typing.Any) -> None: ...
    @abc.abstractmethod
    def ReleaseBoundObjects(self) -> None: ...
    @abc.abstractmethod
    def RevokeObjectBound(self, punk: typing.Any) -> None: ...
    @abc.abstractmethod
    def RevokeObjectParam(self, pszKey: str) -> int: ...
    @abc.abstractmethod
    def SetBindOptions(self, pbindopts: clr.Reference[BIND_OPTS]) -> None: ...


class IConnectionPoint(typing.Protocol):
    @abc.abstractmethod
    def Advise(self, pUnkSink: typing.Any, pdwCookie: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def EnumConnections(self, ppEnum: clr.Reference[IEnumConnections]) -> None: ...
    @abc.abstractmethod
    def GetConnectionInterface(self, pIID: clr.Reference[Guid]) -> None: ...
    @abc.abstractmethod
    def GetConnectionPointContainer(self, ppCPC: clr.Reference[IConnectionPointContainer]) -> None: ...
    @abc.abstractmethod
    def Unadvise(self, dwCookie: int) -> None: ...


class IConnectionPointContainer(typing.Protocol):
    @abc.abstractmethod
    def EnumConnectionPoints(self, ppEnum: clr.Reference[IEnumConnectionPoints]) -> None: ...
    @abc.abstractmethod
    def FindConnectionPoint(self, riid: clr.Reference[Guid], ppCP: clr.Reference[IConnectionPoint]) -> None: ...


class IDLDESC:
    dwReserved : int
    wIDLFlags : IDLFLAG


class IDLFLAG(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    IDLFLAG_NONE : IDLFLAG # 0
    IDLFLAG_FIN : IDLFLAG # 1
    IDLFLAG_FOUT : IDLFLAG # 2
    IDLFLAG_FLCID : IDLFLAG # 4
    IDLFLAG_FRETVAL : IDLFLAG # 8


class IEnumConnectionPoints(typing.Protocol):
    @abc.abstractmethod
    def Clone(self, ppenum: clr.Reference[IEnumConnectionPoints]) -> None: ...
    @abc.abstractmethod
    def Next(self, celt: int, rgelt: Array_1[IConnectionPoint], pceltFetched: int) -> int: ...
    @abc.abstractmethod
    def Reset(self) -> None: ...
    @abc.abstractmethod
    def Skip(self, celt: int) -> int: ...


class IEnumConnections(typing.Protocol):
    @abc.abstractmethod
    def Clone(self, ppenum: clr.Reference[IEnumConnections]) -> None: ...
    @abc.abstractmethod
    def Next(self, celt: int, rgelt: Array_1[CONNECTDATA], pceltFetched: int) -> int: ...
    @abc.abstractmethod
    def Reset(self) -> None: ...
    @abc.abstractmethod
    def Skip(self, celt: int) -> int: ...


class IEnumMoniker(typing.Protocol):
    @abc.abstractmethod
    def Clone(self, ppenum: clr.Reference[IEnumMoniker]) -> None: ...
    @abc.abstractmethod
    def Next(self, celt: int, rgelt: Array_1[IMoniker], pceltFetched: int) -> int: ...
    @abc.abstractmethod
    def Reset(self) -> None: ...
    @abc.abstractmethod
    def Skip(self, celt: int) -> int: ...


class IEnumString(typing.Protocol):
    @abc.abstractmethod
    def Clone(self, ppenum: clr.Reference[IEnumString]) -> None: ...
    @abc.abstractmethod
    def Next(self, celt: int, rgelt: Array_1[str], pceltFetched: int) -> int: ...
    @abc.abstractmethod
    def Reset(self) -> None: ...
    @abc.abstractmethod
    def Skip(self, celt: int) -> int: ...


class IEnumVARIANT(typing.Protocol):
    @abc.abstractmethod
    def Clone(self) -> IEnumVARIANT: ...
    @abc.abstractmethod
    def Next(self, celt: int, rgVar: Array_1[typing.Any], pceltFetched: int) -> int: ...
    @abc.abstractmethod
    def Reset(self) -> int: ...
    @abc.abstractmethod
    def Skip(self, celt: int) -> int: ...


class IMoniker(typing.Protocol):
    @abc.abstractmethod
    def BindToObject(self, pbc: IBindCtx, pmkToLeft: IMoniker, riidResult: clr.Reference[Guid], ppvResult: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def BindToStorage(self, pbc: IBindCtx, pmkToLeft: IMoniker, riid: clr.Reference[Guid], ppvObj: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def CommonPrefixWith(self, pmkOther: IMoniker, ppmkPrefix: clr.Reference[IMoniker]) -> None: ...
    @abc.abstractmethod
    def ComposeWith(self, pmkRight: IMoniker, fOnlyIfNotGeneric: bool, ppmkComposite: clr.Reference[IMoniker]) -> None: ...
    @abc.abstractmethod
    def Enum(self, fForward: bool, ppenumMoniker: clr.Reference[IEnumMoniker]) -> None: ...
    @abc.abstractmethod
    def GetClassID(self, pClassID: clr.Reference[Guid]) -> None: ...
    @abc.abstractmethod
    def GetDisplayName(self, pbc: IBindCtx, pmkToLeft: IMoniker, ppszDisplayName: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def GetSizeMax(self, pcbSize: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetTimeOfLastChange(self, pbc: IBindCtx, pmkToLeft: IMoniker, pFileTime: clr.Reference[FILETIME]) -> None: ...
    @abc.abstractmethod
    def Hash(self, pdwHash: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def Inverse(self, ppmk: clr.Reference[IMoniker]) -> None: ...
    @abc.abstractmethod
    def IsDirty(self) -> int: ...
    @abc.abstractmethod
    def IsEqual(self, pmkOtherMoniker: IMoniker) -> int: ...
    @abc.abstractmethod
    def IsRunning(self, pbc: IBindCtx, pmkToLeft: IMoniker, pmkNewlyRunning: IMoniker) -> int: ...
    @abc.abstractmethod
    def IsSystemMoniker(self, pdwMksys: clr.Reference[int]) -> int: ...
    @abc.abstractmethod
    def Load(self, pStm: IStream) -> None: ...
    @abc.abstractmethod
    def ParseDisplayName(self, pbc: IBindCtx, pmkToLeft: IMoniker, pszDisplayName: str, pchEaten: clr.Reference[int], ppmkOut: clr.Reference[IMoniker]) -> None: ...
    @abc.abstractmethod
    def Reduce(self, pbc: IBindCtx, dwReduceHowFar: int, ppmkToLeft: clr.Reference[IMoniker], ppmkReduced: clr.Reference[IMoniker]) -> None: ...
    @abc.abstractmethod
    def RelativePathTo(self, pmkOther: IMoniker, ppmkRelPath: clr.Reference[IMoniker]) -> None: ...
    @abc.abstractmethod
    def Save(self, pStm: IStream, fClearDirty: bool) -> None: ...


class IMPLTYPEFLAGS(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    IMPLTYPEFLAG_FDEFAULT : IMPLTYPEFLAGS # 1
    IMPLTYPEFLAG_FSOURCE : IMPLTYPEFLAGS # 2
    IMPLTYPEFLAG_FRESTRICTED : IMPLTYPEFLAGS # 4
    IMPLTYPEFLAG_FDEFAULTVTABLE : IMPLTYPEFLAGS # 8


class INVOKEKIND(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    INVOKE_FUNC : INVOKEKIND # 1
    INVOKE_PROPERTYGET : INVOKEKIND # 2
    INVOKE_PROPERTYPUT : INVOKEKIND # 4
    INVOKE_PROPERTYPUTREF : INVOKEKIND # 8


class IPersistFile(typing.Protocol):
    @abc.abstractmethod
    def GetClassID(self, pClassID: clr.Reference[Guid]) -> None: ...
    @abc.abstractmethod
    def GetCurFile(self, ppszFileName: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def IsDirty(self) -> int: ...
    @abc.abstractmethod
    def Load(self, pszFileName: str, dwMode: int) -> None: ...
    @abc.abstractmethod
    def Save(self, pszFileName: str, fRemember: bool) -> None: ...
    @abc.abstractmethod
    def SaveCompleted(self, pszFileName: str) -> None: ...


class IRunningObjectTable(typing.Protocol):
    @abc.abstractmethod
    def EnumRunning(self, ppenumMoniker: clr.Reference[IEnumMoniker]) -> None: ...
    @abc.abstractmethod
    def GetObject(self, pmkObjectName: IMoniker, ppunkObject: clr.Reference[typing.Any]) -> int: ...
    @abc.abstractmethod
    def GetTimeOfLastChange(self, pmkObjectName: IMoniker, pfiletime: clr.Reference[FILETIME]) -> int: ...
    @abc.abstractmethod
    def IsRunning(self, pmkObjectName: IMoniker) -> int: ...
    @abc.abstractmethod
    def NoteChangeTime(self, dwRegister: int, pfiletime: clr.Reference[FILETIME]) -> None: ...
    @abc.abstractmethod
    def Register(self, grfFlags: int, punkObject: typing.Any, pmkObjectName: IMoniker) -> int: ...
    @abc.abstractmethod
    def Revoke(self, dwRegister: int) -> None: ...


class IStream(typing.Protocol):
    @abc.abstractmethod
    def Clone(self, ppstm: clr.Reference[IStream]) -> None: ...
    @abc.abstractmethod
    def Commit(self, grfCommitFlags: int) -> None: ...
    @abc.abstractmethod
    def CopyTo(self, pstm: IStream, cb: int, pcbRead: int, pcbWritten: int) -> None: ...
    @abc.abstractmethod
    def LockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None: ...
    @abc.abstractmethod
    def Read(self, pv: Array_1[int], cb: int, pcbRead: int) -> None: ...
    @abc.abstractmethod
    def Revert(self) -> None: ...
    @abc.abstractmethod
    def Seek(self, dlibMove: int, dwOrigin: int, plibNewPosition: int) -> None: ...
    @abc.abstractmethod
    def SetSize(self, libNewSize: int) -> None: ...
    @abc.abstractmethod
    def Stat(self, pstatstg: clr.Reference[STATSTG], grfStatFlag: int) -> None: ...
    @abc.abstractmethod
    def UnlockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None: ...
    @abc.abstractmethod
    def Write(self, pv: Array_1[int], cb: int, pcbWritten: int) -> None: ...


class ITypeComp(typing.Protocol):
    @abc.abstractmethod
    def Bind(self, szName: str, lHashVal: int, wFlags: int, ppTInfo: clr.Reference[ITypeInfo], pDescKind: clr.Reference[DESCKIND], pBindPtr: clr.Reference[BINDPTR]) -> None: ...
    @abc.abstractmethod
    def BindType(self, szName: str, lHashVal: int, ppTInfo: clr.Reference[ITypeInfo], ppTComp: clr.Reference[ITypeComp]) -> None: ...


class ITypeInfo(typing.Protocol):
    @abc.abstractmethod
    def AddressOfMember(self, memid: int, invKind: INVOKEKIND, ppv: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def CreateInstance(self, pUnkOuter: typing.Any, riid: clr.Reference[Guid], ppvObj: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def GetContainingTypeLib(self, ppTLB: clr.Reference[ITypeLib], pIndex: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetDllEntry(self, memid: int, invKind: INVOKEKIND, pBstrDllName: int, pBstrName: int, pwOrdinal: int) -> None: ...
    @abc.abstractmethod
    def GetDocumentation(self, index: int, strName: clr.Reference[str], strDocString: clr.Reference[str], dwHelpContext: clr.Reference[int], strHelpFile: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def GetFuncDesc(self, index: int, ppFuncDesc: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetIDsOfNames(self, rgszNames: Array_1[str], cNames: int, pMemId: Array_1[int]) -> None: ...
    @abc.abstractmethod
    def GetImplTypeFlags(self, index: int, pImplTypeFlags: clr.Reference[IMPLTYPEFLAGS]) -> None: ...
    @abc.abstractmethod
    def GetMops(self, memid: int, pBstrMops: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def GetNames(self, memid: int, rgBstrNames: Array_1[str], cMaxNames: int, pcNames: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetRefTypeInfo(self, hRef: int, ppTI: clr.Reference[ITypeInfo]) -> None: ...
    @abc.abstractmethod
    def GetRefTypeOfImplType(self, index: int, href: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetTypeAttr(self, ppTypeAttr: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetTypeComp(self, ppTComp: clr.Reference[ITypeComp]) -> None: ...
    @abc.abstractmethod
    def GetVarDesc(self, index: int, ppVarDesc: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def Invoke(self, pvInstance: typing.Any, memid: int, wFlags: int, pDispParams: clr.Reference[DISPPARAMS], pVarResult: int, pExcepInfo: int, puArgErr: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def ReleaseFuncDesc(self, pFuncDesc: int) -> None: ...
    @abc.abstractmethod
    def ReleaseTypeAttr(self, pTypeAttr: int) -> None: ...
    @abc.abstractmethod
    def ReleaseVarDesc(self, pVarDesc: int) -> None: ...


class ITypeInfo2(ITypeInfo, typing.Protocol):
    @abc.abstractmethod
    def AddressOfMember(self, memid: int, invKind: INVOKEKIND, ppv: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def CreateInstance(self, pUnkOuter: typing.Any, riid: clr.Reference[Guid], ppvObj: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def GetAllCustData(self, pCustData: int) -> None: ...
    @abc.abstractmethod
    def GetAllFuncCustData(self, index: int, pCustData: int) -> None: ...
    @abc.abstractmethod
    def GetAllImplTypeCustData(self, index: int, pCustData: int) -> None: ...
    @abc.abstractmethod
    def GetAllParamCustData(self, indexFunc: int, indexParam: int, pCustData: int) -> None: ...
    @abc.abstractmethod
    def GetAllVarCustData(self, index: int, pCustData: int) -> None: ...
    @abc.abstractmethod
    def GetContainingTypeLib(self, ppTLB: clr.Reference[ITypeLib], pIndex: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetCustData(self, guid: clr.Reference[Guid], pVarVal: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def GetDllEntry(self, memid: int, invKind: INVOKEKIND, pBstrDllName: int, pBstrName: int, pwOrdinal: int) -> None: ...
    @abc.abstractmethod
    def GetDocumentation(self, index: int, strName: clr.Reference[str], strDocString: clr.Reference[str], dwHelpContext: clr.Reference[int], strHelpFile: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def GetDocumentation2(self, memid: int, pbstrHelpString: clr.Reference[str], pdwHelpStringContext: clr.Reference[int], pbstrHelpStringDll: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def GetFuncCustData(self, index: int, guid: clr.Reference[Guid], pVarVal: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def GetFuncDesc(self, index: int, ppFuncDesc: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetFuncIndexOfMemId(self, memid: int, invKind: INVOKEKIND, pFuncIndex: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetIDsOfNames(self, rgszNames: Array_1[str], cNames: int, pMemId: Array_1[int]) -> None: ...
    @abc.abstractmethod
    def GetImplTypeCustData(self, index: int, guid: clr.Reference[Guid], pVarVal: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def GetImplTypeFlags(self, index: int, pImplTypeFlags: clr.Reference[IMPLTYPEFLAGS]) -> None: ...
    @abc.abstractmethod
    def GetMops(self, memid: int, pBstrMops: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def GetNames(self, memid: int, rgBstrNames: Array_1[str], cMaxNames: int, pcNames: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetParamCustData(self, indexFunc: int, indexParam: int, guid: clr.Reference[Guid], pVarVal: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def GetRefTypeInfo(self, hRef: int, ppTI: clr.Reference[ITypeInfo]) -> None: ...
    @abc.abstractmethod
    def GetRefTypeOfImplType(self, index: int, href: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetTypeAttr(self, ppTypeAttr: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetTypeComp(self, ppTComp: clr.Reference[ITypeComp]) -> None: ...
    @abc.abstractmethod
    def GetTypeFlags(self, pTypeFlags: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetTypeKind(self, pTypeKind: clr.Reference[TYPEKIND]) -> None: ...
    @abc.abstractmethod
    def GetVarCustData(self, index: int, guid: clr.Reference[Guid], pVarVal: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def GetVarDesc(self, index: int, ppVarDesc: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetVarIndexOfMemId(self, memid: int, pVarIndex: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def Invoke(self, pvInstance: typing.Any, memid: int, wFlags: int, pDispParams: clr.Reference[DISPPARAMS], pVarResult: int, pExcepInfo: int, puArgErr: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def ReleaseFuncDesc(self, pFuncDesc: int) -> None: ...
    @abc.abstractmethod
    def ReleaseTypeAttr(self, pTypeAttr: int) -> None: ...
    @abc.abstractmethod
    def ReleaseVarDesc(self, pVarDesc: int) -> None: ...


class ITypeLib(typing.Protocol):
    @abc.abstractmethod
    def FindName(self, szNameBuf: str, lHashVal: int, ppTInfo: Array_1[ITypeInfo], rgMemId: Array_1[int], pcFound: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetDocumentation(self, index: int, strName: clr.Reference[str], strDocString: clr.Reference[str], dwHelpContext: clr.Reference[int], strHelpFile: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def GetLibAttr(self, ppTLibAttr: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetTypeComp(self, ppTComp: clr.Reference[ITypeComp]) -> None: ...
    @abc.abstractmethod
    def GetTypeInfo(self, index: int, ppTI: clr.Reference[ITypeInfo]) -> None: ...
    @abc.abstractmethod
    def GetTypeInfoCount(self) -> int: ...
    @abc.abstractmethod
    def GetTypeInfoOfGuid(self, guid: clr.Reference[Guid], ppTInfo: clr.Reference[ITypeInfo]) -> None: ...
    @abc.abstractmethod
    def GetTypeInfoType(self, index: int, pTKind: clr.Reference[TYPEKIND]) -> None: ...
    @abc.abstractmethod
    def IsName(self, szNameBuf: str, lHashVal: int) -> bool: ...
    @abc.abstractmethod
    def ReleaseTLibAttr(self, pTLibAttr: int) -> None: ...


class ITypeLib2(ITypeLib, typing.Protocol):
    @abc.abstractmethod
    def FindName(self, szNameBuf: str, lHashVal: int, ppTInfo: Array_1[ITypeInfo], rgMemId: Array_1[int], pcFound: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetAllCustData(self, pCustData: int) -> None: ...
    @abc.abstractmethod
    def GetCustData(self, guid: clr.Reference[Guid], pVarVal: clr.Reference[typing.Any]) -> None: ...
    @abc.abstractmethod
    def GetDocumentation(self, index: int, strName: clr.Reference[str], strDocString: clr.Reference[str], dwHelpContext: clr.Reference[int], strHelpFile: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def GetDocumentation2(self, index: int, pbstrHelpString: clr.Reference[str], pdwHelpStringContext: clr.Reference[int], pbstrHelpStringDll: clr.Reference[str]) -> None: ...
    @abc.abstractmethod
    def GetLibAttr(self, ppTLibAttr: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetLibStatistics(self, pcUniqueNames: int, pcchUniqueNames: clr.Reference[int]) -> None: ...
    @abc.abstractmethod
    def GetTypeComp(self, ppTComp: clr.Reference[ITypeComp]) -> None: ...
    @abc.abstractmethod
    def GetTypeInfo(self, index: int, ppTI: clr.Reference[ITypeInfo]) -> None: ...
    @abc.abstractmethod
    def GetTypeInfoCount(self) -> int: ...
    @abc.abstractmethod
    def GetTypeInfoOfGuid(self, guid: clr.Reference[Guid], ppTInfo: clr.Reference[ITypeInfo]) -> None: ...
    @abc.abstractmethod
    def GetTypeInfoType(self, index: int, pTKind: clr.Reference[TYPEKIND]) -> None: ...
    @abc.abstractmethod
    def IsName(self, szNameBuf: str, lHashVal: int) -> bool: ...
    @abc.abstractmethod
    def ReleaseTLibAttr(self, pTLibAttr: int) -> None: ...


class LIBFLAGS(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    LIBFLAG_FRESTRICTED : LIBFLAGS # 1
    LIBFLAG_FCONTROL : LIBFLAGS # 2
    LIBFLAG_FHIDDEN : LIBFLAGS # 4
    LIBFLAG_FHASDISKIMAGE : LIBFLAGS # 8


class PARAMDESC:
    lpVarValue : int
    wParamFlags : PARAMFLAG


class PARAMFLAG(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    PARAMFLAG_NONE : PARAMFLAG # 0
    PARAMFLAG_FIN : PARAMFLAG # 1
    PARAMFLAG_FOUT : PARAMFLAG # 2
    PARAMFLAG_FLCID : PARAMFLAG # 4
    PARAMFLAG_FRETVAL : PARAMFLAG # 8
    PARAMFLAG_FOPT : PARAMFLAG # 16
    PARAMFLAG_FHASDEFAULT : PARAMFLAG # 32
    PARAMFLAG_FHASCUSTDATA : PARAMFLAG # 64


class STATSTG:
    atime : FILETIME
    cbSize : int
    clsid : Guid
    ctime : FILETIME
    grfLocksSupported : int
    grfMode : int
    grfStateBits : int
    mtime : FILETIME
    pwcsName : str
    reserved : int
    type : int


class SYSKIND(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    SYS_WIN16 : SYSKIND # 0
    SYS_WIN32 : SYSKIND # 1
    SYS_MAC : SYSKIND # 2
    SYS_WIN64 : SYSKIND # 3


class TYPEATTR:
    cbAlignment : int
    cbSizeInstance : int
    cbSizeVft : int
    cFuncs : int
    cImplTypes : int
    cVars : int
    dwReserved : int
    guid : Guid
    idldescType : IDLDESC
    lcid : int
    lpstrSchema : int
    MEMBER_ID_NIL : int
    memidConstructor : int
    memidDestructor : int
    tdescAlias : TYPEDESC
    typekind : TYPEKIND
    wMajorVerNum : int
    wMinorVerNum : int
    wTypeFlags : TYPEFLAGS


class TYPEDESC:
    lpValue : int
    vt : int


class TYPEFLAGS(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    TYPEFLAG_FAPPOBJECT : TYPEFLAGS # 1
    TYPEFLAG_FCANCREATE : TYPEFLAGS # 2
    TYPEFLAG_FLICENSED : TYPEFLAGS # 4
    TYPEFLAG_FPREDECLID : TYPEFLAGS # 8
    TYPEFLAG_FHIDDEN : TYPEFLAGS # 16
    TYPEFLAG_FCONTROL : TYPEFLAGS # 32
    TYPEFLAG_FDUAL : TYPEFLAGS # 64
    TYPEFLAG_FNONEXTENSIBLE : TYPEFLAGS # 128
    TYPEFLAG_FOLEAUTOMATION : TYPEFLAGS # 256
    TYPEFLAG_FRESTRICTED : TYPEFLAGS # 512
    TYPEFLAG_FAGGREGATABLE : TYPEFLAGS # 1024
    TYPEFLAG_FREPLACEABLE : TYPEFLAGS # 2048
    TYPEFLAG_FDISPATCHABLE : TYPEFLAGS # 4096
    TYPEFLAG_FREVERSEBIND : TYPEFLAGS # 8192
    TYPEFLAG_FPROXY : TYPEFLAGS # 16384


class TYPEKIND(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    TKIND_ENUM : TYPEKIND # 0
    TKIND_RECORD : TYPEKIND # 1
    TKIND_MODULE : TYPEKIND # 2
    TKIND_INTERFACE : TYPEKIND # 3
    TKIND_DISPATCH : TYPEKIND # 4
    TKIND_COCLASS : TYPEKIND # 5
    TKIND_ALIAS : TYPEKIND # 6
    TKIND_UNION : TYPEKIND # 7
    TKIND_MAX : TYPEKIND # 8


class TYPELIBATTR:
    guid : Guid
    lcid : int
    syskind : SYSKIND
    wLibFlags : LIBFLAGS
    wMajorVerNum : int
    wMinorVerNum : int


class VARDESC:

    class DESCUNION:
        lpvarValue : int
        oInst : int

    desc : VARDESC.DESCUNION
    elemdescVar : ELEMDESC
    lpstrSchema : str
    memid : int
    varkind : VARKIND
    wVarFlags : int


class VARFLAGS(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    VARFLAG_FREADONLY : VARFLAGS # 1
    VARFLAG_FSOURCE : VARFLAGS # 2
    VARFLAG_FBINDABLE : VARFLAGS # 4
    VARFLAG_FREQUESTEDIT : VARFLAGS # 8
    VARFLAG_FDISPLAYBIND : VARFLAGS # 16
    VARFLAG_FDEFAULTBIND : VARFLAGS # 32
    VARFLAG_FHIDDEN : VARFLAGS # 64
    VARFLAG_FRESTRICTED : VARFLAGS # 128
    VARFLAG_FDEFAULTCOLLELEM : VARFLAGS # 256
    VARFLAG_FUIDEFAULT : VARFLAGS # 512
    VARFLAG_FNONBROWSABLE : VARFLAGS # 1024
    VARFLAG_FREPLACEABLE : VARFLAGS # 2048
    VARFLAG_FIMMEDIATEBIND : VARFLAGS # 4096


class VARKIND(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    VAR_PERINSTANCE : VARKIND # 0
    VAR_STATIC : VARKIND # 1
    VAR_CONST : VARKIND # 2
    VAR_DISPATCH : VARKIND # 3
