using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using PalmSens;
using PalmSens.Analysis;
using PalmSens.Comm;
using PalmSens.Core.Simplified.Data;
using PalmSens.Devices;
using PalmSens.Plottables;
using PalmSens.Techniques;

namespace PSSDKPlotPeakDetectionAsyncExample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            InitCVMethod(); //Create the cyclic voltammetry method that defines the measurement parameters
            InitPlot(); //Resets and initiates the plot control
            DiscoverConnectedDevicesAsync(); //Populate the connected device combobox control
        }

        /// <summary>
        /// The instance of method class containing the Cyclic Voltammetry parameters
        /// </summary>
        private CyclicVoltammetry _methodCV;

        /// <summary>
        /// The connected PalmSens & EmStat devices
        /// </summary>
        private Device[] _connectedDevices = new Device[0];

        /// <summary>
        /// The active SimpleMeasurement
        /// </summary>
        private SimpleMeasurement _activeMeasurement = null;

        /// <summary>
        /// The minimum peak height in µA
        /// </summary>
        private double _minPeakHeight = 0.0001;

        /// <summary>
        /// Initializes the CV method.
        /// </summary>
        private void InitCVMethod()
        {
            _methodCV = new CyclicVoltammetry(); //Create a new cyclic voltammetry method with the default settings
            _methodCV.BeginPotential = -.5f; //Sets the potential to start the scan from
            _methodCV.Vtx1Potential = -.5f; //Sets the first potential where the scan direction reverses
            _methodCV.Vtx2Potential = .5f; //Sets the second potential where the scan direction reverses
            _methodCV.StepPotential = 0.01f; //Sets the step size
            _methodCV.Scanrate = 0.5f; //Sets the scan rate to 1 V/s
            _methodCV.nScans = 3; //Sets the number of scans

            _methodCV.EquilibrationTime = 5f; //Equilabrates the cell at the defined potential for 5 seconds before starting the measurement
            _methodCV.Ranging.StartCurrentRange = new CurrentRange(CurrentRanges.cr1uA); //Starts equilabration in the 1µA current range
            _methodCV.Ranging.MinimumCurrentRange = new CurrentRange(CurrentRanges.cr10nA); //Min current range 10nA
            _methodCV.Ranging.MaximumCurrentRange = new CurrentRange(CurrentRanges.cr1mA); //Max current range 1mA
        }

        /// <summary>
        /// Initializes the plot control.
        /// </summary>
        private void InitPlot()
        {
            plot.ClearAll(); //Clear all curves and data from plot
            //Set the Axis labels
            plot.XAxisLabel = "V";
            plot.YAxisLabel = "µA";
            plot.AddData("", new double[0], new double[0]); //Add a empty data array to draw an empty plot
        }

        /// <summary>
        /// Discovers the connected PalmSens & EmStat devices and adds them to the combobox control.
        /// </summary>
        private async Task DiscoverConnectedDevicesAsync()
        {
            btnRefresh.Enabled = false;
            lbConsole.Items.Add("Searching for connected devices.");
            cmbDevices.Items.Clear();
            _connectedDevices = await psCommSimpleWinForms.GetConnectedDevicesAsync(); //Discover connected devices

            foreach (Device d in _connectedDevices)
                cmbDevices.Items.Add(d.ToString()); //Add connected devices to control

            int nDevices = cmbDevices.Items.Count;
            cmbDevices.SelectedIndex = nDevices > 0 ? 0 : -1;
            lbConsole.Items.Add($"Found {nDevices} device(s).");

            btnConnect.Enabled = nDevices > 0;
            btnRefresh.Enabled = true;
        }

        /// <summary>
        /// Handles the Click event of the btnRefresh control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private async void btnRefresh_Click(object sender, EventArgs e)
        {
            await DiscoverConnectedDevicesAsync(); //Add connected devices to the devices combobox control
        }

        /// <summary>
        /// Handles the Click event of the btnConnect control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private async void btnConnect_Click(object sender, EventArgs e)
        {
            btnConnect.Enabled = false;
            if (!psCommSimpleWinForms.Connected) //Determine whether a device is currently connected
            {
                if (cmbDevices.SelectedIndex == -1)
                    return;

                try
                {
                    //Connect to the device selected in the devices combobox control
                    await psCommSimpleWinForms.ConnectAsync(_connectedDevices[cmbDevices.SelectedIndex]); 
                    lbConsole.Items.Add($"Connected to {psCommSimpleWinForms.ConnectedDevice.ToString()}");
                }
                catch (Exception ex)
                {
                    lbConsole.Items.Add(ex.Message);
                }
            }
            else
            {
                await psCommSimpleWinForms.DisconnectAsync(); //Disconnect from the connected device
            }

            //Update UI based on connection status
            cmbDevices.Enabled = !psCommSimpleWinForms.Connected;
            btnRefresh.Enabled = !psCommSimpleWinForms.Connected;
            btnConnect.Text = psCommSimpleWinForms.Connected ? "Disconnect" : "Connect";
            btnMeasure.Enabled = psCommSimpleWinForms.Connected;
            btnConnect.Enabled = true;
        }

        /// <summary>
        /// Handles the Click event of the btnMeasure control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private async void btnMeasure_Click(object sender, EventArgs e)
        {
            btnMeasure.Enabled = false;
            if (psCommSimpleWinForms.DeviceState == PalmSens.Comm.CommManager.DeviceState.Idle) //Determine whether the device is currently idle or measuring
            {
                try
                {
                    plot.ClearAll(); //Clears data from previous measurements from the plot
                    _activeMeasurement = await psCommSimpleWinForms.MeasureAsync(_methodCV); //Start measurement defined in the method
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
                    await psCommSimpleWinForms.AbortMeasurementAsync(); //Abort the active measurement
                }
                catch (Exception ex)
                {
                    lbConsole.Items.Add(ex.Message);
                }
            }
            btnMeasure.Enabled = true;
        }

        /// <summary>
        /// Handles the Click event of the btnPeaks control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private async void btnPeaks_Click(object sender, EventArgs e)
        {
            btnPeaks.Enabled = false;
            if (_activeMeasurement != null)
                await DetectLSVCVPeaksAsync();
            btnPeaks.Enabled = true;
        }

        /// <summary>
        /// Detects the LSVCV peaks after a measurement is finished.
        /// </summary>
        private async Task DetectLSVCVPeaksAsync()
        {
            //Create an instance of the class used to detect LSV / CV peaks
            SemiDerivativePeakDetection semiDerivativePeakDetection = new SemiDerivativePeakDetection();

            //Create an instance of the peak detection progress reporter (this can also be used to cancel the peak detection)
            PeakDetectProgress peakDetectProgress = new PeakDetectProgress();
            peakDetectProgress.ProgressChanged += PeakDetectProgress_ProgressChanged;

            //Add curves from the last measurement and corresponding min peak heights 
            //to the dictionary that is passed on to LSV / CV peak detection class
            Dictionary<Curve, double> curves = new Dictionary<Curve, double>();
            foreach (Curve c in _activeMeasurement.SimpleCurveCollection.Select(sc => sc.Curve))
                curves.Add(c, _minPeakHeight);

            SimpleCurve activeSimpleCurve = _activeMeasurement.SimpleCurveCollection[0];

            //Start the semiderivative peak detection (alternatively this can be called synchronously without the PeakDetectProgress object
            //but this could block the UI for quite some time)
            await semiDerivativePeakDetection.GetNonOverlappingPeaksAsync(curves, peakDetectProgress);
        }

        /// <summary>
        /// Raised when the peak detect progress has changed.
        /// </summary>
        /// <param name="sender">The sender.</param>
        /// <param name="e">The e.</param>
        private void PeakDetectProgress_ProgressChanged(object sender, PeakDetectProgressUpdate e)
        {
            switch (e.Progress)
            {
                case EnumPeakDetectProgress.Started:
                    lbConsole.Items.Add($"Peak detection started. {e.NCurves} curves remaining.");
                    break;
                case EnumPeakDetectProgress.PeakDetected:
                    lbConsole.Items.Add($"{e.NPeaksFound} peaks found.");
                    break;
                case EnumPeakDetectProgress.ProcessingCurve:
                    lbConsole.Items.Add($"Detecting peaks in {e.CurveTitle}.");
                    break;
                case EnumPeakDetectProgress.CurveProcessed:
                    lbConsole.Items.Add($"{e.NRemainingCurves} curves remaining.");
                    break;
                case EnumPeakDetectProgress.Cancelled:
                    break;
                case EnumPeakDetectProgress.Finished:
                    lbConsole.Items.Add("Completed detecting peaks.");
                    //Draw the peaks in the plot
                    plot.UpdateSimpleCurvesPeaks(_activeMeasurement.SimpleCurveCollection);
                    break;
            }
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
            lbConsole.Items.Add("Cyclic voltammetry measurement started.");
            btnPeaks.Enabled = false;
        }

        /// <summary>
        /// Raised when the measurement is ended
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void psCommSimpleWinForms_MeasurementEnded(object sender, Exception e)
        {
            lbConsole.Items.Add("Measurement ended.");
            btnPeaks.Enabled = _activeMeasurement.SimpleCurveCollection.Count > 0;
        }

        /// <summary>
        /// Raised when a Simple Curve in the active SimpleMeasurement starts receiving data
        /// </summary>
        /// <param name="sender">The sender.</param>
        /// <param name="activeSimpleCurve">The active simple curve.</param>
        private void psCommSimpleWinForms_SimpleCurveStartReceivingData(object sender, SimpleCurve activeSimpleCurve)
        {
            plot.AddSimpleCurve(activeSimpleCurve);

            //Subscribe to the event indicating when the curve stops receiving new data points
            activeSimpleCurve.CurveFinished += activeSimpleCurve_CurveFinished;

            lbConsole.Items.Add("Curve is receiving new data...");
        }

        /// <summary>
        /// Raised when a SimpleCurve stops receiving new data points
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="System.EventArgs" /> instance containing the event data.</param>
        private void activeSimpleCurve_CurveFinished(object sender, EventArgs e)
        {

            if (InvokeRequired) //Data is parsed asynchronously in the case this event was raised on a different thread it must be invoked back onto the UI thread
            {
                BeginInvoke(new EventHandler(activeSimpleCurve_CurveFinished), sender, e);
                return;
            }
            SimpleCurve activeCurve = sender as SimpleCurve;
            int nDataPointsReceived = activeCurve != null ? activeCurve.NDataPoints : 0;
            lbConsole.Items.Add($"{nDataPointsReceived} data point(s) received.");

            //Unsubscribe from the curves events to avoid memory leaks
            activeCurve.CurveFinished -= activeSimpleCurve_CurveFinished;
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
