from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from pydantic import TypeAdapter

import pypalmsens as ps
from pypalmsens._data.curve import CurveMetadata
from pypalmsens._data.measurement import MeasurementMetadata
from pypalmsens._instruments.callback import XYDataPoint


def print_index(data):
    print('index', data.index)


eis_method = ps.ElectrochemicalImpedanceSpectroscopy(
    n_frequencies=100,
    min_sampling_time=0.01,
    scan_type='time',
)

ca_method = ps.ChronoAmperometry(
    run_time=3,
)

cv_method = ps.CyclicVoltammetry(
    n_scans=3,
    step_potential=0.01,
    scanrate=5,
)


def test_measure_stream_cv(tmpdir):
    # path = Path(tmpdir / 'cv.jsonl')
    path = Path('cv.jsonl')

    with ps.connect() as manager:
        measurement = manager.measure(
            cv_method,
            stream=path,
        )

    assert measurement

    assert path.exists()
    lines = path.read_text().splitlines()

    assert lines

    curves = defaultdict(list)
    curves_metadata = {}
    measurement_metadata = None

    for i, line in enumerate(lines):
        parsed = TypeAdapter(MeasurementMetadata | CurveMetadata | XYDataPoint).validate_json(
            line
        )

        if isinstance(parsed, XYDataPoint):
            curves[parsed.id].append(parsed)
        elif isinstance(parsed, CurveMetadata):
            curves_metadata[parsed.id] = parsed
        elif isinstance(parsed, MeasurementMetadata):
            measurement_metadata = parsed
            assert i == 0
        else:
            raise ValueError(f'This should not happen: {parsed}')

    assert measurement_metadata

    assert len(curves) == len(curves_metadata) == len(measurement.curves)
    assert set(curves) == set(curves_metadata)

    for curve in measurement.curves:
        hash = curve._pscurve.GetHashCode()

        metadata = curves_metadata[hash]
        assert metadata.title == curve.title
        assert metadata.units['x'] == curve.x_unit
        assert metadata.units['y'] == curve.y_unit

        x_data = [point.x for point in curves[hash]]
        y_data = [point.y for point in curves[hash]]

        assert x_data == list(curve.x_array)
        assert y_data == list(curve.y_array)


def test_measure_stream_ca():
    path = Path('ca.jsonl')

    with ps.connect() as manager:
        measurement = manager.measure(
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


def test_measure_stream_eis():
    path = Path('eis.jsonl')

    with ps.connect() as manager:
        measurement = manager.measure(
            eis_method,
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
