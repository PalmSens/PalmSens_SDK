import abc
import typing

import clr
from System import (
    Array_1,
    Exception,
    IDisposable,
    IEquatable_1,
    ReadOnlySpan_1,
    Span_1,
    SystemException,
)
from System.Collections import IDictionary
from System.IO import Stream
from System.Reflection import MethodBase
from System.Security import SecureString

class AsymmetricAlgorithm(IDisposable, abc.ABC):
    @property
    def KeyExchangeAlgorithm(self) -> str: ...
    @property
    def KeySize(self) -> int: ...
    @KeySize.setter
    def KeySize(self, value: int) -> int: ...
    @property
    def LegalKeySizes(self) -> Array_1[KeySizes]: ...
    @property
    def SignatureAlgorithm(self) -> str: ...
    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...
    def ExportPkcs8PrivateKey(self) -> Array_1[int]: ...
    def ExportPkcs8PrivateKeyPem(self) -> str: ...
    def ExportSubjectPublicKeyInfo(self) -> Array_1[int]: ...
    def ExportSubjectPublicKeyInfoPem(self) -> str: ...
    def FromXmlString(self, xmlString: str) -> None: ...
    def ImportFromPem(self, input: ReadOnlySpan_1[str]) -> None: ...
    def ImportPkcs8PrivateKey(
        self, source: ReadOnlySpan_1[int], bytesRead: clr.Reference[int]
    ) -> None: ...
    def ImportSubjectPublicKeyInfo(
        self, source: ReadOnlySpan_1[int], bytesRead: clr.Reference[int]
    ) -> None: ...
    def ToXmlString(self, includePrivateParameters: bool) -> str: ...
    def TryExportPkcs8PrivateKey(
        self, destination: Span_1[int], bytesWritten: clr.Reference[int]
    ) -> bool: ...
    def TryExportPkcs8PrivateKeyPem(
        self, destination: Span_1[str], charsWritten: clr.Reference[int]
    ) -> bool: ...
    def TryExportSubjectPublicKeyInfo(
        self, destination: Span_1[int], bytesWritten: clr.Reference[int]
    ) -> bool: ...
    def TryExportSubjectPublicKeyInfoPem(
        self, destination: Span_1[str], charsWritten: clr.Reference[int]
    ) -> bool: ...
    # Skipped Create due to it being static, abstract and generic.

    Create: Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __call__(self) -> AsymmetricAlgorithm: ...
        @typing.overload
        def __call__(self, algName: str) -> AsymmetricAlgorithm: ...

    # Skipped ExportEncryptedPkcs8PrivateKey due to it being static, abstract and generic.

    ExportEncryptedPkcs8PrivateKey: ExportEncryptedPkcs8PrivateKey_MethodGroup
    class ExportEncryptedPkcs8PrivateKey_MethodGroup:
        @typing.overload
        def __call__(
            self, passwordBytes: ReadOnlySpan_1[int], pbeParameters: PbeParameters
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self, password: ReadOnlySpan_1[str], pbeParameters: PbeParameters
        ) -> Array_1[int]: ...

    # Skipped ExportEncryptedPkcs8PrivateKeyPem due to it being static, abstract and generic.

    ExportEncryptedPkcs8PrivateKeyPem: ExportEncryptedPkcs8PrivateKeyPem_MethodGroup
    class ExportEncryptedPkcs8PrivateKeyPem_MethodGroup:
        @typing.overload
        def __call__(
            self, passwordBytes: ReadOnlySpan_1[int], pbeParameters: PbeParameters
        ) -> str: ...
        @typing.overload
        def __call__(
            self, password: ReadOnlySpan_1[str], pbeParameters: PbeParameters
        ) -> str: ...

    # Skipped ImportEncryptedPkcs8PrivateKey due to it being static, abstract and generic.

    ImportEncryptedPkcs8PrivateKey: ImportEncryptedPkcs8PrivateKey_MethodGroup
    class ImportEncryptedPkcs8PrivateKey_MethodGroup:
        @typing.overload
        def __call__(
            self,
            passwordBytes: ReadOnlySpan_1[int],
            source: ReadOnlySpan_1[int],
            bytesRead: clr.Reference[int],
        ) -> None: ...
        @typing.overload
        def __call__(
            self,
            password: ReadOnlySpan_1[str],
            source: ReadOnlySpan_1[int],
            bytesRead: clr.Reference[int],
        ) -> None: ...

    # Skipped ImportFromEncryptedPem due to it being static, abstract and generic.

    ImportFromEncryptedPem: ImportFromEncryptedPem_MethodGroup
    class ImportFromEncryptedPem_MethodGroup:
        @typing.overload
        def __call__(
            self, input: ReadOnlySpan_1[str], password: ReadOnlySpan_1[str]
        ) -> None: ...
        @typing.overload
        def __call__(
            self, input: ReadOnlySpan_1[str], passwordBytes: ReadOnlySpan_1[int]
        ) -> None: ...

    # Skipped TryExportEncryptedPkcs8PrivateKey due to it being static, abstract and generic.

    TryExportEncryptedPkcs8PrivateKey: TryExportEncryptedPkcs8PrivateKey_MethodGroup
    class TryExportEncryptedPkcs8PrivateKey_MethodGroup:
        @typing.overload
        def __call__(
            self,
            passwordBytes: ReadOnlySpan_1[int],
            pbeParameters: PbeParameters,
            destination: Span_1[int],
            bytesWritten: clr.Reference[int],
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            password: ReadOnlySpan_1[str],
            pbeParameters: PbeParameters,
            destination: Span_1[int],
            bytesWritten: clr.Reference[int],
        ) -> bool: ...

    # Skipped TryExportEncryptedPkcs8PrivateKeyPem due to it being static, abstract and generic.

    TryExportEncryptedPkcs8PrivateKeyPem: TryExportEncryptedPkcs8PrivateKeyPem_MethodGroup
    class TryExportEncryptedPkcs8PrivateKeyPem_MethodGroup:
        @typing.overload
        def __call__(
            self,
            passwordBytes: ReadOnlySpan_1[int],
            pbeParameters: PbeParameters,
            destination: Span_1[str],
            charsWritten: clr.Reference[int],
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            password: ReadOnlySpan_1[str],
            pbeParameters: PbeParameters,
            destination: Span_1[str],
            charsWritten: clr.Reference[int],
        ) -> bool: ...

class CryptographicException(SystemException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, format: str, insert: str) -> None: ...
    @typing.overload
    def __init__(self, hr: int) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
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

class CspParameters:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, dwTypeIn: int) -> None: ...
    @typing.overload
    def __init__(self, dwTypeIn: int, strProviderNameIn: str) -> None: ...
    @typing.overload
    def __init__(
        self, dwTypeIn: int, strProviderNameIn: str, strContainerNameIn: str
    ) -> None: ...
    KeyContainerName: str
    KeyNumber: int
    ProviderName: str
    ProviderType: int
    @property
    def Flags(self) -> CspProviderFlags: ...
    @Flags.setter
    def Flags(self, value: CspProviderFlags) -> CspProviderFlags: ...
    @property
    def KeyPassword(self) -> SecureString: ...
    @KeyPassword.setter
    def KeyPassword(self, value: SecureString) -> SecureString: ...
    @property
    def ParentWindowHandle(self) -> int: ...
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: int) -> int: ...

class CspProviderFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    NoFlags: CspProviderFlags  # 0
    UseMachineKeyStore: CspProviderFlags  # 1
    UseDefaultKeyContainer: CspProviderFlags  # 2
    UseNonExportableKey: CspProviderFlags  # 4
    UseExistingKey: CspProviderFlags  # 8
    UseArchivableKey: CspProviderFlags  # 16
    UseUserProtectedKey: CspProviderFlags  # 32
    NoPrompt: CspProviderFlags  # 64
    CreateEphemeralKey: CspProviderFlags  # 128

class DSA(AsymmetricAlgorithm):
    @property
    def KeyExchangeAlgorithm(self) -> str: ...
    @property
    def KeySize(self) -> int: ...
    @KeySize.setter
    def KeySize(self, value: int) -> int: ...
    @property
    def LegalKeySizes(self) -> Array_1[KeySizes]: ...
    @property
    def SignatureAlgorithm(self) -> str: ...
    @abc.abstractmethod
    def ExportParameters(self, includePrivateParameters: bool) -> DSAParameters: ...
    def FromXmlString(self, xmlString: str) -> None: ...
    def GetMaxSignatureSize(self, signatureFormat: DSASignatureFormat) -> int: ...
    def ImportFromPem(self, input: ReadOnlySpan_1[str]) -> None: ...
    @abc.abstractmethod
    def ImportParameters(self, parameters: DSAParameters) -> None: ...
    def ImportPkcs8PrivateKey(
        self, source: ReadOnlySpan_1[int], bytesRead: clr.Reference[int]
    ) -> None: ...
    def ImportSubjectPublicKeyInfo(
        self, source: ReadOnlySpan_1[int], bytesRead: clr.Reference[int]
    ) -> None: ...
    def ToXmlString(self, includePrivateParameters: bool) -> str: ...
    def TryExportPkcs8PrivateKey(
        self, destination: Span_1[int], bytesWritten: clr.Reference[int]
    ) -> bool: ...
    def TryExportSubjectPublicKeyInfo(
        self, destination: Span_1[int], bytesWritten: clr.Reference[int]
    ) -> bool: ...
    # Skipped Create due to it being static, abstract and generic.

    Create: Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __call__(self) -> DSA: ...
        @typing.overload
        def __call__(self, keySizeInBits: int) -> DSA: ...
        @typing.overload
        def __call__(self, algName: str) -> DSA: ...
        @typing.overload
        def __call__(self, parameters: DSAParameters) -> DSA: ...

    # Skipped CreateSignature due to it being static, abstract and generic.

    CreateSignature: CreateSignature_MethodGroup
    class CreateSignature_MethodGroup:
        @typing.overload
        def __call__(self, rgbHash: Array_1[int]) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self, rgbHash: Array_1[int], signatureFormat: DSASignatureFormat
        ) -> Array_1[int]: ...

    # Skipped ImportEncryptedPkcs8PrivateKey due to it being static, abstract and generic.

    ImportEncryptedPkcs8PrivateKey: ImportEncryptedPkcs8PrivateKey_MethodGroup
    class ImportEncryptedPkcs8PrivateKey_MethodGroup:
        @typing.overload
        def __call__(
            self,
            passwordBytes: ReadOnlySpan_1[int],
            source: ReadOnlySpan_1[int],
            bytesRead: clr.Reference[int],
        ) -> None: ...
        @typing.overload
        def __call__(
            self,
            password: ReadOnlySpan_1[str],
            source: ReadOnlySpan_1[int],
            bytesRead: clr.Reference[int],
        ) -> None: ...

    # Skipped ImportFromEncryptedPem due to it being static, abstract and generic.

    ImportFromEncryptedPem: ImportFromEncryptedPem_MethodGroup
    class ImportFromEncryptedPem_MethodGroup:
        @typing.overload
        def __call__(
            self, input: ReadOnlySpan_1[str], password: ReadOnlySpan_1[str]
        ) -> None: ...
        @typing.overload
        def __call__(
            self, input: ReadOnlySpan_1[str], passwordBytes: ReadOnlySpan_1[int]
        ) -> None: ...

    # Skipped SignData due to it being static, abstract and generic.

    SignData: SignData_MethodGroup
    class SignData_MethodGroup:
        @typing.overload
        def __call__(
            self, data: Array_1[int], hashAlgorithm: HashAlgorithmName
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self,
            data: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            signatureFormat: DSASignatureFormat,
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self,
            data: Stream,
            hashAlgorithm: HashAlgorithmName,
            signatureFormat: DSASignatureFormat,
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self, data: Array_1[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self,
            data: Array_1[int],
            offset: int,
            count: int,
            hashAlgorithm: HashAlgorithmName,
            signatureFormat: DSASignatureFormat,
        ) -> Array_1[int]: ...

    # Skipped TryCreateSignature due to it being static, abstract and generic.

    TryCreateSignature: TryCreateSignature_MethodGroup
    class TryCreateSignature_MethodGroup:
        @typing.overload
        def __call__(
            self,
            hash: ReadOnlySpan_1[int],
            destination: Span_1[int],
            bytesWritten: clr.Reference[int],
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            hash: ReadOnlySpan_1[int],
            destination: Span_1[int],
            signatureFormat: DSASignatureFormat,
            bytesWritten: clr.Reference[int],
        ) -> bool: ...

    # Skipped TryExportEncryptedPkcs8PrivateKey due to it being static, abstract and generic.

    TryExportEncryptedPkcs8PrivateKey: TryExportEncryptedPkcs8PrivateKey_MethodGroup
    class TryExportEncryptedPkcs8PrivateKey_MethodGroup:
        @typing.overload
        def __call__(
            self,
            passwordBytes: ReadOnlySpan_1[int],
            pbeParameters: PbeParameters,
            destination: Span_1[int],
            bytesWritten: clr.Reference[int],
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            password: ReadOnlySpan_1[str],
            pbeParameters: PbeParameters,
            destination: Span_1[int],
            bytesWritten: clr.Reference[int],
        ) -> bool: ...

    # Skipped TrySignData due to it being static, abstract and generic.

    TrySignData: TrySignData_MethodGroup
    class TrySignData_MethodGroup:
        @typing.overload
        def __call__(
            self,
            data: ReadOnlySpan_1[int],
            destination: Span_1[int],
            hashAlgorithm: HashAlgorithmName,
            bytesWritten: clr.Reference[int],
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: ReadOnlySpan_1[int],
            destination: Span_1[int],
            hashAlgorithm: HashAlgorithmName,
            signatureFormat: DSASignatureFormat,
            bytesWritten: clr.Reference[int],
        ) -> bool: ...

    # Skipped VerifyData due to it being static, abstract and generic.

    VerifyData: VerifyData_MethodGroup
    class VerifyData_MethodGroup:
        @typing.overload
        def __call__(
            self, data: Array_1[int], signature: Array_1[int], hashAlgorithm: HashAlgorithmName
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: ReadOnlySpan_1[int],
            signature: ReadOnlySpan_1[int],
            hashAlgorithm: HashAlgorithmName,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self, data: Stream, signature: Array_1[int], hashAlgorithm: HashAlgorithmName
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: Array_1[int],
            signature: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            signatureFormat: DSASignatureFormat,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: ReadOnlySpan_1[int],
            signature: ReadOnlySpan_1[int],
            hashAlgorithm: HashAlgorithmName,
            signatureFormat: DSASignatureFormat,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: Stream,
            signature: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            signatureFormat: DSASignatureFormat,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: Array_1[int],
            offset: int,
            count: int,
            signature: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: Array_1[int],
            offset: int,
            count: int,
            signature: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            signatureFormat: DSASignatureFormat,
        ) -> bool: ...

    # Skipped VerifySignature due to it being static, abstract and generic.

    VerifySignature: VerifySignature_MethodGroup
    class VerifySignature_MethodGroup:
        @typing.overload
        def __call__(self, rgbHash: Array_1[int], rgbSignature: Array_1[int]) -> bool: ...
        @typing.overload
        def __call__(
            self, hash: ReadOnlySpan_1[int], signature: ReadOnlySpan_1[int]
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            rgbHash: Array_1[int],
            rgbSignature: Array_1[int],
            signatureFormat: DSASignatureFormat,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            hash: ReadOnlySpan_1[int],
            signature: ReadOnlySpan_1[int],
            signatureFormat: DSASignatureFormat,
        ) -> bool: ...

class DSAParameters:
    Counter: int
    G: Array_1[int]
    J: Array_1[int]
    P: Array_1[int]
    Q: Array_1[int]
    Seed: Array_1[int]
    X: Array_1[int]
    Y: Array_1[int]

class DSASignatureFormat(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    IeeeP1363FixedFieldConcatenation: DSASignatureFormat  # 0
    Rfc3279DerSequence: DSASignatureFormat  # 1

class HashAlgorithmName(IEquatable_1[HashAlgorithmName]):
    def __init__(self, name: str) -> None: ...
    @classmethod
    @property
    def MD5(cls) -> HashAlgorithmName: ...
    @property
    def Name(self) -> str: ...
    @classmethod
    @property
    def SHA1(cls) -> HashAlgorithmName: ...
    @classmethod
    @property
    def SHA256(cls) -> HashAlgorithmName: ...
    @classmethod
    @property
    def SHA3_256(cls) -> HashAlgorithmName: ...
    @classmethod
    @property
    def SHA3_384(cls) -> HashAlgorithmName: ...
    @classmethod
    @property
    def SHA3_512(cls) -> HashAlgorithmName: ...
    @classmethod
    @property
    def SHA384(cls) -> HashAlgorithmName: ...
    @classmethod
    @property
    def SHA512(cls) -> HashAlgorithmName: ...
    @staticmethod
    def FromOid(oidValue: str) -> HashAlgorithmName: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: HashAlgorithmName, right: HashAlgorithmName) -> bool: ...
    def __ne__(self, left: HashAlgorithmName, right: HashAlgorithmName) -> bool: ...
    def ToString(self) -> str: ...
    @staticmethod
    def TryFromOid(oidValue: str, value: clr.Reference[HashAlgorithmName]) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: HashAlgorithmName) -> bool: ...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...

class KeySizes:
    def __init__(self, minSize: int, maxSize: int, skipSize: int) -> None: ...
    @property
    def MaxSize(self) -> int: ...
    @MaxSize.setter
    def MaxSize(self, value: int) -> int: ...
    @property
    def MinSize(self) -> int: ...
    @MinSize.setter
    def MinSize(self, value: int) -> int: ...
    @property
    def SkipSize(self) -> int: ...
    @SkipSize.setter
    def SkipSize(self, value: int) -> int: ...

class PbeEncryptionAlgorithm(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Unknown: PbeEncryptionAlgorithm  # 0
    Aes128Cbc: PbeEncryptionAlgorithm  # 1
    Aes192Cbc: PbeEncryptionAlgorithm  # 2
    Aes256Cbc: PbeEncryptionAlgorithm  # 3
    TripleDes3KeyPkcs12: PbeEncryptionAlgorithm  # 4

class PbeParameters:
    def __init__(
        self,
        encryptionAlgorithm: PbeEncryptionAlgorithm,
        hashAlgorithm: HashAlgorithmName,
        iterationCount: int,
    ) -> None: ...
    @property
    def EncryptionAlgorithm(self) -> PbeEncryptionAlgorithm: ...
    @property
    def HashAlgorithm(self) -> HashAlgorithmName: ...
    @property
    def IterationCount(self) -> int: ...

class RandomNumberGenerator(IDisposable, abc.ABC):
    def Dispose(self) -> None: ...
    @staticmethod
    def Fill(data: Span_1[int]) -> None: ...
    @staticmethod
    def GetString(choices: ReadOnlySpan_1[str], length: int) -> str: ...
    # Skipped Create due to it being static, abstract and generic.

    Create: Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __call__(self) -> RandomNumberGenerator: ...
        @typing.overload
        def __call__(self, rngName: str) -> RandomNumberGenerator: ...

    # Skipped GetBytes due to it being static, abstract and generic.

    GetBytes: GetBytes_MethodGroup
    class GetBytes_MethodGroup:
        @typing.overload
        def __call__(self, count: int) -> Array_1[int]: ...
        @typing.overload
        def __call__(self, data: Array_1[int]) -> None: ...
        @typing.overload
        def __call__(self, data: Span_1[int]) -> None: ...
        @typing.overload
        def __call__(self, data: Array_1[int], offset: int, count: int) -> None: ...

    # Skipped GetHexString due to it being static, abstract and generic.

    GetHexString: GetHexString_MethodGroup
    class GetHexString_MethodGroup:
        @typing.overload
        def __call__(self, stringLength: int, lowercase: bool = ...) -> str: ...
        @typing.overload
        def __call__(self, destination: Span_1[str], lowercase: bool = ...) -> None: ...

    # Skipped GetInt32 due to it being static, abstract and generic.

    GetInt32: GetInt32_MethodGroup
    class GetInt32_MethodGroup:
        @typing.overload
        def __call__(self, toExclusive: int) -> int: ...
        @typing.overload
        def __call__(self, fromInclusive: int, toExclusive: int) -> int: ...

    # Skipped GetItems due to it being static, abstract and generic.

    GetItems: GetItems_MethodGroup
    class GetItems_MethodGroup:
        def __getitem__(self, t: typing.Type[GetItems_1_T1]) -> GetItems_1[GetItems_1_T1]: ...

        GetItems_1_T1 = typing.TypeVar('GetItems_1_T1')
        class GetItems_1(typing.Generic[GetItems_1_T1]):
            GetItems_1_T = RandomNumberGenerator.GetItems_MethodGroup.GetItems_1_T1
            @typing.overload
            def __call__(
                self, choices: ReadOnlySpan_1[GetItems_1_T], length: int
            ) -> Array_1[GetItems_1_T]: ...
            @typing.overload
            def __call__(
                self, choices: ReadOnlySpan_1[GetItems_1_T], destination: Span_1[GetItems_1_T]
            ) -> None: ...

    # Skipped GetNonZeroBytes due to it being static, abstract and generic.

    GetNonZeroBytes: GetNonZeroBytes_MethodGroup
    class GetNonZeroBytes_MethodGroup:
        @typing.overload
        def __call__(self, data: Array_1[int]) -> None: ...
        @typing.overload
        def __call__(self, data: Span_1[int]) -> None: ...

    # Skipped Shuffle due to it being static, abstract and generic.

    Shuffle: Shuffle_MethodGroup
    class Shuffle_MethodGroup:
        def __getitem__(self, t: typing.Type[Shuffle_1_T1]) -> Shuffle_1[Shuffle_1_T1]: ...

        Shuffle_1_T1 = typing.TypeVar('Shuffle_1_T1')
        class Shuffle_1(typing.Generic[Shuffle_1_T1]):
            Shuffle_1_T = RandomNumberGenerator.Shuffle_MethodGroup.Shuffle_1_T1
            def __call__(self, values: Span_1[Shuffle_1_T]) -> None: ...

class RSA(AsymmetricAlgorithm):
    @property
    def KeyExchangeAlgorithm(self) -> str: ...
    @property
    def KeySize(self) -> int: ...
    @KeySize.setter
    def KeySize(self, value: int) -> int: ...
    @property
    def LegalKeySizes(self) -> Array_1[KeySizes]: ...
    @property
    def SignatureAlgorithm(self) -> str: ...
    def DecryptValue(self, rgb: Array_1[int]) -> Array_1[int]: ...
    def EncryptValue(self, rgb: Array_1[int]) -> Array_1[int]: ...
    @abc.abstractmethod
    def ExportParameters(self, includePrivateParameters: bool) -> RSAParameters: ...
    def ExportRSAPrivateKey(self) -> Array_1[int]: ...
    def ExportRSAPrivateKeyPem(self) -> str: ...
    def ExportRSAPublicKey(self) -> Array_1[int]: ...
    def ExportRSAPublicKeyPem(self) -> str: ...
    def FromXmlString(self, xmlString: str) -> None: ...
    def GetMaxOutputSize(self) -> int: ...
    def ImportFromPem(self, input: ReadOnlySpan_1[str]) -> None: ...
    @abc.abstractmethod
    def ImportParameters(self, parameters: RSAParameters) -> None: ...
    def ImportPkcs8PrivateKey(
        self, source: ReadOnlySpan_1[int], bytesRead: clr.Reference[int]
    ) -> None: ...
    def ImportRSAPrivateKey(
        self, source: ReadOnlySpan_1[int], bytesRead: clr.Reference[int]
    ) -> None: ...
    def ImportRSAPublicKey(
        self, source: ReadOnlySpan_1[int], bytesRead: clr.Reference[int]
    ) -> None: ...
    def ImportSubjectPublicKeyInfo(
        self, source: ReadOnlySpan_1[int], bytesRead: clr.Reference[int]
    ) -> None: ...
    def ToXmlString(self, includePrivateParameters: bool) -> str: ...
    def TryDecrypt(
        self,
        data: ReadOnlySpan_1[int],
        destination: Span_1[int],
        padding: RSAEncryptionPadding,
        bytesWritten: clr.Reference[int],
    ) -> bool: ...
    def TryEncrypt(
        self,
        data: ReadOnlySpan_1[int],
        destination: Span_1[int],
        padding: RSAEncryptionPadding,
        bytesWritten: clr.Reference[int],
    ) -> bool: ...
    def TryExportPkcs8PrivateKey(
        self, destination: Span_1[int], bytesWritten: clr.Reference[int]
    ) -> bool: ...
    def TryExportRSAPrivateKey(
        self, destination: Span_1[int], bytesWritten: clr.Reference[int]
    ) -> bool: ...
    def TryExportRSAPrivateKeyPem(
        self, destination: Span_1[str], charsWritten: clr.Reference[int]
    ) -> bool: ...
    def TryExportRSAPublicKey(
        self, destination: Span_1[int], bytesWritten: clr.Reference[int]
    ) -> bool: ...
    def TryExportRSAPublicKeyPem(
        self, destination: Span_1[str], charsWritten: clr.Reference[int]
    ) -> bool: ...
    def TryExportSubjectPublicKeyInfo(
        self, destination: Span_1[int], bytesWritten: clr.Reference[int]
    ) -> bool: ...
    def TrySignData(
        self,
        data: ReadOnlySpan_1[int],
        destination: Span_1[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
        bytesWritten: clr.Reference[int],
    ) -> bool: ...
    def TrySignHash(
        self,
        hash: ReadOnlySpan_1[int],
        destination: Span_1[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
        bytesWritten: clr.Reference[int],
    ) -> bool: ...
    # Skipped Create due to it being static, abstract and generic.

    Create: Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __call__(self) -> RSA: ...
        @typing.overload
        def __call__(self, keySizeInBits: int) -> RSA: ...
        @typing.overload
        def __call__(self, algName: str) -> RSA: ...
        @typing.overload
        def __call__(self, parameters: RSAParameters) -> RSA: ...

    # Skipped Decrypt due to it being static, abstract and generic.

    Decrypt: Decrypt_MethodGroup
    class Decrypt_MethodGroup:
        @typing.overload
        def __call__(
            self, data: Array_1[int], padding: RSAEncryptionPadding
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self, data: ReadOnlySpan_1[int], padding: RSAEncryptionPadding
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self,
            data: ReadOnlySpan_1[int],
            destination: Span_1[int],
            padding: RSAEncryptionPadding,
        ) -> int: ...

    # Skipped Encrypt due to it being static, abstract and generic.

    Encrypt: Encrypt_MethodGroup
    class Encrypt_MethodGroup:
        @typing.overload
        def __call__(
            self, data: Array_1[int], padding: RSAEncryptionPadding
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self, data: ReadOnlySpan_1[int], padding: RSAEncryptionPadding
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self,
            data: ReadOnlySpan_1[int],
            destination: Span_1[int],
            padding: RSAEncryptionPadding,
        ) -> int: ...

    # Skipped ImportEncryptedPkcs8PrivateKey due to it being static, abstract and generic.

    ImportEncryptedPkcs8PrivateKey: ImportEncryptedPkcs8PrivateKey_MethodGroup
    class ImportEncryptedPkcs8PrivateKey_MethodGroup:
        @typing.overload
        def __call__(
            self,
            passwordBytes: ReadOnlySpan_1[int],
            source: ReadOnlySpan_1[int],
            bytesRead: clr.Reference[int],
        ) -> None: ...
        @typing.overload
        def __call__(
            self,
            password: ReadOnlySpan_1[str],
            source: ReadOnlySpan_1[int],
            bytesRead: clr.Reference[int],
        ) -> None: ...

    # Skipped ImportFromEncryptedPem due to it being static, abstract and generic.

    ImportFromEncryptedPem: ImportFromEncryptedPem_MethodGroup
    class ImportFromEncryptedPem_MethodGroup:
        @typing.overload
        def __call__(
            self, input: ReadOnlySpan_1[str], password: ReadOnlySpan_1[str]
        ) -> None: ...
        @typing.overload
        def __call__(
            self, input: ReadOnlySpan_1[str], passwordBytes: ReadOnlySpan_1[int]
        ) -> None: ...

    # Skipped SignData due to it being static, abstract and generic.

    SignData: SignData_MethodGroup
    class SignData_MethodGroup:
        @typing.overload
        def __call__(
            self,
            data: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self,
            data: ReadOnlySpan_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self,
            data: ReadOnlySpan_1[int],
            destination: Span_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> int: ...
        @typing.overload
        def __call__(
            self,
            data: Array_1[int],
            offset: int,
            count: int,
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> Array_1[int]: ...

    # Skipped SignHash due to it being static, abstract and generic.

    SignHash: SignHash_MethodGroup
    class SignHash_MethodGroup:
        @typing.overload
        def __call__(
            self,
            hash: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self,
            hash: ReadOnlySpan_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> Array_1[int]: ...
        @typing.overload
        def __call__(
            self,
            hash: ReadOnlySpan_1[int],
            destination: Span_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> int: ...

    # Skipped TryExportEncryptedPkcs8PrivateKey due to it being static, abstract and generic.

    TryExportEncryptedPkcs8PrivateKey: TryExportEncryptedPkcs8PrivateKey_MethodGroup
    class TryExportEncryptedPkcs8PrivateKey_MethodGroup:
        @typing.overload
        def __call__(
            self,
            passwordBytes: ReadOnlySpan_1[int],
            pbeParameters: PbeParameters,
            destination: Span_1[int],
            bytesWritten: clr.Reference[int],
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            password: ReadOnlySpan_1[str],
            pbeParameters: PbeParameters,
            destination: Span_1[int],
            bytesWritten: clr.Reference[int],
        ) -> bool: ...

    # Skipped VerifyData due to it being static, abstract and generic.

    VerifyData: VerifyData_MethodGroup
    class VerifyData_MethodGroup:
        @typing.overload
        def __call__(
            self,
            data: Array_1[int],
            signature: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: ReadOnlySpan_1[int],
            signature: ReadOnlySpan_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: Stream,
            signature: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            data: Array_1[int],
            offset: int,
            count: int,
            signature: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> bool: ...

    # Skipped VerifyHash due to it being static, abstract and generic.

    VerifyHash: VerifyHash_MethodGroup
    class VerifyHash_MethodGroup:
        @typing.overload
        def __call__(
            self,
            hash: Array_1[int],
            signature: Array_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> bool: ...
        @typing.overload
        def __call__(
            self,
            hash: ReadOnlySpan_1[int],
            signature: ReadOnlySpan_1[int],
            hashAlgorithm: HashAlgorithmName,
            padding: RSASignaturePadding,
        ) -> bool: ...

class RSAEncryptionPadding(IEquatable_1[RSAEncryptionPadding]):
    @property
    def Mode(self) -> RSAEncryptionPaddingMode: ...
    @property
    def OaepHashAlgorithm(self) -> HashAlgorithmName: ...
    @classmethod
    @property
    def OaepSHA1(cls) -> RSAEncryptionPadding: ...
    @classmethod
    @property
    def OaepSHA256(cls) -> RSAEncryptionPadding: ...
    @classmethod
    @property
    def OaepSHA3_256(cls) -> RSAEncryptionPadding: ...
    @classmethod
    @property
    def OaepSHA3_384(cls) -> RSAEncryptionPadding: ...
    @classmethod
    @property
    def OaepSHA3_512(cls) -> RSAEncryptionPadding: ...
    @classmethod
    @property
    def OaepSHA384(cls) -> RSAEncryptionPadding: ...
    @classmethod
    @property
    def OaepSHA512(cls) -> RSAEncryptionPadding: ...
    @classmethod
    @property
    def Pkcs1(cls) -> RSAEncryptionPadding: ...
    @staticmethod
    def CreateOaep(hashAlgorithm: HashAlgorithmName) -> RSAEncryptionPadding: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> bool: ...
    def __ne__(self, left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: RSAEncryptionPadding) -> bool: ...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...

class RSAEncryptionPaddingMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Pkcs1: RSAEncryptionPaddingMode  # 0
    Oaep: RSAEncryptionPaddingMode  # 1

class RSAParameters:
    D: Array_1[int]
    DP: Array_1[int]
    DQ: Array_1[int]
    Exponent: Array_1[int]
    InverseQ: Array_1[int]
    Modulus: Array_1[int]
    P: Array_1[int]
    Q: Array_1[int]

class RSASignaturePadding(IEquatable_1[RSASignaturePadding]):
    @property
    def Mode(self) -> RSASignaturePaddingMode: ...
    @classmethod
    @property
    def Pkcs1(cls) -> RSASignaturePadding: ...
    @classmethod
    @property
    def Pss(cls) -> RSASignaturePadding: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: RSASignaturePadding, right: RSASignaturePadding) -> bool: ...
    def __ne__(self, left: RSASignaturePadding, right: RSASignaturePadding) -> bool: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals: Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: RSASignaturePadding) -> bool: ...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool: ...

class RSASignaturePaddingMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Pkcs1: RSASignaturePaddingMode  # 0
    Pss: RSASignaturePaddingMode  # 1
