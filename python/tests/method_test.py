import pytest

from pspython.methods import techniques


@pytest.fixture
def method(data_cv_1scan):
    return data_cv_1scan[0].method


def test_properties(method):
    assert isinstance(repr(method), str)
    assert method.id == 'cv'
    assert method.name == 'Cyclic Voltammetry'
    assert method.short_name == 'CV'


def test_to_dict(method):
    dct = method.to_dict()
    assert dct


def test_to_parameters(method):
    params = method.to_parameters()
    assert isinstance(params, techniques.CyclicVoltammetryParameters)
