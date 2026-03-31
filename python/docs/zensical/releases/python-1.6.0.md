
## PyPalmSens 1.6.0

python-1.6.0 - https://github.com/PalmSens/PalmSens_SDK/releases/tag/python-1.6.0
2026-01-09T15:35:38Z
pip: https://pypi.org/project/pypalmsens-1.6.0'

PyPalmSens 1.6.0 is now available on PyPi.

To upgrade `pip install pypalmsens -U`.

## Measurement callbacks

This release changes how callbacks work. The callback now receives a dataclass, making it easier to integrate into your workflows. If you use callbacks, this may require small changes to your code. See [the documentation](https://sdk.palmsens.com/python/latest/measuring.html#_callback), [the API reference](https://sdk.palmsens.com/python/latest/api/_attachments/data/#pypalmsens.data.CallbackData) or one of [the examples](https://sdk.palmsens.com/python/latest/examples.html) for more information.

```python
>>> def callback(data):
...    print({'start': data.start, 'x': data.x[data.start:], 'y': data.y[data.start:]})

>>> manager.measure(method, callback=callback)
{'start': 0, 'x': [0.00, 0.01, 0.02], 'y': [-305.055, -740.935, -750.604]}
```

## Reading idle status

You can pass register a callback to the instrument manager to get updates from the idle status/current/bipot/aux updates. These are also passed as data classes. You can also use the callback to retrieve data during the pretreatment (conditioning and depositing) phases. See [this example](https://sdk.palmsens.com/python/latest/examples.html#_status_callback) or checkout the [documentation](https://sdk.palmsens.com/python/latest/measuring.html#_idle_status_updates).

```python
>>> import pypalmsens as ps
>>> import asyncio

>>> async def main():
...     async with await ps.connect_async() as manager:
...         manager.register_status_callback(print)
...         await asyncio.sleep(5)
...         manager.unregister_status_callback()

>>> asyncio.run(main())
Idle: {'current': '0.000 * 1uA', 'potential': '0.527 V'}
Idle: {'current': '0.000 * 1uA', 'potential': '0.526 V'}
Idle: {'current': '0.000 * 1uA', 'potential': '0.526 V'}
```

## Fixing Bipot settings

Finally, this release fixes a bug when setting the BiPot, causing the setting not to register. This has been rectified. See [the documentation](https://sdk.palmsens.com/python/latest/api/_attachments/methods/settings/#pypalmsens.settings.BiPot) or #222 for more information.

Note that the syntax for setting the bipot current range has changed, more in line with the rest of the code. Bipot now expects a fixed current range by default, which is the expected setting for almost all devices:

```python
bipot = ps.settings.BiPot(current_range = '1uA')
```

For autoranging bipot (only available on the Nexus), you can use:

```python
bipot = ps.settings.BiPot(
    current_range = {'min': '1uA', 'max': '10mA', 'start': '1mA'},
)
```

## What's Changed

* Return data arrays for callbacks by @stefsmeets in https://github.com/PalmSens/PalmSens_SDK/pull/219
* Implement callback for Idle Status events by @stefsmeets in https://github.com/PalmSens/PalmSens_SDK/pull/223
* Add timing/reading status and current ranges to DataArray by @stefsmeets in https://github.com/PalmSens/PalmSens_SDK/pull/226
* Make bipot configurable for CV and set default to fixed CR by @stefsmeets in https://github.com/PalmSens/PalmSens_SDK/pull/222

**Full Changelog**: https://github.com/PalmSens/PalmSens_SDK/compare/python-1.5.0...python-1.6.0
