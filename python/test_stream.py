from __future__ import annotations

import json
from pathlib import Path

from pydantic import TypeAdapter, ValidationError

import pypalmsens as ps
from pypalmsens._data.curve import CurveMetadata
from pypalmsens._data.measurement import MeasurementMetadata


def print_index(data):
    print('index', data.index)


def test_measure_stream():
    path = Path('cv.jsonl')

    with ps.connect() as manager:
        measurement = manager.measure(
            # ps.ElectrochemicalImpedanceSpectroscopy(n_frequencies=100, min_sampling_time=0.01),
            # ps.ChronoAmperometry(run_time=3),
            ps.CyclicVoltammetry(n_scans=3, step_potential=0.01, scanrate=5),
            stream=path,
            callback=print_index,
        )

    assert path.exists()
    lines = path.read_text().splitlines()

    # for i, line in enumerate(lines):
    #     try:
    #         metadata = TypeAdapter(MeasurementMetadata | CurveMetadata).validate_json(line)
    #         print(metadata)
    #     except ValidationError:
    #         row = json.loads(line)
    #         print(row)


if __name__ == '__main__':
    test_measure_stream()
