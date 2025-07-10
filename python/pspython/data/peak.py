from typing import Self


class Peak:
    def __init__(
        self,
        *,
        peak_height: float,
        peak_x: float,
        curve_title: str,
    ):
        self.curve_title = curve_title
        self.peak_height = peak_height
        self.peak_x = peak_x

    @classmethod
    def from_dotnet(cls, peak) -> Self:
        """Generate Peaks instance from dotnet Curve."""
        return cls(peak_height=peak.PeakValue, peak_x=peak.PeakX, curve_title=peak.Curve.Title)
