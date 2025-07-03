import pythonnet
import clr
import os
import sys

# Load DLLs
scriptDir = os.path.dirname(os.path.realpath(__file__))
# This dll contains the classes in which the data is stored
clr.AddReference(scriptDir + '/PalmSens.Core.dll')
# This dll is used to load your session file
clr.AddReference(scriptDir + '/PalmSens.Core.Windows.BLE.dll')
clr.AddReference("System")

from PalmSens.Windows import CoreDependencies

CoreDependencies.Init()

import importlib.util
spec_files = importlib.util.find_spec('pspython.pspyfiles')
files = importlib.util.module_from_spec(spec_files)
spec_files.loader.exec_module(files)
spec_instruments = importlib.util.find_spec('pspython.pspyinstruments')
instruments = importlib.util.module_from_spec(spec_instruments)
spec_instruments.loader.exec_module(instruments)
spec_methods = importlib.util.find_spec('pspython.pspymethods')
methods = importlib.util.module_from_spec(spec_methods)
spec_methods.loader.exec_module(methods)