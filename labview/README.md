# Labview SDK for PalmSens devices

With this SDK, you can control your PalmSens instrument and process the data in Labview.
Connect, control and process data from your PalmSens instrument using Labview.

![Control your PalmSens device from Labview](../docs/modules/labview/images/measuring_1.png)

Download the latest release https://github.com/palmsens/palmsens_sdk/releases[here].

See [the installation guidelines](https://palmsens.github.io/PalmSens_SDK/palmsens-sdk/labview/installation.html) for more information.

## SDK overview

The PalmSens SDK contains the following .NET libraries and LabVIEW
classes, controls and Vis in the PalmSens folder:

- Libraries Folder: Contains all the necessary .NET libraries. Labview directly interfaces with the classes and functions defined in these libraries.

- PalmSens LabVIEW class:

    Class that implements the basic features required to use our instruments
    in LabVIEW.

    * `Initialise`: Initialises the class and .NET libraries.
    * `Dispose`: Frees up memory used by .NET libraries.
    * `ListInstruments`: Returns an array of the available instruments.
    * `Connect`: Connects to the specified instrument.
    * `Disconnect`: Disconnects from the connected instrument.
    * `Measure`: Performs a measurement.
    * `AbortMeasurement`: Aborts the current measurement

- `MeasurementResults` and `LiveCurveResults` controls: Type definitions for the in and outputs of the Measure function.

- Event Callback Vis: VIs used by the Measure function to receive data from .NET events.

## Example programs

The following examples are included.

| | |
|-|-|
| **Getting started example**: Demonstrates how to use the PalmSens class to run a measurement. | ![Basic example](../docs/modules/labview/images/examples/basic_example.png) |
| **UI example**: Demonstrates how to use the PalmSens class to run and plot a measurement in real-time and the recommended method to abort, disconnect, or terminate the app during an active measurement. | ![Basic UI example](../docs/modules/labview/images/examples/basic_ui_example.png) |
| **MethodSCRIPT example**: Demonstrates how to use the PalmSens class to run a MethodSCRIPT™ measurement. | ![MethodSCRIPT example](../docs/modules/labview/images/examples/methodscript_example.png) |

For more information, see the [documentation](https://palmsens.github.io/PalmSens_SDK/palmsens-sdk/labview/index.html)
