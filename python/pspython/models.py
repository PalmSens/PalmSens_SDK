from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

from PalmSens import Fitting as PSFitting
from System import Array

from pspython.data.eisdata import EISData


@dataclass(frozen=True)
class FitResult:
    """
    Attributes
    ----------
    chisq: float
        Chi-squared goodness of fit statistic.
    exit_code: str
        Exit code for the minimization.
    n_iterations: int
        Total number of iterations.
    parameters: list[float]
        Optimized parameters for CDC.
    std: list[float]
        Standard deviations on parameters.
    """

    chisq: float
    exit_code: str
    n_iter: int
    parameters: list[float]
    std: list[float]

    @classmethod
    def from_psfitresult(cls, result: PSFitting.FitResult):
        return cls(
            chisq=result.ChiSq,
            exit_code=result.ExitCode.ToString(),
            n_iter=result.NIterations - 1,
            parameters=list(result.FinalParameters),
            std=list(result.ParameterSDs),
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

    def psmodel(self, data: EISData) -> PSFitting.Models.CircuitModel:
        model = PSFitting.Models.CircuitModel()
        model.SetEISdata(data.pseis)
        model.SetCircuit(self.cdc)

        return model

    def psfitoptions(
        self,
        data: EISData,
        *,
        guess: Optional[list[float]] = None,
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

        # model.fit(eis_data, guess=[(random.random()-0.5)*100000000 for x in range(3)])

        if guess:
            if len(guess) != model.NParameters:
                raise ValueError(f'Initial guess must be of length {model.NParameters}')
            model.SetInitialParameters(guess)

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

    def fit(
        self,
        data: EISData,
        *,
        guess: Optional[list[float]] = None,
    ) -> FitResult:
        """Fit circuit model.

        Parameters
        ----------
        data : EISData
            Input data.
        guess : list[float]
            Optional initial guess for starting parameters for minimization.
        """
        if not data.frequency_type == 'Scan':
            raise ValueError(
                f'Fit only supports EIS scans at a fixed potential, got {data.frequency_type=}.'
            )
        if not data.scan_type == 'Fixed':
            raise ValueError(
                f'Fit only supports EIS scans at a fixed potential, got {data.scan_type=}.'
            )

        opts = self.psfitoptions(data=data, guess=guess)

        fitter = PSFitting.FitAlgorithm.FromAlgorithm(opts)
        fitter.ApplyFitCircuit()
        self._last_psfitter = fitter
        self._last_result = FitResult.from_psfitresult(fitter.FitResult)
        return self._last_result

    def get_fitted_curves(self):
        pass
        # modelFit = PalmSens.Fitting.Models.CircuitModel();
        # modelFit.SetEISdata(self.EISData);
        # modelFit.SetCircuit(System.String(self.CDC));
        # modelFit.SetInitialParameters(fitParamters);

        # %Nyquist curve
        # nyquist = modelFit.GetNyquist();
        # nyquist = nyquist(1);
        # ZRe = nyquist.XAxisDataArray;
        # ZIm = nyquist.YAxisDataArray;
        # curves(1).xUnit = ['ZRe(' char(ZRe.Unit.ToString()) ')'];
        # curves(1).xData = double(ZRe.GetValues());
        # curves(1).yUnit = ['ZIm(' char(ZIm.Unit.ToString()) ')'];
        # curves(1).yData = double(ZIm.GetValues());

        # %Bode curves
        # %Impedance over Frequency
        # zvsFreq = modelFit.GetCurveZabsOverFrequency(false);
        # zvsFreq = zvsFreq(1);
        # Frequency = zvsFreq.XAxisDataArray;
        # Zabs = zvsFreq.YAxisDataArray;
        # curves(2).xUnit = ['Frequency(' char(Frequency.Unit.ToString()) ')'];
        # curves(2).xData = double(Frequency.GetValues());
        # curves(2).yUnit = ['Z(' char(Zabs.Unit.ToString()) ')'];
        # curves(2).yData = double(Zabs.GetValues());

        # %-Phase over Frequency
        # phasevsFreq = modelFit.GetCurvePhaseOverFrequency(false);
        # phasevsFreq = phasevsFreq(1);
        # Phase = phasevsFreq.YAxisDataArray;
        # curves(3).xUnit = ['Frequency(' char(Frequency.Unit.ToString()) ')'];
        # curves(3).xData = double(Frequency.GetValues());
        # curves(3).yUnit = ['-Phase(' char(Phase.Unit.ToString()) ')'];
        # curves(3).yData = -1 .* double(Phase.GetValues());
