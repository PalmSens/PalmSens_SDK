# Techniques

This section contains a listing of all available techniques in PyPalmSens.

For example to set up a CV experiment:

```python
>>> import pypalmsens as ps

>>> method = ps.CyclicVoltammetry(
...     begin_potential = -1,
...     vertex1_potential = -1,
...     vertex2_potential = 1,
...     step_potential = 0.25,
...     scanrate = 5,
...     n_scans = 2,
...     current_range = {
...         'max': '1mA',
...         'min': '100nA',
...         'start': '100uA',
...     },
... )
```

!!! note "Shared settings"

    Many configuration settings are shared between methods, like the current ranges above
    or _versus OCP_ or _trigger_ settings. These are listed in [Settings](./settings.md).


| Method | class | ID |
|-|-|-|
| **Voltammetric Techniques**-->
| Linear Sweep Voltammetry | [pypalmsens.LinearSweepVoltammetry][] | `'lsv'` |
| Cyclic Voltammetry | [pypalmsens.CyclicVoltammetry][] | `'cv'` |
| Fast Cyclic Voltammetry | [pypalmsens.FastCyclicVoltammetry][] | `'fcv'` |
| AC Voltammetry | [pypalmsens.ACVoltammetry][] | `'acv'` |
| **Pulsed Techniques**-->
| Differential Pulse Voltammetry | [pypalmsens.DifferentialPulseVoltammetry][] | `'dpv'` |
| Square Wave Voltammetry | [pypalmsens.SquareWaveVoltammetry][] | `'swv'` |
| Normal Pulse Voltammetry | [pypalmsens.NormalPulseVoltammetry][] | `'npv'` |
| **Amperometric Techniques**-->
| Chronoamperometry | [pypalmsens.ChronoAmperometry][] | `'ca'` |
| Multistep Amperometry | [pypalmsens.MultiStepAmperometry][] | `'msa'` |
| Fast Amperometry | [pypalmsens.FastAmperometry][] | `'fam'` |
| Pulsed Amperometric Detection | [pypalmsens.PulsedAmperometricDetection][] | `'pad'` |
| Multiple Pulse Amperometry | [pypalmsens.MultiplePulseAmperometry][] | `'mpa'` |
| **Potentiometric Techniques**-->
| Open Circuit Potentiometry | [pypalmsens.OpenCircuitPotentiometry][] | `'ocp'` |
| Chronopotentiometry | [pypalmsens.ChronoPotentiometry][] | `'cp'` |
| Linear Sweep Potentiometry | [pypalmsens.LinearSweepPotentiometry][] | `'lsp'` |
| Multistep Potentiometry | [pypalmsens.MultiStepPotentiometry][] | `'msp'` |
| Stripping Chronopotentiometry | [pypalmsens.StrippingChronoPotentiometry][] | `'scp'` |
| **Coulometric techniques**-->
| Chronocoulometry | [pypalmsens.ChronoCoulometry][] | `'cc'` |
| **Other**-->
| Impedance Spectroscopy | [pypalmsens.ElectrochemicalImpedanceSpectroscopy][] | `'eis'` |
| Fast Impedance Spectroscopy | [pypalmsens.FastImpedanceSpectroscopy][] | `'fis'` |
| Galvanostatic Impedance Spectroscopy | [pypalmsens.GalvanostaticImpedanceSpectroscopy][] | `'gis'` |
| Fast Galvanostatic Impedance Spectroscopy | [pypalmsens.FastGalvanostaticImpedanceSpectroscopy][] | `'fgis'` |
| Mixed Mode | [pypalmsens.MixedMode] | `'mm'` |
| Method Script | [pypalmsens.MethodScript][] | `'ms'` |

| [Stages | [pypalmsens.stages][]
