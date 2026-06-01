from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from pydantic import TypeAdapter, ValidationError

import pypalmsens as ps
from pypalmsens._data.curve import CurveMetadata
from pypalmsens._data.eisdata import EISDataMetadata
from pypalmsens._data.measurement import MeasurementMetadata
from pypalmsens._instruments.callback import XYDataPoint
from pypalmsens.types import MethodTypeCompatible


def print_index(data):
    print('index', data.index)


def _test_stream(path: Path, method: MethodTypeCompatible):
    with ps.connect() as manager:
        measurement = manager.measure(
            method,
            stream=path,
        )

    assert measurement

    assert path.exists()
    lines = path.read_text(encoding='utf-8').splitlines()

    assert lines

    curves = defaultdict(list)
    curves_metadata = {}
    measurement_metadata = None

    for i, line in enumerate(lines):
        parsed: Any = TypeAdapter(
            MeasurementMetadata | CurveMetadata | XYDataPoint
        ).validate_json(line)

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

    return measurement


def test_measure_stream_cv(tmpdir):
    path = Path('cv.jsonl')

    method = ps.CyclicVoltammetry(
        n_scans=3,
        step_potential=0.01,
        scanrate=5,
    )

    _ = _test_stream(method=method, path=path)


def test_measure_stream_cp_with_aux():
    path = Path('cp.jsonl')

    method = ps.ChronoPotentiometry(
        run_time=3,
        record_auxiliary_input=True,
        record_we_current=True,
    )

    _ = _test_stream(method=method, path=path)


def test_measure_stream_eis():
    path = Path('eis.jsonl')

    method = ps.ElectrochemicalImpedanceSpectroscopy(
        n_frequencies=3,
        begin_potential=0.5,
        step_potential=0.1,
        end_potential=1.0,
        min_sampling_time=0.01,
        scan_type='potential',
    )

    with ps.connect() as manager:
        measurement = manager.measure(
            method,
            stream=path,
        )

    assert measurement

    assert path.exists()
    lines = path.read_text(encoding='utf-8').splitlines()

    assert lines

    eis_data_points = defaultdict(list)
    eis_data = {}
    measurement_metadata = None

    for i, line in enumerate(lines):
        try:
            parsed = TypeAdapter(MeasurementMetadata | EISDataMetadata).validate_json(line)
        except ValidationError:
            parsed = json.loads(line)

        if isinstance(parsed, dict):
            eis_data_points[parsed['id']].append(parsed)
        elif isinstance(parsed, EISDataMetadata):
            eis_data[parsed.id] = parsed
        elif isinstance(parsed, MeasurementMetadata):
            measurement_metadata = parsed
            # This is a quirk of EIS measurements
            # EISDataEvent is always after the first EISData.NewDataEvent
            assert i == 1
        else:
            raise ValueError(f'This should not happen: {parsed}')

    assert measurement_metadata

    assert len(eis_data_points) == len(eis_data) == len(measurement.eis_data)
    assert set(eis_data_points) == set(eis_data)

    for eis in measurement.eis_data:
        hash = eis._pseis.GetHashCode()

        metadata = eis_data[hash]
        assert metadata.title == eis.title
        assert metadata.n_frequencies == eis.n_frequencies
        assert metadata.frequency_type == eis.frequency_type
        assert metadata.scan_type == eis.scan_type

        points = eis_data_points[hash]

        assert len(points) == eis.n_points

        columns = list(metadata.units)

        arrays = {array.name: array for array in eis.arrays()}

        for col in columns:
            assert col in arrays

            ref_values = list(arrays[col])
            col_values = [point[col] for point in points]

            assert ref_values == col_values


def test_combine_callback_stream():
    raise AssertionError
