# Index

- `pypalmsens`

    The most-used functions and classes are available from the root module.

    - [Saving and loading files](./io.md)
    - [Setting up measurements](./techniques.md)
    - [Connecting to and managing an instrument](./instrument.md)

- `pypalmsens.settings`

    This module additional classes for method configuration (e.g. general settings, current ranges, etc).

- `pypalmsens.fitting`

    Contains classes for equivalent circuit fitting.

- `pypalmsens.data`

    Contains the dataclasses for working with measurement data.

    Although `PyPalmSens` will typically construct these dataclasses for you,
    either when loading a `.pssession` file or after a measurement,
    this page documents the attributes and methods available on these classes.
