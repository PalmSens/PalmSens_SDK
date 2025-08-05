from __future__ import annotations

import atexit
from pathlib import Path

from pythonnet import load, unload

ROOT_DIR = Path(__file__).parent / 'mono-libs'

# runtime must be imported before clr is loaded
load('coreclr', runtime_config=str(ROOT_DIR / 'runtimeconfig.json'))

import clr

PLAT_DIR = ROOT_DIR / 'runtimes' / 'linux-x64' / 'native'

core_dll = ROOT_DIR / 'PalmSens.Core.dll'
core_linux_dll = ROOT_DIR / 'PalmSens.Core.Linux.dll'
ioports_dll = PLAT_DIR / 'System.IO.Ports.dll'

assert ioports_dll.exists()

# This dll contains the classes in which the data is stored
clr.AddReference(str(core_dll))
clr.AddReference(str(core_linux_dll))

# This dll is used to load your session file
clr.AddReference(str(ioports_dll))

clr.AddReference('System')

from PalmSens.Core.Linux import CoreDependencies

CoreDependencies.Init()

version = 'PalmSens.Core.Linux 5.12'

atexit.register(unload)
