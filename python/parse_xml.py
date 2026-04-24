from __future__ import annotations

import xml.etree.ElementTree as ET
from collections.abc import Sequence
from importlib.resources import files
from textwrap import indent
from typing import Any

path = files('pypalmsens._libpalmsens.linux-x64') / 'PalmSens.Core.xml'

tree = ET.parse(str(path))

root = tree.getroot()

assembly, members = root


def to_dict(tags: Sequence[str]) -> dict[str, dict[str, Any]]:

    d = {tag: {} for tag in tags}

    for member in members:
        name = member.attrib['name']
        for tag in tags:
            prefix = 'P:PalmSens.Devices'
            if name.startswith(f'{prefix}.{tag}'):
                key = name.replace(f'{prefix}.{tag}.', '')
                value = ' '.join(member[0].text.split())
                d[tag][key] = value

    return d


tags = (
    'DeviceCapabilities',
    'DefaultCapabilities',
    'EmstatCapabilities',
    'Emstat2Capabilities',
    'Emstat3TSCapabilities',
    'Emstat3Capabilities',
    'Emstat3PCapabilities',
    'Emstat3BPCapabilities',
    'MethodScriptDeviceCapabilities',
    'PalmSensCapabilities',
    'PalmSens3Capabilities',
    'PalmSens4Capabilities',
)

cap = to_dict(tags)

for key, value in cap.items():
    print(key, len(value))

class_name = 'DeviceCapabilities'
psclass = f'PalmSens.Devices.{class_name}'
members = cap[class_name]

fields = [f'{k}: Any\n"""{v}"""\n' for k, v in members.items()]

fields_str = '\n'.join(fields)

fields_str = indent(fields_str, '    ')

attrs = [f'{k} = obj.{k}' for k in members]

attrs_str = ',\n'.join(attrs)
attrs_str = indent(attrs_str, '        ')

def_convert = f"""
@classmethod
def _convert(cls, obj: {psclass}):
    return cls(
{attrs_str}
    )
"""

with open('capabilities.py', 'w') as f:
    _ = f.write(f"""
from dataclasses import dataclass

import pypalmsens as ps

import PalmSens

@dataclass
class {class_name}:
{fields_str}
{indent(def_convert, '    ')}
""")

print('## Diff')

root = set(cap[class_name])

for key, value in cap.items():
    print(f'{key} - {len(value)} items')
    s = set(value)
    diff = s - root
    print(f'missing {len(diff)}: {diff}')
    print()

breakpoint()
