from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Literal, Optional

from PalmSens import Fitting as PSFitting
from System import Array

from pspython.data.curve import Curve
from pspython.data.eisdata import EISData


class Parameter:
    def __init__(self, psparameter: PSFitting.Parameter) -> None:
        self.psparameter = psparameter

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'value={self.value}, '
            f'min={self.min}, '
            f'max={self.max}, '
            f'fixed={self.fixed})'
        )

    @property
    def value(self) -> float:
        return self.psparameter.Value

    @value.setter
    def value(self, value):
        self.psparameter.Value = value

    @property
    def min(self) -> float:
        return self.psparameter.MinValue

    @min.setter
    def min(self, value):
        self.psparameter.MinValue = value

    @property
    def max(self) -> float:
        return self.psparameter.MaxValue

    @max.setter
    def max(self, value):
        self.psparameter.MaxValue = value

    @property
    def fixed(self) -> bool:
        return self.psparameter.Fixed

    @fixed.setter
    def fixed(self, value):
        self.psparameter.Fixed = value


@dataclass(frozen=True)
class FitResult:
    """
    Attributes
    ----------
    cdc: str
        Circuit model CDC values.
    chisq: float
        Chi-squared goodness of fit statistic.
    exit_code: str
        Exit code for the minimization.
    n_iterations: int
        Total number of iterations.
    parameters: list[float]
        Optimized parameters for CDC.
    std: list[float]
        Standard deviations (%) on parameters.
    """

    cdc: str
    chisq: float
    exit_code: str
    n_iter: int
    parameters: list[float]
    std: list[float]

    @classmethod
    def from_psfitresult(cls, result: PSFitting.FitResult, **kwargs):
        return cls(
            chisq=result.ChiSq,
            exit_code=result.ExitCode.ToString(),
            n_iter=result.NIterations - 1,
            parameters=list(result.FinalParameters),
            std=list(result.ParameterSDs),
            **kwargs,
        )


@dataclass
class CircuitModel:
    """

    Attributes
    ----------
    cdc: str
    algorithm: str
        Name of the fitting method to use. Valid values are:
            'leastsq' (Levenberg-Marquardt), 'nelder-mead'
    max_iterations: int
        ... (default = 500).
    min_error: float
        ... (default = 1e-9).
    min_step_size: float
        ... (default = 1e-12).
    min_hz: float
        Minimum fitting frequency in Hz (default = None).
    max_hz: float
        Maximum fitting frequency in Hz (default = None).
    tolerance: float
        Nelder-Mead only (default = 1e-4).
    lambda_start_value: float
        Levenberg-Marquardt only (default = 0.01).
    lambda_scale_factor: float
        Levenberg-Marquardt only (default = 10.00).
    """

    cdc: str
    algorithm: Literal['leastsq', 'nelder-mead'] = 'leastsq'
    max_iterations: int = 500
    min_delta_error: float = 1.0e-9
    min_delta_step: float = 1.0e-12
    min_freq: Optional[float] = None
    max_freq: Optional[float] = None
    tolerance: float = 1e-4
    lambda_start: float = 0.01
    lambda_factor: float = 10.00

    _last_result: Optional[FitResult] = None
    _last_psfitter: Optional[PSFitting.FitAlgorithm] = None

    def __post_init__(self):
        self.model = PSFitting.Models.CircuitModel()
        self.model.SetCircuit(self.cdc)

    @property
    def parameters(self) -> MappingProxyType:
        """Proxy to parameters. Use this to modify parameter values."""
        psmodel = PSFitting.Models.CircuitModel()
        psmodel.SetCircuit(self.cdc)

        return MappingProxyType(
            {
                psparam.Name: Parameter(psparameter=psparam)
                for psparam in self.model.InitialParameters
            }
        )

    def psfitoptions(self, data: EISData) -> PSFitting.FitOptions:
        """Fit circuit model.

        Parameters
        ----------
        data : EISData
            Input data.
        """
        model = self.model  # TODO: can we make a copy of this?
        model.SetEISdata(data.pseis)

        opts = PSFitting.FitOptionsCircuit()
        opts.Model = model
        opts.RawData = data.pseis

        opts.MaxIterations = self.max_iterations
        opts.MinimumDeltaErrorTerm = self.min_delta_error
        opts.MinimumDeltaParameters = self.min_delta_step

        if self.min_freq or self.max_freq:
            self.min_freq = self.min_freq or 0
            self.max_freq = self.max_freq or 0

            array = data.dataset.freq_arrays[-1]
            sel = (self.min_freq < val < self.max_freq for val in array)

            opts.SelectedDataPoints = Array[bool]((bool(_) for _ in sel))

        return opts

    @property
    def last_result(self):
        return self._last_result

    @property
    def last_psfitter(self):
        return self._last_psfitter

    def fit(self, data: EISData) -> FitResult:
        """Fit circuit model.

        Parameters
        ----------
        data : EISData
            Input data.
        """
        if not data.frequency_type == 'Scan':
            raise ValueError(
                f'Fit only supports EIS scans at a fixed potential, got {data.frequency_type=}.'
            )
        if not data.scan_type == 'Fixed':
            raise ValueError(
                f'Fit only supports EIS scans at a fixed potential, got {data.scan_type=}.'
            )

        opts = self.psfitoptions(data=data)

        fitter = PSFitting.FitAlgorithm.FromAlgorithm(opts)
        fitter.ApplyFitCircuit()
        self._last_psfitter = fitter
        self._last_result = FitResult.from_psfitresult(fitter.FitResult, cdc=self.cdc)
        return self._last_result

    def get_fitted_curves(self, data: EISData, result: FitResult):
        """This probably better fits as a method on on EISData:

        ```
        def eisdata.plot(self, fitresult=Optional[fitresult]=None):
        if fitresult:
            ...

        Alternatively, the plot code itself can be on fitresult.
        ```


        """
        curves = []

        modelFit = PSFitting.Models.CircuitModel()
        modelFit.SetEISdata(data.pseis)
        modelFit.SetCircuit(result.cdc)
        modelFit.SetInitialParameters(result.parameters)

        nyquist = modelFit.GetNyquist()
        calc, obs = (Curve(pscurve=pscurve) for pscurve in nyquist)
        curves.append(calc)

        zvsFreq = modelFit.GetCurveZabsOverFrequency(True)
        calc, obs = (Curve(pscurve=pscurve) for pscurve in zvsFreq)
        curves.append(calc)

        phasevsFreq = modelFit.GetCurvePhaseOverFrequency(True)
        calc, obs = (Curve(pscurve=pscurve) for pscurve in phasevsFreq)
        curves.append(calc)

        return curves
