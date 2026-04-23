from __future__ import annotations

from dataclasses import dataclass

import PalmSens

import pypalmsens as ps

man = ps.connect()

comm = man._comm
cap = man._comm.Capabilities

"""
get_ADCAuxiliary PalmSens.Devices.AnalogComponent
get_ADCBiPot PalmSens.Devices.AnalogComponent
get_ADCCurrent PalmSens.Devices.AnalogComponent
get_ADCPotential PalmSens.Devices.AnalogComponent
get_ActiveSignalTrainConfiguration HighSpeed
get_BiPotPresent False
get_CellTypes System.String[]
get_ChannelAUX 0
get_ChannelCE 0
get_ChannelCurrent 0
get_ChannelPotential 0
get_ChannelWE2 0
get_ConnDescription USB
get_DACAuxiliary PalmSens.Devices.AnalogComponent
get_DACBiPot PalmSens.Devices.AnalogComponent
get_DACCurrent PalmSens.Devices.AnalogComponent
get_DACPotential PalmSens.Devices.AnalogComponent
get_DefaultBaudRate 230400
get_DefaultSignalTrainConfiguration HighSpeed
get_DeviceType EmStat4LR
get_EnableBipot True
get_EnhancedFSCapabilities False
get_FirmwareIsDebug False
get_FirmwareReleaseType Release
get_FirmwareVersion 1.5
get_HardwareRevision 0
get_HardwareSynchronizationGroupId
get_HasAdvancedMathLicence True
get_HasPSTraceLicence True
get_IRDropCompMaxValue 65535
get_IRDropCompensationResolutionFactor 4095
get_IsGalvanostat True
get_IsHardwareSynchronizationMaster False
get_IsSlaveChannel False
get_LevelStepOverheadTime 0.00039999998989515007
get_MaxCurrent 3.0
get_MaxEISAmplitudeERMS 0.9000099897384644
get_MaxEISFrequency 200000.015625
get_MaxFrequencyACV 50000.0
get_MaxGEISFrequency 100000.0078125
get_MaxNPoints 20000000
get_MaxOfflinePoints 50000
get_MaxPotential 3.0
get_MaxPotentialBipot 6.0
get_MaxSamlingRateAutoRanging 501.0
get_MaxVAux 3.0
get_MethodSCRIPTVersion 1.5
get_MinADIntervalTime 6.6650000007939525e-06
get_MinCurrent -3.0
get_MinEISFrequency 9.989999853132758e-06
get_MinFirmwareDateRequired 10/7/2024 12:00:00 AM
get_MinFirmwareVersionRequired 1.3070000410079956
get_MinLevelStepDuration 0.019999999552965164
get_MinOfflineFAIntervalTime 9.998999530580477e-07
get_MinOfflineIntervalTime 9.999900066759437e-05
get_MinOnlineIntervalTime 0.0003999900072813034
get_MinPotential -3.0
get_MinPotentialBipot -6.0
get_MinimumOfflineEISIntervalTime 0.0009999989997595549
get_MinimumPulseTimeScanMethod 3.0000998973846436
get_SupportedAltMUXTechniques System.Int32[]
get_SupportedAppliedRanges System.Collections.Generic.List`1[PalmSens.CurrentRange]
get_SupportedBipotRanges System.Collections.Generic.List`1[PalmSens.CurrentRange]
get_SupportedCommands tfCsgaLMYzZRJjDcdEy
get_SupportedDigitalInputLineMask 96
get_SupportedDigitalOutputLineMask 31
get_SupportedMethods System.Int32[]
get_SupportedModes PalmSens.Comm.EnumMode[]
get_SupportedMuxModels PalmSens.MuxModel[]
get_SupportedPotentialRanges System.Collections.Generic.List`1[PalmSens.PotentialRange]
get_SupportedPotentiostatChannels Ch0
get_SupportedRanges System.Collections.Generic.List`1[PalmSens.CurrentRange]
get_SupportedRemoteCommands
get_SupportedSignalTrainCapabilities 72
get_SupportedWakeOnTriggers Communication, Timer
get_SupportsAdvancedTriggering True
get_SupportsAdvancedTriggeringOnDelay False
get_SupportsAuxiliaryControl True
get_SupportsBiPotInIdleStatusPackage False
get_SupportsBipotAutoranging False
get_SupportsBipotSoftwareMode False
get_SupportsDisplayMethodName False
get_SupportsEISTDD True
get_SupportsExplicitVariableNames False
get_SupportsILimits True
get_SupportsIRDropComp False
get_SupportsISStartingRange False
get_SupportsISTrim False
get_SupportsImpedance True
get_SupportsImpedimetricACEquilibration False
get_SupportsImpedimetricMeasurementStartSpecificRange True
get_SupportsMainsFrequencyNoiseReduction True
get_SupportsMultipleExtraValues True
get_SupportsOfflineMeasurements True
get_SupportsProgrammableTouchScreen False
get_SupportsStorage True
get_TechniqueNumberMethodSCRIPTCommandMapping System.Collections.Generic.Dictionary`2[System.Int32,System.Int32]
"""

data = {}

data = {
    'Device': str(cap.DeviceType),
    'Model': comm.DeviceSerial.TypeToModelName(),
    'ShortName': comm.DeviceSerial.TypeToString(),
    'Serial number': comm.get_DeviceSerial(),
    'Communication': cap.ConnDescription,
    'Firmware version': cap.FirmwareVersion,
    'Firmware release type': cap.FirmwareReleaseType,
    'Firmware special description': cap.SpecialFirmwareDescription,
    'Potential range': [cap.MinPotential, cap.MaxPotential],  # V
    'Max current read': cap.MaxCurrent,  # * CR
    'Detailed Information': {
        'Firmware build date': cap.FirmwareTimeStamp,
        'Firmware commit': comm.ClientConnection.GetFWCommitHash(),
    },
}


data['has bipot'] = cap.BiPotPresent
data['supports impedance'] = cap.SupportsImpedance
if cap.SupportsImpedance:
    data['Max. frequency'] = cap.MaxEISFrequency  # Hz
    data['Calibration values within limits'] = '???'
data['supports ir drop'] = cap.SupportsIRDropComp

data['Potentiostat'] = {
    'Min. current read': cap.MinCurrent,  # * CR
    'Max. current read': cap.MaxCurrent,  # * CR
    'Supported current ranges': [str(item) for item in cap.SupportedRanges],
    'Min. potential read': cap.MinPotential,  # V
    'Max. potential read/applied': cap.MaxPotential,  # V
    'Min. step potential': cap.DACPotential.StepSize * 1000.0,  # mV
}

data['is_hw_sync_master'] = cap.IsHardwareSynchronizationMaster
data['is_hw_sync_slave'] = cap.IsSlaveChannel

if cap.IsGalvanostat:
    data['Galvanostat'] = (
        {
            'Min. current read': cap.MinCurrent,  # * CR
            'Max. current read': cap.MaxCurrent,  # * CR
            'Supported current ranges': [str(item) for item in cap.SupportedAppliedRanges],
        },
    )

data['Supported techniques'] = [str(item) for item in cap.SupportedMethods]

data['Max EIS frequency'] = int(cap.MaxEISFrequency)  # Hz
data['Max GEIS frequency'] = int(cap.MaxGEISFrequency)  # Hz


@dataclass
class AnalogComponent:
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


data['adc'] = {
    'auxiliary': AnalogComponent._convert(cap.ADCAuxiliary),
    'bipot': AnalogComponent._convert(cap.ADCBiPot),
    'current': AnalogComponent._convert(cap.ADCCurrent),
    'potential': AnalogComponent._convert(cap.ADCPotential),
}

data['dac'] = {
    'auxiliary': AnalogComponent._convert(cap.DACAuxiliary),
    'bipot': AnalogComponent._convert(cap.DACBiPot),
    'current': AnalogComponent._convert(cap.DACCurrent),
    'potential': AnalogComponent._convert(cap.DACPotential),
}

data['supports_advanced_triggering'] = cap.SupportsAdvancedTriggering
data['supports_advanced_triggering_on_delay'] = cap.SupportsAdvancedTriggeringOnDelay
data['supports_auxiliary_control'] = cap.SupportsAuxiliaryControl
data['supports_bipot_in_idle_status_package'] = cap.SupportsBiPotInIdleStatusPackage
data['supports_bipot_autoranging'] = cap.SupportsBipotAutoranging
data['supports_bipot_software_mode'] = cap.SupportsBipotSoftwareMode
data['supports_display_method_name'] = cap.SupportsDisplayMethodName
data['supports_eistdd'] = cap.SupportsEISTDD
data['supports_explicit_variable_names'] = cap.SupportsExplicitVariableNames
data['supports_i_limits'] = cap.SupportsILimits
data['supports_ir_drop_comp'] = cap.SupportsIRDropComp
data['supports_is_starting_range'] = cap.SupportsISStartingRange
data['supports_is_trim'] = cap.SupportsISTrim
data['supports_impedance'] = cap.SupportsImpedance
data['supports_impedimetric_ac_equilibration'] = cap.SupportsImpedimetricACEquilibration
data['supports_impedimetric_measurement_start_specific_range'] = (
    cap.SupportsImpedimetricMeasurementStartSpecificRange
)
data['supports_mains_frequency_noise_reduction'] = cap.SupportsMainsFrequencyNoiseReduction
data['supports_multiple_extra_values'] = cap.SupportsMultipleExtraValues
data['supports_offline_measurements'] = cap.SupportsOfflineMeasurements
data['supports_programmable_touch_screen'] = cap.SupportsProgrammableTouchScreen
data['supports_storage'] = cap.SupportsStorage
