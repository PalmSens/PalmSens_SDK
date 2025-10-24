"""PalmSens Serial Port (UART) interface

This module implements the serial interface to the PalmSens instrument.
"""

from __future__ import annotations

import logging

import serial
import serial.tools.list_ports

logger = logging.getLogger(__name__)


def _is_mscript_device(port_description: str):
    """Check if the specified port is a known MethodSCRIPT device.

    NOTES:
    - Since the EmStat Pico uses a generic FTDI USB-to-Serial chip,
      it is identified by Windows as "USB Serial Port". This is the
      text to look for when using the auto-detection feature. Note
      that an EmStat Pico or Sensit BT cannot be auto-detected if
      there are also other devices connected that use this name.
    - An EmStat4 device in bootloader mode would be identified as
      'EmStat4 Bootloader', but we only want to connect to devices
      that can run MethodSCRIPTs, so we do not include that here.
    """
    return (
        # Linux descriptions
        port_description == 'EmStat4'
        or port_description.startswith('ESPicoDev')
        or port_description.startswith('SensitBT')
        or port_description.startswith('SensitSmart')
        # Windows descriptions
        or port_description.startswith('EmStat4 LR (COM')
        or port_description.startswith('EmStat4 HR (COM')
        or port_description.startswith('MultiEmStat4 LR (COM')
        or port_description.startswith('MultiEmStat4 HR (COM')
        or port_description.startswith('USB Serial Port')
    )


def auto_detect_port():
    """Auto-detect serial communication port.

    This works by searching for an available port with the correct name.
    If exactly one port matches, this port will be returned. If there
    are either no or multiple matches, the auto-detection fails and None
    is returned instead. In that case, the user must explicitly specify
    which port to connect to (or disconnect unneeded devices with the
    same port name).
    """
    logger.info('Auto-detecting serial communication port.')
    ports = serial.tools.list_ports.comports(include_links=False)
    candidates = []

    for port in ports:
        logger.debug('Found port: %s', port.description)
        if _is_mscript_device(port.description):
            candidates.append(port.device)

    if len(candidates) != 1:
        logger.error('%d candidates found. Auto-detect failed.', len(candidates))
        raise RuntimeError('Auto-detection of serial port failed.')

    logger.info('Exactly one candidate found. Using %s.', candidates[0])
    return candidates[0]


class Serial:
    """Serial communication interface for EmStat Pico."""

    def __init__(self, port: str, timeout: float):
        self.connection = serial.Serial(port=None, baudrate=230400, timeout=timeout)
        self.connection.port = port

    def __enter__(self):
        if not self.connection.is_open:
            self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def open(self):
        self.connection.open()

    def close(self):
        self.connection.close()

    def write(self, data: bytes):
        self.connection.write(data)

    def readline(self) -> bytes:
        return self.connection.readline()
