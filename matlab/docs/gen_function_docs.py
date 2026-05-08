# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "maxx>=0.8.0",
# ]
# ///

from __future__ import annotations

from pathlib import Path

import maxx

ROOT = Path(__file__).parents[1]


filenames = (
    ROOT / 'GetConnectedDevices.m',
    ROOT / 'LoadMethod.m',
    ROOT / 'LoadPSSDK.m',
    ROOT / 'LoadSession.m',
    ROOT / 'MultiChannelMeasurementLoopHelper.m',
    ROOT / 'NewMethod.m',
    ROOT / 'OpenConnection.m',
    ROOT / 'SaveMethod.m',
)

out_file = ROOT / 'docs' / 'modules' / 'ROOT' / 'pages' / '_functions.adoc'
out = out_file.open('w', encoding='utf-8')


for filename in filenames:
    parser = maxx.treesitter.FileParser(Path(filename))
    obj = parser.parse()

    doc = obj.docstring.parse('google')

    arguments_s = ', '.join(arg.name for arg in obj.arguments)
    returns_s = ', '.join(arg.name for arg in obj.returns)
    returns_s = f'[{returns_s}] = ' if returns_s else ''

    print(f'[#_{obj.name.lower()}]', file=out)
    print(f'## `{obj.name}`', file=out)
    print('\n[sidebar]', file=out)
    print(f'`function` *`{returns_s}{obj.name}({arguments_s})`*\n', file=out)

    for item in doc:
        if item.kind == 'text':
            print(f'{item.value}\n', file=out)

        elif item.kind == 'parameters':
            print('[discrete]', file=out)
            print('### Input arguments\n', file=out)
            for param in item.value:
                print(
                    f'- *`{param.name}`* (`{param.annotation}`) – {param.description}', file=out
                )
            print('', file=out)

        elif item.kind == 'returns':
            print('[discrete]', file=out)
            print('### Output arguments\n', file=out)
            for param in item.value:
                print(
                    f'- *`{param.name}`* (`{param.annotation}`) – {param.description}', file=out
                )
            print('', file=out)

        else:
            raise ValueError(f'Unknown item in doc: {item.kind} - {item}')
