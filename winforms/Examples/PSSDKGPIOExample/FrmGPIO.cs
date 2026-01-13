using System;
using System.Collections.Generic;
using System.Drawing;
using System.Threading.Tasks;
using System.Windows.Forms;
using PalmSens.Comm;
using PalmSens.Devices;

namespace PSSDKGPIOExample
{
    public partial class FrmGPIO : Form
    {
        private readonly List<Device> _connectedDevices;
        private bool _isRunning;

        public FrmGPIO()
        {
            InitializeComponent();
            _connectedDevices = new List<Device>();
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
                catch (AggregateException aggr)
                {
                    aggr.Handle(LogException);
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

            UpdateFormSelectionControls();
        }

        private async void btnGetGPIO_Click(object sender, EventArgs e)
        {
            _isRunning = true;
            UpdateFormSelectionControls();

            try
            {
                // Prevent script from running if device is not a method script device.
                if (!(psCommSimpleWinForms.Capabilities is MethodScriptDeviceCapabilities))
                {
                    MessageBox.Show($"The device '{psCommSimpleWinForms.Capabilities}' does not support method method script");
                    return;
                }

                // Check state of device.
                if (psCommSimpleWinForms.DeviceState != CommManager.DeviceState.Idle)
                {
                    return;
                }

                // generate the input pin config
                var bitMask = GenerateInputPinConfig();
                // Get the input values from the device.
                var result = await psCommSimpleWinForms.ReadDigitalLineAsync(bitMask);

                UpdatePinValues(bitMask, result);

                LogMessage($"Read GPIO result: {ConvertIntToBinary(result)}");
            }
            catch (AggregateException aggr)
            {
                aggr.Handle(LogException);
            }
            catch (Exception ex)
            {
                LogException(ex);
            }
            finally
            {
                _isRunning = false;
                UpdateFormSelectionControls();
            }
        }

        private async void btnRefresh_Click(object sender, EventArgs e)
        {
            if (_isRunning)
                return;

            await DiscoverConnectedDevices();
        }

        private async void btnSet_Click(object sender, EventArgs e)
        {
            _isRunning = true;
            UpdateFormSelectionControls();

            try
            {
                var bitMask = GenerateOutputPinValues();
                var configGPIO = GenerateOutputPinConfig();
                await psCommSimpleWinForms.SetDigitalOutputAsync(bitMask, configGPIO);
                LogMessage("Set GPIO completed.");
            }
            catch (AggregateException aggr)
            {
                aggr.Handle(LogException);
            }
            catch (Exception ex)
            {
                LogException(ex);
            }
            finally
            {
                _isRunning = false;
                UpdateFormSelectionControls();
            }
        }

        private void cmbDevices_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (psCommSimpleWinForms.Connected)
                return;

            UpdateFormSelectionControls();
        }

        private async void FrmGPIO_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (psCommSimpleWinForms.Connected)
                await psCommSimpleWinForms.DisconnectAsync();
        }

        private async void FrmGPIO_Load(object sender, EventArgs e)
        {
            await DiscoverConnectedDevices();
            UpdateFormSelectionControls();
            UpdatePinInputControls();
        }

        private void psCommSimpleWinForms_Disconnected(object sender, Exception commErrorException)
        {
            _isRunning = false;
            UpdateFormSelectionControls();

            if (commErrorException != null)
                LogException(commErrorException);
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

        private void psCommSimpleWinForms_StateChanged(object sender, CommManager.DeviceState currentState)
        {
            _isRunning = currentState != CommManager.DeviceState.Idle;
            tbDeviceStatus.Text = currentState.ToString(); //Updates the device state indicator text box
            UpdateFormSelectionControls();
        }

        private void radioPin_CheckedChanged(object sender, EventArgs e)
        {
            UpdatePinInputControls();
        }

        /// <summary>
        /// Update the pin with the get result.
        /// </summary>
        /// <param name="inputMask"></param>
        /// <param name="result"></param>
        private void UpdatePinValues(byte inputMask, uint result)
        {
            UpdatePinOutput(inputMask, result, rbLowPin1, rbHighPin1, chkIsOutputPin1, 1 << 0);
            UpdatePinOutput(inputMask, result, rbLowPin2, rbHighPin2, chkIsOutputPin2, 1 << 1);
            UpdatePinOutput(inputMask, result, rbLowPin3, rbHighPin3, chkIsOutputPin3, 1 << 2);
            UpdatePinOutput(inputMask, result, rbLowPin4, rbHighPin4, chkIsOutputPin4, 1 << 3);
            UpdatePinOutput(inputMask, result, rbLowPin5, rbHighPin5, chkIsOutputPin5, 1 << 4);
            UpdatePinOutput(inputMask, result, rbLowPin6, rbHighPin6, chkIsOutputPin6, 1 << 5);
            UpdatePinOutput(inputMask, result, rbLowPin7, rbHighPin7, chkIsOutputPin7, 1 << 6);
            UpdatePinOutput(inputMask, result, rbLowPin8, rbHighPin8, chkIsOutputPin8, 1 << 7);
        }

        private void UpdatePinOutput(byte inputMask, uint result, RadioButton low, RadioButton high, CheckBox isOutput, byte pin)
        {
            isOutput.Checked = (inputMask & pin) != pin;

            high.Checked = (result & pin) == pin;
            low.Checked = !high.Checked;
        }

        /// <summary>
        ///     Discovers the connected PalmSens & EmStat devices and adds them to the combobox control.
        /// </summary>
        private async Task DiscoverConnectedDevices()
        {
            _connectedDevices.Clear();

            UpdateFormSelectionControls();
            btnRefresh.Enabled = false;

            try
            {
                var devices = await psCommSimpleWinForms.GetConnectedDevicesAsync();
                _connectedDevices.AddRange(devices); //Discover connected devices
                ConfigureDevices();
            }
            finally
            {
                UpdateFormSelectionControls();
            }
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
        }

        /// <summary>
        /// Generate the bitmask for the input pin config
        /// </summary>
        /// <returns></returns>
        private byte GenerateInputPinConfig()
        {
            byte bitMask = 0;
            bitMask |= GetBitMaskValueIfEnabled(radioPin1Get.Checked, true, 0);
            bitMask |= GetBitMaskValueIfEnabled(radioPin2Get.Checked, true, 1);
            bitMask |= GetBitMaskValueIfEnabled(radioPin3Get.Checked, true, 2);
            bitMask |= GetBitMaskValueIfEnabled(radioPin4Get.Checked, true, 3);
            bitMask |= GetBitMaskValueIfEnabled(radioPin5Get.Checked, true, 4);
            bitMask |= GetBitMaskValueIfEnabled(radioPin6Get.Checked, true, 5);
            bitMask |= GetBitMaskValueIfEnabled(radioPin7Get.Checked, true, 6);
            bitMask |= GetBitMaskValueIfEnabled(radioPin8Get.Checked, true, 7);

            return bitMask;
        }

        /// <summary>
        /// Generate the bitmask for the output config
        /// </summary>
        /// <returns></returns>
        private byte GenerateOutputPinConfig()
        {
            byte bitMask = 0;
            bitMask |= GetBitMaskValueIfEnabled(radioPin1Set.Checked, true, 0);
            bitMask |= GetBitMaskValueIfEnabled(radioPin2Set.Checked, true, 1);
            bitMask |= GetBitMaskValueIfEnabled(radioPin3Set.Checked, true, 2);
            bitMask |= GetBitMaskValueIfEnabled(radioPin4Set.Checked, true, 3);
            bitMask |= GetBitMaskValueIfEnabled(radioPin5Set.Checked, true, 4);
            bitMask |= GetBitMaskValueIfEnabled(radioPin6Set.Checked, true, 5);
            bitMask |= GetBitMaskValueIfEnabled(radioPin7Set.Checked, true, 6);
            bitMask |= GetBitMaskValueIfEnabled(radioPin8Set.Checked, true, 7);

            return bitMask;
        }

        /// <summary>
        /// Generate the bitmask for the output pin high
        /// </summary>
        /// <returns></returns>
        private byte GenerateOutputPinValues()
        {
            byte bitMask = 0;
            bitMask |= GetBitMaskValueIfEnabled(radioPin1Set.Checked, chkPin1SetHigh.Checked, 0);
            bitMask |= GetBitMaskValueIfEnabled(radioPin2Set.Checked, chkPin2SetHigh.Checked, 1);
            bitMask |= GetBitMaskValueIfEnabled(radioPin3Set.Checked, chkPin3SetHigh.Checked, 2);
            bitMask |= GetBitMaskValueIfEnabled(radioPin4Set.Checked, chkPin4SetHigh.Checked, 3);
            bitMask |= GetBitMaskValueIfEnabled(radioPin5Set.Checked, chkPin5SetHigh.Checked, 4);
            bitMask |= GetBitMaskValueIfEnabled(radioPin6Set.Checked, chkPin6SetHigh.Checked, 5);
            bitMask |= GetBitMaskValueIfEnabled(radioPin7Set.Checked, chkPin7SetHigh.Checked, 6);
            bitMask |= GetBitMaskValueIfEnabled(radioPin8Set.Checked, chkPin8SetHigh.Checked, 7);

            return bitMask;
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

            lbConsole.SelectedIndex = lbConsole.Items.Add(message);
        }

        /// <summary>
        ///     Get the bit mask value for the specified <paramref name="bitNumber" /> if the bit is <paramref name="enabled" />
        /// </summary>
        /// <param name="enabled">Specified if the pin is enabled.</param>
        /// <param name="enableMask">Only get the bitmask if enabled.</param>
        /// <param name="bitNumber">Which bit the mask must be created for.</param>
        /// <returns>Return the bitmask if enabled or 0 if disabled.</returns>
        private byte GetBitMaskValueIfEnabled(bool enabled, bool enableMask, byte bitNumber)
        {
            if (!enabled || !enableMask)
                return 0;

            const byte bit = 1;

            return (byte) (bit << bitNumber);
        }

        /// <summary>
        /// Update the form selection controls.
        /// </summary>
        private void UpdateFormSelectionControls()
        {
            var connected = psCommSimpleWinForms.Connected;
            var methodScriptEnabled = connected && psCommSimpleWinForms.Capabilities is MethodScriptDeviceCapabilities;
            btnGet.Enabled = methodScriptEnabled && !_isRunning;
            btnSet.Enabled = methodScriptEnabled && !_isRunning;
            btnRefresh.Enabled = !connected;
            btnConnect.Enabled = _connectedDevices.Count > 0;
            btnConnect.Text = connected ? "Disconnect" : "Connect";
            cmbDevices.Enabled = !connected;
        }

        /// <summary>
        /// Update the checkbox enabled.
        /// </summary>
        /// <param name="isChecked"></param>
        /// <param name="pinHighCheckBox"></param>
        private void UpdatePinInputControl(bool isChecked, CheckBox pinHighCheckBox)
        {
            pinHighCheckBox.Enabled = isChecked;
        }

        /// <summary>
        /// Update the pin input controls
        /// </summary>
        private void UpdatePinInputControls()
        {
            UpdatePinInputControl(radioPin1Set.Checked, chkPin1SetHigh);
            UpdatePinInputControl(radioPin2Set.Checked, chkPin2SetHigh);
            UpdatePinInputControl(radioPin3Set.Checked, chkPin3SetHigh);
            UpdatePinInputControl(radioPin4Set.Checked, chkPin4SetHigh);
            UpdatePinInputControl(radioPin5Set.Checked, chkPin5SetHigh);
            UpdatePinInputControl(radioPin6Set.Checked, chkPin6SetHigh);
            UpdatePinInputControl(radioPin7Set.Checked, chkPin7SetHigh);
            UpdatePinInputControl(radioPin8Set.Checked, chkPin8SetHigh);
        }

        /// <summary>
        /// Convert an <see cref="uint"/> to a string binary representation 
        /// </summary>
        /// <param name="bitMask">The bit mask value to convert</param>
        /// <returns>A bit string representation of the <paramref name="bitMask"/></returns>
        private static string ConvertIntToBinary(uint bitMask)
        {
            return Convert.ToString(bitMask, 2);
        }
    }
}