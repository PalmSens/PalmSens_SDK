"""PalmSens instrument module

This module implements the communication protocol. This consists of the
high-level read and write methods, methods to read the firmware version,
identify the device type, execute scripts on the device, etc.

The low-level (physical) communication interface,  is implemented in another
module, so that multiple physical interfaces (e.g. serial port, USB, etc.)
can be supported.

MethodSCRIPT specific methods, such as parsing and interpreting the measurement
data, is implemented in the mscript module.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path

logger = logging.getLogger(__name__)


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


class Instrument:
    """Communication interface for MethodSCRIPT instruments.

    This class contains high-level communication methods that are independent
    of the physical interface (e.g.: serial port, USB, Bluetooth, ...). The
    low-level communication should be provided by a communication object that
    is passed to the initializer.

    The low-level communication module should only implement the following
    two methods:
        - write(data: bytes)
        - readline() -> bytes
    """

    def __init__(self, comm):
        """Initialize the object.

        `comm` must be a communication object as described in the
        documentation of this class.
        """
        self.comm = comm
        self.firmware_version = None
        self.device_type = DeviceType.UNKNOWN

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

    def get_device_type(self, force: bool = False):
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
