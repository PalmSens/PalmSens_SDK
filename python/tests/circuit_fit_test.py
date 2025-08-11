from __future__ import annotations

from pathlib import Path

from pspython.pspyfiles import load_session_file

DATA_DIR = Path(__file__).parent / 'test_data'

EIS_DATA = DATA_DIR / 'eis_circuit_fit.pssession'


def test_circuit_fit():
    measurements = load_session_file(EIS_DATA)
    eis_data = measurements[0].eis_data[0]

    from pspython.models import CircuitModel

    model = CircuitModel(cdc='R(RC)')
    result = model.fit(eis_data)

    # test with guess, should converge faster
    result2 = model.fit(eis_data, guess=result.parameters)
