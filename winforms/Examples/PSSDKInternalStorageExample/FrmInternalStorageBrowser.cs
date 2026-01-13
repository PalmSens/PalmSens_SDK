using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using PalmSens;
using PalmSens.Core.Simplified.Data;
using PalmSens.Core.Simplified.InternalStorage;
using PalmSens.Data;
using PalmSens.Devices;

namespace PSSDKInternalStorageExample
{
    public partial class FrmInternalStorageBrowser : Form
    {
        /// <summary>
        ///     The contents of the current directory on the internal storage
        /// </summary>
        private readonly IDictionary<int, IInternalStorageItem> _contents;

        /// <summary>
        ///     The connected PalmSens & EmStat devices
        /// </summary>
        private Device[] _connectedDevices = new Device[0];

        /// <summary>
        ///     The contents of the current root
        /// </summary>
        //private List<DeviceFile> _contents = new List<DeviceFile>();
        private IInternalStorageFolder _root;

        public FrmInternalStorageBrowser()
        {
            InitializeComponent();
            DiscoverConnectedDevices();
            _contents = new Dictionary<int, IInternalStorageItem>();
        }

        /// <summary>
        ///     Handles the Click event of the btnConnect control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
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
                    LogMessage($"Connected to {psCommSimpleWinForms.ConnectedDevice.ToString()}");
                }
                catch (Exception ex)
                {
                    LogMessage(ex.Message);
                }
            }
            else
            {
                psCommSimpleWinForms.Disconnect(); //Disconnect from the connected device
                LogMessage("Disconnected");
            }

            //Update UI based on connection status
            cmbDevices.Enabled = !psCommSimpleWinForms.Connected;
            btnRefresh.Enabled = !psCommSimpleWinForms.Connected;
            btnConnect.Text = psCommSimpleWinForms.Connected ? "Disconnect" : "Connect";
            btnListFiles.Enabled = psCommSimpleWinForms.Connected && psCommSimpleWinForms.Capabilities.SupportsStorage;

            if (psCommSimpleWinForms.Connected && psCommSimpleWinForms.Capabilities.SupportsStorage)
                GetSpaceUsed();
            else if (psCommSimpleWinForms.Connected)
                LogMessage("The connected device does not support internal storage features");
        }

        /// <summary>
        ///     Handles the Click event of the btnListFiles control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private void btnListFiles_Click(object sender, EventArgs e)
        {
            // Clear all nodes
            LogMessage("Reading contents from: Root");

            _root = psCommSimpleWinForms.GetInternalStorageBrowser().GetRoot();

            LoadChildren(_root);
        }

        /// <summary>
        ///     Handles the Click event of the btnOpen control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private void btnOpen_Click(object sender, EventArgs e)
        {
            OpenItem();
        }

        /// <summary>
        ///     Handles the Click event of the btnRefresh control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
        private void btnRefresh_Click(object sender, EventArgs e)
        {
            DiscoverConnectedDevices(); //Add connected devices to the devices combobox control
        }

        /// <summary>
        ///     Discovers the connected PalmSens & EmStat devices and adds them to the combobox control.
        /// </summary>
        private void DiscoverConnectedDevices()
        {
            cmbDevices.Items.Clear();
            _connectedDevices = psCommSimpleWinForms.ConnectedDevices; //Discover connected devices

            foreach (var d in _connectedDevices)
                cmbDevices.Items.Add(d.ToString()); //Add connected devices to control

            var nDevices = cmbDevices.Items.Count;
            cmbDevices.SelectedIndex = nDevices > 0 ? 0 : -1;
            LogMessage($"Found {nDevices} device(s).");

            btnConnect.Enabled = nDevices > 0;
        }

        /// <summary>
        ///     Gets the % of space used on the device.
        /// </summary>
        /// <exception cref="System.NotImplementedException"></exception>
        private void GetSpaceUsed()
        {
            var total = (int) psCommSimpleWinForms.Comm.ClientConnection.GetDeviceSize();
            var free = (int) psCommSimpleWinForms.Comm.ClientConnection.GetDeviceFree();

            var perc = Math.Min((total - free) / (double) total, 1.0);
            LogMessage($"{(int) Math.Round(perc * 100.0):F2}% of storage space used.");
        }

        /// <summary>
        ///     Open the item when the internal storage item has been double clicked on.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void lbInternalStorage_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            var index = lbInternalStorage.IndexFromPoint(e.Location);
            if (index == ListBox.NoMatches) return;

            OpenItem();
        }

        /// <summary>
        ///     Update the number when the selected index changes.
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
            lbInternalStorage.Items.Add($"{index}. {type} {item.Name}");
        }

        /// <summary>
        ///     List the parent item
        /// </summary>
        /// <param name="parent"></param>
        private void ListPreviousItem(IInternalStorageItem parent)
        {
            _contents[0] = parent;
            lbInternalStorage.Items.Add($"0. <Back> {parent.Name}");
        }

        /// <summary>
        ///     Add the selected item children to the form
        /// </summary>
        /// <param name="item"></param>
        private void LoadChildren(IInternalStorageItem item)
        {
            if (item.ItemType == DeviceFileType.Measurement) return;

            lbInternalStorage.Items.Clear();
            _contents.Clear();

            var folder = (IInternalStorageFolder) item;
            var files = folder.GetFiles();
            var subFolders = folder.GetSubFolders();
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
        ///     Load the child items and add to form.
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
            LogMessage($"An error has occurred: {exception.Message}");
        }

        /// <summary>
        ///     Log a message
        /// </summary>
        /// <param name="message"></param>
        private void LogMessage(string message)
        {
            lbConsole.SelectedIndex = lbConsole.Items.Add(message);
        }

        /// <summary>
        ///     Update the selected index when the target number changes
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
        ///     Open the item
        /// </summary>
        private void OpenItem()
        {
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
                    LoadChildren(item);
                }
                else
                {
                    var file = (IInternalStorageFile) item;

                    var m = file.GetMeasurement(MeasType.Overlay);

                    LogMessage(m != null ? $"Load file '{item.Name}', with method '{m.Method}'" : $"Could not load file '{item.Name}'");
                }
            }
            catch (Exception exception)
            {
                LogMessage(exception);
            }
        }
    }
}