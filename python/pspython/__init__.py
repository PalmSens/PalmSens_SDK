from pathlib import Path

import clr

script_dir = Path(__file__).parent

# This dll contains the classes in which the data is stored
clr.AddReference(script_dir / 'PalmSens.Core.dll')

# This dll is used to load your session file
clr.AddReference(script_dir / 'PalmSens.Core.Windows.BLE.dll')

clr.AddReference('System')

from PalmSens.Windows import CoreDependencies  # type: ignore  # noqa: E402

CoreDependencies.Init()
