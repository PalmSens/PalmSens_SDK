"""PalmSens MethodSCRIPT example: simple Cyclic Voltammetry (CV) measurement

This example showcases how to run a Cyclic Voltammetry (CV) measurement on
a MethodSCRIPT capable PalmSens instrument, such as the EmStat Pico.

The following features are demonstrated in this example:
  - Connecting to the PalmSens instrument using the serial port.
  - Running a Cyclic Voltammetry (CV) measurement.
  - Receiving and interpreting the measurement data from the device.
  - Plotting the measurement data.
"""

from __future__ import annotations

import datetime
import logging
import sys
from pathlib import Path

import matplotlib.pyplot as plt

import pypalmsens as ps

# COM port of the device (None = auto detect).
DEVICE_PORT = None

MSCRIPT_FILE_PATH = Path(__file__).parent / 'scripts' / 'cv.mscr'

OUTPUT_PATH = Path(__file__).parent / 'output'


logger = logging.getLogger(__name__)


def main():
    """Run the example."""
    logging.basicConfig(
        level=logging.DEBUG, format='[%(module)s] %(message)s', stream=sys.stdout
    )
    # Uncomment the following line to reduce the log level for our library.
    # logging.getLogger('pypalmsens').setLevel(logging.INFO)

    # Disable excessive logging from matplotlib.
    logging.getLogger('matplotlib').setLevel(logging.INFO)
    logging.getLogger('PIL.PngImagePlugin').setLevel(logging.INFO)

    instruments = ps.serial.discover()
    instrument = instruments[0]

    with ps.serial.InstrumentManager(instrument) as mgr:
        device_type = mgr.get_device_type()
        logger.info('Connected to %s.', device_type)

        logger.info('Sending MethodSCRIPT.')
        mgr.send_script(MSCRIPT_FILE_PATH)

        logger.info('Waiting for results.')
        result_lines = mgr.readlines_until_end()

    OUTPUT_PATH.mkdir(exist_ok=True)
    result_file_name = datetime.datetime.now().strftime('ms_plot_cv_%Y%m%d-%H%M%S.txt')
    result_file_path = OUTPUT_PATH / result_file_name
    with open(result_file_path, 'wt', encoding='ascii') as file:
        file.writelines(result_lines)

    curves = ps.serial.parse_result_lines(result_lines)

    for curve in curves:
        for package in curve:
            logger.info([str(value) for value in package])

    applied_potential = ps.serial.get_values_by_column(curves, 0)
    measured_current = ps.serial.get_values_by_column(curves, 1)

    plt.figure(1)
    plt.plot(applied_potential, measured_current)
    plt.title('Voltammogram')
    plt.xlabel('Applied Potential (V)')
    plt.ylabel('Measured Current (A)')
    plt.grid(visible=True, which='major', linestyle='-')
    plt.grid(visible=True, which='minor', linestyle='--', alpha=0.2)
    plt.minorticks_on()
    plt.show()


if __name__ == '__main__':
    main()
