from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal, Optional

from PalmSens import Fitting as PSFitting
from System import Array

from pspython.data.curve import Curve
from pspython.data.eisdata import EISData


@dataclass
class Parameter:
    """Set or update Parameter attributes.

    Attributes
    ----------
    symbol: str
        Name of the parameter (not used in minimization).
    value: float
        Initial value of the parameter."
    min: float
        Minimum (lower bound) for the parameter.
    max:
        Maximum (upper bound) for the parameter.
    fixed:
        If True, fix the value for this parameter.
    """

    symbol: str
    value: Optional[float] = None
    min: Optional[float] = None
    max: Optional[float] = None
    fixed: Optional[bool] = None

    @classmethod
    def from_psparameter(cls, psparameter: PSFitting.Parameter):
        return cls(
            symbol=psparameter.Symbol,
            value=psparameter.Value,
            min=psparameter.MinValue,
            max=psparameter.MaxValue,
            fixed=psparameter.Fixed,
        )

    def update_psparameter(self, psparameter: PSFitting.Parameter):
        if self.value:
            psparameter.Value = self.value
        if self.min:
            psparameter.MinValue = self.min
        if self.max:
            psparameter.MaxValue = self.max
        if self.fixed:
            psparameter.Fixed = self.fixed


class Parameters(Sequence):
    def __init__(self, cdc: str):
        self.cdc = cdc
        model = PSFitting.Models.CircuitModel()
        model.SetCircuit(cdc)
        self._parameters = tuple(
            Parameter.from_psparameter(psparam) for psparam in model.InitialParameters
        )

    def __len__(self):
        return len(self._parameters)

    def __getitem__(self, key):
        return self._parameters[key]

    def __repr__(self) -> str:
        return self._parameters.__repr__()

    def __str__(self) -> str:
        return self._parameters.__str__()

    def update_psmodel_parameters(self, psmodel: PSFitting.CircuitModel) -> None:
        # if self.cdc != psmodel.CDC:
        #     raise ValueError(
        #         f'Parameters cdc ({self.cdc}) does not match Model ({psmodel.CDC})'
        #     )

        for param, psparam in zip(self, psmodel.InitialParameters):
            param.update_psparameter(psparam)


@dataclass(frozen=True)
class FitResult:
    """Container for fitting results.

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
    error: list[float]
        Error (%) on parameters.
    """

    cdc: str
    chisq: float
    exit_code: str
    n_iter: int
    parameters: list[float]
    error: list[float]

    @classmethod
    def from_psfitresult(cls, result: PSFitting.FitResult, **kwargs):
        return cls(
            chisq=result.ChiSq,
            exit_code=result.ExitCode.ToString(),
            n_iter=result.NIterations - 1,
            parameters=list(result.FinalParameters),
            error=list(result.ParameterSDs),
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

    def default_parameters(self) -> Parameters:
        """Get default parameters. Use this to modify parameter values."""
        return Parameters(self.cdc)

    def psfitoptions(
        self,
        data: EISData,
        *,
        parameters: Optional[Sequence] = None,
    ) -> PSFitting.FitOptions:
        """Fit circuit model.

        Parameters
        ----------
        data : EISData
            Input data.
        """
        model = PSFitting.Models.CircuitModel()
        model.SetCircuit(self.cdc)
        model.SetEISdata(data.pseis)

        if parameters:
            if len(parameters) != model.NParameters:
                raise ValueError(f'Parameters must be of length {model.NParameters}')

            if isinstance(parameters, Parameters):
                parameters.update_psmodel_parameters(model)
            else:
                model.SetInitialParameters(parameters)

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

    def fit(self, data: EISData, *, parameters: Optional[Sequence] = None) -> FitResult:
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

        opts = self.psfitoptions(data=data, parameters=parameters)

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
