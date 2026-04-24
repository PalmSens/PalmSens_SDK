from __future__ import annotations

from typing import Annotated, Any

import PalmSens
from pydantic import BaseModel, BeforeValidator

from .._methods.types import AllowedCurrentRanges, AllowedMethods, AllowedPotentialRanges


class AnalogComponent(BaseModel):
    bits: int
    """Number of bits this device uses."""
    gain: float
    """Voltage gain of the device."""
    max_raw_value: float
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
    def _convert(cls, obj: PalmSens.Devices.AnalogComponent) -> AnalogComponent:
        """Convert dotnet object."""
        return cls(
            bits=obj.Bits,
            gain=obj.Gain,
            max_raw_value=obj.MaxRawValue,
            max_value=obj.MaxValue,
            min_value=obj.MinValue,
            offset=obj.Offset,
            resolution=obj.Resolution,
            step_size=obj.StepSize,
            v_range=obj.VRange,
        )

    @staticmethod
    def convert(value: Any) -> AnalogComponent:
        if isinstance(value, PalmSens.Devices.AnalogComponent):
            value = AnalogComponent._convert(value)
        return value


class Capabilities(BaseModel):
    acv_max_frequency: int
    """The maximum frequency for ACV."""

    adc_auxiliary: Annotated[AnalogComponent, BeforeValidator(AnalogComponent.convert)]
    """Gets an object with values to calculate the auxiliary voltage from the integer value received from the instrument."""

    adc_bipot: Annotated[AnalogComponent, BeforeValidator(AnalogComponent.convert)]
    """Gets an object with values to calculate the bipot current from the integer value received from the instrument."""

    adc_current: Annotated[AnalogComponent, BeforeValidator(AnalogComponent.convert)]
    """Gets an object with values to calculate the current from the integer value received from the instrument."""

    adc_potential: Annotated[AnalogComponent, BeforeValidator(AnalogComponent.convert)]
    """Gets an object with values to calculate the potential from the integer value received from the instrument."""

    connection: str
    """Connection type for this device."""

    dac_auxiliary: Annotated[AnalogComponent, BeforeValidator(AnalogComponent.convert)]
    """Gets an object with values to calculate the instrument integer value for setting the auxiliary output voltage."""

    dac_bipot: Annotated[AnalogComponent, BeforeValidator(AnalogComponent.convert)]
    """Gets an object with values to calculate the instrument integer value for setting the bipot potential."""

    dac_current: Annotated[AnalogComponent, BeforeValidator(AnalogComponent.convert)]
    """Gets an object with values to calculate the instrument integer value for setting the current."""

    dac_potential: Annotated[AnalogComponent, BeforeValidator(AnalogComponent.convert)]
    """Gets an object with values to calculate the potential from the integer value received from the instrument."""

    default_baud_rate: int
    """Gets the default baud rate."""

    device_type: str
    """The device type for this capabilities."""

    max_eis_amplitude_erms: float
    """Gets the maximum E RMS amplitude for EIS."""

    eis_max_frequency: float
    """Maximum frequency for EIS measurements in Hz."""

    eis_min_frequency: float
    """Minimum frequency for EIS measurements in Hz."""

    firmware_build_date: str
    """Build date of the firmware."""

    firmware_commit: str
    """Commit associated with the build of the firmware."""

    firmware_release_type: str
    """Get a string representation if the build is 'Release', 'Beta' or 'Debug'"""

    firmware_special_description: str
    """Special description for the firmware"""

    firmware_version: str
    """Firmware version of connected Device."""

    hardware_revision: int
    """Gets the hardware revision. 1 = ...."""

    max_v_aux: float
    """Maximum potential output of the AUX port."""

    geis_max_frequency: int
    """Gets the maximum GEIS frequency."""

    has_bipot: bool
    """True if bipot (WE2) capabilities are present"""

    is_galvanostat: bool
    """True if the potentiastat can act as a galvanostat."""

    is_hw_sync_master: bool
    """Gets or sets a value indicating whether this instance is designated as the hardware synchronization master in MultiTrace."""

    is_hw_sync_slave: bool
    """Gets or sets a value indicating whether this instance is slave channel in a multichannel device."""

    max_current: float
    """Maximum current (* current range) that can be read/applied"""

    max_n_points: float
    """Maximum amount of points within a measurement technique for this device."""

    max_potential: float
    """Maximum potential that can be read/applied"""

    max_potential_bipot: float
    """Maximum potential that can be read/applied with the bipot"""

    min_current: float
    """Minimum current (* current range) that can be read/applied"""

    min_potential: float
    """Minimum potential that can be read/applied"""

    min_potential_step: float
    """Minimum potential step that can be applied."""

    min_potential_bipot: float
    """Minimum potential that can be read/applied with the bipot"""

    model_name: str
    """Name of the device."""

    model_short_name: str
    """Short name of the device."""

    serial_number: str
    """Serial number of the device."""

    supported_applied_current_ranges: list[AllowedCurrentRanges]
    """list of current ranges supported for applying current by this particular deviceType."""

    supported_bipot_current_ranges: list[AllowedCurrentRanges]
    """list of current ranges for the BiPot module supported by this particular deviceType."""

    supported_current_ranges: list[AllowedCurrentRanges]
    """list of current ranges supported by this particular deviceType."""

    supported_potential_ranges: list[AllowedPotentialRanges]
    """list of potential ranges supported by this particular deviceType."""

    supported_techniques: list[AllowedMethods]
    """List supported techniques."""

    supports_impedance: bool
    """Whether or not the deviceType supports impedance measurements"""

    supports_ir_drop_compensation: bool
    """Whether the device supports IR Drop compensation"""

    @classmethod
    def from_comm(cls, comm: PalmSens.Comm.CommManager):
        cap = comm.Capabilities

        data = {
            'device_type': str(cap.DeviceType),
            'model_name': comm.DeviceSerial.TypeToModelName(),
            'model_short_name': comm.DeviceSerial.TypeToString(),
            'serial_number': comm.get_DeviceSerial(),
            'connection': cap.ConnDescription,
            'firmware_version': cap.FirmwareVersion,
            'firmware_release_type': cap.FirmwareReleaseType,
            'firmware_special_description': cap.SpecialFirmwareDescription,
            'firmware_build_date': cap.FirmwareTimeStamp,
            'firmware_commit': comm.ClientConnection.GetFWCommitHash(),
            'potential_range': [cap.MinPotential, cap.MaxPotential],  # V
            'max_current_read': cap.MaxCurrent,  # * CR
            'min_current': cap.MinCurrent,  # * CR
            'max_current': cap.MaxCurrent,  # * CR
            'min_potential': cap.MinPotential,  # V
            'max_potential': cap.MaxPotential,  # V
            'min_potential_step': cap.DACPotential.StepSize * 1000.0,  # mV
            'supported_current_ranges': [str(item) for item in cap.SupportedRanges],
            'supported_applied_current_ranges': [
                str(item) for item in cap.SupportedAppliedRanges
            ],
            'supported_techniques': [str(item) for item in cap.SupportedMethods],
            'supported_bipot_ranges': [str(item) for item in cap.SupportedBipotRanges],
            'supported_potential_ranges': [str(item) for item in cap.SupportedPotentialRanges],
        }

        data['is_galvanostat'] = cap.IsGalvanostat
        data['has_bipot'] = cap.BiPotPresent
        data['supports_ir_drop_compensation'] = cap.SupportsIRDropComp
        data['supports_impedance'] = cap.SupportsImpedance
        data['eis_max_frequency'] = cap.MaxEISFrequency  # Hz
        data['eis_min_frequency'] = cap.MinEISFrequency  # Hz
        data['geis_max_frequency'] = int(cap.MaxEISFrequency)  # Hz
        data['is_hw_sync_master'] = cap.IsHardwareSynchronizationMaster
        data['is_hw_sync_slave'] = cap.IsSlaveChannel
        data['adc_auxiliary'] = cap.ADCAuxiliary
        data['adc_bipot'] = cap.ADCBiPot
        data['adc_current'] = cap.ADCCurrent
        data['adc_potential'] = cap.ADCPotential
        data['dac_auxiliary'] = cap.DACAuxiliary
        data['dac_bipot'] = cap.DACBiPot
        data['dac_current'] = cap.DACCurrent
        data['dac_potential'] = cap.DACPotential

        return cls.model_validate(data)
