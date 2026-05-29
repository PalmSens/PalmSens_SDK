from __future__ import annotations

from pathlib import Path

import pypalmsens as ps


def print_index(data):
    print('index', data.index)


eis_method = ps.ElectrochemicalImpedanceSpectroscopy(
    n_frequencies=100,
    min_sampling_time=0.01,
    scan_type='time',
)

cv_method = ps.ChronoAmperometry(
    run_time=3,
)

ca_method = ps.CyclicVoltammetry(
    n_scans=3,
    step_potential=0.01,
    scanrate=5,
)


def test_measure_stream():
    path = Path('cv.jsonl')

    with ps.connect() as manager:
        measurement = manager.measure(
            # eis_method,
            # cv_method,
            ca_method,
            stream=path,
            callback=print_index,
        )

    assert measurement

    assert path.exists()
    lines = path.read_text().splitlines()

    assert lines

    # for i, line in enumerate(lines):
    #     try:
    #         metadata = TypeAdapter(MeasurementMetadata | CurveMetadata).validate_json(line)
    #         print(metadata)
    #     except ValidationError:
    #         row = json.loads(line)
    #         print(row)


if __name__ == '__main__':
    test_measure_stream()
