from __future__ import annotations

import json
from pathlib import Path

from pydantic import TypeAdapter

import pypalmsens as ps
from pypalmsens._data.measurement import Metadata


def test_measure_stream():
    path = Path('cv.jsonl')

    with ps.connect() as manager:
        # measurement = manager.measure(ps.ChronoAmperometry(run_time=3), stream=path)
        measurement = manager.measure(ps.ElectrochemicalImpedanceSpectroscopy(), stream=path)

    assert path.exists()
    lines = path.read_text().splitlines()

    metadata = TypeAdapter(Metadata).validate_json(lines[1])

    assert metadata.method

    for line in lines[2:]:
        assert json.loads(line)


if __name__ == '__main__':
    test_measure_stream()
