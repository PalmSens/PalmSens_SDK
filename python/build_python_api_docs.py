from __future__ import annotations

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
    show_bases=False,
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
    signature_crossrefs=True,
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
                'ACVoltammetry',
                'ChronoAmperometry',
                'ChronoCoulometry',
                'ChronoPotentiometry',
                'CyclicVoltammetry',
                'DifferentialPulseVoltammetry',
                'ElectrochemicalImpedanceSpectroscopy',
                'FastAmperometry',
                'FastCyclicVoltammetry',
                'FastGalvanostaticImpedanceSpectroscopy',
                'FastImpedanceSpectroscopy',
                'GalvanostaticImpedanceSpectroscopy',
                'LinearSweepPotentiometry',
                'LinearSweepVoltammetry',
                'MethodScript',
                'MultiplePulseAmperometry',
                'MultiStepAmperometry',
                'MultiStepPotentiometry',
                'NormalPulseVoltammetry',
                'OpenCircuitPotentiometry',
                'PulsedAmperometricDetection',
                'SquareWaveVoltammetry',
                'StrippingChronoPotentiometry',
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
                'discover',
                'InstrumentManager',
                'InstrumentPool',
            ]
        },
    ),
    Page(
        name='instrument_async',
        title='Instrument management (async)',
        module='pypalmsens',
        extra_config={
            'members': [
                'connect_async',
                'discover_async',
                'InstrumentManagerAsync',
                'InstrumentPoolAsync',
            ]
        },
    ),
    Page(
        name='settings',
        title='Settings',
        module='pypalmsens.settings',
        extra_config={
            'members': [
                'CurrentRange',
                'PotentialRange',
                'Pretreatment',
                'VersusOCP',
                'BiPot',
                'ELevel',
                'ILevel',
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
        name='settings_enums',
        title='Enums',
        module='pypalmsens.settings',
        extra_config={
            'members': [
                'CURRENT_RANGE',
                'POTENTIAL_RANGE',
            ]
        },
    ),
    Page(
        name='mixed_mode',
        title='Mixed Mode',
        module='pypalmsens.mixed_mode',
    ),
    Page(
        name='fitting',
        title='Fitting',
        module='pypalmsens.fitting',
    ),
    Page(
        name='data',
        title='Data',
        module='pypalmsens.data',
    ),
)

ROOT_DIR = Path(__file__).parent
WORKDIR = ROOT_DIR / 'docs' / 'api' / 'docs'


with tempfile.TemporaryDirectory() as temp_dir:
    for page in pages:
        with open(WORKDIR / f'{page.name}.md', 'w') as f:
            f.write(f'# {page.title}\n')

            try:
                members = page.extra_config['members']
            except KeyError:
                f.write(f'\n::: {page.module}')
            else:
                for member in members:
                    f.write(f'\n::: {page.module}.{member}')
