from __future__ import annotations

import atexit
import sys
from pathlib import Path

import clr
from pythonnet import unload

ROOT_DIR = Path(__file__).parent

core_dll = ROOT_DIR / 'PalmSens.Core.dll'
ble_dll = ROOT_DIR / 'PalmSens.Core.Windows.BLE.dll'


def unblock(path: Path):
    """Unblock DLL: https://stackoverflow.com/q/20886450"""
    path.with_name(path.name + ':Zone.Identifier')
    if path.exists():
        path.unlink()


if sys.platform == 'win32':
    unblock(core_dll)
    unblock(ble_dll)


# This dll contains the classes in which the data is stored
clr.AddReference(str(core_dll))

# This dll is used to load your session file
clr.AddReference(str(ble_dll))

clr.AddReference('System')

from PalmSens.Windows import CoreDependencies  # type: ignore  # noqa: E402

CoreDependencies.Init()

atexit.register(unload)
