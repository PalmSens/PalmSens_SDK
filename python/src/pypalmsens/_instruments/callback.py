from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

from typing_extensions import override

from .._data.data_array import DataArray
from .._data.dataset import DataSet


@dataclass(slots=True)
class CallbackData:
    x_array: DataArray
    """Data array for the x variable."""

    y_array: DataArray
    """Data array for the y variable."""

    start: int
    """Start index for the new data."""

    @property
    def index(self) -> int:
        """Index of last point."""
        return len(self.x_array) - 1

    def last_datapoint(self) -> dict[str, float]:
        """Return last measured data point."""
        return {
            'index': self.index,
            'x': self.x_array[-1],
            'y': self.y_array[-1],
        }

    def new_datapoints(self) -> dict[str, int | Sequence[float]]:
        """Return new data points since last callback."""
        return {
            'start': self.index,
            'x': self.x_array[self.start :],
            'y': self.y_array[self.start :],
        }

    @override
    def __str__(self):
        return str(self.last_datapoint())


@dataclass(slots=True)
class CallbackDataEIS:
    data: DataSet
    """EIS dataset."""

    start: int
    """Start index for the new data."""

    @property
    def index(self) -> int:
        """Index of last point."""
        return self.data.n_points - 1

    def last_datapoint(self) -> dict[str, float]:
        """Return last measured data point."""
        ret = {array.name: array[-1] for array in self.data.arrays()}
        ret['index'] = self.index
        return ret

    def new_datapoints(self) -> dict[str, int | Sequence[float]]:
        """Return new data points since last callback."""
        ret: dict[str, int | Sequence[float]] = {
            array.name: array[self.start :] for array in self.data.arrays()
        }
        ret['start'] = self.start
        return ret

    @override
    def __str__(self):
        return str(self.last_datapoint())


class Callback(Protocol):
    """Type signature for callback."""

    def __call__(self, data: CallbackData | CallbackDataEIS): ...
