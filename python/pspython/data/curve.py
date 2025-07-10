from typing import Optional

from .peak import Peak


class Curve:
    def __init__(self, *, dotnet_curve):
        self.dotnet_curve = dotnet_curve

    def __str__(self):
        return f'{self.__class__.__name__}(n_points={self.n_points})'

    def smooth(self, smooth_level: int):
        """Smooth the .y_array using a Savitsky-Golay filter with the specified smooth
        level.

        Parameters
        ----------
        smooth_level : int
            The smooth level to be used. -1 = none, 0 = no smooth (spike rejection only),
            1 = 5 points, 2 = 9 points, 3 = 15 points, 4 = 25 points
        """
        success = self.dotnet_curve.Smooth(smoothLevel=smooth_level)
        assert success

    def savitsky_golay(self, window_size: int):
        """Smooth the .y_array using a Savitsky-Golay filter with the specified window
        size.

        (i.e. window size 2 will filter points based on the values of the next/previous 2 points)

        Parameters
        ----------
        window_size : int
            Size of the window
        """
        success = self.dotnet_curve.Smooth(windowSize=window_size)
        assert success

    def find_peaks(
        self,
        min_peak_width: float,
        min_peak_height: float,
        peak_shoulders: bool = False,
        merge_overlapping_peaks: bool = True,
    ) -> list[Peak]:
        """
        Find peaks in a curve in all directions; CV can have 1 or 2 direction changes

        Parameters
        ----------
        min_peak_width : float
            Minimum width of the peak in V
        min_peak_height : float
            Minimum height of the peak in uA
        peak_shoulders : bool, optional
            ...
        merge_overlapping_peaks : bool, optional
            ...

        Returns
        -------
        peak_list : list[Peak]
        """
        dotnet_peaks = self.dotnet_curve.FindPeaks(
            minPeakWidth=min_peak_width,
            minPeakHeight=min_peak_height,
            peakShoulders=peak_shoulders,
            mergeOverlappingPeaks=merge_overlapping_peaks,
        )

        peaks_list = [Peak(dotnet_peak=peak) for peak in dotnet_peaks]

        return peaks_list

    @property
    def max_x(self) -> float:
        return self.dotnet_curve.MaxX

    @property
    def max_y(self) -> float:
        return self.dotnet_curve.MaxY

    @property
    def min_x(self) -> float:
        return self.dotnet_curve.MinX

    @property
    def min_y(self) -> float:
        return self.dotnet_curve.MinY

    @property
    def mux_channel(self) -> int:
        return self.dotnet_curve.MuxChannel

    @property
    def n_points(self) -> str:
        return self.dotnet_curve.NPoints

    __len__ = n_points

    @property
    def referenc_eelectrode_name(self) -> str:
        return self.dotnet_curve.ReferenceElectrodeName

    @property
    def reference_electrode_potential(self) -> str:
        return self.dotnet_curve.ReferenceElectrodePotential

    @property
    def x_unit(self) -> str:
        return self.dotnet_curve.XUnit

    @property
    def y_unit(self) -> str:
        return self.dotnet_curve.YUnit

    @property
    def z_unit(self) -> str:
        return self.dotnet_curve.ZUnit

    @property
    def title(self) -> str:
        return self.dotnet_curve.Title

    @title.setter
    def title(self, title: str):
        self.dotnet_curve.Title = title

    @property
    def peaks(self) -> list[Peak]:
        return [Peak(dotnet_peak=peak) for peak in self.dotnet_curve.Peaks]

    def clear_peaks(self):
        self.dotnet_curve.ClearPeaks()

    @property
    def x_array(self) -> list[float]:
        return list(self.dotnet_curve.GetXValues())

    @property
    def y_array(self) -> list[float]:
        return list(self.dotnet_curve.GetYValues())

    def linear_slope(
        self, start: Optional[int] = None, stop: Optional[int] = None
    ) -> tuple[float, float, float]:
        """Calculate linear line parameters for this curve between two indexes.

        current = a + b * x

        Parameters
        ----------
        from : int, optional
            begin index
        to : int, optional
            end index

        Returns
        -------
        a : float
        b : float
        coefdet : float
            Coefficient of determination (R2)
        """
        if start and stop:
            return self.dotnet_curve.LLS(start, stop)
        else:
            return self.dotnet_curve.LLS()

    # FindLevels
    # ClearLevels
    # Levels
