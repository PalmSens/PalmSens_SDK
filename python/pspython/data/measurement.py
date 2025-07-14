import PalmSens

from ._shared import ArrayType
from .curve import Curve
from .fit_result import EISFitResult
from .peak import Peak

# print(f'ocp: {measurement.curves[0].dotnet_curve.OCPValue}')
# measurements[0].dotnet_measurement.Method


class Measurement:
    """Python wrapper for dotnet Measurement class."""

    def __init__(self, *, dotnet_measurement):
        self.dotnet_measurement = dotnet_measurement

    def __str__(self):
        return f'{self.__class__.__name__}(title={self.title})'

    @property
    def title(self) -> str:
        """Title for the measurement."""
        return self.dotnet_measurement.Title

    @property
    def timestamp(self) -> str:
        """Date and time of the start of this measurement.."""
        return str(self.dotnet_measurement.TimeStamp)

    @property
    def blank_curve(self) -> Curve:
        """Blank curve.

        if Blank curve is present (not null) a new curve will be added after each measurement
        containing the result of the measured curve subtracted with the Blank curve.
        """
        return self.dotnet_measurement.BlankCurve

    @property
    def contains_blank_subtracted_curves(self) -> bool:
        """Return True if the curve collection contains a blank subtracted curve."""
        return self.dotnet_measurement.ContainsBlankSubtractedCurves

    def contains_eis_data(self) -> bool:
        """Return True if EIS data are is available."""
        return self.dotnet_measurement.ContainsEISData

    def dataset(self) -> ...:
        """Dataset containing multiple arrays of values.

        All values are related by means of their indices.
        Data arrays in a dataset should always have an equal amount of entries.
        """
        _ = self.dotnet_measurement.Dataset
        raise NotImplementedError('Data sets are not implemented')

    def eis_data(self) -> list:
        """EIS data in measurement."""
        _ = self.dotnet_measurement.EISdata
        raise NotImplementedError('Working with EIS data sets is not implemented')

    def get_curve_by_index(self, index: int) -> Curve:
        """Retrieve curve with given index."""
        dotnet_curve = self.dotnet_measurement.Item(index)
        return Curve(dotnet_curve=dotnet_curve)

    def get_curve_by_type(self, meas_type: str) -> Curve:
        """Retrieve curve with given measuremnt type.

        Parameters
        ----------
        meas_type : str
            Possible values: `New`, `Overlay`, `Blank`, `Sample`, `Standard_1`,
            `Standard_2`, `Standard_3`, `Standard_4`

        Returns
        -------
        curve : Curve
        """
        meas_type_dotnet = getattr(PalmSens.MeasType, meas_type)
        dotnet_curve = self.dotnet_measurement.Item(meas_type_dotnet)
        return Curve(dotnet_curve=dotnet_curve)

    def method(self) -> ...:
        """Method related with this Measurement.

        The information from the Method is used when saving Curves."""
        return self.dotnet_measurement.Method

    def ocpvalue(self) -> float:
        """First OCP Value from either curves or EISData."""
        return self.dotnet_measurement.OcpValue

    def n_curves(self) -> int:
        """Number of curves that are part of the Measurement class."""
        return self.dotnet_measurement.nCurves

    def n_eis_data(self) -> int:
        """Number of EISdata curves that are part of the Measurement class."""
        return self.dotnet_measurement.nEISData

    def get_array_by_type(self, array_type: str) -> list:
        enum = ArrayType[array_type]
        return [
            list(array.GetValues())
            for array in self.dotnet_measurement.DataSet.GetDataArrays()
            if ArrayType(array.ArrayType) == enum
        ]

    @property
    def current_arrays(self) -> list:
        # # get the current range the current was measured in
        # currentranges = __getcurrentrangesfromcurrentarray(array)
        # # get the status of the meausured data point
        # currentstatus = __getstatusfromcurrentorpotentialarray(array)
        return self.get_array_by_type('Current')

    @property
    def potential_arrays(self) -> list:
        # # Get the status of the meausured data point
        # potentialStatus = __getstatusfromcurrentorpotentialarray(array)
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

    @property
    def peaks(self) -> list[Peak]:
        """Get peaks from aal curves.

        Returns
        -------
        peaks : list[Peak]
            List of peaks
        """
        peaks = []
        for curve in self.curves:
            peaks.extend(curve.peaks)
        return peaks

    @property
    def eis_fit(self) -> list[EISFitResult]:
        """Get all EIS fits from measurement

        Returns
        -------
        eis_fits : list[EISFitResults]
            Return list of EIS fits
        """
        eisdatas = self.dotnet_measurement.EISdata

        if not eisdatas:
            return []

        eis_fits = []

        for eisdata in eisdatas:
            if not eisdata:
                continue
            eis_fits.append(EISFitResult(eisdata.CDC, eisdata.CDCValues))

        return eis_fits

    @property
    def curves(self) -> list[Curve]:
        """Get all curves in measurement.

        Returns
        -------
        curves : list[Curve]
            List of curves
        """
        curves = self.dotnet_measurement.GetCurveArray()
        return [Curve(dotnet_curve=curve) for curve in curves]
