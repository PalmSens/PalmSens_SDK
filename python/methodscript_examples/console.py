"""PalmSens MethodSCRIPT console example

This example demonstrates how to communicate with a MethodSCRIPT capable
PalmSens instrument, such as the EmStat Pico.

The following features are demonstrated in this example:
  - Auto-detecting the serial port.
  - Connecting to the device using the serial port.
  - Reading the firmware version and device type.
  - Reading a MethodSCRIPT from file and executing it on the device. The
    MethodSCRIPT used in this example performs a Cyclic Voltammetry (CV)
    measurement.
  - Receiving and interpreting the response from the device (i.e., the data
    packages) and printing the measurement data to the console.
"""

from __future__ import annotations

import logging
import sys

import pypalmsens.methodscript as mscript

# COM port of the MethodSCRIPT device (None = auto-detect).
# In case auto-detection does not work or is not wanted, fill in the correct
# port name, e.g. 'COM6' on Windows, or '/dev/ttyUSB0' on Linux.
DEVICE_PORT = None

MSCRIPT_FILE_PATH = 'scripts/cv.mscr'


logger = logging.getLogger(__name__)


def main():
    """Run the example."""
    logging.basicConfig(
        level=logging.INFO, format='[%(module)s] %(message)s', stream=sys.stdout
    )
    # Uncomment the following line to reduce the log level for our library.
    # logging.getLogger('pypalmsens').setLevel(logging.INFO)

    port = DEVICE_PORT
    if port is None:
        port = mscript.auto_detect_port()

    logger.info('Trying to connect to device using port %s...', port)
    with mscript.Serial(port, 5) as comm:
        device = mscript.Instrument(comm)
        logger.info('Connected.')

        # Abort any previous script and restore communication.
        device.abort_and_sync()

        # Check if device is connected and responding successfully.
        firmware_version = device.get_firmware_version()
        device_type = device.get_device_type()
        logger.info('Connected to %s.', device_type)
        logger.info('Firmware version: %s', firmware_version)
        logger.info('MethodSCRIPT version: %s', device.get_mscript_version())
        logger.info('Serial number = %s', device.get_serial_number())

        # Read MethodSCRIPT from file and send to device.
        device.send_script(MSCRIPT_FILE_PATH)

        # Read the script output (results) from the device.
        while True:
            line = device.readline()

            # No data means timeout, so ignore it and try again.
            if not line:
                continue

            # An empty line means end of script.
            if line == '\n':
                break

            # Non-empty line received. Try to parse as data package.
            variables = mscript.parse_mscript_data_package(line)

            if variables:
                # Apparently it was a data package. Print all variables.
                cols = []
                for var in variables:
                    cols.append(f'{var.type.name} = {var.value:11.4g} {var.type.unit}')
                    if 'status' in var.metadata:
                        status_text = mscript.metadata_status_to_text(var.metadata['status'])
                        cols.append(f'STATUS: {status_text:<16s}')
                    if 'cr' in var.metadata:
                        cr_text = mscript.metadata_current_range_to_text(
                            device_type, var.type, var.metadata['cr']
                        )
                        cols.append(f'CR: {cr_text}')
                print(' | '.join(cols))


if __name__ == '__main__':
    main()
