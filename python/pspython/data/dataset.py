from typing import Union

from ._shared import ArrayType
from .data_array import DataArray


class DataSet:
    def __init__(self, *, dotnet_dataset):
        self.dotnet_dataset = dotnet_dataset

    def get_array_by_type(
        self, array_type: Union[str, ArrayType], index: int = 0
    ) -> list[DataArray]:
        """Get array by its data type.

        Parameters
        ----------
        description : str
            Description of the array.

        Returns
        -------
        arrays : list[DataArray]
        """
        if isinstance(array_type, str):
            array_type = ArrayType[array_type]

        return [
            DataArray(dotnet_data_array=dotnet_data_array)
            for dotnet_data_array in self.dotnet_dataset
            if dotnet_data_array.ArrayType == array_type.value
        ]

    def get_array_by_description(self, description: str) -> list[DataArray]:
        """Get arrays by description.

        Parameters
        ----------
        description : str
            Description of the array.

        Returns
        -------
        arrays : list[DataArray]
        """
        return [
            DataArray(dotnet_data_array=dotnet_data_array)
            for dotnet_data_array in self.dotnet_dataset
            if dotnet_data_array.Description == description
        ]

    def list_array_types(self):
        """Return array type (enum) for arrays in dataset."""
        return [ArrayType(arr.ArrayType) for arr in self.dotnet_dataset]

    def list_array_names(self):
        """Return names for array in dataset."""
        return [arr.Description for arr in self.dotnet_dataset]

    @property
    def current_arrays(self) -> list:
        return self.get_array_by_type('Current')

    @property
    def potential_arrays(self) -> list:
        return self.get_array_by_type('Potential')

    @property
    def time_arrays(self) -> list:
        return self.get_array_by_type('Time')

    @property
    def freq_arrays(self) -> list:
        return self.get_array_by_type('Frequency')

    @property
    def zre_arrays(self) -> list:
        return self.get_array_by_type('ZRe')

    @property
    def zim_arrays(self) -> list:
        return self.get_array_by_type('ZIm')

    @property
    def aux_input_arrays(self) -> list:
        return self.get_array_by_type('AuxInput')
