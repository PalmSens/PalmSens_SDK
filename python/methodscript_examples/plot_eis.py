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
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

import methodscript

# COM port of the device (None = auto detect).
DEVICE_PORT = None

MSCRIPT_FILE_PATH = Path(__file__).parent / 'scripts' / 'eis.mscr'

OUTPUT_PATH = Path(__file__).parent / 'output'

AX1_COLOR = 'tab:red'  # Color for impedance (Z)
AX2_COLOR = 'tab:blue'  # Color for phase


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

    port = DEVICE_PORT
    if port is None:
        port = methodscript.auto_detect_port()

    with methodscript.Serial(port, 1) as comm:
        device = methodscript.Instrument(comm)
        device_type = device.get_device_type()
        logger.info('Connected to %s.', device_type)

        logger.info('Sending MethodSCRIPT.')
        device.send_script(MSCRIPT_FILE_PATH)

        logger.info('Waiting for results.')
        result_lines = device.readlines_until_end()

    OUTPUT_PATH.mkdir(exist_ok=True)
    result_file_name = datetime.datetime.now().strftime('ms_plot_eis_%Y%m%d-%H%M%S.txt')
    result_file_path = OUTPUT_PATH / result_file_name

    with open(result_file_path, 'wt', encoding='ascii') as file:
        file.writelines(result_lines)

    curves = methodscript.parse_result_lines(result_lines)

    for curve in curves:
        for package in curve:
            logger.info([str(value) for value in package])

    applied_frequency = methodscript.get_values_by_column(curves, 0)
    measured_z_real = methodscript.get_values_by_column(curves, 1)
    measured_z_imag = methodscript.get_values_by_column(curves, 2)

    # Invert the imaginary part for the electrochemist convention.
    measured_z_imag = -measured_z_imag

    z_complex = measured_z_real + 1j * measured_z_imag
    z_phase = np.angle(z_complex, deg=True)
    z = np.abs(z_complex)

    plt.figure(1)
    plt.plot(measured_z_real, measured_z_imag)
    plt.title('Nyquist plot')
    plt.axis('equal')
    plt.grid()
    plt.xlabel("Z'")
    plt.ylabel("-Z''")
    # plt.savefig('nyquist_plot.png')

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.set_xlabel('Frequency (Hz)')
    ax1.grid(which='major', axis='x', linestyle='--', linewidth=0.5, alpha=0.5)
    ax1.set_ylabel('Z', color=AX1_COLOR)
    ax1.semilogx(applied_frequency, z, color=AX1_COLOR)
    ax1.tick_params(axis='y', labelcolor=AX1_COLOR)
    ax1.minorticks_on()
    ax1.grid(which='major', axis='y', linestyle='--', linewidth=0.5, alpha=0.5, color=AX1_COLOR)

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
