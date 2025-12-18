# /// script
# dependencies = [
#   "pythonnet",
# ]
# ///

from __future__ import annotations

import json
import sys
from pathlib import Path

import clr

clr.AddReference('System')
from System import Diagnostics

ROOT = Path(__file__).parent


def version(write_json=False):
    dirs = 'python/snstrc/', 'matlab', 'labview'

    directories = {}

    for dir in dirs:
        assert dir.exists()
        paths = list(Path(ROOT, dir).glob('**/PalmSens*.dll'))

        for path in paths:
            print(path)
            version = Diagnostics.FileVersionInfo.GetVersionInfo(str(path)).ProductVersion

            if path.parent not in directories:
                directories[path.parent] = {}

            directories[path.parent][path.name] = version

    for drc, data in directories.items():
        if write_json:
            with open(drc / 'version.json', 'w') as f:
                json.dump(data, f, indent=4)

        else:
            print(drc)
            for file, value in data.items():
                print(f'- {file}: {value}')
            print()


if __name__ == '__main__':
    write_json = 'json' in sys.argv

    version(write_json=write_json)
