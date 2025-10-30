"""PalmSens MethodSCRIPT module

This module provides functionality to translate and interpret the output of a
MethodSCRIPT (the measurement data).

The most relevant functions are:
  - parse_mscript_data_package(line)
  - parse_result_lines(lines)
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


@dataclass
class VarType:
    id: str
    name: str
    unit: str


SI_PREFIX_FACTOR = {
    # supported SI prefixes:
    'a': 1e-18,  # atto
    'f': 1e-15,  # femto
    'p': 1e-12,  # pico
    'n': 1e-9,  # nano
    'u': 1e-6,  # micro
    'm': 1e-3,  # milli
    ' ': 1e0,
    'k': 1e3,  # kilo
    'M': 1e6,  # mega
    'G': 1e9,  # giga
    'T': 1e12,  # tera
    'P': 1e15,  # peta
    'E': 1e18,  # exa
    # special case:
    'i': 1e0,  # integer
}

MSCRIPT_VAR_TYPES_DICT = {
    'aa': VarType('aa', 'unknown', ''),
    'ab': VarType('ab', 'WE vs RE potential', 'V'),
    'ac': VarType('ac', 'CE vs GND potential', 'V'),
    'ad': VarType('ad', 'SE vs GND potential', 'V'),
    'ae': VarType('ae', 'RE vs GND potential', 'V'),
    'af': VarType('af', 'WE vs GND potential', 'V'),
    'ag': VarType('ag', 'WE vs CE potential', 'V'),
    'as': VarType('as', 'AIN0 potential', 'V'),
    'at': VarType('at', 'AIN1 potential', 'V'),
    'au': VarType('au', 'AIN2 potential', 'V'),
    'av': VarType('av', 'AIN3 potential', 'V'),
    'aw': VarType('aw', 'AIN4 potential', 'V'),
    'ax': VarType('ax', 'AIN5 potential', 'V'),
    'ay': VarType('ay', 'AIN6 potential', 'V'),
    'az': VarType('az', 'AIN7 potential', 'V'),
    'ba': VarType('ba', 'WE current', 'A'),
    'ca': VarType('ca', 'Phase', 'degrees'),
    'cb': VarType('cb', 'Impedance', '\u2126'),  # NB: '\u2126' = ohm symbol
    'cc': VarType('cc', 'Z_real', '\u2126'),
    'cd': VarType('cd', 'Z_imag', '\u2126'),
    'ce': VarType('ce', 'EIS E TDD', 'V'),
    'cf': VarType('cf', 'EIS I TDD', 'A'),
    'cg': VarType('cg', 'EIS sampling frequency', 'Hz'),
    'ch': VarType('ch', 'EIS E AC', 'Vrms'),
    'ci': VarType('ci', 'EIS E DC', 'V'),
    'cj': VarType('cj', 'EIS I AC', 'Arms'),
    'ck': VarType('ck', 'EIS I DC', 'A'),
    'da': VarType('da', 'Applied potential', 'V'),
    'db': VarType('db', 'Applied current', 'A'),
    'dc': VarType('dc', 'Applied frequency', 'Hz'),
    'dd': VarType('dd', 'Applied AC amplitude', 'Vrms'),
    'ea': VarType('ea', 'Channel', ''),
    'eb': VarType('eb', 'Time', 's'),
    'ec': VarType('ec', 'Pin mask', ''),
    'ed': VarType('ed', 'Temperature', '\u00b0 Celsius'),  # NB: '\u00B0' = degrees symbol
    'ee': VarType('ee', 'Count', ''),
    'ha': VarType('ha', 'Generic current 1', 'A'),
    'hb': VarType('hb', 'Generic current 2', 'A'),
    'hc': VarType('hc', 'Generic current 3', 'A'),
    'hd': VarType('hd', 'Generic current 4', 'A'),
    'ia': VarType('ia', 'Generic potential 1', 'V'),
    'ib': VarType('ib', 'Generic potential 2', 'V'),
    'ic': VarType('ic', 'Generic potential 3', 'V'),
    'id': VarType('id', 'Generic potential 4', 'V'),
    'ja': VarType('ja', 'Misc. generic 1', ''),
    'jb': VarType('jb', 'Misc. generic 2', ''),
    'jc': VarType('jc', 'Misc. generic 3', ''),
    'jd': VarType('jd', 'Misc. generic 4', ''),
}

METADATA_STATUS_FLAGS = [
    (0x1, 'TIMING_ERROR'),
    (0x2, 'OVERLOAD'),
    (0x4, 'UNDERLOAD'),
    (0x8, 'OVERLOAD_WARNING'),
]

MSCRIPT_CURRENT_RANGES_EMSTAT_PICO = {
    0: '100 nA',
    1: '2 uA',
    2: '4 uA',
    3: '8 uA',
    4: '16 uA',
    5: '32 uA',
    6: '63 uA',
    7: '125 uA',
    8: '250 uA',
    9: '500 uA',
    10: '1 mA',
    11: '5 mA',
    128: '100 nA (High speed)',
    129: '1 uA (High speed)',
    130: '6 uA (High speed)',
    131: '13 uA (High speed)',
    132: '25 uA (High speed)',
    133: '50 uA (High speed)',
    134: '100 uA (High speed)',
    135: '200 uA (High speed)',
    136: '1 mA (High speed)',
    137: '5 mA (High speed)',
}

MSCRIPT_CURRENT_RANGES_EMSTAT4 = {
    # EmStat4 LR only:
    3: '1 nA',
    6: '10 nA',
    # EmStat4 LR/HR:
    9: '100 nA',
    12: '1 uA',
    15: '10 uA',
    18: '100 uA',
    21: '1 mA',
    24: '10 mA',
    # EmStat4 HR only:
    27: '100 mA',
}

MSCRIPT_POTENTIAL_RANGES_EMSTAT4 = {
    2: '50 mV',
    3: '100 mV',
    4: '200 mV',
    5: '500 mV',
    6: '1 V',
}


def metadata_status_to_text(status: int) -> str:
    """Format metadata status."""
    descriptions = [description for mask, description in METADATA_STATUS_FLAGS if status & mask]
    return ' | '.join(descriptions) if descriptions else 'OK'


def metadata_current_range_to_text(device_type: str, var_type: VarType, cr: int) -> str:
    """Format metadata current range."""
    cr_text = None
    if device_type == 'EmStat Pico':
        cr_text = MSCRIPT_CURRENT_RANGES_EMSTAT_PICO.get(cr)
    elif 'EmStat4' in device_type:
        # For EmStat4 series instruments, the range can be a current range or
        # potential range, depending on the variable type.
        if var_type.id in ['ab', 'cd']:
            cr_text = MSCRIPT_POTENTIAL_RANGES_EMSTAT4.get(cr)
        else:
            cr_text = MSCRIPT_CURRENT_RANGES_EMSTAT4.get(cr)
    return cr_text or 'UNKNOWN CURRENT RANGE'


@dataclass
class MScriptVar:
    """Class to store and parse a received MethodSCRIPT variable."""

    data: str
    """Data package."""

    raw_value: float
    """Raw data value."""

    si_prefix: str
    """SI prefix for value."""

    metadata: dict[str, int]
    """Metadata associated with value."""

    @classmethod
    def from_package(cls, data: str):
        """Return dataclass from data package."""
        if len(data) < 10:
            raise ValueError(f'Data package has less than 10 characters: {data}')

        data = data[:]

        if data[2:10] == '     nan':
            raw_value = math.nan
            si_prefix = ' '
        else:
            raw_value = cls.decode_value(data[2:9])
            si_prefix = data[9]

        tokens = data.split(',')[1:]
        metadata = cls.parse_metadata(tokens)

        return cls(data=data, raw_value=raw_value, si_prefix=si_prefix, metadata=metadata)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.data!r})'

    def __str__(self):
        return self.value_string

    @property
    def id(self) -> str:
        """Variable ID."""
        return self.data[0:2]

    @property
    def type(self) -> VarType:
        """Variable type."""
        return MSCRIPT_VAR_TYPES_DICT.get(self.id, VarType(self.id, 'unknown', ''))

    @property
    def si_prefix_factor(self) -> float:
        """Prefix for variable."""
        return SI_PREFIX_FACTOR[self.si_prefix]

    @property
    def value(self) -> float:
        """Value for variable."""
        return self.raw_value * self.si_prefix_factor

    @property
    def value_string(self) -> str:
        """Formatted variable."""
        if not self.type.unit:
            return f'{self.value:.9g}'

        if self.si_prefix_factor != 1:
            return f'{self.raw_value} {self.si_prefix}{self.type.unit}'

        if math.isnan(self.value):
            return f'NaN {self.type.unit}'

        return f'{self.raw_value} {self.type.unit}'

    def status_string(self) -> str:
        """Formatted status variable."""
        return metadata_status_to_text(self.metadata['status'])

    def current_range_string(self, device_type: str) -> str:
        """Formatted current range variable for given device type."""
        return metadata_current_range_to_text(
            device_type=device_type, var_type=self.type, cr=self.metadata['cr']
        )

    @staticmethod
    def decode_value(var: str) -> int:
        """Decode the raw value of a MethodSCRIPT variable in a data package.

        The input is a 7-digit hexadecimal string (without the variable type
        and/or SI prefix). The output is the converted (signed) integer value.
        """
        assert len(var) == 7
        return int(var, 16) - (2**27)

    @staticmethod
    def parse_metadata(tokens: list[str]) -> dict[str, int]:
        """Parse the (optional) metadata."""
        metadata = {}
        for token in tokens:
            if (len(token) == 2) and (token[0] == '1'):
                value = int(token[1], 16)
                metadata['status'] = value
            if (len(token) == 3) and (token[0] == '2'):
                value = int(token[1:], 16)
                metadata['cr'] = value
        return metadata


def parse_mscript_data_package(line: str) -> None | list[MScriptVar]:
    """Parse a MethodSCRIPT data package.

    The format of a MethodSCRIPT data package is described in the
    MethodSCRIPT documentation. It starts with a 'P' and ends with a
    '\n' character. A package consists of an arbitrary number of
    variables. Each variable consists of a type (describing the
    variable), a value, and optionally one or more metadata values.

    This method returns a list of variables (of type `MScriptVar`)
    found in the line, if the line could successfully be decoded.
    If the line was not a MethodSCRIPT data package, `None` is
    returned.
    """
    if line.startswith('P') and line.endswith('\n'):
        return [MScriptVar.from_package(var) for var in line[1:-1].split(';')]
    return None


def parse_result_lines(lines: list[str]) -> list[list[list[MScriptVar]]]:
    """Parse the result of a MethodSCRIPT and return a list of curves.

    This method returns a list of curves, where each curve is a list of
    measurement data (packages) seperated by an end-of-curve terminator
    such as '*', '+' or '-'. Each data package is a list of variables of
    type MScriptVar.

    So, the return type is a list of list of list of MScriptVars, and
    each variable can be accessed as `result[curve][row][col]`. For
    example, `result[1][2][3]` is the 4th variable of the 3th data point
    of the 2nd measurement loop.
    """
    curves: list[list[list[MScriptVar]]] = []
    current_curve: list[list[MScriptVar]] = []
    for line in lines:
        # NOTE:
        # '+' = end of loop
        # '*' = end of measurement loop
        # '-' = end of scan, within measurement loop, in case nscans(>1)
        if line and line[0] in '+*-':
            # End of scan or (measurement) loop detected.
            # Store curve if not empty.
            if current_curve:
                curves.append(current_curve)
                current_curve = []
        else:
            # No end of scan. Try to parse as data package.
            package = parse_mscript_data_package(line)
            if package:
                # Line was a valid package.
                # Append the package to the current curve.
                current_curve.append(package)
    return curves


def get_values_by_column(
    curves: list[list[list[MScriptVar]]], column: int, icurve: None | int = None
) -> np.ndarray:
    """Get all values from the specified column.

    Parameters
    ----------
    curves : Matrix of MScriptVar
        List of list of list of variables of type `MScriptVar`, as
        returned by `parse_result_lines()`.
    column : int
        Specifies which variable to return (i.e., the index within each
        data package).
    icurve : int, optional
        Specifies the index of the curve to use. If `None` (the default
        value), the data from all curves are used and concatenated into one list.

    Returns
    -------
    np.ndarray
        Return a numpy array containing (only) the values of each
        variable in the specified column, so they can easily be used for further
        processing and/or plotting.
    """
    if icurve is None:
        values: list[float] = []
        for curve in curves:
            values.extend(row[column].value for row in curve)
    else:
        values = [row[column].value for row in curves[icurve]]
    return np.asarray(values)
