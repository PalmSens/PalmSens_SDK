from __future__ import annotations

from typing import Any, Literal

import PalmSens
import System
from pydantic import BaseModel, PrivateAttr, computed_field

from .._helpers import single_to_double


from .._methods.types import (
    AllowedCurrentRanges,
    AllowedMethods,
    AllowedPotentialRanges,
    cr_enum_to_string,
    pr_enum_to_string,
)


class AnalogComponent(BaseModel):
    bits: int
    """Number of bits this device uses."""

    gain: float
    """Voltage gain of the device."""

    max_raw_value: int
    """Maximum raw value, based on the amount of bits."""

    max_value: float
    """Maximum analog value this device can handle."""

    min_value: float
    """Minimum analog value this device can handle."""

    offset: float
    """Voltage offset of the device."""

    resolution: float
    """Resolution of this analog device."""

    step_size: float
    """Analog step size for the input or output of this component."""

    v_range: float
    """Gets the reference voltage range of the device."""

    @classmethod
    def _init(cls, obj: PalmSens.Devices.AnalogComponent) -> AnalogComponent:
        """Convert dotnet object."""
        return cls(
            bits=obj.Bits,
            gain=obj.Gain,
            max_raw_value=int(obj.MaxRawValue),
            max_value=single_to_double(obj.MaxValue),
            min_value=single_to_double(obj.MinValue),
            offset=single_to_double(obj.Offset),
            resolution=single_to_double(obj.Resolution),
            step_size=single_to_double(obj.StepSize),
            v_range=single_to_double(obj.VRange),
        )


class Capabilities(BaseModel):
    """Dataclass for device capabilities and device info."""
    _comm: PalmSens.Comm.CommManager = PrivateAttr()

    model_config = {'arbitrary_types_allowed': True}

    @classmethod
    def _init(cls, comm: PalmSens.Comm.CommManager) -> Capabilities:
        """Work-around to initialize BaseModel."""
        model = cls()
        model._comm = comm
        return model

    @property
    def _cap(self) -> PalmSens.Comm.Capabilities:
        return self._comm.Capabilities

    @computed_field
    @property
    def acv_max_frequency(self) -> int:
        """The maximum frequency for ACV in Hz."""
        return int(self._cap.MaxFrequencyACV)

    @computed_field
    @property
    def adc_auxiliary(self) -> AnalogComponent:
        """Gets an object with values to calculate the auxiliary voltage from the integer value received from the instrument."""
        return AnalogComponent._init(self._cap.ADCAuxiliary)

    @computed_field
    @property
    def adc_bipot(self) -> AnalogComponent:
        """Gets an object with values to calculate the bipot current from the integer value received from the instrument."""
        return AnalogComponent._init(self._cap.ADCBiPot)

    @computed_field
    @property
    def adc_current(self) -> AnalogComponent:
        """Gets an object with values to calculate the current from the integer value received from the instrument."""
        return AnalogComponent._init(self._cap.ADCCurrent)

    @computed_field
    @property
    def adc_potential(self) -> AnalogComponent:
        """Gets an object with values to calculate the potential from the integer value received from the instrument."""
        return AnalogComponent._init(self._cap.ADCPotential)

    @computed_field
    @property
    def connection(self) -> str:
        """Connection type for this device."""
        return self._cap.ConnDescription

    @computed_field
    @property
    def dac_auxiliary(self) -> AnalogComponent:
        """Gets an object with values to calculate the instrument integer value for setting the auxiliary output voltage."""
        return AnalogComponent._init(self._cap.DACAuxiliary)

    @computed_field
    @property
    def dac_bipot(self) -> AnalogComponent:
        """Gets an object with values to calculate the instrument integer value for setting the bipot potential."""
        return AnalogComponent._init(self._cap.DACBiPot)

    @computed_field
    @property
    def dac_current(self) -> AnalogComponent:
        """Gets an object with values to calculate the instrument integer value for setting the current."""
        return AnalogComponent._init(self._cap.DACCurrent)

    @computed_field
    @property
    def dac_potential(self) -> AnalogComponent:
        """Gets an object with values to calculate the potential from the integer value received from the instrument."""
        return AnalogComponent._init(self._cap.DACPotential)

    @computed_field
    @property
    def default_baudrate(self) -> int:
        """Gets the default baud rate."""
        return self._cap.DefaultBaudRate

    @computed_field
    @property
    def device_type(self) -> str:
        """The device type for this capabilities."""
        return str(self._cap.DeviceType)

    @computed_field
    @property
    def max_eis_amplitude_erms(self) -> float:
        """Gets the maximum E RMS amplitude for EIS."""
        return single_to_double(self._cap.MaxEISAmplitudeERMS)

    @computed_field
    @property
    def eis_max_frequency(self) -> float:
        """Maximum frequency for EIS measurements in Hz."""
        return single_to_double(self._cap.MaxEISFrequency)

    @computed_field
    @property
    def eis_min_frequency(self) -> float:
        """Minimum frequency for EIS measurements in Hz."""
        return single_to_double(self._cap.MinEISFrequency)

    @computed_field
    @property
    def firmware_build_date(self) -> str:
        """Build date of the firmware."""
        return self._cap.FirmwareTimeStamp

    @computed_field
    @property
    def firmware_commit(self) -> str:
        """Commit associated with the build of the firmware."""
        return self._comm.ClientConnection.GetFWCommitHash()

    @computed_field
    @property
    def firmware_release_type(self) -> Literal['Release', 'Beta', 'Debug']:
        """Get a string representation if the build is 'Release', 'Beta' or 'Debug'"""
        return self._cap.FirmwareReleaseType

    @computed_field
    @property
    def firmware_special_description(self) -> str:
        """Special description for the firmware"""
        return self._cap.SpecialFirmwareDescription

    @computed_field
    @property
    def firmware_version(self) -> float:
        """Firmware version of connected device."""
        return single_to_double(self._cap.FirmwareVersion)

    @computed_field
    @property
    def hardware_revision(self) -> int:
        """Gets the hardware revision."""
        return self._cap.HardwareRevision

    @computed_field
    @property
    def max_v_aux(self) -> float:
        """Maximum potential output of the AUX port in V."""
        return single_to_double(self._cap.MaxVAux)

    @computed_field
    @property
    def geis_max_frequency(self) -> int:
        """Gets the maximum GEIS frequency in Hz."""
        return int(self._cap.MaxEISFrequency)

    @computed_field
    @property
    def has_bipot(self) -> bool:
        """True if bipot (WE2) capabilities are present"""
        return self._cap.BiPotPresent

    @computed_field
    @property
    def is_galvanostat(self) -> bool:
        """True if the potentiastat can act as a galvanostat."""
        return self._cap.IsGalvanostat

    @computed_field
    @property
    def is_hw_sync_master(self) -> bool:
        """Gets or sets a value indicating whether this instance is designated as the hardware synchronization master in MultiTrace."""
        return self._cap.IsHardwareSynchronizationMaster

    @computed_field
    @property
    def is_hw_sync_slave(self) -> bool:
        """Gets or sets a value indicating whether this instance is slave channel in a multichannel device."""
        return self._cap.IsSlaveChannel

    @computed_field
    @property
    def max_current(self) -> float:
        """Maximum current (* current range) that can be read/applied"""
        return single_to_double(self._cap.MaxCurrent)

    @computed_field
    @property
    def max_n_points(self) -> int:
        """Maximum amount of points within a measurement technique for this device."""
        return self._cap.MaxNPoints

    @computed_field
    @property
    def max_potential(self) -> float:
        """Maximum potential in V that can be read/applied."""
        return single_to_double(self._cap.MaxPotential)

    @computed_field
    @property
    def max_potential_bipot(self) -> float:
        """Maximum potential in V that can be read/applied with the bipot."""
        return single_to_double(self._cap.MaxPotentialBipot)

    @computed_field
    @property
    def min_current(self) -> float:
        """Minimum current (* current range) that can be read/applied."""
        return single_to_double(self._cap.MinCurrent)

    @computed_field
    @property
    def min_potential(self) -> float:
        """Minimum potential in V that can be read/applied"""
        return single_to_double(self._cap.MinPotential)

    @computed_field
    @property
    def min_potential_step(self) -> float:
        """Minimum potential step in mV that can be applied."""
        return self._cap.DACPotential.StepSize * 1000.0

    @computed_field
    @property
    def min_potential_bipot(self) -> float:
        """Minimum potential that can be read/applied with the bipot"""
        return single_to_double(self._cap.MinPotentialBipot)

    @computed_field
    @property
    def model_name(self) -> str:
        """Name of the device."""
        return self._comm.DeviceSerial.TypeToModelName()

    @computed_field
    @property
    def model_short_name(self) -> str:
        """Short name of the device."""
        return self._comm.DeviceSerial.TypeToString()

    @computed_field
    @property
    def serial_number(self) -> str:
        """Serial number of the device."""
        return str(self._comm.DeviceSerial)

    @computed_field
    @property
    def supported_applied_current_ranges(self) -> list[AllowedCurrentRanges]:
        """list of current ranges supported for applying current by this particular deviceType."""
        return [cr_enum_to_string(item) for item in self._cap.SupportedAppliedRanges]

    @computed_field
    @property
    def supported_bipot_current_ranges(self) -> list[AllowedCurrentRanges]:
        """list of current ranges for the BiPot module supported by this particular deviceType."""
        return [cr_enum_to_string(item) for item in self._cap.SupportedBipotRanges]

    @computed_field
    @property
    def supported_current_ranges(self) -> list[AllowedCurrentRanges]:
        """list of current ranges supported by this particular deviceType."""
        return [cr_enum_to_string(item) for item in self._cap.SupportedRanges]

    @computed_field
    @property
    def supported_potential_ranges(self) -> list[AllowedPotentialRanges]:
        """list of potential ranges supported by this particular deviceType."""
        return [pr_enum_to_string(item) for item in self._cap.SupportedPotentialRanges]

    @computed_field
    @property
    def supported_techniques(self) -> list[AllowedMethods]:
        """List supported techniques."""
        method_ids = []

        for number in self._cap.SupportedMethods:
            try:
                id = PalmSens.Method.FromTechniqueNumber(number).MethodID
            except Exception:
                pass
            else:
                method_ids.append(id)

        return method_ids

    @computed_field
    @property
    def supports_impedance(self) -> bool:
        """Whether or not the deviceType supports impedance measurements"""
        return self._cap.SupportsImpedance

    @computed_field
    @property
    def supports_ir_drop_compensation(self) -> bool:
        """Whether the device supports IR Drop compensation"""
        return self._cap.SupportsIRDropComp
