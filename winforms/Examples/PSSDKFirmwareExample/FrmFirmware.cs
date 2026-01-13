using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using PalmSens.Comm;
using PalmSens.Core.Simplified.WinForms.DeviceFirmware;
using PalmSens.Devices;

namespace PSSDKFirmwareExample
{
    public partial class FrmFirmware : Form
    {
        /// <summary>
        /// The firmware extensions
        /// </summary>
        private const string FileListExtension = "Firmware Files (*.hex, *.bin)|*.hex;*.bin|All Files (*.*)|*.*";
        private readonly List<Device> _connectedDevices;
        private readonly StringBuilder _currentDeviceInfo;
        private bool _discovering;
        private IFirmwareManager _firmwareManager;
        private enumDeviceType _selectedDeviceType;
        private bool _updating;

        public FrmFirmware()
        {
            InitializeComponent();
            _connectedDevices = new List<Device>();
            _currentDeviceInfo = new StringBuilder();
        }

        private void btnLoadFile_Click(object sender, EventArgs e)
        {
            // Open file dialog
            using (var fileDialog = new OpenFileDialog())
            {
                // Specify that the file must exist.
                fileDialog.CheckPathExists = true;
                // Specify extensions filter
                fileDialog.Filter = FileListExtension;
                
                // Show file dialog
                var result = fileDialog.ShowDialog(this);

                if (result == DialogResult.OK)
                {
                    // If a file has been selected. create the firmware manager.
                    txtFileLocation.Text = fileDialog.FileName;
                    _firmwareManager = FirmwareManager.CreateManager(fileDialog.FileName);
                }
            }

            UpdateFirmWareInfo();
            UpdateFormControls();
            UpdateStatus(FirmwareUploadStatus.None);
            UpdateDownloadProgress(0, 1);
        }

        private async void btnRefresh_Click(object sender, EventArgs e)
        {
            await DiscoverConnectedDevicesAsync();
        }

        private async void btnUpload_Click(object sender, EventArgs e)
        {
            // Do nothing if no firmware manager or selected device.
            if (_firmwareManager == null || cmbDevices.SelectedIndex < 0) return;

            // Validate that the selected device can be used by the firmware.
            if (!_firmwareManager.Validate(_selectedDeviceType))
            {
                // Log and show an error message when the device is not supported.
                var message = $"The selected device {_selectedDeviceType} is not supported by the firmware.";
                LogMessage(message);
                MessageBox.Show(message, "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                return;
            }

            // Update the controls for the form.
            _updating = true;
            UpdateFormControls();
            IDeviceFirmwareUploader uploader = null;

            try
            {
                // Get the selected device.
                var device = _connectedDevices[cmbDevices.SelectedIndex];
                // Set the device in download mode and get its uploader.
                uploader = await _firmwareManager.SetDeviceInDownloadModeAndGetDeviceFirmwareUploader(device);
                // Subscribe to the uploader events.
                uploader.Progress += Uploader_Progress;
                uploader.Message += Uploader_Message;

                // Upload the firmware to the device.
                await uploader.UploadAsync();
            }
            catch(Exception exception)
            {
                // Log and display any errors that have occurred.
                LogException(exception);
                MessageBox.Show($"And error occurred while trying to upload the new firmware, {exception}");
            }
            finally
            {
                _updating = false;
                // Discover devices, this will display the updated device information.
                await DiscoverConnectedDevicesAsync();
                UpdateFormControls();
                UpdateFirmWareInfo();
                UpdateStatus(FirmwareUploadStatus.None);
                // Unsubscribe from the uploader and dispose.
                if (uploader != null)
                {
                    uploader.Progress -= Uploader_Progress;
                    uploader.Message -= Uploader_Message;
                    uploader.Dispose();
                }
            }
        }

        private async void FrmFirmware_Load(object sender, EventArgs e)
        {
            // On form load, discover connected devices.
            await DiscoverConnectedDevicesAsync();
            // Update the status and download status to default.
            UpdateStatus(FirmwareUploadStatus.None);
            UpdateDownloadProgress(0, 0);
        }

        private void psCommSimpleWinForms_Disconnected(object sender, Exception commErrorException)
        {
            // Update form when device disconnects
            LogMessage("Disconnected from device.");

            // Log any errors
            if (commErrorException != null) LogException(commErrorException);

            UpdateFormControls();
        }

        private void Uploader_Message(object sender, DeviceFirmwareUploaderMessageEventArgs e)
        {
            // Log uploader messages and status.
            LogMessage(e.ToString());
            UpdateStatus(e.Status);
        }

        private void Uploader_Progress(object sender, DeviceFirmwareUploaderProgressEventArgs e)
        {
            // Update the uploader status.
            UpdateDownloadProgress(e.Current, e.Total);
            UpdateStatus(e.Status);
        }

        private async Task DisconnectAsync()
        {
            await psCommSimpleWinForms.DisconnectAsync();
        }

        /// <summary>
        /// Update the download progress
        /// </summary>
        /// <param name="current">The current amount.</param>
        /// <param name="total">The total.</param>
        private void UpdateDownloadProgress(int current, int total)
        {
            if (InvokeRequired)
            {
                Invoke((Action<int, int>) UpdateDownloadProgress, current, total);
                return;
            }

            pgsBarUpload.Maximum = total;
            pgsBarUpload.Value = current;
        }

        /// <summary>
        /// Update the status of the uploader.
        /// </summary>
        /// <param name="status"></param>
        private void UpdateStatus(FirmwareUploadStatus status)
        {
            if (InvokeRequired)
            {
                Invoke((Action<FirmwareUploadStatus>) UpdateStatus, status);
                return;
            }

            lblCurrentStatus.Text = status == FirmwareUploadStatus.None ? "" : status.ToString();
        }

        /// <summary>
        ///     Discovers the connected PalmSens & EmStat devices and adds them to the combobox control.
        /// </summary>
        private async Task DiscoverConnectedDevicesAsync()
        {
            // Ignore if connected to a device.
            if (psCommSimpleWinForms.Connected)
                return;

            // Clear controls
            cmbDevices.Items.Clear();
            _connectedDevices.Clear();

            LogMessage("Searching for devices.");
            
            // Update form controls, prevent interaction
            _discovering = true;
            UpdateFormControls();
            btnRefresh.Enabled = false;

            try
            {
                // Get connected devices list.
                var devices = await psCommSimpleWinForms.GetConnectedDevicesAsync(); //Discover connected devices

                // Add the devices
                foreach (var device in devices)
                {
                    _connectedDevices.Add(device);
                    cmbDevices.Items.Add(device.ToString()); //Add connected devices to control
                }

                // Set the initial selection
                var nDevices = cmbDevices.Items.Count;
                cmbDevices.SelectedIndex = nDevices > 0 ? 0 : -1;

                LogMessage($"Found {nDevices} device(s).");
            }
            finally
            {
                // Reset controls
                UpdateFormControls();
                _discovering = false;
            }

            // Get device info
            await GetDeviceInfo();
        }

        private void UpdateFormControls()
        {
            if (InvokeRequired)
            {
                Invoke((Action) UpdateFormControls);
                return;
            }

            // Get an indicator if the comms is connected.
            var connected = psCommSimpleWinForms.Connected;

            // Enable refresh button if not connected or updating.
            btnRefresh.Enabled = !connected && !_updating;
            // Enable upload button if valid device, has selected device and firmware selected.
            btnUpload.Enabled = _connectedDevices.Count > 0 && cmbDevices.SelectedIndex >= 0 && _firmwareManager != null && !_updating && CheckDeviceAndWarn(_selectedDeviceType);
        }

        /// <summary>
        /// Update the firmware info
        /// </summary>
        private void UpdateFirmWareInfo()
        {
            var builder = new StringBuilder();

            // Update the current selected device info if selected.
            if (_currentDeviceInfo.Length > 0) builder.AppendLine(_currentDeviceInfo.ToString());
            // Update the current firmware info if selected.
            if (_firmwareManager != null) builder.Append(_firmwareManager);

            // Update firmware text with all info
            txtFirmware.Text = builder.ToString().Trim();
        }

        /// <summary>
        /// Log a message to the log.
        /// </summary>
        /// <param name="message"></param>
        private void LogMessage(string message)
        {
            if (InvokeRequired)
            {
                Invoke((Action<string>) LogMessage, message);
                return;
            }

            // Log the message to the console.
            lbConsole.SelectedIndex = lbConsole.Items.Add(message);
        }

        /// <summary>
        /// Log an error
        /// </summary>
        /// <param name="e">The error to log.</param>
        /// <returns></returns>
        private bool LogException(Exception e)
        {
            LogMessage(e.ToString());
            return true;
        }

        /// <summary>
        /// Connect to the device.
        /// </summary>
        /// <returns></returns>
        private async Task ConnectAsync()
        {
            // Ignore if already connected.
            if (psCommSimpleWinForms.Connected) return;

            try
            {
                // Get the selected device.
                var device = _connectedDevices[cmbDevices.SelectedIndex];
                // Connect to the device
                await psCommSimpleWinForms.ConnectAsync(device);

                LogMessage($"Connected to {psCommSimpleWinForms.ConnectedDevice}");
            }
            // Handle any exceptions that occur
            catch (AggregateException a)
            {
                a.Handle(LogException);
            }
            catch (Exception exc)
            {
                LogException(exc);
            }
        }

        /// <summary>
        /// Handle device selection.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private async void cmbDevices_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (_updating || _discovering) return;

            try
            {
                // Get the device info
                await GetDeviceInfo();
            }
            // Handle any exceptions that occur
            catch (Exception exception)
            {
                LogException(exception);
            }
        }

        private async Task GetDeviceInfo()
        {
            cmbDevices.Enabled = false;
            btnUpload.Enabled = false;
            // Clear the device info builder.
            _currentDeviceInfo.Clear();
            // Reset the selected device.
            _selectedDeviceType = enumDeviceType.None;
            try
            {
                // Connect if a device is selected.
                if (cmbDevices.SelectedIndex < 0) return;
            
                // Connect
                await ConnectAsync();

                if (psCommSimpleWinForms.Connected)
                {
                    // Get the connected device type
                    _selectedDeviceType = psCommSimpleWinForms.ConnectedDevice;

                    // Validate if the device type is supported and warn, do not prevent interaction.
                    if(!CheckDeviceAndWarn(_selectedDeviceType)) LogMessage($"The device {_selectedDeviceType} is currently not supported.");

                    // Check of the device is a MethodScript device, they currently only devices that use the binary format.
                    var isMsDevice = psCommSimpleWinForms.Comm.ClientConnection is ClientConnectionMS;

                    // Create device info
                    _currentDeviceInfo.AppendLine("Device Information:")
                        .Append("   Connected device: ").Append(psCommSimpleWinForms.ConnectedDevice).AppendLine()
                        .Append("   Firmware version: ").AppendLine(psCommSimpleWinForms.Capabilities.FirmwareVersion.ToString(isMsDevice ? "0.000" : "0.0"))
                        .Append("   Firmware build date: ").Append(psCommSimpleWinForms.Capabilities.FirmwareTimeStamp);

                    if (!string.IsNullOrEmpty(psCommSimpleWinForms.Capabilities.SpecialFirmwareDescription))
                        _currentDeviceInfo.AppendLine()
                            .Append($"   Special firmware description: {psCommSimpleWinForms.Capabilities.SpecialFirmwareDescription}");
                }
            }
            finally
            {
                // Disconnect if needed.
                await DisconnectAsync();

                // Update form details.
                UpdateFirmWareInfo();
                UpdateFormControls();
                UpdateStatus(FirmwareUploadStatus.None);
                UpdateDownloadProgress(0, 1);
                cmbDevices.Enabled = true;
            }
        }

        private bool CheckDeviceAndWarn(enumDeviceType deviceType)
        {
            // The list below is the current list of untested devices.
            switch (deviceType)
            {
                case enumDeviceType.Unknown:
                case enumDeviceType.None:
                case enumDeviceType.PalmSens:
                case enumDeviceType.EmStat1:
                case enumDeviceType.EmStat2:
                case enumDeviceType.PalmSens3:
                case enumDeviceType.EmStat2BP:
                    return false;
            }

            return true;
        }
    }
}