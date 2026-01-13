using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using PalmSens;
using PalmSens.Comm;
using PalmSens.Core.Simplified.Data;
using PalmSens.Data;
using PalmSens.Devices;
using PalmSens.Plottables;
using PalmSens.Techniques;

namespace PSSDKMethodScriptExamples
{
    public partial class FrmSandBox : Form
    {
        private const string MethodScriptGetter = "Get GPIO";
        private const string MethodScriptSetter = "Set GPIO";

        private const string SandboxScript =
            "e\nvar c\nvar p\nset_pgstat_chan 1\nset_pgstat_mode 0\nset_pgstat_chan 0\nset_pgstat_mode 3\nset_max_bandwidth 400\nset_range_minmax da -1 1\nset_range ba 590u\nset_autoranging ba 590n 590u\ncell_on\nmeas_loop_lsv p c -500m 500m 10m 1\npck_start\npck_add p\npck_add c\npck_end\nendloop\nmeas_loop_cv p c -500m -1 1 10m 1\npck_start\npck_add p\npck_add c\npck_end\nendloop\non_finished:\ncell_off\n\n";

        private readonly List<Device> _connectedDevices;
        private volatile bool _isRunning;

        public FrmSandBox()
        {
            InitializeComponent();
            _connectedDevices = new List<Device>();
        }

        /// <summary>
        ///     Raised when a SimpleCurve stops receiving new data points
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private void activeSimpleCurve_CurveFinished(object sender, EventArgs e)
        {
            if (InvokeRequired) //Data is parsed asynchronously in the case this event was raised on a different thread it must be invoked back onto the UI thread
            {
                BeginInvoke(new EventHandler(activeSimpleCurve_CurveFinished), sender, e);
                return;
            }

            var activeSimpleCurve = (SimpleCurve) sender;

            //Unsubscribe from the curves events to avoid memory leaks
            activeSimpleCurve.NewDataAdded -= activeSimpleCurve_NewDataAdded;
            activeSimpleCurve.CurveFinished -= activeSimpleCurve_CurveFinished;

            var nDataPointsReceived = activeSimpleCurve.NDataPoints;
            LogMessage($"{nDataPointsReceived} data point(s) received.");

            LogMessage("Curve Finished");
        }

        /// <summary>
        ///     Raised when new data points are added to the active SimpleCurve
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="PalmSens.Data.ArrayDataAddedEventArgs" /> instance containing the event data.</param>
        private void activeSimpleCurve_NewDataAdded(object sender, ArrayDataAddedEventArgs e)
        {
            if (InvokeRequired) //Data is parsed asynchronously in the case this event was raised on a different thread it must be invoked back onto the UI thread
            {
                BeginInvoke(new Curve.NewDataAddedEventHandler(activeSimpleCurve_NewDataAdded), sender, e);
                return;
            }

            var activeSimpleCurve = (SimpleCurve) sender;
            var startIndex = e.StartIndex; //The index of the first new data point added to the curve
            var count = e.Count; //The number of new data points added to the curve

            for (var i = startIndex; i < startIndex + count; i++)
            {
                var xValue =
                    activeSimpleCurve
                        .XAxisValue(i); //Get the value on Curve's X-Axis (potential) at the specified index
                var yValue =
                    activeSimpleCurve.YAxisValue(i); //Get the value on Curve's Y-Axis (current) at the specified index

                var rowIndex = dgvMeasurement.Rows.Add(1);
                dgvMeasurement.Rows[rowIndex].Cells[0].Value = (i + 1).ToString();
                dgvMeasurement.Rows[rowIndex].Cells[1].Value = xValue.ToString("F2");
                dgvMeasurement.Rows[rowIndex].Cells[2].Value = yValue.ToString("E3");
            }

            tbPotential.Text = activeSimpleCurve.XAxisValue(startIndex + count - 1).ToString("F3");
            tbCurrent.Text = activeSimpleCurve.YAxisValue(startIndex + count - 1).ToString("F3");

            var displayCount = dgvMeasurement.DisplayedRowCount(false);

            if (displayCount < dgvMeasurement.Rows.Count)
                dgvMeasurement.FirstDisplayedScrollingRowIndex = dgvMeasurement.Rows.Count - displayCount - 1;
        }

        private async void btnConnect_Click(object sender, EventArgs e)
        {
            if (!psCommSimpleWinForms.Connected) //Determine whether a device is currently connected
            {
                if (cmbDevices.SelectedIndex == -1)
                    return;

                try
                {
                    //Connect to the device selected in the devices combobox control
                    await psCommSimpleWinForms.ConnectAsync(_connectedDevices[cmbDevices.SelectedIndex]);
                    LogMessage($"Connected to {cmbDevices.Text}");
                }
                catch (Exception ex)
                {
                    LogException(ex);
                }
            }
            else
            {
                await psCommSimpleWinForms.DisconnectAsync(); //Disconnect from the connected device
                LogMessage("Disconnected");
            }

            UpdateFormInteraction();
        }

        private async void btnRefresh_Click(object sender, EventArgs e)
        {
            if (psCommSimpleWinForms.Connected)
                return;

            await DiscoverConnectedDevicesAsync();
        }

        private async void btnRun_Click(object sender, EventArgs e)
        {
            try
            {
                // Prevent script from running if device is not a method script device.
                if (!(psCommSimpleWinForms.Capabilities is MethodScriptDeviceCapabilities))
                {
                    MessageBox.Show($"The device '{psCommSimpleWinForms.Capabilities}' does not support method method script");
                    return;
                }

                // Check state of device.
                if (psCommSimpleWinForms.DeviceState == CommManager.DeviceState.Idle)
                {
                    var script = txtScript.Text;
                    if (rbSandBox.Checked)
                    {
                        // Run Sandbox measurement.
                        InitDataGrid();

                        var sandbox = new MethodScriptSandbox
                        {
                            MethodScript = script
                        };
                        await psCommSimpleWinForms.MeasureAsync(sandbox);

                        return;
                    }

                    // Otherwise execute the method script directly.
                    await SendCommandAsync(rbGetter.Checked, script);
                }
                else
                {
                    await psCommSimpleWinForms.AbortMeasurementAsync();
                }
            }
            catch (AggregateException aggr)
            {
                aggr.Handle(LogException);
            }
            catch (Exception ex)
            {
                LogException(ex);
            }
        }

        private void cmbMethod_SelectedIndexChanged(object sender, EventArgs e)
        {
            SetTemplate();
        }

        private async void FrmSandBox_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (psCommSimpleWinForms.Connected)
                await psCommSimpleWinForms.DisconnectAsync();
        }

        private async void FrmSandBox_Load(object sender, EventArgs e)
        {
            AddItem("Please Select");
            AddItem(LinearSweep.Name);
            AddItem(CyclicVoltammetry.Name);
            AddItem(DifferentialPulse.Name);
            AddItem(SquareWave.Name);
            AddItem(NormalPulse.Name);
            AddItem(AmperometricDetection.Name);
            AddItem(PulsedAmpDetection.Name);
            AddItem(OpenCircuitPotentiometry.Name);
            AddItem(Chronocoulometry.Name);
            AddItem(ImpedimetricMethod.Name);
            AddItem("2 Measurements: LSV & CV.");
            AddItem(MethodScriptGetter);
            AddItem(MethodScriptSetter);

            cmbMethod.SelectedIndex = 0;

            await DiscoverConnectedDevicesAsync();
        }

        private void psCommSimpleWinForms_Disconnected(object sender, Exception commErrorException)
        {
            _isRunning = false;
            UpdateFormInteraction();

            if (commErrorException != null)
                LogException(commErrorException);
        }

        private void psCommSimpleWinForms_MeasurementEnded(object sender, Exception e)
        {
            LogMessage("Measurement ended.");
        }

        private void psCommSimpleWinForms_MeasurementStarted(object sender, EventArgs e)
        {
            LogMessage("Sandbox measurement started.");
        }

        private void psCommSimpleWinForms_ReceiveStatus(object sender, StatusEventArgs e)
        {
            var status = e.GetStatus(); //Get the PalmSens.Comm.Status instance from the event data
            var potential = status.PotentialReading.Value; //Get the potential
            var currentInRange =
                status.CurrentReading.ValueInRange; //Get the current expressed in the active current range
            var currentStatus = status.CurrentReading.ReadingStatus; //Get the status of the current reading
            var cr = status.CurrentReading.CurrentRange; //Get the active current range

            tbPotential.Text = potential.ToString("F3");
            tbCurrent.Text = currentInRange.ToString("F3");
            switch (currentStatus)
            {
                case ReadingStatus.OK:
                    tbCurrent.ForeColor = Color.Black;
                    break;
                case ReadingStatus.Overload:
                    tbCurrent.ForeColor = Color.Red;
                    break;
                case ReadingStatus.Underload:
                    tbCurrent.ForeColor = Color.Yellow;
                    break;
            }

            lblCurrentRange.Text = $"* {cr}";
        }

        private void psCommSimpleWinForms_SimpleCurveStartReceivingData(object sender, SimpleCurve activeSimpleCurve)
        {
            //Subscribe to the curve's events to receive updates when new data is available and when it iss finished receiving data
            activeSimpleCurve.NewDataAdded += activeSimpleCurve_NewDataAdded;
            activeSimpleCurve.CurveFinished += activeSimpleCurve_CurveFinished;

            LogMessage("Curve is receiving new data...");

            var rowIndex = dgvMeasurement.Rows.Add(1);
            dgvMeasurement.Rows[rowIndex].Cells[0].Value = activeSimpleCurve.Title;
        }

        private void psCommSimpleWinForms_StateChanged(object sender, CommManager.DeviceState currentState)
        {
            _isRunning = currentState != CommManager.DeviceState.Idle;
            tbDeviceStatus.Text = currentState.ToString(); //Updates the device state indicator text box
            UpdateFormInteraction();
        }

        private async Task DiscoverConnectedDevicesAsync()
        {
            _connectedDevices.Clear();

            UpdateFormInteraction();
            btnRefresh.Enabled = false;

            try
            {
                psCommSimpleWinForms.EnableBluetooth = chkEnableBluetooth.Checked;

                var devices = await psCommSimpleWinForms.GetConnectedDevicesAsync();
                _connectedDevices.AddRange(devices); //Discover connected devices
                ConfigureDevices();
            }
            finally
            {
                UpdateFormInteraction();
            }
        }

        public void LoadScript(string scriptLocation)
        {
            if (!File.Exists(scriptLocation))
                return;

            var text = File.ReadAllText(scriptLocation);

            SetText(text);
        }

        private void SetText(string text)
        {
            if (!text.Contains('\r'))
                text = text.Replace("\n", Environment.NewLine);

            txtScript.Text = text;
        }

        /// <summary>
        ///     Get the <see cref="Method" /> from the <paramref name="name" />, otherwise the default method
        ///     <see cref="MethodScriptSandbox" /> with the default script
        /// </summary>
        /// <param name="name">The script name.</param>
        /// <returns>A <see cref="Method" /> for the <paramref name="name" /></returns>
        private Method GetMethod(string name)
        {
            switch (name)
            {
                case LinearSweep.Name:
                    return new LinearSweep();
                case CyclicVoltammetry.Name:
                    return new CyclicVoltammetry();
                case DifferentialPulse.Name:
                    return new DifferentialPulse();
                case SquareWave.Name:
                    return new SquareWave();
                case NormalPulse.Name:
                    return new NormalPulse();
                case AmperometricDetection.Name:
                    return new AmperometricDetection();
                case MultistepAmperometry.Name:
                    return new MultistepAmperometry();
                case PulsedAmpDetection.Name:
                    return new PulsedAmpDetection();
                case OpenCircuitPotentiometry.Name:
                    return new OpenCircuitPotentiometry();
                case ImpedimetricMethod.Name:
                    return new ImpedimetricMethod();
                default:
                    return new MethodScriptSandbox {MethodScript = SandboxScript};
            }
        }

        /// <summary>
        ///     Update the form interaction
        /// </summary>
        private void UpdateFormInteraction()
        {
            var connected = psCommSimpleWinForms.Connected;
            btnRun.Enabled = connected && (!_isRunning || rbSandBox.Checked);
            btnRun.Text = _isRunning ? "Stop" : "Run";
            btnRefresh.Enabled = !_isRunning;
            btnConnect.Enabled = _connectedDevices.Count > 0;
            btnConnect.Text = connected ? "Disconnect" : "Connect";
            cmbDevices.Enabled = !connected;

            txtScript.Enabled = !_isRunning;
        }

        private void AddItem(string name)
        {
            cmbMethod.Items.Add(name);
        }

        /// <summary>
        ///     Initializes the data grid view control.
        /// </summary>
        private void InitDataGrid()
        {
            dgvMeasurement.Rows.Clear();
            dgvMeasurement.Columns.Clear();

            var dgvColId = new DataGridViewTextBoxColumn
            {
                HeaderText = "ID",
                AutoSizeMode = DataGridViewAutoSizeColumnMode.AllCells,
                ReadOnly = true
            };

            var dgvColPotential = new DataGridViewTextBoxColumn
            {
                HeaderText = "Potential (V)",
                AutoSizeMode = DataGridViewAutoSizeColumnMode.AllCells,
                ReadOnly = true
            };

            var dgvColCurrent = new DataGridViewTextBoxColumn
            {
                HeaderText = "Current (µA)",
                AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill,
                ReadOnly = true
            };

            dgvMeasurement.Columns.Add(dgvColId);
            dgvMeasurement.Columns.Add(dgvColPotential);
            dgvMeasurement.Columns.Add(dgvColCurrent);
        }

        /// <summary>
        ///     Log an exception
        /// </summary>
        /// <param name="exc">The exception to log</param>
        /// <returns>return true</returns>
        private bool LogException(Exception exc)
        {
            LogMessage(exc.Message);
            return true;
        }

        /// <summary>
        ///     Log a message to the console
        /// </summary>
        /// <param name="message"></param>
        private void LogMessage(string message)
        {
            // Ensure that this method is invoked on the UI thread.
            if (InvokeRequired) Invoke((Action<string>) LogMessage, message);

            foreach (string s in message.Split(new [] { '\n' }, StringSplitOptions.RemoveEmptyEntries))
                lbConsole.Items.Add(s);
        }

        /// <summary>
        ///     Discovers the connected PalmSens & EmStat devices and adds them to the combobox control.
        /// </summary>
        private void ConfigureDevices()
        {
            // Ensure that this method is invoked on the UI thread.
            if (InvokeRequired)
            {
                Invoke((Action) ConfigureDevices);
                return;
            }

            // Update the UI with all devices found.
            cmbDevices.Items.Clear();

            foreach (var d in _connectedDevices)
                cmbDevices.Items.Add(d.ToString()); //Add connected devices to control

            var nDevices = cmbDevices.Items.Count;
            cmbDevices.SelectedIndex = nDevices > 0 ? 0 : -1;

            LogMessage($"Found {nDevices} device(s).");
            UpdateFormInteraction();
        }

        /// <summary>
        ///     Create and set the template text.
        /// </summary>
        private void SetTemplate()
        {
            if (cmbMethod.SelectedIndex < 1)
                return;

            var name = (string) cmbMethod.SelectedItem;
            string script;

            if (name == MethodScriptGetter)
            {
                script = "e\nvar p\nset_gpio_cfg 0b11111111 0\nget_gpio p\npck_start\npck_add p\npck_end\n\n";
            }
            else if (name == MethodScriptSetter)
            {
                script = "e\nset_gpio_cfg 0b11111111 1\nset_gpio 0b10101010i\n\n";
            }
            else
            {
                // Get the method from the name.
                var method = GetMethod(name);
                // Get the method script from the method.
                script = GetMethodScript(method).ToString();
            }

            // Set the script text
            SetText(script);
        }

        /// <summary>
        ///     Get the method script for the specified <see cref="Method" />
        /// </summary>
        /// <param name="method"></param>
        /// <returns></returns>
        private MethodScript GetMethodScript(Method method)
        {
            // If the device is not connected, make use of the the simulator capabilities.
            var capabilities = psCommSimpleWinForms.Connected
                ? psCommSimpleWinForms.Capabilities as MethodScriptDeviceCapabilities
                : new EmStatPicoCapabilitiesSim();

            return method.ToMethodScript(capabilities, psCommSimpleWinForms.Comm?.ClientConnection as ClientConnectionMS);
        }

        /// <summary>
        ///     Send the script to the device.
        /// </summary>
        /// <param name="isGetter">Specify to make use of the getter or setter command</param>
        /// <param name="script"></param>
        /// <returns></returns>
        private async Task SendCommandAsync(bool isGetter, string script)
        {
            // Update UI for running.
            _isRunning = true;
            UpdateFormInteraction();

            // Log message
            LogMessage($"Sending script to device '{psCommSimpleWinForms.Capabilities}', in {(isGetter ? "Getter" : "Setter")} mode");

            // Clean the script by removing all return carriages ('\r')
            var cleanedScript = script.Replace("\r", "");

            try
            {
                // If getter, run getter command on device
                if (isGetter) await SendGetCommand(cleanedScript);
                // else run setter command on device
                else await SendSetCommand(cleanedScript);

                LogMessage("Sending script to device completed.");
            }
            catch (OperationCanceledException)
            {
                // Log of the task has been cancelled.
                LogMessage("Sending script to device has been cancelled.");
            }
            catch (AggregateException aggr)
            {
                // Handle all aggregate exceptions thrown
                aggr.Handle(LogException);
            }
            catch (Exception ex)
            {
                // Handle all other exceptions
                LogException(ex);
            }
            finally
            {
                // Update the UI.
                _isRunning = false;
                UpdateFormInteraction();
            }
        }

        private async Task SendGetCommand(string line)
        {
            // Run the script on the device and get the result.
            var result = await psCommSimpleWinForms.StartGetterMethodScriptAsync(line);
            LogMessage("Getter result:\n" + result);
        }

        private Task SendSetCommand(string line)
        {
            // Run a fire and forget script to the device.
            return psCommSimpleWinForms.StartSetterMethodScriptAsync(line);
        }
    }
}