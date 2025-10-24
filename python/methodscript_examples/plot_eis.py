"""PalmSens MethodSCRIPT example: Electrochemical Impedance Spectroscopy (EIS)

This example showcases how to run an Electrochemical Impedance Spectroscopy
(EIS) measurement on a MethodSCRIPT capable PalmSens instrument, such as the
EmStat Pico.

The following features are demonstrated in this example:
  - Connecting to the PalmSens instrument using the serial port.
  - Running an Electrochemical Impedance Spectroscopy (EIS) measurement.
  - Receiving and interpreting the measurement data from the device.
  - Plotting the measurement data.
"""

from __future__ import annotations

import datetime
import logging
import os
import os.path
import sys

import matplotlib.pyplot as plt
import numpy as np

import pypalmsens.instrument
import pypalmsens.mscript
import pypalmsens.serial

# COM port of the device (None = auto detect).
DEVICE_PORT = None

# Location of MethodSCRIPT file to use.
MSCRIPT_FILE_PATH = 'scripts/eis.mscr'

# Location of output files. Directory will be created if it does not exist.
OUTPUT_PATH = 'output'

# Plot colors.
AX1_COLOR = 'tab:red'  # Color for impedance (Z)
AX2_COLOR = 'tab:blue'  # Color for phase


LOG = logging.getLogger(__name__)


def main():
    """Run the example."""
    # Configure the logging.
    logging.basicConfig(
        level=logging.DEBUG, format='[%(module)s] %(message)s', stream=sys.stdout
    )
    # Uncomment the following line to reduce the log level for our library.
    # logging.getLogger('pypalmsens').setLevel(logging.INFO)
    # Disable excessive logging from matplotlib.
    logging.getLogger('matplotlib').setLevel(logging.INFO)
    logging.getLogger('PIL.PngImagePlugin').setLevel(logging.INFO)

    port = DEVICE_PORT
    if port is None:
        port = pypalmsens.serial.auto_detect_port()

    # Create and open serial connection to the device.
    with pypalmsens.serial.Serial(port, 1) as comm:
        device = pypalmsens.instrument.Instrument(comm)
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
    result_file_name = datetime.datetime.now().strftime('ms_plot_eis_%Y%m%d-%H%M%S.txt')
    result_file_path = os.path.join(OUTPUT_PATH, result_file_name)
    with open(result_file_path, 'wt', encoding='ascii') as file:
        file.writelines(result_lines)

    # Parse the result.
    curves = pypalmsens.mscript.parse_result_lines(result_lines)

    # Log the results.
    for curve in curves:
        for package in curve:
            LOG.info([str(value) for value in package])

    # Get the applied frequencies.
    applied_frequency = pypalmsens.mscript.get_values_by_column(curves, 0)
    # Get the measured real part of the complex impedance.
    measured_z_real = pypalmsens.mscript.get_values_by_column(curves, 1)
    # Get the measured imaginary part of the complex impedance.
    measured_z_imag = pypalmsens.mscript.get_values_by_column(curves, 2)

    # Calculate Z and phase.
    # Invert the imaginary part for the electrochemist convention.
    measured_z_imag = -measured_z_imag
    # Compose the complex impedance.
    z_complex = measured_z_real + 1j * measured_z_imag
    # Get the phase from the complex impedance in degrees.
    z_phase = np.angle(z_complex, deg=True)
    # Get the impedance value.
    z = np.abs(z_complex)

    # Plot the results.
    # Show the Nyquist plot as figure 1.
    plt.figure(1)
    plt.plot(measured_z_real, measured_z_imag)
    plt.title('Nyquist plot')
    plt.axis('equal')
    plt.grid()
    plt.xlabel("Z'")
    plt.ylabel("-Z''")
    # plt.savefig('nyquist_plot.png')

    # Show the Bode plot as dual y axis (sharing the same x axis).
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.set_xlabel('Frequency (Hz)')
    ax1.grid(which='major', axis='x', linestyle='--', linewidth=0.5, alpha=0.5)
    ax1.set_ylabel('Z', color=AX1_COLOR)
    # Make x axis logarithmic.
    ax1.semilogx(applied_frequency, z, color=AX1_COLOR)
    # Show ticks.
    ax1.tick_params(axis='y', labelcolor=AX1_COLOR)
    # Turn on the minor ticks, which are required for the minor grid.
    ax1.minorticks_on()
    # Customize the major grid.
    ax1.grid(which='major', axis='y', linestyle='--', linewidth=0.5, alpha=0.5, color=AX1_COLOR)

    # We already set the x label with ax1.
    ax2.set_ylabel('-Phase (degrees)', color=AX2_COLOR)
    ax2.semilogx(applied_frequency, z_phase, color=AX2_COLOR)
    ax2.tick_params(axis='y', labelcolor=AX2_COLOR)
    ax2.minorticks_on()
    ax2.grid(which='major', axis='y', linestyle='--', linewidth=0.5, alpha=0.5, color=AX2_COLOR)

    fig.suptitle('Bode plot')
    fig.tight_layout()
    # fig.savefig('bode_plot.png')
    plt.show()


if __name__ == '__main__':
    main()
