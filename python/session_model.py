from __future__ import annotations

import time
from pathlib import Path
from typing import Any

from deepdiff import DeepDiff
from pydantic import AliasChoices, AliasGenerator, ConfigDict, TypeAdapter
from pydantic.dataclasses import dataclass
from pydantic.experimental.missing_sentinel import MISSING

import pypalmsens as ps

CONFIG = ConfigDict(
    extra='forbid',
    alias_generator=AliasGenerator(
        validation_alias=lambda field_name: AliasChoices(field_name, field_name.lower()),
        serialization_alias=lambda field_name: field_name.lower(),
    ),
)


@dataclass(config=CONFIG)
class SessionModel:
    CoreVersion: str
    MethodForMeasurement: str
    Measurements: list[MeasurementModel]
    Type: str


@dataclass(config=CONFIG)
class MeasurementModel:
    Title: str
    Type: str
    DataSet: DataSetModel
    Method: str
    Curves: list[CurveModel]
    EISDataList: list[EisDataModel]
    TimeStamp: int | MISSING = MISSING
    DeviceUsed: int | MISSING = MISSING
    DeviceSerial: str | MISSING = MISSING
    DeviceFW: str | MISSING = MISSING
    UTCTimeStamp: int | MISSING = MISSING
    Channel: int | MISSING = MISSING


@dataclass(config=CONFIG)
class DataSetModel:
    Type: str
    Values: list[ValueModel]
    Keys: list[Any] | MISSING | None = MISSING


@dataclass(config=CONFIG)
class ValueModel:
    Type: str
    Description: str
    DataValueType: str
    Unit: UnitModel
    DataValues: list[GenericValue | CurrentReading | VoltageReading]
    OcpValue: float | MISSING | None = MISSING
    ArrayType: int | MISSING = MISSING
    Index: int | MISSING = MISSING
    Hidden: bool | MISSING = MISSING
    IntervalTime: float | MISSING | None = MISSING


@dataclass(config=CONFIG)
class UnitModel:
    Type: str
    S: str | MISSING | None = None  # SyMISSING
    Q: str | MISSING | None = None  # QuanMISSING
    A: str | MISSING | None = None  # AbbreviaMISSING
    OUnit: dict[str, Any] | MISSING | None = MISSING
    MinCrange: float | MISSING | None = MISSING


@dataclass(config=CONFIG)
class GenericValue:
    # PalmSens.Data.GenericValues
    V: float = 0  # Value
    T: str | MISSING = MISSING  # Text


@dataclass(config=CONFIG)
class CurrentReading:
    # PalmSens.Data.VoltageReadings
    V: float = 0  # Value
    R: int | MISSING = MISSING  # CR (old)
    C: int | MISSING = MISSING  # CurrentRange.CRByte
    G: float | MISSING = MISSING  # CurrentRange.Gain
    S: int = 0  # ReadingStatus (enum)
    T: int | MISSING = MISSING  # TimingStatus (enum)


@dataclass(config=CONFIG)
class VoltageReading:
    # PalmSens.Data.VoltageReadings
    V: float = 0  # Value
    S: int = 0  # ReadingStatus (enum)
    R: int = 0  # PotentialRange
    T: int = 0  # TimingStatus (enum)


@dataclass(config=CONFIG)
class CurveModel:
    Appearance: dict[str, Any]
    Title: str
    Type: str
    XAxis: int
    YAxis: int
    XAxisDataArray: ArrayModel
    YAxisDataArray: ArrayModel
    CorrosionButlerVolmer: list[float] | MISSING = MISSING
    CorrosionTafel: list[float] | MISSING = MISSING
    PeakList: list[Any] | MISSING = MISSING
    MeasType: int | MISSING | None = MISSING
    Hash: list[int] | MISSING | None = MISSING


@dataclass(config=CONFIG)
class PeakModel: ...


@dataclass(config=CONFIG)
class ArrayModel:
    Type: str
    Description: str
    DataValueType: str
    Unit: UnitModel
    DataValues: list[GenericValue | CurrentReading | VoltageReading]
    Index: int | MISSING = MISSING
    ArrayType: int | MISSING = MISSING
    IntervalTime: float | MISSING | None = MISSING


@dataclass(config=CONFIG)
class EisDataModel:
    Title: str
    Type: str
    ScanType: int
    FreqType: int
    Appearance: dict[str, Any] | MISSING | None = MISSING
    CDC: str | MISSING | None = MISSING
    DataSet: DataSetModel | MISSING | None = MISSING
    FitValues: list[float] | None | MISSING = MISSING
    Hash: list[int] | MISSING | None = MISSING
    SubScans: list[SubScanModel] | MISSING | None = MISSING
    TitleFrequencySubScanCurves: Any | MISSING | None = MISSING
    AppearanceFrequencySubScanCurves: Any | MISSING | None = MISSING


@dataclass(config=CONFIG)
class SubScanModel:
    Title: str
    Type: str
    ScanType: int
    FreqType: int
    DataSet: DataSetModel
    Appearance: dict[str, Any] | MISSING | None = MISSING
    AppearanceFrequencySubScanCurves: Any | MISSING | None = MISSING
    CDC: str | MISSING | None = MISSING
    FitValues: list[float] | None | MISSING = MISSING
    Hash: list[int] | MISSING | None = MISSING
    TitleFrequencySubScanCurves: Any | MISSING | None = MISSING


DATA: dict[str, Any] = {}


def parse_json(filename: Path) -> SessionModel:
    with open(filename, encoding='utf-16') as f:
        data = f.read()
        data = data[:-1]  # skip last line BOM

    import json

    global DATA
    DATA = json.loads(data)

    return TypeAdapter(SessionModel).validate_json(data)


def dump_json(session: SessionModel, filename: Path):
    json = TypeAdapter(SessionModel).dump_json(session)

    with open(filename, 'wb') as f:
        f.write(json)


if __name__ == '__main__':
    testing = Path(r'.\tests\test_data')

    paths = testing.glob('**/*.pssession')

    dt_rel_lst = []

    for i, path in enumerate(paths):
        if path.stem.endswith('_py'):
            continue

        relative_path = path.relative_to(testing)
        try:
            t0 = time.time()
            sess = parse_json(path)
            dt = time.time() - t0
        except Exception as e:
            print(f'\033[0;31mFAIL\033[0m: {relative_path}, {str(e).splitlines()[0]}')
            breakpoint()
        else:
            dt_ref0 = time.time()
            ps.load_session_file(path)
            dt_ref = time.time() - dt_ref0
            dt_rel = dt / dt_ref
            dt_rel_lst.append(dt_rel)

            print(
                (
                    f'\033[0;32mpass\033[0m: {relative_path}'
                    f'\n      time: {dt:.3f} s, ref: {dt_ref:.3f}, vs. ref: {dt_rel:.2}x'
                )
            )

            if check_round_trip := True:
                dump_json(sess, path.with_name(f'{path.stem}_py{path.suffix}'))

                new = TypeAdapter(SessionModel).dump_python(
                    sess,
                    by_alias='measurements' in DATA,  # check if lower case
                )
                diff = DeepDiff(DATA, new)
                print(f'      diff: {len(diff)} items - {list(diff.keys())}')

                if 'dictionary_item_added' in diff:
                    breakpoint()

    print(f'Average: {sum(dt_rel_lst) / len(dt_rel_lst):.3f}')

    # dump_json(sess, Path('test_output.pssession'))

    # breakpoint()
