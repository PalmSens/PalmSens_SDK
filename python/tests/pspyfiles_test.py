from __future__ import annotations

from dataclasses import asdict

from pytest import approx

from pspython.methods import techniques
from pspython.pspyfiles import load_method_file, save_method_file


def test_save_session():
    ...

    # session.MethodForEditor.MethodFilename = path.name


def test_save_load_method(tmpdir):
    path = tmpdir / 'test.psmethod'
    cv = techniques.CyclicVoltammetryParameters()
    save_method_file(path=path, method=cv)

    method_cv2 = load_method_file(path=path)

    assert method_cv2.filename == path

    cv2 = method_cv2.to_parameters()

    cv_dict = asdict(cv)
    cv2_dict = asdict(cv2)

    for k, v in cv_dict.items():
        assert k in cv2_dict
        v2 = cv2_dict[k]
        if isinstance(v, float):
            # work around for floating point rounding error on round-trip
            assert v2 == approx(v)
        else:
            assert v == v2
