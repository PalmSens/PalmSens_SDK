from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING, Union

from PalmSens.Data import SessionManager
from PalmSens.DataFiles import MethodFile, MethodFile2
from System.IO import StreamReader, StreamWriter
from System.Text import Encoding

from .data.measurement import Measurement

if TYPE_CHECKING:
    from .methods.method import Method


def load_session_file(
    path: Union[str, Path],
) -> list[Measurement]:
    """Load a session file (.pssession).

    Parameters
    ----------
    path : Path | str
        Path to session file

    Returns
    -------
    measurements : list[Measurement]
        Return list of measurements
    """
    path = Path(path)

    session = SessionManager()
    stream = StreamReader(str(path))

    session.Load(stream.BaseStream, str(path))

    stream.Close()

    session.MethodForEditor.MethodFilename = path.name

    return [Measurement(psmeasurement=m) for m in session]


def save_session_file(path: Union[str, Path], measurements: list[Measurement]):
    """Load a session file (.pssession).

    Parameters
    ----------
    path : Path | str
        Path to save the session file
    measurements : list[Measurement]
        List of measurements to save
    """
    if any((measurement is None) for measurement in measurements):
        raise ValueError('cannot save null measurement')

    session = SessionManager()
    session.MethodForEditor = measurements[0].psmeasurement.Method

    for measurement in measurements:
        session.AddMeasurement(measurement.psmeasurement)

    path = Path(path)

    session.MethodForEditor.MethodFilename = path.name

    stream = StreamWriter(str(path), False, Encoding.Unicode)

    session.Save(stream.BaseStream, str(path))

    stream.Close()


def load_method_file(path: Union[str, Path]):
    """Load a method file (.psmethod).

    Parameters
    ----------
    path : Path | str
        Path to method file

    Returns
    -------
    method : Method
        Return method instance
    """
    path = Path(path)

    stream = StreamReader(str(path))

    if path.suffix == MethodFile2.FileExtension:
        method = MethodFile2.FromStream(stream)
    else:
        method = MethodFile.FromStream(stream, str(path))

    stream.Close()

    method.MethodFilename = str(path.absolute())

    return method


def save_method_file(path: Union[str, Path], method: Method):
    """Load a method file (.psmethod).

    Parameters
    ----------
    path : Path | str
        Path to save the method file
    method : Method
        Method to save
    """
    path = Path(path)

    stream = StreamWriter(str(path), False, Encoding.Unicode)

    from pspython import __sdk_version__

    MethodFile2.Save(method, stream.BaseStream, str(path), True, __sdk_version__)

    stream.Close()


def read_notes(path: Union[str, Path], n_chars: int = 3000):
    with open(path, encoding='utf16') as myfile:
        contents = myfile.read()
    raw_txt = contents[1:n_chars].split('\\r\\n')
    notes_list = [x for x in raw_txt if 'NOTES=' in x]
    notes_txt = (
        notes_list[0].replace('%20', ' ').replace('NOTES=', '').replace('%crlf', os.linesep)
    )
    return notes_txt
