from __future__ import annotations

import atexit
from pathlib import Path

import clr
from pythonnet import unload

script_dir = Path(__file__).parent

# This dll contains the classes in which the data is stored
clr.AddReference(str(script_dir / 'PalmSens.Core.dll'))

# This dll is used to load your session file
clr.AddReference(str(script_dir / 'PalmSens.Core.Windows.BLE.dll'))

clr.AddReference('System')

from PalmSens.Windows import (  # type: ignore  # noqa: E402
    CoreDependencies,
    LoadSaveHelperFunctions,
)

CoreDependencies.Init()

atexit.register(unload)

__version__ = '0.0.1'
__sdk_version__ = LoadSaveHelperFunctions.GetExecutingAssemblyNameAndVersion()
