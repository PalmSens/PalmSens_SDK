"""PalmSens MethodSCRIPT example: advanced SWV measurement and plotting

This example showcases how to run two Square Wave Voltammetry (SWV)
measurements using an EmStat Pico instrument, and then plot the results for
easy verification.

To run this example, connect the EmStat Pico to the RedOx Circuit (WE A) on
the PalmSens Dummy Cell.

The following features are demonstrated in this example:
  - Connecting to the EmStat Pico using the serial port.
  - Running two consecutive Square Wave Voltammetry (SWV) measurements.
  - Receiving and interpreting the measurement data from the device.
  - Plotting the measurement data from both measurements in a plot.
    Specifically, multiple curves are drawn in the same figure against a
    common x axis.
  - Exporting the measurement data to a file in CSV format.

Although this example demonstrates how to plot the SWV measurement data from
an EmStat Pico device, the principles could be applied just as well for other
measurement types using any MethodSCRIPT capable PalmSens instrument. The code
can easily be modified for other (similar) types of measurements.
"""

from __future__ import annotations

import csv
import datetime
import logging
import sys
import typing
from pathlib import Path

import matplotlib.pyplot as plt

import methodscript

# COM port of the device (None = auto detect).
DEVICE_PORT = None

MSCRIPT_FILE_PATH_ES4 = Path(__file__).parent / 'scripts' / 'advanced_swv_es4.mscr'
MSCRIPT_FILE_PATH_ESPICO = Path(__file__).parent / 'scripts' / 'advanced_swv_espico.mscr'

OUTPUT_PATH = Path(__file__).parent / 'output'

# In this example, columns refer to the separate "pck_add" entries in each
# MethodSCRIPT data package. For example, in the used script there are
# four columns per data package:
#   pck_start
#   pck_add p
#   pck_add c
#   pck_add f
#   pck_add r
#   pck_end
# Here, the indices 0/1/2/3 refer to the variables p/c/f/r/ respectively.
# The following variables define which columns (i.e. variables) to plot, and
# how they are named in the figure.

COLUMN_NAMES = ['Potential', 'Current', 'Forward Current', 'Reverse Current']

# Index of column to put on the x axis.
XAXIS_COLUMN_INDEX = 0
# Indices of columns to put on the y axis. The variables must be same type.
YAXIS_COLUMN_INDICES = [1, 2, 3]


logger = logging.getLogger(__name__)


def write_curves_to_csv(file: typing.IO, curves: list[list[list[methodscript.MScriptVar]]]):
    """Write the curves to file in CSV format.

    `file` must be a file-like object in text mode with newlines translation
    disabled.

    The header row is based on the first row of the first curve. It is assumed
    that all rows in all curves have the same data types.

    NOTE: Although the extension is CSV, which stands for Comma Separated
    Values, a semicolon (';') is used as delimiter. This is done to be
    compatible with MS Excel, which may use a comma (',') as decimal
    separator in some regions, depending on regional settings on the
    computer. If you use anoter program to read the CSV files, you may need
    to change this. The CSV writer can be configured differently to support
    a different format. See
    https://docs.python.org/3/library/csv.html#csv.writer for all options.
    """
    # NOTE: The following line writes a Microsoft Excel specific header line to
    # the CSV file, to tell it we use a semicolon as delimiter. If you don't
    # use Excel to read the CSV file, you might want to remove this line.
    file.write('sep=;\n')
    writer = csv.writer(file, delimiter=';')

    for curve in curves:
        writer.writerow([f'{value.type.name} [{value.type.unit}]' for value in curve[0]])

        for package in curve:
            writer.writerow([value.value for value in package])


def main():
    """Run the example."""
    logging.basicConfig(
        level=logging.DEBUG, format='[%(module)s] %(message)s', stream=sys.stdout
    )
    # Uncomment the following line to reduce the log level of our library.
    # logging.getLogger('pypalmsens').setLevel(logging.INFO)

    # Disable excessive logging from matplotlib.
    logging.getLogger('matplotlib').setLevel(logging.INFO)
    logging.getLogger('PIL.PngImagePlugin').setLevel(logging.INFO)

    base_name = datetime.datetime.now().strftime('ms_plot_swv_%Y%m%d-%H%M%S')
    base_path = OUTPUT_PATH / base_name

    port = DEVICE_PORT
    if port is None:
        port = methodscript.auto_detect_port()

    with methodscript.Serial(port, 1) as comm:
        device = methodscript.Instrument(comm)
        device_type = device.get_device_type()
        logger.info('Connected to %s.', device_type)

        if device_type == methodscript.DeviceType.EMSTAT_PICO:
            mscript_file_path = MSCRIPT_FILE_PATH_ESPICO
        elif 'EmStat4' in device_type:
            mscript_file_path = MSCRIPT_FILE_PATH_ES4
        else:
            logger.error('No SWV script for this device found.')
            return

        logger.info('Sending MethodSCRIPT.')
        device.send_script(mscript_file_path)

        logger.info('Waiting for results.')
        result_lines = device.readlines_until_end()

    OUTPUT_PATH.mkdir(exist_ok=True)
    with open(base_path.with_suffix('.txt'), 'wt', encoding='ascii') as file:
        file.writelines(result_lines)

    curves = methodscript.parse_result_lines(result_lines)

    with open(base_path.with_suffix('.csv'), 'wt', newline='', encoding='ascii') as file:
        write_curves_to_csv(file, curves)

    plt.figure()
    plt.title(base_name)

    xvar = curves[0][0][XAXIS_COLUMN_INDEX]
    plt.xlabel(f'{xvar.type.name} [{xvar.type.unit}]')

    yvar = curves[0][0][YAXIS_COLUMN_INDICES[0]]
    plt.ylabel(f'{yvar.type.name} [{yvar.type.unit}]')

    plt.grid(visible=True, which='major', linestyle='-')
    plt.grid(visible=True, which='minor', linestyle='--', alpha=0.2)
    plt.minorticks_on()

    for icurve, curve in enumerate(curves):
        xvalues = methodscript.get_values_by_column(curves, XAXIS_COLUMN_INDEX, icurve)

        for yaxis_column_index in YAXIS_COLUMN_INDICES:
            yvalues = methodscript.get_values_by_column(curves, yaxis_column_index, icurve)

            if curve[0][yaxis_column_index].type != yvar.type:
                continue

            label = f'{COLUMN_NAMES[yaxis_column_index]} vs {COLUMN_NAMES[XAXIS_COLUMN_INDEX]}'

            if len(curves) > 1:
                label += f' {icurve}'

            plt.plot(xvalues, yvalues, label=label)

    plt.legend()

    plt.savefig(base_path.with_suffix('.png'))
    plt.show()


if __name__ == '__main__':
    main()
