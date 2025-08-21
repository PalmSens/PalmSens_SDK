from __future__ import annotations

import subprocess as sp
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import griffe2md

# https://mkdocstrings.github.io/griffe2md/reference/api/#griffe2md.ConfigDict
config = griffe2md.ConfigDict(
    allow_inspection=True,
    annotations_path='brief',
    docstring_options={'ignore_init_summary': True},
    docstring_section_style='list',
    docstring_style='numpy',
    filters=['!^_'],
    group_by_category=True,  # Group the object's children by categories: attributes, classes, functions, and modules.
    heading_level=1,  # The initial heading level to use.
    inherited_members=True,
    line_length=96,
    load_external_modules=False,
    members=None,
    members_order='source',
    merge_init_into_class=True,
    preload_modules=None,
    separate_signature=True,
    show_bases=True,
    show_category_heading=False,  # When grouped by categories, show a heading for each category.
    show_docstring_attributes=False,
    show_docstring_classes=True,
    show_docstring_description=True,
    show_docstring_examples=True,
    show_docstring_functions=True,
    show_docstring_modules=True,
    show_docstring_other_parameters=True,
    show_docstring_parameters=True,
    show_docstring_raises=True,
    show_docstring_receives=True,
    show_docstring_returns=True,
    show_docstring_warns=True,
    show_docstring_yields=True,
    show_if_no_docstring=True,
    show_object_full_path=False,
    show_root_full_path=True,  # Show the full Python path for the root object heading.
    show_root_heading=True,
    show_root_members_full_path=False,  # Show the full Python path of the root members.
    show_signature=True,
    show_signature_annotations=False,
    show_submodules=True,
    signature_crossrefs=False,
    summary=True,
)


@dataclass
class Page:
    name: str
    title: str
    module: str
    extra_config: dict[str, Any] = field(default_factory=dict)


pages = (
    Page(
        name='io',
        title='Saving/loading',
        module='pypalmsens',
        extra_config={
            'members': [
                'load_method_file',
                'load_session_file',
                'save_method_file',
                'save_session_file',
            ]
        },
    ),
    Page(
        name='techniques',
        title='Techniques',
        module='pypalmsens',
        extra_config={
            'members': [
                'ChronoAmperometry',
                'ChronoPotentiometry',
                'CyclicVoltammetry',
                'DifferentialPulseVoltammetry',
                'ElectrochemicalImpedanceSpectroscopy',
                'GalvanostaticImpedanceSpectroscopy',
                'LinearSweepVoltammetry',
                'MethodScript',
                'MultiStepAmperometry',
                'OpenCircuitPotentiometry',
                'SquareWaveVoltammetry',
            ]
        },
    ),
    Page(
        name='instrument',
        title='Instrument management',
        module='pypalmsens',
        extra_config={
            'members': [
                'connect',
                'connect_async',
                'discover',
                'discover_async',
                'InstrumentManager',
                'InstrumentManagerAsync',
            ]
        },
    ),
    Page(
        name='config',
        title='Config',
        module='pypalmsens.config',
        extra_config={
            'members': [
                'BaseSettings',
                'CurrentRanges',
                'PotentialRanges',
                'Pretreatment',
                'VersusOCP',
                'BiPot',
                'ELevel',
                'PostMeasurement',
                'CurrentLimits',
                'PotentialLimits',
                'ChargeLimits',
                'IrDropCompensation',
                'EquilibrationTriggers',
                'MeasurementTriggers',
                'Multiplexer',
                'DataProcessing',
                'General',
            ]
        },
    ),
    Page(
        name='config_enums',
        title='Enums',
        module='pypalmsens.config',
        extra_config={
            'members': [
                'CURRENT_RANGE',
                'POTENTIAL_RANGE',
            ]
        },
    ),
    Page(name='fitting', title='Fitting', module='pypalmsens.models'),
    Page(name='data', title='Data', module='pypalmsens.data'),
)

WORKDIR = Path(__file__).parents[1] / 'docs' / 'modules' / 'python' / 'pages'


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n\n' + content)


for page in pages:
    page_config = config.copy()
    page_config.update(page.extra_config)

    tmp = tempfile.NamedTemporaryFile()
    outputmd = tmp.name

    griffe2md.write_package_docs(
        package=page.module,
        config=page_config,
        output=str(outputmd),
    )

    outputadoc = WORKDIR / f'{page.name}.adoc'

    print('Generating', outputadoc)

    sp.run(f'pandoc {outputmd} -o {outputadoc} -f markdown -t asciidoc'.split())

    # Manually insert document title for asciidoc,
    # because markdown has no concept of this
    # https://github.com/jgm/pandoc/issues/5615
    line_prepender(outputadoc, f'= {page.title}\n')
