# Examples

The following examples are also available in the [examples directory](https://github.com/PalmSens/PalmSens_SDK/tree/main/python).

## Load and save data

This example shows how to load/save methods and measurements and how to inspect the data.

```python title="load_save_data.py"
--8<-- "examples/load_save_data.py"
```

[:fontawesome-solid-download: load_save_data.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/load_save_data.py){ .md-button .md-button--primary} [:fontawesome-solid-download: Demo CV DPV EIS.pssession](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/Demo CV DPV EIS IS-C electrode.pssession){ .md-button } [:fontawesome-solid-download: LSV.psmethod](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/PSDummyCell_LSV.psmethod){ .md-button }

## Manual control

This example shows how to discover devices, establish a connection and control an instrument manually.

```python title="manual_control.py"
--8<-- "examples/manual_control.py"
```

[:fontawesome-solid-download: manual_control.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/manual_control.py){ .md-button .md-button--primary}

## Manual control async

This example shows how to discover devices, establish a connection and control an instrument manually using the asynchronous instrument manager.

```python title="manual_control_async.py"
--8<-- "examples/manual_control_async.py"
```

[:fontawesome-solid-download: manual_control_async.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/manual_control_async.py){ .md-button .md-button--primary}

## Measure CA

This example shows how to set up and run a chronoamperometry measurement.

```python title="measurement_CA.py"
--8<-- "examples/measurement_CA.py"
```

[:fontawesome-solid-download: measurement_CA.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/measurement_CA.py){ .md-button .md-button--primary}

## Measure CA async

This example shows how to set up and run a chronoamperometry measurement using the asynchronous instrument manager.

```python title="measurement_CA_async.py"
--8<-- "examples/measurement_CA_async.py"
```

[:fontawesome-solid-download: measurement_CA_async.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/measurement_CA_async.py){ .md-button .md-button--primary}

## Measure CV

This example shows how to set up and run a cyclic voltammetry measurement.

```python title="measurement_CV.py"
--8<-- "examples/measurement_CV.py"
```

[:fontawesome-solid-download: measurement_CV.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/measurement_CV.py){ .md-button .md-button--primary}

## Measure EIS

This example shows how to set up and run a EIS measurement.

```python title="measurement_EIS.py"
--8<-- "examples/measurement_EIS.py"
```

[:fontawesome-solid-download: measurement_EIS.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/measurement_EIS.py){ .md-button .md-button--primary}

## Mixed Mode

This example shows how to set up a Mixed Mode measurement for a typicial charge / discharge cycle of a common Lithium battery.
Note that the example has a reduced number of cycles and maximum run time.

```python title="mixed_mode.py"
--8<-- "examples/mixed_mode.py"
```

[:fontawesome-solid-download: mixed_mode.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/mixed_mode.py){ .md-button .md-button--primary}

## MethodSCRIPT sandbox

This example shows how to set up and run a MethodSCRIPT Sandbox measurement.

```python title="measurement_MethodSCRIPT_sandbox.py"
--8<-- "examples/measurement_MethodSCRIPT_sandbox.py"
```

[:fontawesome-solid-download: pdownload.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/load_save_data.measurement_MethodSCRIPT_sandbox.pdownload"){ .md-button .md-button--primary}

## Status callback

This example shows how to set up a callback to read out the idle status updates (current/potential) and store the pretreatment data.

```python title="measurement_status_callback.py"
--8<-- "examples/measurement_status_callback.py"
```

[:fontawesome-solid-download: measurement_status_callback.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/measurement_status_callback.py){ .md-button .md-button--primary}

## Stream data to CSV

This example shows how to set up and run a chronoamperometry measurement and write the results to a CSV file in real-time.

```python title="measurement_stream_to_csv.py"
--8<-- "examples/measurement_stream_to_csv.py"
```

[:fontawesome-solid-download: measurement_stream_to_csv.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/measurement_stream_to_csv.py){ .md-button .md-button--primary}

## SWV versus OCP

This example shows how to set up and run a square wave voltammetry measurement versus OCP.

```python title="measurement_SWV_vs_OCP.py"
--8<-- "examples/measurement_SWV_vs_OCP.py"
```

[:fontawesome-solid-download: measurement_SWV_vs_OCP.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/measurement_SWV_vs_OCP.py){ .md-button .md-button--primary}

## Multiplexer

This example shows how to set up and control a multiplexer and run consecutive and alternating multiplexer measurments.

```python title="multiplexer.py"
--8<-- "examples/multiplexer.py"
```

[:fontawesome-solid-download: multiplexer.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/multiplexer.py){ .md-button .md-button--primary}

## Multichannel measurement   { #multichannel_basic }

This example shows how to connect to a collection of instruments and run a chronoamperometry measurement on all channels simultaneously.

```python title="multichannel_measurement.py"
--8<-- "examples/multichannel_measurement.py"
```

[:fontawesome-solid-download: multichannel_measurement.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/multichannel_measurement.py){ .md-button .md-button--primary}

## Multichannel CSV writer  { #multichannel_csv_writer }

This example shows how to connect to a how to use a callback to automatically store data to a csv file while collecting data from collection of instruments.

```python title="multichannel_csv_callback.py"
--8<-- "examples/multichannel_csv_callback.py"
```

[:fontawesome-solid-download: multichannel_csv_callback.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/multichannel_csv_callback.py){ .md-button .md-button--primary}

## Multichannel custom loop  { #multichannel_custom_loop }

This example shows how to run and set up a sequence of measurements on a collection of channels simultaneously.

```python title="multichannel_custom_loop.py"
--8<-- "examples/multichannel_custom_loop.py"
```

[:fontawesome-solid-download: multichannel_custom_loop.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/multichannel_custom_loop.py){ .md-button .md-button--primary}

## Multichannel HW sync  { #multichannel_hw_sync }

On multi-channel devices that support it, hardware sync can be used to synchronize measurements between multiple channels.
When synchronization is enabled the follower device will wait until the main channel enables synchronisation.
After that, the follower and main will synchronize their measurement loop start and iterations.

This example shows how to connect to a collection of instruments and run a chronopotentiometry measurement on all channels simultaneously using hardware synchronization.

For hardware synchronization, you set `use_hardware_sync = True` on the method.
This is the equivalent of `set_channel_sync 1` in MethodSCRIPT.
At the moment this only works with async.

In addition, your pool of instruments must contain:

* channels from a single [multi-channel instrument](https://www.palmsens.com/knowledgebase-article/multichannel-potentiostat/)
* the first (main) channel of the instrument
* at least one follower channel

All instruments are prepared and put in a waiting state.
The measurements are started via a hardware sync trigger on channel 1.
Only channel 1 (the main channel) has hardware required to trigger the other channels.

```python title="multichannel_HW_sync.py"
--8<-- "examples/multichannel_HW_sync.py"
```

[:fontawesome-solid-download: multichannel_HW_sync.py](https://raw.githubusercontent.com/PalmSens/PalmSens_SDK/refs/heads/main/python/examples/multichannel_HW_sync.py){ .md-button .md-button--primary}
