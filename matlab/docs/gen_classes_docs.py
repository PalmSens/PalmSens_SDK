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
    ROOT / 'EquivalentCircuitFit.m',
    ROOT / 'Measurement.m',
    ROOT / 'MultiChannelMeasurement.m',
    ROOT / 'MeasurementGUI.m',
)

out_file = ROOT / 'docs' / 'modules' / 'ROOT' / 'pages' / '_classes.adoc'
out = out_file.open('w', encoding='utf-8')

hide_props = {
    'EquivalentCircuitFit': (
        'Model',
        'FitOptions',
        'EISData',
        'CDC',
    ),
    'Measurement': (
        'listenerIdleData',
        'listenerCurveReceived',
        'listenerBeginMeasurement',
        'listenerEndMeasurement',
        'listenerData',
    ),
    'MeasurementGUI': (
        'listenerIdleData',
        'listenerCurveReceived',
        'listenerBeginMeasurement',
        'listenerEndMeasurement',
        'listenerData',
    ),
    'MultiChannelMeasurement': (
        'listenerIdleData',
        'listenerCurveReceived',
        'listenerBeginMeasurement',
        'listenerEndMeasurement',
        'listenerData',
    ),
}


for filename in filenames:
    parser = maxx.treesitter.FileParser(Path(filename))
    obj = parser.parse()

    class_doc = obj.docstring.parse('google')

    print(f'[#_{obj.name.lower()}]', file=out)
    print(f'## `{obj.name}`', file=out)

    properties = [
        member
        for member in obj.members.values()
        if not member.is_private
        and member.is_property
        and member.name not in hide_props[obj.name]
    ]

    methods = [
        member
        for member in obj.members.values()
        if not member.is_private and member.is_function
    ]

    for item in class_doc:
        if item.kind == 'text':
            print(f'{item.value}\n', file=out)
        else:
            raise ValueError(f'Unknown item in doc: {item.kind} - {item}')

    if properties:
        print('*Properties*\n', file=out)
        for prop in properties:
            docstring = prop.docstring.value.split('\n', maxsplit=1)[0]
            print(
                f'- *`{prop.name}`* – {docstring}',
                file=out,
            )
        print('', file=out)

    if methods:
        print('*Methods*\n', file=out)
        for method in methods:
            docstring = method.docstring.value.split('\n', maxsplit=1)[0]
            print(
                f'- *<<_{obj.name.lower()}-{method.name.lower()}>>* – {docstring}',
                file=out,
            )
        print('', file=out)

    for method in methods:
        method_doc = method.docstring.parse('google')

        arguments_s = ', '.join(arg.name for arg in method.arguments)
        returns_s = ', '.join(arg.name for arg in method.returns)
        returns_s = f'[{returns_s}] = ' if returns_s else ''

        print(f'[#_{obj.name.lower()}-{method.name.lower()}]', file=out)
        print(f'### `{method.name}`', file=out)
        print('\n[sidebar]', file=out)
        print(f'`function` *`{returns_s}{method.name}({arguments_s})`*\n', file=out)

        for item in method_doc:
            if item.kind == 'text':
                print(f'{item.value}\n', file=out)

            elif item.kind == 'parameters':
                print('*Input arguments*\n', file=out)
                for param in item.value:
                    print(
                        f'- *`{param.name}`* (`{param.annotation}`) – {param.description}',
                        file=out,
                    )
                print('', file=out)

            elif item.kind == 'returns':
                print('*Output arguments*\n', file=out)
                for param in item.value:
                    print(
                        f'- *`{param.name}`* (`{param.annotation}`) – {param.description}',
                        file=out,
                    )
                print('', file=out)

            else:
                raise ValueError(f'Unknown item in doc: {item.kind} - {item}')
