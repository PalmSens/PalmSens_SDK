from collections.abc import Mapping
from typing import Callable, Generator

from ._shared import ArrayType
from .data_array import DataArray


class DataSet(Mapping):
    def __init__(self, *, dotnet_dataset):
        self.dotnet_dataset = dotnet_dataset

    def __repr__(self):
        return f'{self.__class__.__name__}({list(self.keys())})'

    def __getitem__(self, key: tuple[str, str]):
        if not (isinstance(key, tuple) and len(key) == 2):
            raise KeyError(f'Key must be a tuple with 2 values, got: {key}')
        name, quantity = key

        ret = self._filter(
            key=lambda array: array.Description == name and array.Unit.Quantity == quantity
        )

        if not ret:
            raise KeyError(f'{key}')
        if len(ret) > 1:
            raise KeyError(f'This should not happen, got multiple instances for key: {key}')
        return ret[0]

    def __iter__(self) -> Generator[tuple[str, str], None, None]:
        for array in self.dotnet_dataset:
            yield (array.Description, ArrayType(array.ArrayType).name)

    def __len__(self):
        return self.dotnet_dataset.Count

    def to_list(self) -> list[DataArray]:
        """Return list of arrays."""
        return list(self.values())

    arrays = to_list  # alias

    def _filter(self, key: Callable) -> list[DataArray]:
        """Filter array list based on callable.

        Callable takes dotnet DataArray as its only argument.
        """
        return [
            DataArray(dotnet_data_array=dotnet_data_array)
            for dotnet_data_array in self.dotnet_dataset
            if key(dotnet_data_array)
        ]

    def get_array_by_name(self, description: str) -> list[DataArray]:
        """Get arrays by description.

        Parameters
        ----------
        description : str
            Description of the array.

        Returns
        -------
        arrays : list[DataArray]
        """
        return self._filter(key=lambda array: array.Description == description)

    def get_array_by_quantity(self, quantity: str) -> list[DataArray]:
        """Get array by its quantity.

        Parameters
        ----------
        quantity : str
            Quantity of the array.

        Returns
        -------
        arrays : list[DataArray]
        """
        return self._filter(key=lambda array: array.Unit.Quantity == quantity)

    def get_array_by_type(self, array_type: ArrayType) -> list[DataArray]:
        """Get array by its data type.

        Parameters
        ----------
        description : str
            Description of the array.

        Returns
        -------
        arrays : list[DataArray]
        """
        return self._filter(key=lambda array: array.ArrayType == array_type.value)

    def list_array_types(self) -> list[ArrayType]:
        """Return array type (enum) for arrays in dataset."""
        return [ArrayType(arr.ArrayType) for arr in self.dotnet_dataset]

    def list_array_names(self) -> list[str]:
        """Return names for arrays in dataset."""
        return [arr.Description for arr in self.dotnet_dataset]

    def list_array_quantities(self) -> list[str]:
        """Return quantities for arrays in dataset."""
        return [arr.Unit.Quantity for arr in self.dotnet_dataset]

    @property
    def current_arrays(self) -> list[DataArray]:
        """Return all Current arrays."""
        return self.get_array_by_type(ArrayType.Current)

    @property
    def potential_arrays(self) -> list[DataArray]:
        """Return all Potential arrays."""
        return self.get_array_by_type(ArrayType.Potential)

    @property
    def time_arrays(self) -> list[DataArray]:
        """Return all Time arrays."""
        return self.get_array_by_type(ArrayType.Time)

    @property
    def freq_arrays(self) -> list[DataArray]:
        """Return all Frequency arrays."""
        return self.get_array_by_type(ArrayType.Frequency)

    @property
    def zre_arrays(self) -> list[DataArray]:
        """Return all ZRe arrays."""
        return self.get_array_by_type(ArrayType.ZRe)

    @property
    def zim_arrays(self) -> list[DataArray]:
        """Return all ZIm arrays."""
        return self.get_array_by_type(ArrayType.ZIm)

    @property
    def aux_input_arrays(self) -> list[DataArray]:
        """Return all AuxInput arrays."""
        return self.get_array_by_type(ArrayType.AuxInput)

    def to_dict(self) -> dict[tuple[str, str], DataArray]:
        """Return DataSet as dictionary."""
        return dict(self)
