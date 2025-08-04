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
__minimum_firmware_version__ = {
    'EmStat1': '3.7',
    'EmStat2': '7.7',
    'EmStat2BP': '7.7',
    'EmStat3': '7.7',
    'EmStat3BP': '7.7',
    'EmStat3P': '7.7',
    'EmStat4LR': '1.3',
    'EmStat4HR': '1.3',
    'EmStatPico': '1.5',
    'EmStatPicoSim': '1.5',
    'SensitWearable': '1.5',
    'PalmSens3': '2.8',
    'PalmSens4': '1.7',
}
