from __future__ import annotations

import pypalmsens as ps

if True:
    pass

man = ps.connect()

comm = man._comm
cap = man._comm.Capabilities


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
    'supported_applied_current_ranges': [str(item) for item in cap.SupportedAppliedRanges],
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


if __name__ == '__main__':
    breakpoint()
