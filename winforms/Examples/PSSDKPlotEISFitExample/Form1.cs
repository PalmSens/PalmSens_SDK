using System;
using System.Drawing;
using System.Windows.Forms;
using PalmSens;
using PalmSens.Comm;
using PalmSens.Core.Simplified.Data;
using PalmSens.Devices;
using PalmSens.Fitting;
using PalmSens.Fitting.Models;
using PalmSens.Techniques;
using PalmSens.Techniques.Impedance;

namespace PSSDKPlotEISFitExample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            InitEISMethod(); //Create the cyclic voltammetry method that defines the measurement parameters
            InitPlot(); //Resets and initiates the plot control
            DiscoverConnectedDevices(); //Populate the connected device combobox control
        }

        /// <summary>
        /// The instance of method class containing the Cyclic Voltammetry parameters
        /// </summary>
        private ImpedimetricMethod _methodEIS;

        /// <summary>
        /// The connected PalmSens & EmStat devices
        /// </summary>
        private Device[] _connectedDevices = new Device[0];

        /// <summary>
        /// The active SimpleMeasurement
        /// </summary>
        private SimpleMeasurement _activeMeasurement = null;

        /// <summary>
        /// The fit result SimpleCurve
        /// </summary>
        private SimpleCurve[] _fitResultCurves = null;

        /// <summary>
        /// The fit progress instance, reports progress of active fit and allows cancellation
        /// </summary>
        private FitProgress _fitProgress = null;

        /// <summary>
        /// The circuit model class defining the model that will be used for the equivalent circuit fit
        /// </summary>
        private CircuitModel _circuitModel = null;

        /// <summary>
        /// Initializes the EIS method.
        /// </summary>
        private void InitEISMethod()
        {
            _methodEIS = new ImpedimetricMethod();
            _methodEIS.EquilibrationTime = 0f; //Equilabrates the cell at the defined potential for 5 seconds before starting the measurement
            _methodEIS.Potential = 0f; //Sets the dc potential
            _methodEIS.Eac = 0.01f; // Sets the ac potential at 10 mV RMS
            _methodEIS.ScanType = enumScanType.Fixed; //Single measurement at fixed frequency
            _methodEIS.FreqType = enumFrequencyType.Scan; //Scan a range of frequencies
            _methodEIS.MaxFrequency = 200000; //Start scan at 200 000 Hz
            _methodEIS.MinFrequency = 100; //End scan at 100 Hz
            _methodEIS.nFrequencies = 50; //Sets number of frequencies in scan to 50

            _methodEIS.Ranging.StartCurrentRange = new CurrentRange(CurrentRanges.cr10mA); //Starts equilabration in the 10mA current range
            _methodEIS.Ranging.MinimumCurrentRange = new CurrentRange(CurrentRanges.cr1uA); //Min current range 1µA
            _methodEIS.Ranging.MaximumCurrentRange = new CurrentRange(CurrentRanges.cr10mA); //Max current range 10mA
        }

        /// <summary>
        /// Initializes the plot control.
        /// </summary>
        private void InitPlot()
        {
            plot.ClearAll(); //Clear all curves and data from plot
            //Set the Axis labels
            plot.XAxisLabel = "Log Frequency (Hz)";
            plot.XAxisType = SDKPlot.AxisType.Logarithmic;
            plot.YAxisLabel = "Log Z (Ω)";
            plot.YAxisType = SDKPlot.AxisType.Logarithmic;
            plot.YAxisSecondaryLabel = "-Phase (°)";
            plot.YAxisSecondaryType = SDKPlot.AxisType.Linear;
            plot.AddData("", new double[0], new double[0]); //Add a empty data array to draw an empty plot
        }

        /// <summary>
        /// Discovers the connected PalmSens & EmStat devices and adds them to the combobox control.
        /// </summary>
        private void DiscoverConnectedDevices()
        {
            cmbDevices.Items.Clear();
            _connectedDevices = psCommSimpleWinForms.ConnectedDevices; //Discover connected devices

            foreach (Device d in _connectedDevices) 
                cmbDevices.Items.Add(d.ToString()); //Add connected devices to control

            int nDevices = cmbDevices.Items.Count;
            cmbDevices.SelectedIndex = nDevices > 0 ? 0 : -1;
            lbConsole.Items.Add($"Found {nDevices} device(s).");

            btnConnect.Enabled = nDevices > 0;
        }

        /// <summary>
        /// Handles the Click event of the btnRefresh control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnRefresh_Click(object sender, EventArgs e)
        {
            DiscoverConnectedDevices(); //Add connected devices to the devices combobox control
        }

        /// <summary>
        /// Handles the Click event of the btnConnect control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnConnect_Click(object sender, EventArgs e)
        {
            if (!psCommSimpleWinForms.Connected) //Determine whether a device is currently connected
            {
                if (cmbDevices.SelectedIndex == -1)
                    return;

                try
                {
                    //Connect to the device selected in the devices combobox control
                    psCommSimpleWinForms.Connect(_connectedDevices[cmbDevices.SelectedIndex]); 
                    lbConsole.Items.Add($"Connected to {psCommSimpleWinForms.ConnectedDevice.ToString()}");
                }
                catch (Exception ex)
                {
                    lbConsole.Items.Add(ex.Message);
                }
            }
            else
            {
                psCommSimpleWinForms.Disconnect(); //Disconnect from the connected device
            }

            //Update UI based on connection status
            cmbDevices.Enabled = !psCommSimpleWinForms.Connected;
            btnRefresh.Enabled = !psCommSimpleWinForms.Connected;
            btnConnect.Text = psCommSimpleWinForms.Connected ? "Disconnect" : "Connect";
            btnMeasure.Enabled = psCommSimpleWinForms.Connected;
        }

        /// <summary>
        /// Handles the Click event of the btnMeasure control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnMeasure_Click(object sender, EventArgs e)
        {
            if (psCommSimpleWinForms.DeviceState == PalmSens.Comm.CommManager.DeviceState.Idle) //Determine whether the device is currently idle or measuring
            {
                try
                {
                    plot.ClearAll(); //Clears data from previous measurements from the plot
                    _activeMeasurement = psCommSimpleWinForms.Measure(_methodEIS); //Start measurement defined in the method

                    //Add bode curves to plot
                    plot.AddSimpleCurve(_activeMeasurement.NewSimpleCurve(PalmSens.Data.DataArrayType.Frequency, PalmSens.Data.DataArrayType.Z, "Z Abs")[0]);
                    plot.AddSimpleCurve(_activeMeasurement.NewSimpleCurve(PalmSens.Data.DataArrayType.Frequency, PalmSens.Data.DataArrayType.Phase, "-Phase")[0], true);
                }
                catch (Exception ex)
                {
                    lbConsole.Items.Add(ex.Message);
                }
            }
            else
            {
                try
                {
                    psCommSimpleWinForms.AbortMeasurement(); //Abort the active measurement
                }
                catch (Exception ex)
                {
                    lbConsole.Items.Add(ex.Message);
                }
            }
        }

        /// <summary>
        /// Handles the Click event of the btnFit control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnFit_Click(object sender, EventArgs e)
        {
            FitEquivalentCircuit(); //Fits a specified equivalent circuit to the measured data
        }

        /// <summary>
        /// Handles the Click event of the btnCancel control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnCancel_Click(object sender, EventArgs e)
        {
            if (_fitProgress != null) _fitProgress.Cancel(); //Cancels the active fit
        }

        /// <summary>
        /// Fits the equivalent circuit.
        /// </summary>
        /// <exception cref="System.NotImplementedException"></exception>
        private void FitEquivalentCircuit()
        {
            _circuitModel = BuildEquivalentCircuitModel(); //Build the model to fit on the data
            FitOptionsCircuit fitOptions = InitFitOptions(_circuitModel); //Define the options for the fit
            FitAlgorithm fitAlgorithm = FitAlgorithm.FromAlgorithm(fitOptions); //Set up the instance of the fit class
            _fitProgress = new FitProgress(); //Create an instance of the peak detection progress reporter (this can also be used to cancel the peak detection)
            _fitProgress.ProgressChanged += FitProgress_ProgressChanged;
            fitAlgorithm.ApplyFitCircuit(_fitProgress); //Start the fit
        }

        /// <summary>
        /// Builds the equivalent circuit model.
        /// </summary>
        /// <returns></returns>
        private CircuitModel BuildEquivalentCircuitModel()
        {
            CircuitModel circuitModel = new CircuitModel();
            circuitModel.SetEISdata(_activeMeasurement.Measurement.EISdata[0]); //Sets reference to measured data
            circuitModel.SetCircuit("R(RC)"); //Sets the circuit defined in the CDC code string, in this case a Randles circuit
            circuitModel.SetInitialParameters(
                new double[] {
                    100, //The initial value for the solution resistance (series resistor)
                    8000, //The initial value for the charge transfer resistance (parallel resistor)
                    1e-8 //The initial value for the double layer capacitance (parallel capacitor)
                });
            //Setting the initial parameters is recommended to ensure a good quality fit and 
            //reduce to the time it takes to find the fit

            return circuitModel;
        }

        /// <summary>
        /// Initializes the fit options.
        /// </summary>
        /// <param name="circuitModel">The circuit model.</param>
        /// <returns></returns>
        private FitOptionsCircuit InitFitOptions(CircuitModel circuitModel)
        {
            FitOptionsCircuit fitOptions = new FitOptionsCircuit();
            fitOptions.Model = circuitModel;
            fitOptions.RawData = _activeMeasurement.Measurement.EISdata[0]; //The measured data to fit onto
            fitOptions.SelectedAlgorithm = Algorithm.LevenbergMarquardt;
            fitOptions.MaxIterations = 100; //The maximum number of iterations, 500 by default
            fitOptions.MinimumDeltaErrorTerm = 1e-9; //The minimum delta in the error term (sum of squares difference between model and data), default is 1e-9      
            fitOptions.EnableMinimunDeltaErrorTerm = true; //Enable the minimum delta error as a stop condition within the fit algorithm, default is true
            fitOptions.MinimumDeltaParameters = 1e-12; //The minimum delta parameter step size, default is 1e-12
            fitOptions.EnableMinimunDeltaParameters = true; //Enable the minimum delta parameter step size as a stop condition within the fit algorithm, default is true
            fitOptions.Lambda = 1e-2; //The starting value for the Levenberg Marquardt scaling factor, default is 1e-2
            fitOptions.LambdaFactor = 10; //The scaling value for the Levenberg Marquardt scaling factor, default is 10

            return fitOptions;
        }

        /// <summary>
        /// Raised when fit progress changed.
        /// </summary>
        /// <param name="sender">The sender.</param>
        /// <param name="e">The e.</param>
        /// <exception cref="NotImplementedException"></exception>
        private void FitProgress_ProgressChanged(object sender, FitProgressUpdate e)
        {
            switch (e.Progress)
            {
                case EnumFitProgress.Started:
                    lbConsole.Items.Add("Started circuit fit.");
                    lblIterations.Text = "";
                    btnCancel.Enabled = true;
                    progressBar.MarqueeAnimationSpeed = 100;
                    break;
                case EnumFitProgress.FitIterated:
                    lblIterations.Text = e.NIterations.ToString();
                    break;
                case EnumFitProgress.Cancelled:
                case EnumFitProgress.Finished:
                    btnCancel.Enabled = false;
                    progressBar.MarqueeAnimationSpeed = 0;
                    lblIterations.Text = (e.Result.NIterations - 1).ToString(); //Excludes initial guess as iteration
                    SetFitResults(e.Result);
                    lbConsole.Items.Add("Circuit fit completed.");
                    _fitProgress.ProgressChanged -= FitProgress_ProgressChanged;
                    _fitProgress = null;
                    break;
            }
        }

        /// <summary>
        /// Sets the fit results.
        /// </summary>
        /// <param name="result">The result.</param>
        private void SetFitResults(FitResult result)
        {
            //Add results to console
            lbResults.Items.Clear();
            lbResults.Items.Add($"Rs = {result.FinalParameters[0].ToString("0.00E+000")} Ω");
            lbResults.Items.Add($"%error = {result.ParameterSDs[0].ToString("0.00E+000")} %");
            lbResults.Items.Add($"Rct = {result.FinalParameters[1].ToString("0.00E+000")} Ω");
            lbResults.Items.Add($"%error = {result.ParameterSDs[1].ToString("0.00E+000")} %");
            lbResults.Items.Add($"Cdl = {result.FinalParameters[2].ToString("0.00E+000")} F");
            lbResults.Items.Add($"%error = {result.ParameterSDs[2].ToString("0.00E+000")} %");
            lbResults.Items.Add($"Chi² = {result.ChiSq.ToString("0.00E+000")}");
            switch (result.ExitCode)
            {
                case ExitCodes.MinimumDeltaErrorTerm:
                    lbResults.Items.Add("Reached min delta error sum squares");
                    break;
                case ExitCodes.MinimumDeltaParameters:
                    lbResults.Items.Add("Reached min delta parameter step size");
                    break;
                case ExitCodes.MaxIterations:
                    lbResults.Items.Add("Reached max iterations");
                    break;
                case ExitCodes.HessianNonPositive:
                    lbResults.Items.Add("Error determing step for next iteration");
                    break;
            }

            //Remove previous fit results from plot
            if (_fitResultCurves != null)
                foreach (SimpleCurve sc in _fitResultCurves)
                    if (plot.ContainsSimpleCurve(sc))
                        plot.RemoveSimpleCurve(sc);

            //Generate new simple curves based on fit results
            _circuitModel.SetInitialParameters(result.FinalParameters); //Update the initial parameters with fit results
            _fitResultCurves = new SimpleCurve[2];
            _fitResultCurves[0] = new SimpleCurve(_circuitModel.GetCurveZabsOverFrequency(false)[0], _activeMeasurement);
            _fitResultCurves[0].Title = "Z Abs Fit";
            _fitResultCurves[1] = new SimpleCurve(_circuitModel.GetCurvePhaseOverFrequency(false)[0], _activeMeasurement);
            _fitResultCurves[1].Title = "-Phase Fit";

            //Add results to plot   
            plot.AddSimpleCurve(_fitResultCurves[0], false, false);
            plot.AddSimpleCurve(_fitResultCurves[1], true, true);
        }

        /// <summary>
        /// Raised when device status package is received (the device does not send status packages while measuring)
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="PalmSens.Comm.StatusEventArgs"/> instance containing the event data.</param>
        private void psCommSimpleWinForms_ReceiveStatus(object sender, PalmSens.Comm.StatusEventArgs e)
        {
            Status status = e.GetStatus(); //Get the PalmSens.Comm.Status instance from the event data
            double potential = status.PotentialReading.Value; //Get the potential
            double currentInRange = status.CurrentReading.ValueInRange; //Get the current expressed inthe active current range
            PalmSens.Comm.ReadingStatus currentStatus = status.CurrentReading.ReadingStatus; //Get the status of the current reading
            CurrentRange cr = status.CurrentReading.CurrentRange; //Get the active current range

            tbPotential.Text = potential.ToString("F3");
            tbCurrent.Text = currentInRange.ToString("F3");
            switch (currentStatus)
            {
                case PalmSens.Comm.ReadingStatus.OK:
                    tbCurrent.ForeColor = Color.Black;
                    break;
                case PalmSens.Comm.ReadingStatus.Overload:
                    tbCurrent.ForeColor = Color.Red;
                    break;
                case PalmSens.Comm.ReadingStatus.Underload:
                    tbCurrent.ForeColor = Color.Yellow;
                    break;
            }
            lblCurrentRange.Text = $"* {cr.ToString()}";
        }

        /// <summary>
        /// Raised when the connected device's status changes
        /// </summary>
        /// <param name="sender">The sender.</param>
        /// <param name="CurrentState">State of the current.</param>
        private void psCommSimpleWinForms_StateChanged(object sender, PalmSens.Comm.CommManager.DeviceState CurrentState)
        {
            tbDeviceStatus.Text = CurrentState.ToString(); //Updates the device state indicator textbox
            btnConnect.Enabled = CurrentState == PalmSens.Comm.CommManager.DeviceState.Idle;
            btnMeasure.Text = CurrentState == PalmSens.Comm.CommManager.DeviceState.Idle ? "Measure" : "Abort";
        }

        /// <summary>
        /// Raised when the measurement is started
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void psCommSimpleWinForms_MeasurementStarted(object sender, EventArgs e)
        {
            lbConsole.Items.Add("EIS measurement started.");
            btnFit.Enabled = false;
        }

        /// <summary>
        /// Raised when the measurement is ended
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void psCommSimpleWinForms_MeasurementEnded(object sender, Exception e)
        {
            lbConsole.Items.Add("Measurement ended.");
            btnFit.Enabled = _activeMeasurement.Measurement.EISdata.Count > 0 && _activeMeasurement.Measurement.EISdata[0].NPoints > 0;
        }

        /// <summary>
        /// Raised when the instrument has been disconnected.
        /// If the instrument was disconnected due to a communication the exception is provided.
        /// In the case of a regular disconnect the exception will be set to null.
        /// </summary>
        /// <param name="sender">The sender.</param>
        /// <param name="exception">The exception.</param>
        private void psCommSimpleWinForms_Disconnected(object sender, Exception exception)
        {
            if (exception != null)
            {
                lbConsole.Items.Add(exception.Message);
            }

            lbConsole.Items.Add("Disconnected.");
            btnConnect.Text = "Connect";
            btnConnect.Enabled = true;
            btnMeasure.Text = "Measure";
        }
    }
}
