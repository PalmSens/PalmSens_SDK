# Matlab SDK for PalmSens devices

With this SDK, you can control your PalmSens instrument and process the data in MATLAB.
Connect, control and process data from your PalmSens instrument using MATLAB.


| | | |
| - | - | - |
| ![Measurement]("./docs/modules/matlab/images/measurement-gui.webp)| ![Import measurement](./docs/modules/matlab/images/import-measurement.webp.webp) | ![Equivalent circuit fitting](./docs/modules/matlab/images/equivalent-circuit-fitting.webp) |
| **Control your PalmSens instrument using MATLAB** | **Import experimental results from PSTrace directly into MATLAB** | **Plot results in Nyquist and Bode plot** |

## Installation

To use the matlab SDK, download the latest https://github.com/palmsens/palmsens_sdk/releases[release here].
Unzip and load the directory in Matlab.

## Examples

The SDK contains the following examples and functions aimed to help you with using PalmSens and Emstat devices in Matlab.

`ConnnectionExample.m`
: Detailed explanation on how to detect and connect to your device.

`MethodExample.m`
: Detailed explanation on how to load, edit and create new methods (methods are used to specify technique and the settings for a measurment).

`ImportSessionExample.m`
: Detailed explanation on how to import and view measurements from a `.pssession` file created with PSTrace 5.x or MultiTrace 4.x.

`MeasurementExample.m`
: Detailed explanation on how to perform a measurement, specified in a method, with a connected PalmSens or Emstat device.

`EquivalentCircuitFitExample.m`
: An example of equivalent circuit fitting

`GUIExample.m`
: An example of a Matlab user interface for performing measurements with your device.

`ManualControlExample.m`
: An example of a Maltab user interface for manual control of your device.

`MultiChannelMeasurementLoopExample.m`
: An example of connecting to and running measurements on multiple instruments/channels.

## Functions

`LoadPSSDK.m`
: Loads the PalmSens Matlab SDK.

`LoadMethod.m`
: Loads a method from a *.psmethod file.

`NewMethod.m`
: Creates a new method.

`SaveMethod.m`
: Saves a method.

`LoadSession.m`
: Load (a) measurement(s) from a *.pssession file.

`GetConnectedDevices.m`
: Returns a list of connected PalmSens and Emstat devices.

`OpenConnection.m`
: Opens a connection to a device.

`MultiChannelMeasurementLoopHelper.m`
: Waits for multiple instruments to finish their measurements


## Classes

`Measurement.m`
: Returns data measured by a device as a variable, message in the command window and/or a plot in a figure.
`MeasurementGUI.m`

: Version of the Measurement.m class that can be used with a Matlab GUIDE user interface.
`MultiChannelMeasurement.m`

: Used for running when connected to multiple instruments simultaneaously, please refer to the `MultiChannelMeasurementLoopExample`

`EquivalentCircuitFit.m`
: Handles the equivalent circuit fitting using the PalmSens.Core.Matlab.dll
