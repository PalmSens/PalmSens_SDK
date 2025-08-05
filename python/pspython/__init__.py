from __future__ import annotations

import atexit
import sys
from pathlib import Path

if sys.platform == 'win32':
    from .platform.windows import version
else:
    from .platform.mono import version


__version__ = '0.0.1'
__sdk_version__ = version
