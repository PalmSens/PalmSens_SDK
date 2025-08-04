from __future__ import annotations

import asyncio
import warnings
from dataclasses import dataclass
from typing import Any

from packaging.version import Version
from System import Action


def create_future(clr_task):
    loop = asyncio.get_running_loop()
    future = asyncio.Future()
    callback = Action(lambda: on_completion(future, loop, clr_task))

    clr_task.GetAwaiter().OnCompleted(callback)
    return future


def on_completion(future, loop, task):
    if task.IsFaulted:
        clr_error = task.Exception.GetBaseException()
        future.set_exception(clr_error)
    else:
        loop.call_soon_threadsafe(lambda: future.set_result(task.GetAwaiter().GetResult()))


def firmware_warning(capabilities, /) -> None:
    """Raise warning if firmware is not supported."""
    from pspython import __minimum_firmware_version__, __sdk_version__

    device_type = str(capabilities.DeviceType)
    firmware_version = str(capabilities.FirmwareVersion)
    min_version = __minimum_firmware_version__.get(device_type, None)

    if not min_version:
        return

    if not Version(firmware_version) >= Version(min_version):
        warnings.warn(
            (
                f'Device firmware: {firmware_version} on {device_type} '
                f' is not supported by SDK ({__sdk_version__}), '
                f'minimum required firmware version: {min_version}'
            ),
            UserWarning,
            stacklevel=2,
        )


@dataclass
class Instrument:
    name: str
    connection: str
    device: Any
