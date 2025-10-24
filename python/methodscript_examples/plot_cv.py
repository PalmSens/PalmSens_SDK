"""PalmSens MethodSCRIPT example: simple Cyclic Voltammetry (CV) measurement

This example showcases how to run a Cyclic Voltammetry (CV) measurement on
a MethodSCRIPT capable PalmSens instrument, such as the EmStat Pico.

The following features are demonstrated in this example:
  - Connecting to the PalmSens instrument using the serial port.
  - Running a Cyclic Voltammetry (CV) measurement.
  - Receiving and interpreting the measurement data from the device.
  - Plotting the measurement data.
"""

# Standard library imports
from __future__ import annotations

import datetime
import logging
import os
import os.path
import sys

# Third-party imports
import matplotlib.pyplot as plt

# Local imports
import palmsens.instrument
import palmsens.mscript
import palmsens.serial

###############################################################################
# Start of configuration
###############################################################################

# COM port of the device (None = auto detect).
DEVICE_PORT = None

# Location of MethodSCRIPT file to use.
MSCRIPT_FILE_PATH = 'scripts/cv.mscr'

# Location of output files. Directory will be created if it does not exist.
OUTPUT_PATH = 'output'

###############################################################################
# End of configuration
###############################################################################


LOG = logging.getLogger(__name__)


def main():
    """Run the example."""
    # Configure the logging.
    logging.basicConfig(
        level=logging.DEBUG, format='[%(module)s] %(message)s', stream=sys.stdout
    )
    # Uncomment the following line to reduce the log level for our library.
    # logging.getLogger('palmsens').setLevel(logging.INFO)
    # Disable excessive logging from matplotlib.
    logging.getLogger('matplotlib').setLevel(logging.INFO)
    logging.getLogger('PIL.PngImagePlugin').setLevel(logging.INFO)

    port = DEVICE_PORT
    if port is None:
        port = palmsens.serial.auto_detect_port()

    # Create and open serial connection to the device.
    with palmsens.serial.Serial(port, 1) as comm:
        device = palmsens.instrument.Instrument(comm)
        device_type = device.get_device_type()
        LOG.info('Connected to %s.', device_type)

        # Read and send the MethodSCRIPT file.
        LOG.info('Sending MethodSCRIPT.')
        device.send_script(MSCRIPT_FILE_PATH)

        # Read the result lines.
        LOG.info('Waiting for results.')
        result_lines = device.readlines_until_end()

    # Store results in file.
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    result_file_name = datetime.datetime.now().strftime('ms_plot_cv_%Y%m%d-%H%M%S.txt')
    result_file_path = os.path.join(OUTPUT_PATH, result_file_name)
    with open(result_file_path, 'wt', encoding='ascii') as file:
        file.writelines(result_lines)

    # Parse the result.
    curves = palmsens.mscript.parse_result_lines(result_lines)

    # Log the results.
    for curve in curves:
        for package in curve:
            LOG.info([str(value) for value in package])

    # Get the applied potentials (first column of each row)
    applied_potential = palmsens.mscript.get_values_by_column(curves, 0)
    # Get the measured currents (second column of each row)
    measured_current = palmsens.mscript.get_values_by_column(curves, 1)

    # Plot the results.
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
