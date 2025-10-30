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
from pathlib import Path

import pypalmsens as ps

MSCRIPT_FILE_PATH = MSCRIPT_FILE_PATH_ES4 = Path(__file__).parent / 'scripts' / 'cv.mscr'


def main():
    logging.basicConfig(
        level=logging.INFO, format='[%(module)s] %(message)s', stream=sys.stdout
    )
    # Uncomment the following line to reduce the log level for our library.
    # logging.getLogger('pypalmsens').setLevel(logging.INFO)

    instruments = ps.serial.discover()
    instrument = instruments[0]

    with ps.serial.InstrumentManager(instrument) as mgr:
        # Abort any previous script and restore communication.
        mgr.abort_and_sync()

        # Check if device is connected and responding successfully.
        firmware_version = mgr.get_firmware_version()
        device_type = mgr.get_device_type()
        print(f'Connected to {device_type}')
        print(f'Firmware version: {firmware_version}')
        print(f'MethodSCRIPT version: {mgr.get_mscript_version()}')
        print(f'Serial number: {mgr.get_serial_number()}')

        # Read MethodSCRIPT from file and send to device.
        mgr.send_script(MSCRIPT_FILE_PATH)

        # Read the script output (results) from the device.
        while True:
            line = mgr.readline()

            # No data means timeout, so ignore it and try again.
            if not line:
                continue

            # An empty line means end of script.
            if line == '\n':
                break

            # Non-empty line received. Try to parse as data package.
            variables = ps.serial.parse_mscript_data_package(line)

            if variables:
                # Apparently it was a data package. Print all variables.
                cols = []

                for var in variables:
                    cols.append(f'{var.type.name} = {var.value:11.4g} {var.type.unit}')

                    if 'status' in var.metadata:
                        cols.append(f'STATUS: {var.status_string():<16s}')

                    if 'cr' in var.metadata:
                        cr_text = var.current_range_string(device_type=device_type)
                        cols.append(f'CR: {cr_text}')

                print(' | '.join(cols))


if __name__ == '__main__':
    main()
