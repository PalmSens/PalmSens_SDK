import typing

class FormatterAssemblyStyle(typing.SupportsInt):
    @typing.overload
    def __init__(self, value: int) -> None: ...
    @typing.overload
    def __init__(self, value: int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...

    # Values:
    Simple: FormatterAssemblyStyle  # 0
    Full: FormatterAssemblyStyle  # 1
