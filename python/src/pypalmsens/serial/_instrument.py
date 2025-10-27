"""PalmSens Serial Port (UART) interface

This module implements the serial interface to the PalmSens instrument.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path

import serial
import serial.tools.list_ports

from .._instruments import Instrument

logger = logging.getLogger(__name__)


logger = logging.getLogger(__name__)

BAUDRATE = 230400


class DeviceType:
    UNKNOWN = 'unknown device'
    EMSTAT_PICO = 'EmStat Pico'
    EMSTAT4_HR = 'EmStat4 HR'
    EMSTAT4_LR = 'EmStat4 LR'
    MULTI_EMSTAT4_HR = 'MultiEmStat4 HR'
    MULTI_EMSTAT4_LR = 'MultiEmStat4 LR'
    EMSTAT_PICO_BOOTLOADER = 'EmStat Pico bootloader'


_FIRMWARE_VERSION_TO_DEVICE_TYPE_MAPPING = [
    ('espico', DeviceType.EMSTAT_PICO),
    ('es4_hr', DeviceType.EMSTAT4_HR),
    ('es4_lr', DeviceType.EMSTAT4_LR),
    ('mes4hr', DeviceType.MULTI_EMSTAT4_HR),
    ('mes4lr', DeviceType.MULTI_EMSTAT4_LR),
    ('espbl', DeviceType.EMSTAT_PICO_BOOTLOADER),
]


class CommunicationError(Exception):
    """Generic communication error class."""


class CommunicationTimeout(Exception):
    """Communication timeout.

    Note that a communication timeout does not have to be an error. If a long
    measurement is running, it is possible that a communication timeout occurs
    while waiting on the response. In that case, just keep trying to read and
    (optionally) handle a global timeout in the calling method.
    This exception could be avoided by increasing the timeout on the low-level
    (serial) interface. However, that could cause the application to block and
    become unresponsive. It's better to keep the low-level read timeouts low
    (< 1 s) and handle timeouts at the application level.
    """


def _is_mscript_device(port_description: str) -> bool:
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


def discover() -> list[Instrument]:
    """Discover MethodSCRIPT compatible serial communication devices.

    This works by searching for an available port with the correct name.
    """
    ports = serial.tools.list_ports.comports(include_links=False)
    instruments = []

    for port in ports:
        logger.debug('Found port: %s', port.description)
        if _is_mscript_device(port.description):
            device = serial.Serial(baudrate=BAUDRATE)
            device.port = port.device

            instruments.append(
                Instrument(
                    id=port.description,
                    interface='pyserial',
                    device=device,
                )
            )

    return instruments


class InstrumentManager:
    """Instrument manager for PalmSens instruments.

    Parameters
    ----------
    instrument: Instrument
        Instrument to connect to, use `discover()` to find connected instruments.
    """

    def __init__(self, instrument: Instrument):
        self.instrument = instrument
        """Instrument to connect to."""

        self.comm = self.instrument.device
        """Communication channel."""

        self.firmware_version = None
        """Firmware version."""

        self.device_type = DeviceType.UNKNOWN
        """Device type."""

    def __repr__(self):
        return (
            f'{self.__class__.__name__}({self.instrument.id}, connected={self.is_connected()})'
        )

    def __enter__(self):
        if not self.is_connected():
            self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def is_connected(self) -> bool:
        """Return True if an instrument connection exists."""
        return self.instrument.device.is_open

    def connect(self):
        """Connect to instrument."""
        self.instrument.device.open()

    def disconnect(self):
        """Disconnect from the instrument."""
        self.instrument.device.close()

    def write(self, text: str):
        """Write to device.

        The text is encoded using ASCII encoding, since all MethodSCRIPT
        commands are plain ASCII text. String literals (as used in the
        `send_string` command) and comments *could* contain non-ASCII
        characters, but this is not officially supported or recommended.
        Although using another encoding here could be beneficial for some
        users, it could lead to unexpected problems for other users.
        Therefore, the ASCII encoding is chosen, which is always safe and
        easy to use as long as the input MethodSCRIPT does not contain
        non-ASCII characters.
        """
        data = text.encode('ascii')
        logger.debug('TX: %r', data)
        self.comm.write(data)

    def writelines(self, lines):
        """Write multiple lines to the device."""
        for line in lines:
            self.write(line)

    def readline(self) -> str:
        """Read one response line from the device."""
        data = self.comm.readline()

        if data:
            logger.debug('RX: %r', data)

        line = data.decode('ascii', errors='replace')

        if not line:
            raise CommunicationTimeout()

        if line[-1] != '\n':
            raise CommunicationError('No EOL character received.')

        return line

    def readlines_until_end(self):
        """Receive all lines until an empty line is received."""
        lines = []
        while True:
            try:
                line = self.readline()
            except CommunicationTimeout:
                continue
            if line == '\n':
                break
            lines.append(line)
        return lines

    def _update_firmware_version_and_device_type(self, force=False):
        if force or not self.firmware_version:
            self.write('t\n')
            line1 = self.readline()
            line2 = self.readline()

            if not (line1.startswith('t') and line2.endswith('*\n')):
                raise CommunicationError('Invalid response to firmware version request.')

            self.firmware_version = (line1 + line2).replace('\n', ' ')[1:-1]

        self.device_type = DeviceType.UNKNOWN

        for device_id, device_type in _FIRMWARE_VERSION_TO_DEVICE_TYPE_MAPPING:
            if self.firmware_version.startswith(device_id):
                self.device_type = device_type
                break

    def get_firmware_version(self, force: bool = False):
        """Get the device firmware version.

        The result of this call is cached. If it is changed on the device, use
        `force=true` to force reading it from the device again.
        """
        self._update_firmware_version_and_device_type(force=force)
        return self.firmware_version

    def get_device_type(self, force: bool = False) -> str:
        """Get the device type.

        The result of this call is cached. If it is changed on the device, use
        `force=true` to force reading it from the device again.
        """
        self._update_firmware_version_and_device_type(force=force)
        return self.device_type

    def get_mscript_version(self) -> str:
        self.write('v\n')
        response = self.readline()
        return response[1:-1]

    def get_serial_number(self) -> str:
        """Read the EmStat Pico serial number."""
        self.write('i\n')
        return self.readline()[1:-1]

    def get_register(self, register) -> str:
        """Get the value of a register."""
        self.write(f'G{register:02d}\n')
        return self.readline()[1:-1]

    def load_mscript_from_flash(self):
        """Load the MethodSCRIPT from flash to RAM."""
        self.write('Lmscr\n')
        self.readline()
        # TODO: check response!

    def run_mscript_from_flash(self):
        """Load the MethodSCRIPT from flash to RAM and execute it."""
        self.write('Lmscr\n')
        self.readline()
        # TODO: check response!
        self.write('r\n')

    def send_script(self, path: str | Path):
        """Read a script from file and send it to the device.

        Note that the file should contain ASCII characters only. Other
        characters or encodings are not supported. The file may contain
        any common end-of-line style (e.g. Unix or Windows line endings).
        The lines written to the device will always use '\n' line endings
        (Linux format).
        """
        with open(path, 'rt', encoding='ascii') as file:
            lines = file.readlines()
        self.writelines(lines)

    def abort_and_sync(self):
        """Abort a possibly running script and wait for it to finish.

        This method tries to get the device in a known valid state by sending an
        abort command and checking the response. If a script was still running, it
        will wait for it to complete. Note that this could take long, depending on
        the measurement that was running.

        Note that it should normally not be necessary to call this method, but it
        could be useful in case the Python script was interrupted or the serial
        communication was lost during a measurement. In that case, when restarting
        the script, it would receive data from the previous measurement, which
        would cause communication issues.
        This method should recover from such situation and restore communication.
        """
        logger.info('Aborting possible active scripts and syncing communication.')

        # Send new line character to flush possible command in command buffer.
        self.write('\n')

        # Send abort command.
        self.write('Z\n')

        # Wait for acknowledgment of abort command.
        while True:
            response = self.readline()
            if response.startswith('Z'):
                break

        if response == 'Z!0006\n':
            logger.info('No active scripts are currently running.')
            # Wait for > 50 ms after a failed command ('!' in response).
            time.sleep(0.1)

        if response == 'Z\n':
            logger.info('Waiting for active script to finish...')
            self.readlines_until_end()

        logger.info('Device is ready.')
