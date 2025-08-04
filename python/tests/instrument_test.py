from __future__ import annotations

import warnings
from dataclasses import dataclass

import pytest

from pspython import __minimum_firmware_version__
from pspython.instruments.common import firmware_warning


@dataclass
class MockCapabilities:
    DeviceType: str
    FirmwareVersion: float | str


@pytest.mark.parametrize(
    'cap',
    (
        MockCapabilities(DeviceType='PalmSens4', FirmwareVersion=13.37),
        MockCapabilities(DeviceType='idontexist', FirmwareVersion=0.0),
        MockCapabilities(
            DeviceType='EmStat4HR',
            FirmwareVersion=__minimum_firmware_version__['EmStat4HR'],
        ),
    ),
)
def test_firmware_warning_ok(cap):
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        firmware_warning(cap)


def test_firmware_warning_fail():
    cap = MockCapabilities(DeviceType='PalmSens4', FirmwareVersion=0.123)

    with pytest.warns(UserWarning):
        firmware_warning(cap)
