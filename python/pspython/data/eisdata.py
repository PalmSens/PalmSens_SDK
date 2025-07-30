from __future__ import annotations

from .dataset import DataSet


class EISData:
    def __init__(self, *, pseis):
        self.pseis = pseis

    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title!r})'

    @property
    def title(self) -> str:
        return self.pseis.Title

    @property
    def dataset(self) -> DataSet:
        """Dataset containing multiple arrays of values.

        All values are related by means of their indices.
        Data arrays in a dataset should always have an equal amount of entries.
        """
        return DataSet(psdataset=self.pseis.EISDataSet)

    @property
    def subscans(self) -> list[EISData]:
        return [EISData(pseis=subscan) for subscan in self.pseis.GetSubScans()]

    def n_points(self) -> int:
        return self.pseis.NPoints

    def n_frequencies(self) -> int:
        return self.pseis.NFrequencies


"""
CDC None
CDCValues System.Double[]
EISDataSet PalmSens.Data.DataSetEIS
EISValueType <class 'PalmSens.Plottables.EISValueType'>
FreqType Scan
FrequencyCurves None
GetAllEISDatas <bound method 'GetAllEISDatas'>
GetCurrentRange <bound method 'GetCurrentRange'>
GetDataArrayVsX <bound method 'GetDataArrayVsX'>
GetDataValue <bound method 'GetDataValue'>
GetDebugValue <bound method 'GetDebugValue'>
GetFreqScanSelectedSeries <bound method 'GetFreqScanSelectedSeries'>
GetIQRValues <bound method 'GetIQRValues'>
GetNPoints <bound method 'GetNPoints'>
GetPotentialRange <bound method 'GetPotentialRange'>
GetScanTypeString <bound method 'GetScanTypeString'>
GetSubScans <bound method 'GetSubScans'>
GetType <bound method 'GetType'>
HasSubScans True
MuxChannel -1
NFrequencies 89
NPoints 801
OCPValue 0.0005855560302734375
ScanType PGScan
SecondaryPlotMode None
Title CH 3: PGScan at 89 freqs [6]
ToString <bound method 'ToString'>
XUnit V
"""
