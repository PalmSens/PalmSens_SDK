using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using PalmSens;
using PalmSens.Core.Simplified.InternalStorage;
using PalmSens.Data;
using PalmSens.Devices;

namespace PSSDKInternalStorageAsyncExample
{
    public partial class FrmInternalStorageBrowser : Form
    {
        /// <summary>
        ///     The contents of the current directory on the internal storage
        /// </summary>
        //private List<DeviceFile> _contents = new List<DeviceFile>();
        private readonly IDictionary<int, IInternalStorageItem> _contents;

        /// <summary>
        ///     The connected PalmSens & EmStat devices
        /// </summary>
        private Device[] _connectedDevices = new Device[0];

        /// <summary>
        ///     The measuring
        /// </summary>
        private bool _retrievedMeasurementFromStorage;

        /// <summary>
        ///     The contents of the current root
        /// </summary>
        //private List<DeviceFile> _contents = new List<DeviceFile>();
        private IInternalStorageFolder _root;

        public FrmInternalStorageBrowser()
        {
            InitializeComponent();
            _contents = new Dictionary<int, IInternalStorageItem>();
        }

        /// <summary>
        ///     Handles the Click event of the btnConnect control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private async void btnConnect_Click(object sender, EventArgs e)
        {
            try
            {
                UpdateFormControls(true);
                _root = null;
                ClearInternalStorageList();

                if (psCommSimpleWinForms.Connected)
                {
                    await psCommSimpleWinForms.DisconnectAsync(); //Disconnect from the connected device
                    LogMessage("Disconnected");
                }
                else
                {
                    if (cmbDevices.SelectedIndex == -1)
                        return;

                    //Connect to the device selected in the devices combobox control
                    await psCommSimpleWinForms.ConnectAsync(_connectedDevices[cmbDevices.SelectedIndex]);
                    LogMessage($"Connected to {psCommSimpleWinForms.ConnectedDevice}");
                }
            }
            catch (Exception exception)
            {
                LogMessage(exception);
            }
            finally
            {
                UpdateFormControls(false);
            }

            switch (psCommSimpleWinForms.Connected)
            {
                case true when psCommSimpleWinForms.Capabilities.SupportsStorage:
                    await GetSpaceUsedAsync();
                    break;
                case true:
                    LogMessage("The connected device does not support internal storage features");
                    break;
            }
        }

        /// <summary>
        ///     Handles the Click event of the btnListFiles control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private async void btnListFiles_Click(object sender, EventArgs e)
        {
            UpdateFormControls(true);
            try
            {
                LogMessage("Reading contents from: Root");

                _root = await psCommSimpleWinForms.GetInternalStorageBrowser().GetRootAsync();

                await LoadChildrenAsync(_root);
            }
            catch (Exception exception)
            {
                LogMessage(exception);
            }
            finally
            {
                UpdateFormControls(false);
            }
        }

        /// <summary>
        ///     Handles the Click event of the btnOpen control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private async void btnOpen_Click(object sender, EventArgs e)
        {
            if (_root == null || _contents.Count == 0) return;

            await OpenItemAsync();
        }

        /// <summary>
        ///     Handles the Click event of the btnRefresh control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private async void btnRefresh_Click(object sender, EventArgs e)
        {
            if (psCommSimpleWinForms.Connected) return;

            UpdateFormControls(true);

            try
            {
                await DiscoverConnectedDevicesAsync(); //Add connected devices to the devices combobox control
            }
            catch (Exception exception)
            {
                LogMessage(exception);
            }
            finally
            {
                UpdateFormControls(false);
            }
        }

        /// <summary>
        ///     Clear the internal storage display list
        /// </summary>
        private void ClearInternalStorageList()
        {
            _contents.Clear();
            InvokeAction(() => lbInternalStorage.Items.Clear());
        }

        /// <summary>
        ///     Discovers the connected PalmSens & EmStat devices and adds them to the combobox control.
        /// </summary>
        private async Task DiscoverConnectedDevicesAsync()
        {
            try
            {
                UpdateFormControls(true);
                _connectedDevices = await psCommSimpleWinForms.GetConnectedDevicesAsync(); //Discover connected devices

                InvokeAction(() =>
                {
                    cmbDevices.Items.Clear();
                    foreach (var d in _connectedDevices)
                        cmbDevices.Items.Add(d.ToString()); //Add connected devices to control

                    var nDevices = cmbDevices.Items.Count;
                    cmbDevices.SelectedIndex = nDevices > 0 ? 0 : -1;
                    LogMessage($"Found {nDevices} device(s).");
                });
            }
            catch (Exception exception)
            {
                LogMessage(exception);
            }
            finally
            {
                UpdateFormControls(false);
            }
        }

        /// <summary>
        ///     On form load, discover connected devices.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private async void FrmInternalStorageBrowser_Load(object sender, EventArgs e)
        {
            await DiscoverConnectedDevicesAsync();
        }

        /// <summary>
        ///     Gets the % of space used on the device.
        /// </summary>
        /// <exception cref="System.NotImplementedException"></exception>
        private async Task GetSpaceUsedAsync()
        {
            var total = (int) await psCommSimpleWinForms.Comm.ClientConnection.GetDeviceSizeAsync();
            var free = (int) await psCommSimpleWinForms.Comm.ClientConnection.GetDeviceFreeAsync();

            var perc = Math.Min((total - free) / (double) total, 1.0);
            LogMessage($"{(int) Math.Round(perc * 100.0):F2}% of storage space used.");
        }

        private void InvokeAction(Action action)
        {
            if (InvokeRequired)
            {
                BeginInvoke(action);
                return;
            }

            action();
        }

        /// <summary>
        ///     Open the storage item when mouse double click
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private async void lbInternalStorage_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            var index = lbInternalStorage.IndexFromPoint(e.Location);
            if (index == ListBox.NoMatches) return;

            await OpenItemAsync();
        }

        /// <summary>
        ///     Update the num list when the selected index changes.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void lbInternalStorage_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (lbInternalStorage.SelectedIndex == -1) return;

            var index = lbInternalStorage.SelectedIndex;
            if (_contents.Count <= 1) index++;

            numUDTargetItem.Value = index;
        }

        /// <summary>
        ///     List the internal storage item
        /// </summary>
        /// <param name="item"></param>
        /// <param name="index"></param>
        private void ListInternalStorageItem(IInternalStorageItem item, int index)
        {
            var type = item.ItemType == DeviceFileType.Folder ? "<Dir>" : "<File>";
            InvokeAction(() => lbInternalStorage.Items.Add($"{index}. {type} {item.Name}"));
        }

        /// <summary>
        ///     List the parent item.
        /// </summary>
        /// <param name="parent"></param>
        private void ListPreviousItem(IInternalStorageItem parent)
        {
            _contents[0] = parent;
            InvokeAction(() => lbInternalStorage.Items.Add($"0. <Back> {parent.Name}"));
        }

        /// <summary>
        ///     Load the children for the selected folder.
        /// </summary>
        /// <param name="item"></param>
        /// <returns></returns>
        private async Task LoadChildrenAsync(IInternalStorageItem item)
        {
            if (item.ItemType == DeviceFileType.Measurement) return;

            ClearInternalStorageList();

            var folder = (IInternalStorageFolder) item;
            var files = await folder.GetFilesAsync();
            var subFolders = await folder.GetSubFoldersAsync();
            var totalItems = files.Count + subFolders.Count;
            var hasParent = !ReferenceEquals(item, _root);

            numUDTargetItem.Enabled = totalItems > 0;
            btnOpen.Enabled = numUDTargetItem.Enabled;
            numUDTargetItem.Value = totalItems > 0 ? 1 : 0;
            numUDTargetItem.Minimum = hasParent ? 0 : 1;
            numUDTargetItem.Maximum = totalItems;

            LogMessage($"Loading {totalItems} storage items.");

            if (hasParent)
                ListPreviousItem(folder.Parent);
            var currentIndex = LoadChildrenItems(subFolders, 1);
            LoadChildrenItems(files, currentIndex);
        }

        /// <summary>
        ///     Add all the items to the form
        /// </summary>
        /// <param name="items"></param>
        /// <param name="index"></param>
        /// <returns></returns>
        private int LoadChildrenItems(IEnumerable<IInternalStorageItem> items, int index)
        {
            foreach (var item in items.OrderBy(i => i.Name))
            {
                ListInternalStorageItem(item, index);
                _contents[index] = item;
                index++;
            }

            return index;
        }

        /// <summary>
        ///     Log an error message
        /// </summary>
        /// <param name="exception"></param>
        private void LogMessage(Exception exception)
        {
            LogMessage($"An error occurred: {exception.Message}");
        }

        /// <summary>
        ///     Log a message
        /// </summary>
        /// <param name="message"></param>
        private void LogMessage(string message)
        {
            InvokeAction(() => lbConsole.SelectedIndex = lbConsole.Items.Add(message));
        }

        /// <summary>
        ///     Update the selected item when the number has been changed.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void numUDTargetItem_ValueChanged(object sender, EventArgs e)
        {
            if (lbInternalStorage.Items.Count == 0) return;

            var index = (int) numUDTargetItem.Value;
            if (_contents.Count <= 1) index--;

            lbInternalStorage.SelectedIndex = index;
        }

        /// <summary>
        ///     Open the internal storage item.
        /// </summary>
        /// <returns></returns>
        private async Task OpenItemAsync()
        {
            UpdateFormControls(true);

            try
            {
                if (numUDTargetItem.Value < 0 || numUDTargetItem.Value > _contents.Count)
                {
                    LogMessage("The item at the specified position does not exist");
                    return;
                }

                var item = _contents[(int) numUDTargetItem.Value];

                if (item.ItemType == DeviceFileType.Folder)
                {
                    LogMessage($"Opening path: {item.Name}");
                    await LoadChildrenAsync(item);
                }
                else
                {
                    var file = (IInternalStorageFile) item;
                    var m = await file.GetMeasurementAsync(MeasType.Overlay);

                    LogMessage(m != null ? $"Load file '{item.Name}', with method '{m.Method}'" : $"Could not load file '{item.Name}'");
                }
            }
            catch (Exception exception)
            {
                LogMessage(exception);
            }
            finally
            {
                UpdateFormControls(false);
            }
        }

        /// <summary>
        ///     Update the form UI controls.
        /// </summary>
        /// <param name="interaction"></param>
        private void UpdateFormControls(bool interaction)
        {
            if (InvokeRequired)
            {
                BeginInvoke((Action<bool>) UpdateFormControls, interaction);
                return;
            }

            cmbDevices.Enabled = !interaction && !psCommSimpleWinForms.Connected;
            btnRefresh.Enabled = !interaction && !psCommSimpleWinForms.Connected;
            btnConnect.Text = !interaction & psCommSimpleWinForms.Connected ? "Disconnect" : "Connect";
            btnConnect.Enabled = !interaction && cmbDevices.Items.Count > 0;
            btnListFiles.Enabled = !interaction && psCommSimpleWinForms.Connected && psCommSimpleWinForms.Capabilities.SupportsStorage;
            btnOpen.Enabled = !interaction && psCommSimpleWinForms.Connected;
        }
    }
}