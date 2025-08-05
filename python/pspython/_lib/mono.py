from __future__ import annotations

import atexit
from pathlib import Path

from pythonnet import load, unload

PSSDK_DIR = Path(__file__).parents[1] / '_pssdk' / 'mono'

# runtime must be imported before clr is loaded
load('coreclr', runtime_config=str(PSSDK_DIR / 'runtimeconfig.json'))

import clr  # noqa: E402

plat = 'linux-x64'  # todo: add osx/arm support
RUNTIME_DIR = Path(__file__).parents[1] / '_runtimes' / plat / 'native'

core_dll = PSSDK_DIR / 'PalmSens.Core.dll'
core_linux_dll = PSSDK_DIR / 'PalmSens.Core.Linux.dll'
ioports_dll = RUNTIME_DIR / 'System.IO.Ports.dll'

assert ioports_dll.exists()

# This dll contains the classes in which the data is stored
clr.AddReference(str(core_dll))
clr.AddReference(str(core_linux_dll))

# This dll is used to load your session file
clr.AddReference(str(ioports_dll))

clr.AddReference('System')

from PalmSens.Core.Linux import CoreDependencies  # noqa: E402

CoreDependencies.Init()

version = 'PalmSens.Core.Linux 5.12'

atexit.register(unload)
