import os
import traceback

from PalmSens.Data import SessionManager  # type: ignore

# Import the static LoadSaveHelperFunctions
from PalmSens.Windows import LoadSaveHelperFunctions  # type: ignore

from . import pspymethods
from .data.convert import convert_to_measurement


def load_session_file(
    path,
):
    session = LoadSaveHelperFunctions.LoadSessionFile(path)
    measurements = []

    for m in session:
        measurements.append(
            convert_to_measurement(
                m,
            )
        )

    return measurements


def save_session_file(path, measurements):
    for measurement in measurements:
        if measurement is None:
            raise Exception('cannot save null measurement')
        if measurement.dotnet_measurement is None:
            raise Exception(
                'cannot save measurements that do not have a reference to the dotnet measurement object'
            )

    try:
        session = SessionManager()
        session.MethodForEditor = measurements[0].dotnet_measurement.Method

        for measurement in measurements:
            session.AddMeasurement(measurement.dotnet_measurement)

        LoadSaveHelperFunctions.SaveSessionFile(path, session)
        return
    except Exception:
        traceback.print_exc()
        return 0


def read_notes(path, n_chars=3000):
    with open(path, encoding='utf16') as myfile:
        contents = myfile.read()
    raw_txt = contents[1:n_chars].split('\\r\\n')
    notes_txt = [x for x in raw_txt if 'NOTES=' in x]
    notes_txt = (
        notes_txt[0].replace('%20', ' ').replace('NOTES=', '').replace('%crlf', os.linesep)
    )
    return notes_txt


def load_method_file(path):
    try:
        method = LoadSaveHelperFunctions.LoadMethod(path)
        return method
    except Exception:
        return 0


def save_method_file(path, method):
    try:
        LoadSaveHelperFunctions.SaveMethod(method, path)
        return 1
    except Exception:
        return 0


def get_method_estimated_duration(path):
    method = load_method_file(path)
    if method == 0:
        return 0
    else:
        return pspymethods.get_method_estimated_duration(method)
