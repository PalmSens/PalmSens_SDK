using System;
using System.Drawing;
using System.Windows.Forms;
using PalmSens;
using PalmSens.Comm;
using PalmSens.Core.Simplified.Data;
using PalmSens.Devices;
using PalmSens.Techniques;
using System.Collections.Generic;

namespace PSSDKMultiplexerExample
{
    public partial class Form1 : Form
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Form1"/> class.
        /// </summary>
        public Form1()
        {
            InitializeComponent();

            cmbChannels.SelectedIndex = 0;
            InitCAMethod(); //Create the chronoamperometry method that defines the measurement parameters
            InitDataGrid(); //Set up the columns for the datagridview control
            DiscoverConnectedDevices(); //Populate the connected device combobox control
        }

        /// <summary>
        /// The instance of method class containing the Chronoamperometry parameters
        /// </summary>
        private AmperometricDetection _methodCA;

        /// <summary>
        /// The instance of method class containing the Chronoamperometry parameters 
        /// and mulitplexer settings for sequential measurements on different channels
        /// </summary>
        private AmperometricDetection _methodCASequential;

        /// <summary>
        /// The instance of method class containing the Chronoamperometry parameters 
        /// and mulitplexer settings for alternating measurements on different channels
        /// </summary>
        private AmperometricDetection _methodCAAlternating;

        /// <summary>
        /// The connected PalmSens & EmStat devices
        /// </summary>
        private Device[] _connectedDevices = new Device[0];

        /// <summary>
        /// The active SimpleMeasurement
        /// </summary>
        private SimpleMeasurement _activeMeasurement = null;

        /// <summary>
        /// Initializes the data grid view control.
        /// </summary>
        private void InitDataGrid()
        {
            dgvMeasurement.Rows.Clear();
            dgvMeasurement.Columns.Clear();

            DataGridViewTextBoxColumn dgvColID = new DataGridViewTextBoxColumn();
            dgvColID.HeaderText = "ID";
            dgvColID.AutoSizeMode = DataGridViewAutoSizeColumnMode.AllCells;
            dgvColID.ReadOnly = true;

            DataGridViewTextBoxColumn dgvColTime = new DataGridViewTextBoxColumn();
            dgvColTime.HeaderText = "Time (s)";
            dgvColTime.AutoSizeMode = DataGridViewAutoSizeColumnMode.AllCells;
            dgvColTime.ReadOnly = true;

            DataGridViewTextBoxColumn dgvColCurrent = new DataGridViewTextBoxColumn();
            dgvColCurrent.HeaderText = "Current (µA)";
            dgvColCurrent.AutoSizeMode = DataGridViewAutoSizeColumnMode.AllCells;
            dgvColCurrent.ReadOnly = true;

            DataGridViewTextBoxColumn dgvColMuxChannel = new DataGridViewTextBoxColumn();
            dgvColMuxChannel.HeaderText = "Channel";
            dgvColMuxChannel.AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
            dgvColMuxChannel.ReadOnly = true;

            dgvMeasurement.Columns.Add(dgvColID);
            dgvMeasurement.Columns.Add(dgvColTime);
            dgvMeasurement.Columns.Add(dgvColCurrent);
            dgvMeasurement.Columns.Add(dgvColMuxChannel);
        }

        /// <summary>
        /// Initializes the CA method.
        /// </summary>
        private void InitCAMethod()
        {
            _methodCA = new AmperometricDetection(); //Create a new chronoamperometry method with the default settings
            _methodCA.Potential = 1f; //Sets the potential at 1V
            _methodCA.IntervalTime = 0.1f; //Sets the sampling interval time at 0.1s
            _methodCA.RunTime = 3f; //Sets the measurement runtime at 3s

            _methodCA.EquilibrationTime = 1f; //Equilabrates the cell at the defined potential for 1 second before starting the measurement
            _methodCA.Ranging.StartCurrentRange = new CurrentRange(CurrentRanges.cr1uA); //Starts equilabration in the 1µA current range
            _methodCA.Ranging.MinimumCurrentRange = new CurrentRange(CurrentRanges.cr10nA); //Min current range 10nA
            _methodCA.Ranging.MaximumCurrentRange = new CurrentRange(CurrentRanges.cr1mA); //Max current range 1mA

            //Sequential multiplexer measurement settings
            _methodCASequential = new AmperometricDetection(); //Create a new chronoamperometry method with the default settings
            _methodCASequential.Potential = 1f; //Sets the potential at 1V
            _methodCASequential.IntervalTime = 0.1f; //Sets the sampling interval time at 0.1s
            _methodCASequential.RunTime = 1f; //Sets the measurement runtime at 1s
            _methodCASequential.MuxMethod = MuxMethod.Sequentially; //Set the type of multiplexer measurement
            //Create an array of booleans indicating on which channels you would like to measure
            //For a 16 channel mux you can create a bool array for 16 channels
            bool[] measureOnChannels1 = new bool[8];  //Define bool array for 8 channel multiplexer
            //Specify on which channels to measure            
            measureOnChannels1[0] = false;
            measureOnChannels1[1] = true;
            measureOnChannels1[2] = true;
            measureOnChannels1[3] = false;
            measureOnChannels1[4] = true;
            measureOnChannels1[5] = false;
            measureOnChannels1[6] = false;
            measureOnChannels1[7] = false;
            _methodCASequential.UseMuxChannel = new System.Collections.BitArray(measureOnChannels1); //Set to measure sequentially on channel 1, 3 and 5

            //Alternating multiplexer measurement settings
            //Only Chronoamperometry (Amperometric Detection) and (Open Circuit) Potentiometry support alternating measurements. 
            _methodCAAlternating = new AmperometricDetection(); //Create a new chronoamperometry method with the default settings
            _methodCAAlternating.Potential = 1f; //Sets the potential at 1V
            _methodCAAlternating.IntervalTime = 0.25f; //Sets the sampling interval time at 0.25s (0.25s is the minimum sample time for the multiplexer in alternating mode)
            _methodCAAlternating.RunTime = 2.5f; //Sets the measurement runtime at 2.5s
            _methodCAAlternating.MuxMethod = MuxMethod.Alternatingly; //Set the type of multiplexer measurement
            //Create an array of booleans indicating on which channels you would like to measure
            //For a 16 channel mux you can create a bool array for 16 channels
            bool[] measureOnChannels2 = new bool[8];  //Define bool array for 8 channel multiplexer
            //Specify on which channels to measure
            //For alternating mux measurements only successive channels can be selected starting at the first channel (i.e. 1, 2 and 3 not for example 2, 4 and 7)                  
            measureOnChannels2[0] = true;
            measureOnChannels2[1] = true;
            measureOnChannels2[2] = true;
            measureOnChannels2[3] = false;
            measureOnChannels2[4] = false;
            measureOnChannels2[5] = false;
            measureOnChannels2[6] = false;
            measureOnChannels2[7] = false;
            _methodCAAlternating.UseMuxChannel = new System.Collections.BitArray(measureOnChannels2); //Set to measure alternatingly on channel 1, 2 and 3
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
            btnMeasureSequentially.Enabled = psCommSimpleWinForms.Connected;
            btnMeasureAlternatingly.Enabled = psCommSimpleWinForms.Connected;
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
                    InitDataGrid(); //Reset the data grid view control
                    //Start measurement defined in the method on the multiplexer channel specified in the channel combobox control
                    _activeMeasurement = psCommSimpleWinForms.Measure(_methodCA, cmbChannels.SelectedIndex); 
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
        /// Handles the Click event of the btnMeasureSequentially control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnMeasureSequentially_Click(object sender, EventArgs e)
        {
            if (psCommSimpleWinForms.DeviceState == PalmSens.Comm.CommManager.DeviceState.Idle) //Determine whether the device is currently idle or measuring
            {
                try
                {
                    InitDataGrid(); //Reset the data grid view control
                    //Start the sequential multiplexer measurement on the channels defined in the method
                    _activeMeasurement = psCommSimpleWinForms.Measure(_methodCASequential); 
                }
                catch (Exception ex)
                {
                    lbConsole.Items.Add(ex.Message);
                }
            }
        }

        /// <summary>
        /// Handles the Click event of the btnMeasureAlternatingly control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnMeasureAlternatingly_Click(object sender, EventArgs e)
        {
            if (psCommSimpleWinForms.DeviceState == PalmSens.Comm.CommManager.DeviceState.Idle) //Determine whether the device is currently idle or measuring
            {
                try
                {
                    InitDataGrid(); //Reset the data grid view control
                    //Start the alternating multiplexer measurement on the channels defined in the method
                    _activeMeasurement = psCommSimpleWinForms.Measure(_methodCAAlternating);
                }
                catch (Exception ex)
                {
                    lbConsole.Items.Add(ex.Message);
                }
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
            btnMeasureSequentially.Enabled = CurrentState == PalmSens.Comm.CommManager.DeviceState.Idle;
            btnMeasureAlternatingly.Enabled = CurrentState == PalmSens.Comm.CommManager.DeviceState.Idle;
        }

        /// <summary>
        /// Raised when the measurement is ended
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void psCommSimpleWinForms_MeasurementEnded(object sender, Exception e)
        {
            lbConsole.Items.Add("Measurement ended.");
        }

        /// <summary>
        /// Raised when the measurement is started
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void psCommSimpleWinForms_MeasurementStarted(object sender, EventArgs e)
        {
            lbConsole.Items.Add("Measurement started.");
        }

        /// <summary>
        /// Raised when a Simple Curve in the active SimpleMeasurement starts receiving data
        /// </summary>
        /// <param name="sender">The sender.</param>
        /// <param name="activeSimpleCurve">The active simple curve.</param>
        private void psCommSimpleWinForms_SimpleCurveStartReceivingData(object sender, SimpleCurve activeSimpleCurve)
        {
            //Subscribe to the curve's events to receive updates when new data is available and when it iss finished receiving data
            activeSimpleCurve.NewDataAdded += ActiveSimpleCurve_NewDataAdded;
            activeSimpleCurve.CurveFinished += ActiveSimpleCurve_CurveFinished;

            lbConsole.Items.Add($"Channel {activeSimpleCurve.MuxChannel + 1}: Curve is receiving new data...");
        }

        /// <summary>
        /// Raised when new data points are added to an active SimpleCurve
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="PalmSens.Data.ArrayDataAddedEventArgs"/> instance containing the event data.</param>
        private void ActiveSimpleCurve_NewDataAdded(object sender, PalmSens.Data.ArrayDataAddedEventArgs e)
        {
            SimpleCurve activeCurve = sender as SimpleCurve;
            int startIndex = e.StartIndex; //The index of the first new data point added to the curve
            int count = e.Count; //The number of new data points added to the curve

            for (int i = startIndex; i < startIndex + count; i++)
            {
                double xValue = activeCurve.XAxisValue(i); //Get the value on Curve's X-Axis (potential) at the specified index
                double yValue = activeCurve.YAxisValue(i); //Get the value on Curve's Y-Axis (current) at the specified index
                dgvMeasurement.Rows.Add(1);
                dgvMeasurement.Rows[dgvMeasurement.Rows.Count - 1].Cells[0].Value = (i + 1).ToString();
                dgvMeasurement.Rows[dgvMeasurement.Rows.Count - 1].Cells[1].Value = xValue.ToString("F2");
                dgvMeasurement.Rows[dgvMeasurement.Rows.Count - 1].Cells[2].Value = yValue.ToString("E3");
                dgvMeasurement.Rows[dgvMeasurement.Rows.Count - 1].Cells[3].Value = activeCurve.MuxChannel + 1;
            }
        }

        /// <summary>
        /// Raised when a SimpleCurve stops receiving new data points
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void ActiveSimpleCurve_CurveFinished(object sender, EventArgs e)
        {
            SimpleCurve activeCurve = sender as SimpleCurve;

            int nDataPointsReceived = activeCurve.NDataPoints;
            lbConsole.Items.Add($"Channel {activeCurve.MuxChannel + 1}: {nDataPointsReceived} data point(s) received.");

            //Unsubscribe from the curves events to avoid memory leaks
            activeCurve.NewDataAdded -= ActiveSimpleCurve_NewDataAdded;
            activeCurve.CurveFinished -= ActiveSimpleCurve_CurveFinished;

            lbConsole.Items.Add($"Channel {activeCurve.MuxChannel + 1}: Finished");
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
