using System;
using System.Drawing;
using System.Windows.Forms;
using PalmSens;
using PalmSens.Comm;
using PalmSens.Core.Simplified.Data;
using PalmSens.Devices;
using PalmSens.Techniques;
using System.Collections.Generic;

namespace PSSDKBiPotAuxExample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            cmbBiPotMode.SelectedIndex = 0;
            cmbStatusExtraValue.SelectedIndex = 1;
            InitCAMethod(); //Create the chronoamperometry methods that defines the measurement parameters
            InitDataGrid(); //Set up the columns for the datagridview control
            DiscoverConnectedDevices(); //Populate the connected device combobox control
        }

        /// <summary>
        /// The instance of method class containing the Chronoamperometry parameters with BiPot enabled
        /// </summary>
        private AmperometricDetection _methodCABiPot;

        /// <summary>
        /// The instance of method class containing the Chronoamperometry parameters with Aux Recording enabled
        /// </summary>
        private AmperometricDetection _methodCAAux;

        /// <summary>
        /// The connected PalmSens & EmStat devices
        /// </summary>
        private Device[] _connectedDevices = new Device[0];

        /// <summary>
        /// The active SimpleMeasurement
        /// </summary>
        private SimpleMeasurement _activeMeasurement = null;

        /// <summary>
        /// The extra value curve
        /// </summary>
        private SimpleCurve _extraValueCurve = null;

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

            DataGridViewTextBoxColumn dgvColExtraValue = new DataGridViewTextBoxColumn();
            dgvColExtraValue.HeaderText = "Extra Value";
            dgvColExtraValue.AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
            dgvColExtraValue.ReadOnly = true;

            dgvMeasurement.Columns.Add(dgvColID);
            dgvMeasurement.Columns.Add(dgvColTime);
            dgvMeasurement.Columns.Add(dgvColCurrent);
            dgvMeasurement.Columns.Add(dgvColExtraValue);
        }

        /// <summary>
        /// Initializes the CA method.
        /// </summary>
        private void InitCAMethod()
        {
            //BiPot Method
            _methodCABiPot = new AmperometricDetection(); //Create a new chronoamperometry method with the default settings
            _methodCABiPot.Potential = 1f; //Sets the potential at 1V
            _methodCABiPot.IntervalTime = 0.1f; //Sets the sampling interval time at 0.1s
            _methodCABiPot.RunTime = 3f; //Sets the measurement runtime at 3s

            _methodCABiPot.EquilibrationTime = 1f; //Equilabrates the cell at the defined potential for 1 second before starting the measurement
            _methodCABiPot.Ranging.StartCurrentRange = new CurrentRange(CurrentRanges.cr1uA); //Starts equilabration in the 1µA current range
            _methodCABiPot.Ranging.MinimumCurrentRange = new CurrentRange(CurrentRanges.cr10nA); //Min current range 10nA
            _methodCABiPot.Ranging.MaximumCurrentRange = new CurrentRange(CurrentRanges.cr1mA); //Max current range 1mA

            //BiPot settings
            _methodCABiPot.ExtraValueMsk = ExtraValueMask.BipotWE;
            //The BiPot mode and potential are updated with the settings specified in the Form in btnMeasureBiPot_Click
            _methodCABiPot.BipotModePS = Method.EnumPalmSensBipotMode.offset; 
            _methodCABiPot.BiPotPotential = 0;
            _methodCABiPot.BiPotCR = new CurrentRange(3); //Set BiPot to measure in the 1µA current range

            //Set BiPot to measure in the 1µA current range//Init EmStat Pico settings, these do not affect other devices (alternatively use the method _methodCABiPot.DeterminePGStatMode((EmStatPicoCapabilities)_psCommSimpleAndroid.Capabilities) to determine the recommended settings for the EmStat Pico)
            _methodCABiPot.PGStatMode = MethodScript.PGStatModes.LowSpeed; //BiPot measurements require the device to be set to lowspeed mode
            _methodCABiPot.SelectedPotentiostatChannel = PotentionstatChannels.Ch0; //In BiPot measurements the main we, the re and ce are controlled by channel 0 and the BiPot we by channel 1

            //Aux Method
            _methodCAAux = new AmperometricDetection(); //Create a new chronoamperometry method with the default settings
            _methodCAAux.Potential = 1f; //Sets the potential at 1V
            _methodCAAux.IntervalTime = 0.1f; //Sets the sampling interval time at 0.1s
            _methodCAAux.RunTime = 3f; //Sets the measurement runtime at 3s
                     
            _methodCAAux.EquilibrationTime = 1f; //Equilabrates the cell at the defined potential for 1 second before starting the measurement
            _methodCAAux.Ranging.StartCurrentRange = new CurrentRange(CurrentRanges.cr1uA); //Starts equilabration in the 1µA current range
            _methodCAAux.Ranging.MinimumCurrentRange = new CurrentRange(CurrentRanges.cr10nA); //Min current range 10nA
            _methodCAAux.Ranging.MaximumCurrentRange = new CurrentRange(CurrentRanges.cr1mA); //Max current range 1mA

            //Aux settings
            _methodCAAux.ExtraValueMsk = ExtraValueMask.AuxInput;
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
            btnMeasureAux.Enabled = psCommSimpleWinForms.Connected;

            //Check device capabilities to see if BiPot is supported
            btnMeasureBiPot.Enabled = psCommSimpleWinForms.Connected && psCommSimpleWinForms.Capabilities.BiPotPresent;
            cmbStatusExtraValue.Enabled = psCommSimpleWinForms.Connected && psCommSimpleWinForms.Capabilities.BiPotPresent;
            cmbStatusExtraValue.SelectedIndex = (psCommSimpleWinForms.Connected && psCommSimpleWinForms.Capabilities.BiPotPresent) ? 0 : 1;
        }

        /// <summary>
        /// Handles the Click event of the btnMeasure control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnMeasureBiPot_Click(object sender, EventArgs e)
        {
            if (psCommSimpleWinForms.DeviceState == PalmSens.Comm.CommManager.DeviceState.Idle) //Determine whether the device is currently idle or measuring
            {
                try
                {
                    //Parse the BiPot potential specified in the textbox
                    float potentialBiPot;
                    if (!float.TryParse(tbBiPotPotential.Text, out potentialBiPot))
                    {
                        lbConsole.Items.Add("Could not parse BiPot potential.");
                        return;
                    }
                    _methodCABiPot.BiPotPotential = potentialBiPot; //Set the BiPot potential specified in the form
                    //Set the BiPot mode specified in the form
                    _methodCABiPot.BipotModePS = cmbBiPotMode.SelectedIndex == 0 ? Method.EnumPalmSensBipotMode.constant : Method.EnumPalmSensBipotMode.offset;

                    InitDataGrid(); //Reset the data grid view control
                    //Start BiPot measurement defined in the method
                    _activeMeasurement = psCommSimpleWinForms.Measure(_methodCABiPot);

                    //Create a new SimpleCurve with ExtraValue(BiPot/Aux) readings (Set to silent to prevent the new data event from being raised by multiple curves)
                    _extraValueCurve = (_activeMeasurement.NewSimpleCurve(PalmSens.Data.DataArrayType.Time, PalmSens.Data.DataArrayType.BipotCurrent, "", true))[0];
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
        /// Handles the Click event of the btnMeasureAux control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnMeasureAux_Click(object sender, EventArgs e)
        {
            if (psCommSimpleWinForms.DeviceState == PalmSens.Comm.CommManager.DeviceState.Idle) //Determine whether the device is currently idle or measuring
            {
                try
                {
                    InitDataGrid(); //Reset the data grid view control
                    //Start measurement with auxillary readings enabled defined in the method
                    _activeMeasurement = psCommSimpleWinForms.Measure(_methodCAAux);

                    //Create a new SimpleCurve with ExtraValue(BiPot/Aux) readings (Set to silent to prevent the new data event from being raised by multiple curves)
                    _extraValueCurve = (_activeMeasurement.NewSimpleCurve(PalmSens.Data.DataArrayType.Time, PalmSens.Data.DataArrayType.AuxInput, "", true))[0];
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
        /// Raised when device status package is received (the device does not send status packages while measuring)
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="PalmSens.Comm.StatusEventArgs"/> instance containing the event data.</param>
        private void psCommSimpleWinForms_ReceiveStatus(object sender, StatusEventArgs e)
        {
            Status status = e.GetStatus(); //Get the PalmSens.Comm.Status instance from the event data
            double potential = status.PotentialReading.Value; //Get the potential
            double currentInRange = status.CurrentReading.ValueInRange; //Get the current expressed inthe active current range
            ReadingStatus currentStatus = status.CurrentReading.ReadingStatus; //Get the status of the current reading
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

            if (cmbStatusExtraValue.SelectedIndex == 0)
            {
                tbExtraValue.Text = status.GetCorrectedBiPotCurrent().ToString("F3");
                lblExtaValueUnit.Text = lblCurrentRange.Text;
            }
            else
            {
                tbExtraValue.Text = status.GetAuxInputAsVoltage().ToString("F3");
                lblExtaValueUnit.Text = "V";
            }
        }

        /// <summary>
        /// Raised when the connected device's status changes
        /// </summary>
        /// <param name="sender">The sender.</param>
        /// <param name="CurrentState">State of the current.</param>
        private void psCommSimpleWinForms_StateChanged(object sender, CommManager.DeviceState CurrentState)
        {
            tbDeviceStatus.Text = CurrentState.ToString(); //Updates the device state indicator textbox
            btnConnect.Enabled = CurrentState == CommManager.DeviceState.Idle;
            btnMeasureBiPot.Text = CurrentState == CommManager.DeviceState.Idle ? "Measure" : "Abort";
            btnMeasureAux.Text = CurrentState == CommManager.DeviceState.Idle ? "Measure" : "Abort";
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
            if (activeSimpleCurve.YAxisDataType != PalmSens.Data.DataArrayType.Current) //Ignore other automatically generated curves
                return;

            //Subscribe to the curve's events to receive updates when new data is available and when it iss finished receiving data
            activeSimpleCurve.NewDataAdded += ActiveSimpleCurve_NewDataAdded;
            activeSimpleCurve.CurveFinished += ActiveSimpleCurve_CurveFinished;

            lbConsole.Items.Add($"Curve is receiving new data...");
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

                //Get the BiPot/Aux reading
                double extraValue = _extraValueCurve.YAxisValue(i); //BiPot
                string extraValueUnit = _activeMeasurement.Measurement.Method.ExtraValueMsk == ExtraValueMask.BipotWE ? "µA" : "V";

                dgvMeasurement.Rows.Add(1);
                dgvMeasurement.Rows[dgvMeasurement.Rows.Count - 1].Cells[0].Value = (i + 1).ToString();
                dgvMeasurement.Rows[dgvMeasurement.Rows.Count - 1].Cells[1].Value = xValue.ToString("F2");
                dgvMeasurement.Rows[dgvMeasurement.Rows.Count - 1].Cells[2].Value = yValue.ToString("E3");
                dgvMeasurement.Rows[dgvMeasurement.Rows.Count - 1].Cells[3].Value = $"{extraValue.ToString("E3")} {extraValueUnit}";
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
            lbConsole.Items.Add($"{nDataPointsReceived} data point(s) received.");

            //Unsubscribe from the curves events to avoid memory leaks
            activeCurve.NewDataAdded -= ActiveSimpleCurve_NewDataAdded;
            activeCurve.CurveFinished -= ActiveSimpleCurve_CurveFinished;

            lbConsole.Items.Add("Curve Finished");
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
            btnMeasureAux.Text = "Measure";
        }
    }
}
