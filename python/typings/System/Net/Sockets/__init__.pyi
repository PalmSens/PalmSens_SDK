import typing

from System import Exception
from System.Collections import IDictionary
from System.ComponentModel import Win32Exception
from System.Reflection import MethodBase

class SocketError(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Success: SocketError  # 0
    OperationAborted: SocketError  # 995
    IOPending: SocketError  # 997
    Interrupted: SocketError  # 10004
    AccessDenied: SocketError  # 10013
    Fault: SocketError  # 10014
    InvalidArgument: SocketError  # 10022
    TooManyOpenSockets: SocketError  # 10024
    WouldBlock: SocketError  # 10035
    InProgress: SocketError  # 10036
    AlreadyInProgress: SocketError  # 10037
    NotSocket: SocketError  # 10038
    DestinationAddressRequired: SocketError  # 10039
    MessageSize: SocketError  # 10040
    ProtocolType: SocketError  # 10041
    ProtocolOption: SocketError  # 10042
    ProtocolNotSupported: SocketError  # 10043
    SocketNotSupported: SocketError  # 10044
    OperationNotSupported: SocketError  # 10045
    ProtocolFamilyNotSupported: SocketError  # 10046
    AddressFamilyNotSupported: SocketError  # 10047
    AddressAlreadyInUse: SocketError  # 10048
    AddressNotAvailable: SocketError  # 10049
    NetworkDown: SocketError  # 10050
    NetworkUnreachable: SocketError  # 10051
    NetworkReset: SocketError  # 10052
    ConnectionAborted: SocketError  # 10053
    ConnectionReset: SocketError  # 10054
    NoBufferSpaceAvailable: SocketError  # 10055
    IsConnected: SocketError  # 10056
    NotConnected: SocketError  # 10057
    Shutdown: SocketError  # 10058
    TimedOut: SocketError  # 10060
    ConnectionRefused: SocketError  # 10061
    HostDown: SocketError  # 10064
    HostUnreachable: SocketError  # 10065
    ProcessLimit: SocketError  # 10067
    SystemNotReady: SocketError  # 10091
    VersionNotSupported: SocketError  # 10092
    NotInitialized: SocketError  # 10093
    Disconnecting: SocketError  # 10101
    TypeNotFound: SocketError  # 10109
    HostNotFound: SocketError  # 11001
    TryAgain: SocketError  # 11002
    NoRecovery: SocketError  # 11003
    NoData: SocketError  # 11004
    SocketError: SocketError  # -1

class SocketException(Win32Exception):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, errorCode: int) -> None: ...
    @typing.overload
    def __init__(self, errorCode: int, message: str) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def ErrorCode(self) -> int: ...
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
    def NativeErrorCode(self) -> int: ...
    @property
    def SocketErrorCode(self) -> SocketError: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
