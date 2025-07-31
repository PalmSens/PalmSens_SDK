from __future__ import annotations

from collections.abc import Mapping
from typing import Callable, Generator

import clr
from PalmSens.Data import CurrentReading

from ._shared import ArrayType
from .data_array import DataArray


class DataSet(Mapping):
    def __init__(self, *, psdataset):
        self.psdataset = psdataset

        arrays = [array for array in psdataset.GetDataArrays()]
        array_names = {array.Description for array in arrays}

        if len(array_names) != len(arrays):
            raise ValueError(f'Data arrays are not unique, {len(array_names)} {len(arrays)}')

    def __repr__(self):
        return f'{self.__class__.__name__}({list(self.keys())})'

    def __getitem__(self, key: str):
        ret = self._filter(key=lambda array: ArrayType(array.ArrayType).name == key)

        if not ret:
            raise KeyError(f'{key}')
        if len(ret) > 1:
            raise KeyError(f'Internal error, got multiple instances for key: {key}')

        return ret[0]

    def __iter__(self) -> Generator[str, None, None]:
        # Note that iterating over self.psdataset also returns the 'hidden' debug arrays
        # `.GetDataArrays()` excludes those.
        for array in self.psarrays():
            yield ArrayType(array.ArrayType).name

    def __len__(self):
        return self.psdataset.Count

    def _filter(self, key: Callable) -> list[DataArray]:
        """Filter array list based on callable.

        Callable takes dotnet DataArray as its only argument.
        """
        return [DataArray(psarray=psarray) for psarray in self.psarrays() if key(psarray)]

    def psarrays(self):
        """Return underlying PalmSens SDK objects."""
        return self.psdataset.GetDataArrays()

    def to_dict(self) -> dict[str, DataArray]:
        """Return arrays as dictionary."""
        return dict(self)

    def to_list(self) -> list[DataArray]:
        """Return list of arrays."""
        return list(self.values())

    def arrays(self) -> list[DataArray]:
        """Return list of all arrays. Alias for `.to_list()`"""
        return self.to_list()

    def hidden_arrays(self) -> list[DataArray]:
        """Return 'hidden' arrays used for debugging."""
        return [DataArray(psarray=psarray) for psarray in self.psdataset if psarray.Hidden]

    def arrays_by_name(self, name: str) -> list[DataArray]:
        """Get arrays by name.

        Parameters
        ----------
        name : str
            Name of the array.

        Returns
        -------
        arrays : list[DataArray]
        """
        return self._filter(key=lambda array: array.Description == name)

    def arrays_by_quantity(self, quantity: str) -> list[DataArray]:
        """Get arrays by quantity.

        Parameters
        ----------
        quantity : str
            Quantity of the array.

        Returns
        -------
        arrays : list[DataArray]
        """
        return self._filter(key=lambda array: array.Unit.Quantity == quantity)

    def arrays_by_type(self, array_type: ArrayType) -> list[DataArray]:
        """Get arrays by data type.

        Parameters
        ----------
        description : str
            Description of the array.

        Returns
        -------
        arrays : list[DataArray]
        """
        return self._filter(key=lambda array: array.ArrayType == array_type.value)

    @property
    def array_types(self) -> set[ArrayType]:
        """Return unique set of array type (enum) for arrays in dataset."""
        return set(array.type for array in self.arrays())

    @property
    def array_names(self) -> set[str]:
        """Return unique set of names for arrays in dataset."""
        return set(array.name for array in self.arrays())

    @property
    def array_quantities(self) -> set[str]:
        """Return unique set of quantities for arrays in dataset."""
        return set(arr.quantity for arr in self.arrays())

    @property
    def current_arrays(self) -> list[DataArray]:
        """Return all Current arrays."""
        return self.arrays_by_type(ArrayType.Current)

    @property
    def potential_arrays(self) -> list[DataArray]:
        """Return all Potential arrays."""
        return self.arrays_by_type(ArrayType.Potential)

    @property
    def time_arrays(self) -> list[DataArray]:
        """Return all Time arrays."""
        return self.arrays_by_type(ArrayType.Time)

    @property
    def freq_arrays(self) -> list[DataArray]:
        """Return all Frequency arrays."""
        return self.arrays_by_type(ArrayType.Frequency)

    @property
    def zre_arrays(self) -> list[DataArray]:
        """Return all ZRe arrays."""
        return self.arrays_by_type(ArrayType.ZRe)

    @property
    def zim_arrays(self) -> list[DataArray]:
        """Return all ZIm arrays."""
        return self.arrays_by_type(ArrayType.ZIm)

    @property
    def aux_input_arrays(self) -> list[DataArray]:
        """Return all AuxInput arrays."""
        return self.arrays_by_type(ArrayType.AuxInput)

    @property
    def current_range(self) -> list[str]:
        """Return current range as list of strings."""
        array = self['Current']

        clr_type = clr.GetClrType(CurrentReading)
        field_info = clr_type.GetField('CurrentRange')

        return [field_info.GetValue(val).ToString() for val in array.psarray]

    def reading_status(self) -> list[str]:
        """Return reading status as list of strings."""
        array = self['Current']

        clr_type = clr.GetClrType(CurrentReading)
        field_info = clr_type.GetField('ReadingStatus')

        return [field_info.GetValue(val).ToString() for val in array.psarray]

    def timing_status(self) -> list[str]:
        """Return timing status as list of strings."""
        array = self['Current']

        clr_type = clr.GetClrType(CurrentReading)
        field_info = clr_type.GetField('TimingStatus')

        return [field_info.GetValue(val).ToString() for val in array.psarray]

    def to_dataframe(self):
        """Return dataset as pandas dataframe."""
        import pandas as pd

        data = self.arrays()

        df = pd.DataFrame({arr.name: arr.to_list() for arr in data if len(arr)})
        df['CR'] = self.current_range
        df['ReadingStatus'] = self.reading_status
        return df
