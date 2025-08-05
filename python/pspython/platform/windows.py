from __future__ import annotations

import atexit
from pathlib import Path

import clr
from pythonnet import unload

ROOT_DIR = Path(__file__).parent

core_dll = ROOT_DIR / 'win-libs' / 'PalmSens.Core.dll'
ble_dll = ROOT_DIR / 'win-libs' / 'PalmSens.Core.Windows.BLE.dll'


def unblock(path: Path):
    """Unblock DLL: https://stackoverflow.com/q/20886450"""
    zone_id = path.with_name(path.name + ':Zone.Identifier')
    if zone_id.exists():
        zone_id.unlink()


unblock(core_dll)
unblock(ble_dll)

# This dll contains the classes in which the data is stored
clr.AddReference(str(core_dll))

# This dll is used to load your session file
clr.AddReference(str(ble_dll))

clr.AddReference('System')

from PalmSens.Windows import (  # type: ignore  # noqa: E402
    CoreDependencies,
    LoadSaveHelperFunctions,
)

CoreDependencies.Init()

version = LoadSaveHelperFunctions.GetExecutingAssemblyNameAndVersion()

atexit.register(unload)
