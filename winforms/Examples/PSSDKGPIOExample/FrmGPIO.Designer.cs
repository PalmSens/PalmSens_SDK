
namespace PSSDKGPIOExample
{
    partial class FrmGPIO
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.grpConnection = new System.Windows.Forms.GroupBox();
            this.cmbDevices = new System.Windows.Forms.ComboBox();
            this.btnRefresh = new System.Windows.Forms.Button();
            this.btnConnect = new System.Windows.Forms.Button();
            this.grpDevice = new System.Windows.Forms.GroupBox();
            this.lblStatus = new System.Windows.Forms.Label();
            this.tbDeviceStatus = new System.Windows.Forms.TextBox();
            this.lblCurrentRange = new System.Windows.Forms.Label();
            this.lblCurrent = new System.Windows.Forms.Label();
            this.tbCurrent = new System.Windows.Forms.TextBox();
            this.lblVolt = new System.Windows.Forms.Label();
            this.tbPotential = new System.Windows.Forms.TextBox();
            this.lblPotential = new System.Windows.Forms.Label();
            this.grpPinSelection = new System.Windows.Forms.GroupBox();
            this.grpPin8 = new System.Windows.Forms.GroupBox();
            this.chkPin8SetHigh = new System.Windows.Forms.CheckBox();
            this.lblPin8 = new System.Windows.Forms.Label();
            this.radioPin8Set = new System.Windows.Forms.RadioButton();
            this.radioPin8Get = new System.Windows.Forms.RadioButton();
            this.grpPin7 = new System.Windows.Forms.GroupBox();
            this.chkPin7SetHigh = new System.Windows.Forms.CheckBox();
            this.lblPin7 = new System.Windows.Forms.Label();
            this.radioPin7Set = new System.Windows.Forms.RadioButton();
            this.radioPin7Get = new System.Windows.Forms.RadioButton();
            this.grpPin6 = new System.Windows.Forms.GroupBox();
            this.chkPin6SetHigh = new System.Windows.Forms.CheckBox();
            this.lblPin6 = new System.Windows.Forms.Label();
            this.radioPin6Set = new System.Windows.Forms.RadioButton();
            this.radioPin6Get = new System.Windows.Forms.RadioButton();
            this.grpPin5 = new System.Windows.Forms.GroupBox();
            this.chkPin5SetHigh = new System.Windows.Forms.CheckBox();
            this.lblPin5 = new System.Windows.Forms.Label();
            this.radioPin5Set = new System.Windows.Forms.RadioButton();
            this.radioPin5Get = new System.Windows.Forms.RadioButton();
            this.grpPin4 = new System.Windows.Forms.GroupBox();
            this.chkPin4SetHigh = new System.Windows.Forms.CheckBox();
            this.lblPin4 = new System.Windows.Forms.Label();
            this.radioPin4Set = new System.Windows.Forms.RadioButton();
            this.radioPin4Get = new System.Windows.Forms.RadioButton();
            this.grpPin3 = new System.Windows.Forms.GroupBox();
            this.chkPin3SetHigh = new System.Windows.Forms.CheckBox();
            this.lblPin3 = new System.Windows.Forms.Label();
            this.radioPin3Set = new System.Windows.Forms.RadioButton();
            this.radioPin3Get = new System.Windows.Forms.RadioButton();
            this.grpPin2 = new System.Windows.Forms.GroupBox();
            this.chkPin2SetHigh = new System.Windows.Forms.CheckBox();
            this.lblPin2 = new System.Windows.Forms.Label();
            this.radioPin2Set = new System.Windows.Forms.RadioButton();
            this.radioPin2Get = new System.Windows.Forms.RadioButton();
            this.grpPin1 = new System.Windows.Forms.GroupBox();
            this.chkPin1SetHigh = new System.Windows.Forms.CheckBox();
            this.lblPin1 = new System.Windows.Forms.Label();
            this.radioPin1Set = new System.Windows.Forms.RadioButton();
            this.radioPin1Get = new System.Windows.Forms.RadioButton();
            this.grpPinOutput = new System.Windows.Forms.GroupBox();
            this.grpOutputPin8 = new System.Windows.Forms.GroupBox();
            this.chkIsOutputPin8 = new System.Windows.Forms.CheckBox();
            this.rbHighPin8 = new System.Windows.Forms.RadioButton();
            this.rbLowPin8 = new System.Windows.Forms.RadioButton();
            this.grpOutputPin7 = new System.Windows.Forms.GroupBox();
            this.chkIsOutputPin7 = new System.Windows.Forms.CheckBox();
            this.rbHighPin7 = new System.Windows.Forms.RadioButton();
            this.rbLowPin7 = new System.Windows.Forms.RadioButton();
            this.grpOutputPin6 = new System.Windows.Forms.GroupBox();
            this.chkIsOutputPin6 = new System.Windows.Forms.CheckBox();
            this.rbHighPin6 = new System.Windows.Forms.RadioButton();
            this.rbLowPin6 = new System.Windows.Forms.RadioButton();
            this.grpOutputPin5 = new System.Windows.Forms.GroupBox();
            this.chkIsOutputPin5 = new System.Windows.Forms.CheckBox();
            this.rbHighPin5 = new System.Windows.Forms.RadioButton();
            this.rbLowPin5 = new System.Windows.Forms.RadioButton();
            this.grpOutputPin4 = new System.Windows.Forms.GroupBox();
            this.chkIsOutputPin4 = new System.Windows.Forms.CheckBox();
            this.rbHighPin4 = new System.Windows.Forms.RadioButton();
            this.rbLowPin4 = new System.Windows.Forms.RadioButton();
            this.grpOutputPin3 = new System.Windows.Forms.GroupBox();
            this.chkIsOutputPin3 = new System.Windows.Forms.CheckBox();
            this.rbHighPin3 = new System.Windows.Forms.RadioButton();
            this.rbLowPin3 = new System.Windows.Forms.RadioButton();
            this.grpOutputPin2 = new System.Windows.Forms.GroupBox();
            this.chkIsOutputPin2 = new System.Windows.Forms.CheckBox();
            this.rbHighPin2 = new System.Windows.Forms.RadioButton();
            this.rbLowPin2 = new System.Windows.Forms.RadioButton();
            this.grpOutputPin1 = new System.Windows.Forms.GroupBox();
            this.chkIsOutputPin1 = new System.Windows.Forms.CheckBox();
            this.rbHighPin1 = new System.Windows.Forms.RadioButton();
            this.rbLowPin1 = new System.Windows.Forms.RadioButton();
            this.grpOutput = new System.Windows.Forms.GroupBox();
            this.lbConsole = new System.Windows.Forms.ListBox();
            this.grpAction = new System.Windows.Forms.GroupBox();
            this.btnSet = new System.Windows.Forms.Button();
            this.btnGet = new System.Windows.Forms.Button();
            this.psCommSimpleWinForms = new PalmSens.Core.Simplified.WinForms.PSCommSimpleWinForms(this.components);
            this.grpConnection.SuspendLayout();
            this.grpDevice.SuspendLayout();
            this.grpPinSelection.SuspendLayout();
            this.grpPin8.SuspendLayout();
            this.grpPin7.SuspendLayout();
            this.grpPin6.SuspendLayout();
            this.grpPin5.SuspendLayout();
            this.grpPin4.SuspendLayout();
            this.grpPin3.SuspendLayout();
            this.grpPin2.SuspendLayout();
            this.grpPin1.SuspendLayout();
            this.grpPinOutput.SuspendLayout();
            this.grpOutputPin8.SuspendLayout();
            this.grpOutputPin7.SuspendLayout();
            this.grpOutputPin6.SuspendLayout();
            this.grpOutputPin5.SuspendLayout();
            this.grpOutputPin4.SuspendLayout();
            this.grpOutputPin3.SuspendLayout();
            this.grpOutputPin2.SuspendLayout();
            this.grpOutputPin1.SuspendLayout();
            this.grpOutput.SuspendLayout();
            this.grpAction.SuspendLayout();
            this.SuspendLayout();
            // 
            // grpConnection
            // 
            this.grpConnection.Controls.Add(this.cmbDevices);
            this.grpConnection.Controls.Add(this.btnRefresh);
            this.grpConnection.Controls.Add(this.btnConnect);
            this.grpConnection.Location = new System.Drawing.Point(12, 12);
            this.grpConnection.Name = "grpConnection";
            this.grpConnection.Size = new System.Drawing.Size(257, 79);
            this.grpConnection.TabIndex = 6;
            this.grpConnection.TabStop = false;
            this.grpConnection.Text = "Connection";
            // 
            // cmbDevices
            // 
            this.cmbDevices.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.cmbDevices.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbDevices.FormattingEnabled = true;
            this.cmbDevices.Location = new System.Drawing.Point(6, 17);
            this.cmbDevices.Name = "cmbDevices";
            this.cmbDevices.Size = new System.Drawing.Size(241, 21);
            this.cmbDevices.TabIndex = 0;
            this.cmbDevices.SelectedIndexChanged += new System.EventHandler(this.cmbDevices_SelectedIndexChanged);
            // 
            // btnRefresh
            // 
            this.btnRefresh.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnRefresh.Location = new System.Drawing.Point(91, 44);
            this.btnRefresh.Name = "btnRefresh";
            this.btnRefresh.Size = new System.Drawing.Size(75, 23);
            this.btnRefresh.TabIndex = 1;
            this.btnRefresh.Text = "Refresh";
            this.btnRefresh.UseVisualStyleBackColor = true;
            this.btnRefresh.Click += new System.EventHandler(this.btnRefresh_Click);
            // 
            // btnConnect
            // 
            this.btnConnect.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnConnect.Enabled = false;
            this.btnConnect.Location = new System.Drawing.Point(172, 44);
            this.btnConnect.Name = "btnConnect";
            this.btnConnect.Size = new System.Drawing.Size(75, 23);
            this.btnConnect.TabIndex = 2;
            this.btnConnect.Text = "Connect";
            this.btnConnect.UseVisualStyleBackColor = true;
            this.btnConnect.Click += new System.EventHandler(this.btnConnect_Click);
            // 
            // grpDevice
            // 
            this.grpDevice.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.grpDevice.Controls.Add(this.lblStatus);
            this.grpDevice.Controls.Add(this.tbDeviceStatus);
            this.grpDevice.Controls.Add(this.lblCurrentRange);
            this.grpDevice.Controls.Add(this.lblCurrent);
            this.grpDevice.Controls.Add(this.tbCurrent);
            this.grpDevice.Controls.Add(this.lblVolt);
            this.grpDevice.Controls.Add(this.tbPotential);
            this.grpDevice.Controls.Add(this.lblPotential);
            this.grpDevice.Location = new System.Drawing.Point(287, 12);
            this.grpDevice.Name = "grpDevice";
            this.grpDevice.Size = new System.Drawing.Size(332, 79);
            this.grpDevice.TabIndex = 10;
            this.grpDevice.TabStop = false;
            this.grpDevice.Text = "Device Status";
            // 
            // lblStatus
            // 
            this.lblStatus.AutoSize = true;
            this.lblStatus.Location = new System.Drawing.Point(189, 20);
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(40, 13);
            this.lblStatus.TabIndex = 7;
            this.lblStatus.Text = "Status:";
            // 
            // tbDeviceStatus
            // 
            this.tbDeviceStatus.Location = new System.Drawing.Point(192, 45);
            this.tbDeviceStatus.Name = "tbDeviceStatus";
            this.tbDeviceStatus.ReadOnly = true;
            this.tbDeviceStatus.Size = new System.Drawing.Size(134, 20);
            this.tbDeviceStatus.TabIndex = 6;
            // 
            // lblCurrentRange
            // 
            this.lblCurrentRange.AutoSize = true;
            this.lblCurrentRange.Location = new System.Drawing.Point(140, 48);
            this.lblCurrentRange.Name = "lblCurrentRange";
            this.lblCurrentRange.Size = new System.Drawing.Size(44, 13);
            this.lblCurrentRange.TabIndex = 5;
            this.lblCurrentRange.Text = "* 10 mA";
            // 
            // lblCurrent
            // 
            this.lblCurrent.AutoSize = true;
            this.lblCurrent.Location = new System.Drawing.Point(6, 49);
            this.lblCurrent.Name = "lblCurrent";
            this.lblCurrent.Size = new System.Drawing.Size(44, 13);
            this.lblCurrent.TabIndex = 4;
            this.lblCurrent.Text = "Current:";
            // 
            // tbCurrent
            // 
            this.tbCurrent.Location = new System.Drawing.Point(63, 45);
            this.tbCurrent.Name = "tbCurrent";
            this.tbCurrent.ReadOnly = true;
            this.tbCurrent.Size = new System.Drawing.Size(70, 20);
            this.tbCurrent.TabIndex = 3;
            // 
            // lblVolt
            // 
            this.lblVolt.AutoSize = true;
            this.lblVolt.Location = new System.Drawing.Point(139, 20);
            this.lblVolt.Name = "lblVolt";
            this.lblVolt.Size = new System.Drawing.Size(14, 13);
            this.lblVolt.TabIndex = 2;
            this.lblVolt.Text = "V";
            // 
            // tbPotential
            // 
            this.tbPotential.Location = new System.Drawing.Point(63, 17);
            this.tbPotential.Name = "tbPotential";
            this.tbPotential.ReadOnly = true;
            this.tbPotential.Size = new System.Drawing.Size(70, 20);
            this.tbPotential.TabIndex = 1;
            // 
            // lblPotential
            // 
            this.lblPotential.AutoSize = true;
            this.lblPotential.Location = new System.Drawing.Point(6, 20);
            this.lblPotential.Name = "lblPotential";
            this.lblPotential.Size = new System.Drawing.Size(51, 13);
            this.lblPotential.TabIndex = 0;
            this.lblPotential.Text = "Potential:";
            // 
            // grpPinSelection
            // 
            this.grpPinSelection.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
            this.grpPinSelection.Controls.Add(this.grpPin8);
            this.grpPinSelection.Controls.Add(this.grpPin7);
            this.grpPinSelection.Controls.Add(this.grpPin6);
            this.grpPinSelection.Controls.Add(this.grpPin5);
            this.grpPinSelection.Controls.Add(this.grpPin4);
            this.grpPinSelection.Controls.Add(this.grpPin3);
            this.grpPinSelection.Controls.Add(this.grpPin2);
            this.grpPinSelection.Controls.Add(this.grpPin1);
            this.grpPinSelection.Location = new System.Drawing.Point(12, 97);
            this.grpPinSelection.Name = "grpPinSelection";
            this.grpPinSelection.Size = new System.Drawing.Size(263, 363);
            this.grpPinSelection.TabIndex = 12;
            this.grpPinSelection.TabStop = false;
            this.grpPinSelection.Text = "Pin Selection";
            // 
            // grpPin8
            // 
            this.grpPin8.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpPin8.Controls.Add(this.chkPin8SetHigh);
            this.grpPin8.Controls.Add(this.lblPin8);
            this.grpPin8.Controls.Add(this.radioPin8Set);
            this.grpPin8.Controls.Add(this.radioPin8Get);
            this.grpPin8.Location = new System.Drawing.Point(6, 310);
            this.grpPin8.Name = "grpPin8";
            this.grpPin8.Size = new System.Drawing.Size(251, 42);
            this.grpPin8.TabIndex = 6;
            this.grpPin8.TabStop = false;
            this.grpPin8.Text = "Pin 8";
            // 
            // chkPin8SetHigh
            // 
            this.chkPin8SetHigh.AutoSize = true;
            this.chkPin8SetHigh.Checked = true;
            this.chkPin8SetHigh.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkPin8SetHigh.Location = new System.Drawing.Point(182, 15);
            this.chkPin8SetHigh.Name = "chkPin8SetHigh";
            this.chkPin8SetHigh.Size = new System.Drawing.Size(67, 17);
            this.chkPin8SetHigh.TabIndex = 4;
            this.chkPin8SetHigh.Text = "Set High";
            this.chkPin8SetHigh.UseVisualStyleBackColor = true;
            // 
            // lblPin8
            // 
            this.lblPin8.AutoSize = true;
            this.lblPin8.Location = new System.Drawing.Point(6, 16);
            this.lblPin8.Name = "lblPin8";
            this.lblPin8.Size = new System.Drawing.Size(75, 13);
            this.lblPin8.TabIndex = 0;
            this.lblPin8.Text = "Get/Set Value";
            // 
            // radioPin8Set
            // 
            this.radioPin8Set.AutoSize = true;
            this.radioPin8Set.Location = new System.Drawing.Point(135, 14);
            this.radioPin8Set.Name = "radioPin8Set";
            this.radioPin8Set.Size = new System.Drawing.Size(41, 17);
            this.radioPin8Set.TabIndex = 2;
            this.radioPin8Set.TabStop = true;
            this.radioPin8Set.Text = "Set";
            this.radioPin8Set.UseVisualStyleBackColor = true;
            this.radioPin8Set.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // radioPin8Get
            // 
            this.radioPin8Get.AutoSize = true;
            this.radioPin8Get.Checked = true;
            this.radioPin8Get.Location = new System.Drawing.Point(87, 14);
            this.radioPin8Get.Name = "radioPin8Get";
            this.radioPin8Get.Size = new System.Drawing.Size(42, 17);
            this.radioPin8Get.TabIndex = 1;
            this.radioPin8Get.TabStop = true;
            this.radioPin8Get.Text = "Get";
            this.radioPin8Get.UseVisualStyleBackColor = true;
            this.radioPin8Get.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // grpPin7
            // 
            this.grpPin7.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpPin7.Controls.Add(this.chkPin7SetHigh);
            this.grpPin7.Controls.Add(this.lblPin7);
            this.grpPin7.Controls.Add(this.radioPin7Set);
            this.grpPin7.Controls.Add(this.radioPin7Get);
            this.grpPin7.Location = new System.Drawing.Point(6, 268);
            this.grpPin7.Name = "grpPin7";
            this.grpPin7.Size = new System.Drawing.Size(251, 42);
            this.grpPin7.TabIndex = 4;
            this.grpPin7.TabStop = false;
            this.grpPin7.Text = "Pin 7";
            // 
            // chkPin7SetHigh
            // 
            this.chkPin7SetHigh.AutoSize = true;
            this.chkPin7SetHigh.Checked = true;
            this.chkPin7SetHigh.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkPin7SetHigh.Location = new System.Drawing.Point(182, 15);
            this.chkPin7SetHigh.Name = "chkPin7SetHigh";
            this.chkPin7SetHigh.Size = new System.Drawing.Size(67, 17);
            this.chkPin7SetHigh.TabIndex = 4;
            this.chkPin7SetHigh.Text = "Set High";
            this.chkPin7SetHigh.UseVisualStyleBackColor = true;
            // 
            // lblPin7
            // 
            this.lblPin7.AutoSize = true;
            this.lblPin7.Location = new System.Drawing.Point(6, 16);
            this.lblPin7.Name = "lblPin7";
            this.lblPin7.Size = new System.Drawing.Size(75, 13);
            this.lblPin7.TabIndex = 0;
            this.lblPin7.Text = "Get/Set Value";
            // 
            // radioPin7Set
            // 
            this.radioPin7Set.AutoSize = true;
            this.radioPin7Set.Location = new System.Drawing.Point(135, 14);
            this.radioPin7Set.Name = "radioPin7Set";
            this.radioPin7Set.Size = new System.Drawing.Size(41, 17);
            this.radioPin7Set.TabIndex = 2;
            this.radioPin7Set.TabStop = true;
            this.radioPin7Set.Text = "Set";
            this.radioPin7Set.UseVisualStyleBackColor = true;
            this.radioPin7Set.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // radioPin7Get
            // 
            this.radioPin7Get.AutoSize = true;
            this.radioPin7Get.Checked = true;
            this.radioPin7Get.Location = new System.Drawing.Point(87, 14);
            this.radioPin7Get.Name = "radioPin7Get";
            this.radioPin7Get.Size = new System.Drawing.Size(42, 17);
            this.radioPin7Get.TabIndex = 1;
            this.radioPin7Get.TabStop = true;
            this.radioPin7Get.Text = "Get";
            this.radioPin7Get.UseVisualStyleBackColor = true;
            this.radioPin7Get.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // grpPin6
            // 
            this.grpPin6.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpPin6.Controls.Add(this.chkPin6SetHigh);
            this.grpPin6.Controls.Add(this.lblPin6);
            this.grpPin6.Controls.Add(this.radioPin6Set);
            this.grpPin6.Controls.Add(this.radioPin6Get);
            this.grpPin6.Location = new System.Drawing.Point(6, 226);
            this.grpPin6.Name = "grpPin6";
            this.grpPin6.Size = new System.Drawing.Size(251, 42);
            this.grpPin6.TabIndex = 4;
            this.grpPin6.TabStop = false;
            this.grpPin6.Text = "Pin 6";
            // 
            // chkPin6SetHigh
            // 
            this.chkPin6SetHigh.AutoSize = true;
            this.chkPin6SetHigh.Checked = true;
            this.chkPin6SetHigh.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkPin6SetHigh.Location = new System.Drawing.Point(182, 15);
            this.chkPin6SetHigh.Name = "chkPin6SetHigh";
            this.chkPin6SetHigh.Size = new System.Drawing.Size(67, 17);
            this.chkPin6SetHigh.TabIndex = 4;
            this.chkPin6SetHigh.Text = "Set High";
            this.chkPin6SetHigh.UseVisualStyleBackColor = true;
            // 
            // lblPin6
            // 
            this.lblPin6.AutoSize = true;
            this.lblPin6.Location = new System.Drawing.Point(6, 16);
            this.lblPin6.Name = "lblPin6";
            this.lblPin6.Size = new System.Drawing.Size(75, 13);
            this.lblPin6.TabIndex = 0;
            this.lblPin6.Text = "Get/Set Value";
            // 
            // radioPin6Set
            // 
            this.radioPin6Set.AutoSize = true;
            this.radioPin6Set.Location = new System.Drawing.Point(135, 14);
            this.radioPin6Set.Name = "radioPin6Set";
            this.radioPin6Set.Size = new System.Drawing.Size(41, 17);
            this.radioPin6Set.TabIndex = 2;
            this.radioPin6Set.TabStop = true;
            this.radioPin6Set.Text = "Set";
            this.radioPin6Set.UseVisualStyleBackColor = true;
            this.radioPin6Set.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // radioPin6Get
            // 
            this.radioPin6Get.AutoSize = true;
            this.radioPin6Get.Checked = true;
            this.radioPin6Get.Location = new System.Drawing.Point(87, 14);
            this.radioPin6Get.Name = "radioPin6Get";
            this.radioPin6Get.Size = new System.Drawing.Size(42, 17);
            this.radioPin6Get.TabIndex = 1;
            this.radioPin6Get.TabStop = true;
            this.radioPin6Get.Text = "Get";
            this.radioPin6Get.UseVisualStyleBackColor = true;
            this.radioPin6Get.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // grpPin5
            // 
            this.grpPin5.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpPin5.Controls.Add(this.chkPin5SetHigh);
            this.grpPin5.Controls.Add(this.lblPin5);
            this.grpPin5.Controls.Add(this.radioPin5Set);
            this.grpPin5.Controls.Add(this.radioPin5Get);
            this.grpPin5.Location = new System.Drawing.Point(6, 184);
            this.grpPin5.Name = "grpPin5";
            this.grpPin5.Size = new System.Drawing.Size(251, 42);
            this.grpPin5.TabIndex = 5;
            this.grpPin5.TabStop = false;
            this.grpPin5.Text = "Pin 5";
            // 
            // chkPin5SetHigh
            // 
            this.chkPin5SetHigh.AutoSize = true;
            this.chkPin5SetHigh.Checked = true;
            this.chkPin5SetHigh.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkPin5SetHigh.Location = new System.Drawing.Point(182, 15);
            this.chkPin5SetHigh.Name = "chkPin5SetHigh";
            this.chkPin5SetHigh.Size = new System.Drawing.Size(67, 17);
            this.chkPin5SetHigh.TabIndex = 4;
            this.chkPin5SetHigh.Text = "Set High";
            this.chkPin5SetHigh.UseVisualStyleBackColor = true;
            // 
            // lblPin5
            // 
            this.lblPin5.AutoSize = true;
            this.lblPin5.Location = new System.Drawing.Point(6, 16);
            this.lblPin5.Name = "lblPin5";
            this.lblPin5.Size = new System.Drawing.Size(75, 13);
            this.lblPin5.TabIndex = 0;
            this.lblPin5.Text = "Get/Set Value";
            // 
            // radioPin5Set
            // 
            this.radioPin5Set.AutoSize = true;
            this.radioPin5Set.Location = new System.Drawing.Point(135, 14);
            this.radioPin5Set.Name = "radioPin5Set";
            this.radioPin5Set.Size = new System.Drawing.Size(41, 17);
            this.radioPin5Set.TabIndex = 2;
            this.radioPin5Set.TabStop = true;
            this.radioPin5Set.Text = "Set";
            this.radioPin5Set.UseVisualStyleBackColor = true;
            this.radioPin5Set.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // radioPin5Get
            // 
            this.radioPin5Get.AutoSize = true;
            this.radioPin5Get.Checked = true;
            this.radioPin5Get.Location = new System.Drawing.Point(87, 14);
            this.radioPin5Get.Name = "radioPin5Get";
            this.radioPin5Get.Size = new System.Drawing.Size(42, 17);
            this.radioPin5Get.TabIndex = 1;
            this.radioPin5Get.TabStop = true;
            this.radioPin5Get.Text = "Get";
            this.radioPin5Get.UseVisualStyleBackColor = true;
            this.radioPin5Get.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // grpPin4
            // 
            this.grpPin4.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpPin4.Controls.Add(this.chkPin4SetHigh);
            this.grpPin4.Controls.Add(this.lblPin4);
            this.grpPin4.Controls.Add(this.radioPin4Set);
            this.grpPin4.Controls.Add(this.radioPin4Get);
            this.grpPin4.Location = new System.Drawing.Point(6, 142);
            this.grpPin4.Name = "grpPin4";
            this.grpPin4.Size = new System.Drawing.Size(251, 42);
            this.grpPin4.TabIndex = 4;
            this.grpPin4.TabStop = false;
            this.grpPin4.Text = "Pin 4";
            // 
            // chkPin4SetHigh
            // 
            this.chkPin4SetHigh.AutoSize = true;
            this.chkPin4SetHigh.Checked = true;
            this.chkPin4SetHigh.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkPin4SetHigh.Location = new System.Drawing.Point(182, 15);
            this.chkPin4SetHigh.Name = "chkPin4SetHigh";
            this.chkPin4SetHigh.Size = new System.Drawing.Size(67, 17);
            this.chkPin4SetHigh.TabIndex = 4;
            this.chkPin4SetHigh.Text = "Set High";
            this.chkPin4SetHigh.UseVisualStyleBackColor = true;
            // 
            // lblPin4
            // 
            this.lblPin4.AutoSize = true;
            this.lblPin4.Location = new System.Drawing.Point(6, 16);
            this.lblPin4.Name = "lblPin4";
            this.lblPin4.Size = new System.Drawing.Size(75, 13);
            this.lblPin4.TabIndex = 0;
            this.lblPin4.Text = "Get/Set Value";
            // 
            // radioPin4Set
            // 
            this.radioPin4Set.AutoSize = true;
            this.radioPin4Set.Location = new System.Drawing.Point(135, 14);
            this.radioPin4Set.Name = "radioPin4Set";
            this.radioPin4Set.Size = new System.Drawing.Size(41, 17);
            this.radioPin4Set.TabIndex = 2;
            this.radioPin4Set.TabStop = true;
            this.radioPin4Set.Text = "Set";
            this.radioPin4Set.UseVisualStyleBackColor = true;
            this.radioPin4Set.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // radioPin4Get
            // 
            this.radioPin4Get.AutoSize = true;
            this.radioPin4Get.Checked = true;
            this.radioPin4Get.Location = new System.Drawing.Point(87, 14);
            this.radioPin4Get.Name = "radioPin4Get";
            this.radioPin4Get.Size = new System.Drawing.Size(42, 17);
            this.radioPin4Get.TabIndex = 1;
            this.radioPin4Get.TabStop = true;
            this.radioPin4Get.Text = "Get";
            this.radioPin4Get.UseVisualStyleBackColor = true;
            this.radioPin4Get.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // grpPin3
            // 
            this.grpPin3.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpPin3.Controls.Add(this.chkPin3SetHigh);
            this.grpPin3.Controls.Add(this.lblPin3);
            this.grpPin3.Controls.Add(this.radioPin3Set);
            this.grpPin3.Controls.Add(this.radioPin3Get);
            this.grpPin3.Location = new System.Drawing.Point(6, 100);
            this.grpPin3.Name = "grpPin3";
            this.grpPin3.Size = new System.Drawing.Size(251, 42);
            this.grpPin3.TabIndex = 4;
            this.grpPin3.TabStop = false;
            this.grpPin3.Text = "Pin 3";
            // 
            // chkPin3SetHigh
            // 
            this.chkPin3SetHigh.AutoSize = true;
            this.chkPin3SetHigh.Checked = true;
            this.chkPin3SetHigh.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkPin3SetHigh.Location = new System.Drawing.Point(182, 15);
            this.chkPin3SetHigh.Name = "chkPin3SetHigh";
            this.chkPin3SetHigh.Size = new System.Drawing.Size(67, 17);
            this.chkPin3SetHigh.TabIndex = 4;
            this.chkPin3SetHigh.Text = "Set High";
            this.chkPin3SetHigh.UseVisualStyleBackColor = true;
            // 
            // lblPin3
            // 
            this.lblPin3.AutoSize = true;
            this.lblPin3.Location = new System.Drawing.Point(6, 16);
            this.lblPin3.Name = "lblPin3";
            this.lblPin3.Size = new System.Drawing.Size(75, 13);
            this.lblPin3.TabIndex = 0;
            this.lblPin3.Text = "Get/Set Value";
            // 
            // radioPin3Set
            // 
            this.radioPin3Set.AutoSize = true;
            this.radioPin3Set.Location = new System.Drawing.Point(135, 14);
            this.radioPin3Set.Name = "radioPin3Set";
            this.radioPin3Set.Size = new System.Drawing.Size(41, 17);
            this.radioPin3Set.TabIndex = 2;
            this.radioPin3Set.TabStop = true;
            this.radioPin3Set.Text = "Set";
            this.radioPin3Set.UseVisualStyleBackColor = true;
            this.radioPin3Set.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // radioPin3Get
            // 
            this.radioPin3Get.AutoSize = true;
            this.radioPin3Get.Checked = true;
            this.radioPin3Get.Location = new System.Drawing.Point(87, 14);
            this.radioPin3Get.Name = "radioPin3Get";
            this.radioPin3Get.Size = new System.Drawing.Size(42, 17);
            this.radioPin3Get.TabIndex = 1;
            this.radioPin3Get.TabStop = true;
            this.radioPin3Get.Text = "Get";
            this.radioPin3Get.UseVisualStyleBackColor = true;
            this.radioPin3Get.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // grpPin2
            // 
            this.grpPin2.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpPin2.Controls.Add(this.chkPin2SetHigh);
            this.grpPin2.Controls.Add(this.lblPin2);
            this.grpPin2.Controls.Add(this.radioPin2Set);
            this.grpPin2.Controls.Add(this.radioPin2Get);
            this.grpPin2.Location = new System.Drawing.Point(6, 58);
            this.grpPin2.Name = "grpPin2";
            this.grpPin2.Size = new System.Drawing.Size(251, 42);
            this.grpPin2.TabIndex = 4;
            this.grpPin2.TabStop = false;
            this.grpPin2.Text = "Pin 2";
            // 
            // chkPin2SetHigh
            // 
            this.chkPin2SetHigh.AutoSize = true;
            this.chkPin2SetHigh.Checked = true;
            this.chkPin2SetHigh.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkPin2SetHigh.Location = new System.Drawing.Point(182, 15);
            this.chkPin2SetHigh.Name = "chkPin2SetHigh";
            this.chkPin2SetHigh.Size = new System.Drawing.Size(67, 17);
            this.chkPin2SetHigh.TabIndex = 4;
            this.chkPin2SetHigh.Text = "Set High";
            this.chkPin2SetHigh.UseVisualStyleBackColor = true;
            // 
            // lblPin2
            // 
            this.lblPin2.AutoSize = true;
            this.lblPin2.Location = new System.Drawing.Point(6, 16);
            this.lblPin2.Name = "lblPin2";
            this.lblPin2.Size = new System.Drawing.Size(75, 13);
            this.lblPin2.TabIndex = 0;
            this.lblPin2.Text = "Get/Set Value";
            // 
            // radioPin2Set
            // 
            this.radioPin2Set.AutoSize = true;
            this.radioPin2Set.Location = new System.Drawing.Point(135, 14);
            this.radioPin2Set.Name = "radioPin2Set";
            this.radioPin2Set.Size = new System.Drawing.Size(41, 17);
            this.radioPin2Set.TabIndex = 2;
            this.radioPin2Set.TabStop = true;
            this.radioPin2Set.Text = "Set";
            this.radioPin2Set.UseVisualStyleBackColor = true;
            this.radioPin2Set.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // radioPin2Get
            // 
            this.radioPin2Get.AutoSize = true;
            this.radioPin2Get.Checked = true;
            this.radioPin2Get.Location = new System.Drawing.Point(87, 14);
            this.radioPin2Get.Name = "radioPin2Get";
            this.radioPin2Get.Size = new System.Drawing.Size(42, 17);
            this.radioPin2Get.TabIndex = 1;
            this.radioPin2Get.TabStop = true;
            this.radioPin2Get.Text = "Get";
            this.radioPin2Get.UseVisualStyleBackColor = true;
            this.radioPin2Get.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // grpPin1
            // 
            this.grpPin1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpPin1.Controls.Add(this.chkPin1SetHigh);
            this.grpPin1.Controls.Add(this.lblPin1);
            this.grpPin1.Controls.Add(this.radioPin1Set);
            this.grpPin1.Controls.Add(this.radioPin1Get);
            this.grpPin1.Location = new System.Drawing.Point(6, 16);
            this.grpPin1.Name = "grpPin1";
            this.grpPin1.Size = new System.Drawing.Size(251, 42);
            this.grpPin1.TabIndex = 3;
            this.grpPin1.TabStop = false;
            this.grpPin1.Text = "Pin1";
            // 
            // chkPin1SetHigh
            // 
            this.chkPin1SetHigh.AutoSize = true;
            this.chkPin1SetHigh.Checked = true;
            this.chkPin1SetHigh.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkPin1SetHigh.Location = new System.Drawing.Point(182, 15);
            this.chkPin1SetHigh.Name = "chkPin1SetHigh";
            this.chkPin1SetHigh.Size = new System.Drawing.Size(67, 17);
            this.chkPin1SetHigh.TabIndex = 3;
            this.chkPin1SetHigh.Text = "Set High";
            this.chkPin1SetHigh.UseVisualStyleBackColor = true;
            // 
            // lblPin1
            // 
            this.lblPin1.AutoSize = true;
            this.lblPin1.Location = new System.Drawing.Point(6, 16);
            this.lblPin1.Name = "lblPin1";
            this.lblPin1.Size = new System.Drawing.Size(75, 13);
            this.lblPin1.TabIndex = 0;
            this.lblPin1.Text = "Get/Set Value";
            // 
            // radioPin1Set
            // 
            this.radioPin1Set.AutoSize = true;
            this.radioPin1Set.Location = new System.Drawing.Point(135, 14);
            this.radioPin1Set.Name = "radioPin1Set";
            this.radioPin1Set.Size = new System.Drawing.Size(41, 17);
            this.radioPin1Set.TabIndex = 2;
            this.radioPin1Set.TabStop = true;
            this.radioPin1Set.Text = "Set";
            this.radioPin1Set.UseVisualStyleBackColor = true;
            this.radioPin1Set.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // radioPin1Get
            // 
            this.radioPin1Get.AutoSize = true;
            this.radioPin1Get.Checked = true;
            this.radioPin1Get.Location = new System.Drawing.Point(87, 14);
            this.radioPin1Get.Name = "radioPin1Get";
            this.radioPin1Get.Size = new System.Drawing.Size(42, 17);
            this.radioPin1Get.TabIndex = 1;
            this.radioPin1Get.TabStop = true;
            this.radioPin1Get.Text = "Get";
            this.radioPin1Get.UseVisualStyleBackColor = true;
            this.radioPin1Get.CheckedChanged += new System.EventHandler(this.radioPin_CheckedChanged);
            // 
            // grpPinOutput
            // 
            this.grpPinOutput.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.grpPinOutput.Controls.Add(this.grpOutputPin8);
            this.grpPinOutput.Controls.Add(this.grpOutputPin7);
            this.grpPinOutput.Controls.Add(this.grpOutputPin6);
            this.grpPinOutput.Controls.Add(this.grpOutputPin5);
            this.grpPinOutput.Controls.Add(this.grpOutputPin4);
            this.grpPinOutput.Controls.Add(this.grpOutputPin3);
            this.grpPinOutput.Controls.Add(this.grpOutputPin2);
            this.grpPinOutput.Controls.Add(this.grpOutputPin1);
            this.grpPinOutput.Enabled = false;
            this.grpPinOutput.Location = new System.Drawing.Point(584, 97);
            this.grpPinOutput.Name = "grpPinOutput";
            this.grpPinOutput.Size = new System.Drawing.Size(204, 363);
            this.grpPinOutput.TabIndex = 13;
            this.grpPinOutput.TabStop = false;
            this.grpPinOutput.Text = "Pin Get Result";
            // 
            // grpOutputPin8
            // 
            this.grpOutputPin8.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutputPin8.Controls.Add(this.chkIsOutputPin8);
            this.grpOutputPin8.Controls.Add(this.rbHighPin8);
            this.grpOutputPin8.Controls.Add(this.rbLowPin8);
            this.grpOutputPin8.Location = new System.Drawing.Point(6, 310);
            this.grpOutputPin8.Name = "grpOutputPin8";
            this.grpOutputPin8.Size = new System.Drawing.Size(192, 42);
            this.grpOutputPin8.TabIndex = 21;
            this.grpOutputPin8.TabStop = false;
            this.grpOutputPin8.Text = "Pin 8";
            // 
            // chkIsOutputPin8
            // 
            this.chkIsOutputPin8.AutoCheck = false;
            this.chkIsOutputPin8.AutoSize = true;
            this.chkIsOutputPin8.Checked = true;
            this.chkIsOutputPin8.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkIsOutputPin8.Location = new System.Drawing.Point(111, 15);
            this.chkIsOutputPin8.Name = "chkIsOutputPin8";
            this.chkIsOutputPin8.Size = new System.Drawing.Size(69, 17);
            this.chkIsOutputPin8.TabIndex = 5;
            this.chkIsOutputPin8.Text = "Is Output";
            this.chkIsOutputPin8.UseVisualStyleBackColor = true;
            // 
            // rbHighPin8
            // 
            this.rbHighPin8.AutoCheck = false;
            this.rbHighPin8.AutoSize = true;
            this.rbHighPin8.Location = new System.Drawing.Point(57, 14);
            this.rbHighPin8.Name = "rbHighPin8";
            this.rbHighPin8.Size = new System.Drawing.Size(47, 17);
            this.rbHighPin8.TabIndex = 2;
            this.rbHighPin8.TabStop = true;
            this.rbHighPin8.Text = "High";
            this.rbHighPin8.UseVisualStyleBackColor = true;
            // 
            // rbLowPin8
            // 
            this.rbLowPin8.AutoCheck = false;
            this.rbLowPin8.AutoSize = true;
            this.rbLowPin8.Checked = true;
            this.rbLowPin8.Location = new System.Drawing.Point(6, 14);
            this.rbLowPin8.Name = "rbLowPin8";
            this.rbLowPin8.Size = new System.Drawing.Size(45, 17);
            this.rbLowPin8.TabIndex = 1;
            this.rbLowPin8.TabStop = true;
            this.rbLowPin8.Text = "Low";
            this.rbLowPin8.UseVisualStyleBackColor = true;
            // 
            // grpOutputPin7
            // 
            this.grpOutputPin7.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutputPin7.Controls.Add(this.chkIsOutputPin7);
            this.grpOutputPin7.Controls.Add(this.rbHighPin7);
            this.grpOutputPin7.Controls.Add(this.rbLowPin7);
            this.grpOutputPin7.Location = new System.Drawing.Point(6, 268);
            this.grpOutputPin7.Name = "grpOutputPin7";
            this.grpOutputPin7.Size = new System.Drawing.Size(192, 42);
            this.grpOutputPin7.TabIndex = 15;
            this.grpOutputPin7.TabStop = false;
            this.grpOutputPin7.Text = "Pin 7";
            // 
            // chkIsOutputPin7
            // 
            this.chkIsOutputPin7.AutoCheck = false;
            this.chkIsOutputPin7.AutoSize = true;
            this.chkIsOutputPin7.Checked = true;
            this.chkIsOutputPin7.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkIsOutputPin7.Location = new System.Drawing.Point(111, 19);
            this.chkIsOutputPin7.Name = "chkIsOutputPin7";
            this.chkIsOutputPin7.Size = new System.Drawing.Size(69, 17);
            this.chkIsOutputPin7.TabIndex = 5;
            this.chkIsOutputPin7.Text = "Is Output";
            this.chkIsOutputPin7.UseVisualStyleBackColor = true;
            // 
            // rbHighPin7
            // 
            this.rbHighPin7.AutoCheck = false;
            this.rbHighPin7.AutoSize = true;
            this.rbHighPin7.Location = new System.Drawing.Point(57, 14);
            this.rbHighPin7.Name = "rbHighPin7";
            this.rbHighPin7.Size = new System.Drawing.Size(47, 17);
            this.rbHighPin7.TabIndex = 2;
            this.rbHighPin7.TabStop = true;
            this.rbHighPin7.Text = "High";
            this.rbHighPin7.UseVisualStyleBackColor = true;
            // 
            // rbLowPin7
            // 
            this.rbLowPin7.AutoCheck = false;
            this.rbLowPin7.AutoSize = true;
            this.rbLowPin7.Checked = true;
            this.rbLowPin7.Location = new System.Drawing.Point(6, 14);
            this.rbLowPin7.Name = "rbLowPin7";
            this.rbLowPin7.Size = new System.Drawing.Size(45, 17);
            this.rbLowPin7.TabIndex = 1;
            this.rbLowPin7.TabStop = true;
            this.rbLowPin7.Text = "Low";
            this.rbLowPin7.UseVisualStyleBackColor = true;
            // 
            // grpOutputPin6
            // 
            this.grpOutputPin6.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutputPin6.Controls.Add(this.chkIsOutputPin6);
            this.grpOutputPin6.Controls.Add(this.rbHighPin6);
            this.grpOutputPin6.Controls.Add(this.rbLowPin6);
            this.grpOutputPin6.Location = new System.Drawing.Point(6, 226);
            this.grpOutputPin6.Name = "grpOutputPin6";
            this.grpOutputPin6.Size = new System.Drawing.Size(192, 42);
            this.grpOutputPin6.TabIndex = 16;
            this.grpOutputPin6.TabStop = false;
            this.grpOutputPin6.Text = "Pin 6";
            // 
            // chkIsOutputPin6
            // 
            this.chkIsOutputPin6.AutoCheck = false;
            this.chkIsOutputPin6.AutoSize = true;
            this.chkIsOutputPin6.Checked = true;
            this.chkIsOutputPin6.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkIsOutputPin6.Location = new System.Drawing.Point(111, 15);
            this.chkIsOutputPin6.Name = "chkIsOutputPin6";
            this.chkIsOutputPin6.Size = new System.Drawing.Size(69, 17);
            this.chkIsOutputPin6.TabIndex = 5;
            this.chkIsOutputPin6.Text = "Is Output";
            this.chkIsOutputPin6.UseVisualStyleBackColor = true;
            // 
            // rbHighPin6
            // 
            this.rbHighPin6.AutoCheck = false;
            this.rbHighPin6.AutoSize = true;
            this.rbHighPin6.Location = new System.Drawing.Point(57, 14);
            this.rbHighPin6.Name = "rbHighPin6";
            this.rbHighPin6.Size = new System.Drawing.Size(47, 17);
            this.rbHighPin6.TabIndex = 2;
            this.rbHighPin6.TabStop = true;
            this.rbHighPin6.Text = "High";
            this.rbHighPin6.UseVisualStyleBackColor = true;
            // 
            // rbLowPin6
            // 
            this.rbLowPin6.AutoCheck = false;
            this.rbLowPin6.AutoSize = true;
            this.rbLowPin6.Checked = true;
            this.rbLowPin6.Location = new System.Drawing.Point(6, 14);
            this.rbLowPin6.Name = "rbLowPin6";
            this.rbLowPin6.Size = new System.Drawing.Size(45, 17);
            this.rbLowPin6.TabIndex = 1;
            this.rbLowPin6.TabStop = true;
            this.rbLowPin6.Text = "Low";
            this.rbLowPin6.UseVisualStyleBackColor = true;
            // 
            // grpOutputPin5
            // 
            this.grpOutputPin5.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutputPin5.Controls.Add(this.chkIsOutputPin5);
            this.grpOutputPin5.Controls.Add(this.rbHighPin5);
            this.grpOutputPin5.Controls.Add(this.rbLowPin5);
            this.grpOutputPin5.Location = new System.Drawing.Point(6, 184);
            this.grpOutputPin5.Name = "grpOutputPin5";
            this.grpOutputPin5.Size = new System.Drawing.Size(192, 42);
            this.grpOutputPin5.TabIndex = 20;
            this.grpOutputPin5.TabStop = false;
            this.grpOutputPin5.Text = "Pin 5";
            // 
            // chkIsOutputPin5
            // 
            this.chkIsOutputPin5.AutoCheck = false;
            this.chkIsOutputPin5.AutoSize = true;
            this.chkIsOutputPin5.Checked = true;
            this.chkIsOutputPin5.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkIsOutputPin5.Location = new System.Drawing.Point(111, 15);
            this.chkIsOutputPin5.Name = "chkIsOutputPin5";
            this.chkIsOutputPin5.Size = new System.Drawing.Size(69, 17);
            this.chkIsOutputPin5.TabIndex = 5;
            this.chkIsOutputPin5.Text = "Is Output";
            this.chkIsOutputPin5.UseVisualStyleBackColor = true;
            // 
            // rbHighPin5
            // 
            this.rbHighPin5.AutoCheck = false;
            this.rbHighPin5.AutoSize = true;
            this.rbHighPin5.Location = new System.Drawing.Point(57, 14);
            this.rbHighPin5.Name = "rbHighPin5";
            this.rbHighPin5.Size = new System.Drawing.Size(47, 17);
            this.rbHighPin5.TabIndex = 2;
            this.rbHighPin5.TabStop = true;
            this.rbHighPin5.Text = "High";
            this.rbHighPin5.UseVisualStyleBackColor = true;
            // 
            // rbLowPin5
            // 
            this.rbLowPin5.AutoCheck = false;
            this.rbLowPin5.AutoSize = true;
            this.rbLowPin5.Checked = true;
            this.rbLowPin5.Location = new System.Drawing.Point(6, 14);
            this.rbLowPin5.Name = "rbLowPin5";
            this.rbLowPin5.Size = new System.Drawing.Size(45, 17);
            this.rbLowPin5.TabIndex = 1;
            this.rbLowPin5.TabStop = true;
            this.rbLowPin5.Text = "Low";
            this.rbLowPin5.UseVisualStyleBackColor = true;
            // 
            // grpOutputPin4
            // 
            this.grpOutputPin4.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutputPin4.Controls.Add(this.chkIsOutputPin4);
            this.grpOutputPin4.Controls.Add(this.rbHighPin4);
            this.grpOutputPin4.Controls.Add(this.rbLowPin4);
            this.grpOutputPin4.Location = new System.Drawing.Point(6, 142);
            this.grpOutputPin4.Name = "grpOutputPin4";
            this.grpOutputPin4.Size = new System.Drawing.Size(192, 42);
            this.grpOutputPin4.TabIndex = 17;
            this.grpOutputPin4.TabStop = false;
            this.grpOutputPin4.Text = "Pin 4";
            // 
            // chkIsOutputPin4
            // 
            this.chkIsOutputPin4.AutoCheck = false;
            this.chkIsOutputPin4.AutoSize = true;
            this.chkIsOutputPin4.Checked = true;
            this.chkIsOutputPin4.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkIsOutputPin4.Location = new System.Drawing.Point(111, 15);
            this.chkIsOutputPin4.Name = "chkIsOutputPin4";
            this.chkIsOutputPin4.Size = new System.Drawing.Size(69, 17);
            this.chkIsOutputPin4.TabIndex = 5;
            this.chkIsOutputPin4.Text = "Is Output";
            this.chkIsOutputPin4.UseVisualStyleBackColor = true;
            // 
            // rbHighPin4
            // 
            this.rbHighPin4.AutoCheck = false;
            this.rbHighPin4.AutoSize = true;
            this.rbHighPin4.Location = new System.Drawing.Point(57, 14);
            this.rbHighPin4.Name = "rbHighPin4";
            this.rbHighPin4.Size = new System.Drawing.Size(47, 17);
            this.rbHighPin4.TabIndex = 2;
            this.rbHighPin4.TabStop = true;
            this.rbHighPin4.Text = "High";
            this.rbHighPin4.UseVisualStyleBackColor = true;
            // 
            // rbLowPin4
            // 
            this.rbLowPin4.AutoCheck = false;
            this.rbLowPin4.AutoSize = true;
            this.rbLowPin4.Checked = true;
            this.rbLowPin4.Location = new System.Drawing.Point(6, 14);
            this.rbLowPin4.Name = "rbLowPin4";
            this.rbLowPin4.Size = new System.Drawing.Size(45, 17);
            this.rbLowPin4.TabIndex = 1;
            this.rbLowPin4.TabStop = true;
            this.rbLowPin4.Text = "Low";
            this.rbLowPin4.UseVisualStyleBackColor = true;
            // 
            // grpOutputPin3
            // 
            this.grpOutputPin3.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutputPin3.Controls.Add(this.chkIsOutputPin3);
            this.grpOutputPin3.Controls.Add(this.rbHighPin3);
            this.grpOutputPin3.Controls.Add(this.rbLowPin3);
            this.grpOutputPin3.Location = new System.Drawing.Point(6, 100);
            this.grpOutputPin3.Name = "grpOutputPin3";
            this.grpOutputPin3.Size = new System.Drawing.Size(192, 42);
            this.grpOutputPin3.TabIndex = 18;
            this.grpOutputPin3.TabStop = false;
            this.grpOutputPin3.Text = "Pin 3";
            // 
            // chkIsOutputPin3
            // 
            this.chkIsOutputPin3.AutoCheck = false;
            this.chkIsOutputPin3.AutoSize = true;
            this.chkIsOutputPin3.Checked = true;
            this.chkIsOutputPin3.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkIsOutputPin3.Location = new System.Drawing.Point(111, 15);
            this.chkIsOutputPin3.Name = "chkIsOutputPin3";
            this.chkIsOutputPin3.Size = new System.Drawing.Size(69, 17);
            this.chkIsOutputPin3.TabIndex = 5;
            this.chkIsOutputPin3.Text = "Is Output";
            this.chkIsOutputPin3.UseVisualStyleBackColor = true;
            // 
            // rbHighPin3
            // 
            this.rbHighPin3.AutoCheck = false;
            this.rbHighPin3.AutoSize = true;
            this.rbHighPin3.Location = new System.Drawing.Point(57, 14);
            this.rbHighPin3.Name = "rbHighPin3";
            this.rbHighPin3.Size = new System.Drawing.Size(47, 17);
            this.rbHighPin3.TabIndex = 2;
            this.rbHighPin3.TabStop = true;
            this.rbHighPin3.Text = "High";
            this.rbHighPin3.UseVisualStyleBackColor = true;
            // 
            // rbLowPin3
            // 
            this.rbLowPin3.AutoCheck = false;
            this.rbLowPin3.AutoSize = true;
            this.rbLowPin3.Checked = true;
            this.rbLowPin3.Location = new System.Drawing.Point(6, 14);
            this.rbLowPin3.Name = "rbLowPin3";
            this.rbLowPin3.Size = new System.Drawing.Size(45, 17);
            this.rbLowPin3.TabIndex = 1;
            this.rbLowPin3.TabStop = true;
            this.rbLowPin3.Text = "Low";
            this.rbLowPin3.UseVisualStyleBackColor = true;
            // 
            // grpOutputPin2
            // 
            this.grpOutputPin2.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutputPin2.Controls.Add(this.chkIsOutputPin2);
            this.grpOutputPin2.Controls.Add(this.rbHighPin2);
            this.grpOutputPin2.Controls.Add(this.rbLowPin2);
            this.grpOutputPin2.Location = new System.Drawing.Point(6, 58);
            this.grpOutputPin2.Name = "grpOutputPin2";
            this.grpOutputPin2.Size = new System.Drawing.Size(192, 42);
            this.grpOutputPin2.TabIndex = 19;
            this.grpOutputPin2.TabStop = false;
            this.grpOutputPin2.Text = "Pin 2";
            // 
            // chkIsOutputPin2
            // 
            this.chkIsOutputPin2.AutoCheck = false;
            this.chkIsOutputPin2.AutoSize = true;
            this.chkIsOutputPin2.Checked = true;
            this.chkIsOutputPin2.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkIsOutputPin2.Location = new System.Drawing.Point(111, 15);
            this.chkIsOutputPin2.Name = "chkIsOutputPin2";
            this.chkIsOutputPin2.Size = new System.Drawing.Size(69, 17);
            this.chkIsOutputPin2.TabIndex = 5;
            this.chkIsOutputPin2.Text = "Is Output";
            this.chkIsOutputPin2.UseVisualStyleBackColor = true;
            // 
            // rbHighPin2
            // 
            this.rbHighPin2.AutoCheck = false;
            this.rbHighPin2.AutoSize = true;
            this.rbHighPin2.Location = new System.Drawing.Point(57, 14);
            this.rbHighPin2.Name = "rbHighPin2";
            this.rbHighPin2.Size = new System.Drawing.Size(48, 17);
            this.rbHighPin2.TabIndex = 2;
            this.rbHighPin2.TabStop = true;
            this.rbHighPin2.Text = "HIgh";
            this.rbHighPin2.UseVisualStyleBackColor = true;
            // 
            // rbLowPin2
            // 
            this.rbLowPin2.AutoCheck = false;
            this.rbLowPin2.AutoSize = true;
            this.rbLowPin2.Checked = true;
            this.rbLowPin2.Location = new System.Drawing.Point(6, 14);
            this.rbLowPin2.Name = "rbLowPin2";
            this.rbLowPin2.Size = new System.Drawing.Size(45, 17);
            this.rbLowPin2.TabIndex = 1;
            this.rbLowPin2.TabStop = true;
            this.rbLowPin2.Text = "Low";
            this.rbLowPin2.UseVisualStyleBackColor = true;
            // 
            // grpOutputPin1
            // 
            this.grpOutputPin1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutputPin1.Controls.Add(this.chkIsOutputPin1);
            this.grpOutputPin1.Controls.Add(this.rbHighPin1);
            this.grpOutputPin1.Controls.Add(this.rbLowPin1);
            this.grpOutputPin1.Location = new System.Drawing.Point(6, 16);
            this.grpOutputPin1.Name = "grpOutputPin1";
            this.grpOutputPin1.Size = new System.Drawing.Size(192, 42);
            this.grpOutputPin1.TabIndex = 14;
            this.grpOutputPin1.TabStop = false;
            this.grpOutputPin1.Text = "Pin1";
            // 
            // chkIsOutputPin1
            // 
            this.chkIsOutputPin1.AutoCheck = false;
            this.chkIsOutputPin1.AutoSize = true;
            this.chkIsOutputPin1.Checked = true;
            this.chkIsOutputPin1.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkIsOutputPin1.Location = new System.Drawing.Point(111, 15);
            this.chkIsOutputPin1.Name = "chkIsOutputPin1";
            this.chkIsOutputPin1.Size = new System.Drawing.Size(69, 17);
            this.chkIsOutputPin1.TabIndex = 4;
            this.chkIsOutputPin1.Text = "Is Output";
            this.chkIsOutputPin1.UseVisualStyleBackColor = true;
            // 
            // rbHighPin1
            // 
            this.rbHighPin1.AutoCheck = false;
            this.rbHighPin1.AutoSize = true;
            this.rbHighPin1.Location = new System.Drawing.Point(57, 14);
            this.rbHighPin1.Name = "rbHighPin1";
            this.rbHighPin1.Size = new System.Drawing.Size(47, 17);
            this.rbHighPin1.TabIndex = 2;
            this.rbHighPin1.TabStop = true;
            this.rbHighPin1.Text = "High";
            this.rbHighPin1.UseVisualStyleBackColor = true;
            // 
            // rbLowPin1
            // 
            this.rbLowPin1.AutoCheck = false;
            this.rbLowPin1.AutoSize = true;
            this.rbLowPin1.Checked = true;
            this.rbLowPin1.Location = new System.Drawing.Point(6, 14);
            this.rbLowPin1.Name = "rbLowPin1";
            this.rbLowPin1.Size = new System.Drawing.Size(45, 17);
            this.rbLowPin1.TabIndex = 1;
            this.rbLowPin1.TabStop = true;
            this.rbLowPin1.Text = "Low";
            this.rbLowPin1.UseVisualStyleBackColor = true;
            // 
            // grpOutput
            // 
            this.grpOutput.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutput.Controls.Add(this.lbConsole);
            this.grpOutput.Location = new System.Drawing.Point(281, 97);
            this.grpOutput.Name = "grpOutput";
            this.grpOutput.Size = new System.Drawing.Size(291, 363);
            this.grpOutput.TabIndex = 14;
            this.grpOutput.TabStop = false;
            this.grpOutput.Text = "Output";
            // 
            // lbConsole
            // 
            this.lbConsole.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lbConsole.FormattingEnabled = true;
            this.lbConsole.HorizontalScrollbar = true;
            this.lbConsole.Location = new System.Drawing.Point(3, 16);
            this.lbConsole.Name = "lbConsole";
            this.lbConsole.Size = new System.Drawing.Size(285, 344);
            this.lbConsole.TabIndex = 0;
            // 
            // grpAction
            // 
            this.grpAction.Controls.Add(this.btnSet);
            this.grpAction.Controls.Add(this.btnGet);
            this.grpAction.Location = new System.Drawing.Point(625, 12);
            this.grpAction.Name = "grpAction";
            this.grpAction.Size = new System.Drawing.Size(163, 79);
            this.grpAction.TabIndex = 15;
            this.grpAction.TabStop = false;
            // 
            // btnSet
            // 
            this.btnSet.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnSet.Location = new System.Drawing.Point(82, 50);
            this.btnSet.Name = "btnSet";
            this.btnSet.Size = new System.Drawing.Size(75, 23);
            this.btnSet.TabIndex = 1;
            this.btnSet.Text = "Set GPIO";
            this.btnSet.UseVisualStyleBackColor = true;
            this.btnSet.Click += new System.EventHandler(this.btnSet_Click);
            // 
            // btnGet
            // 
            this.btnGet.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnGet.Location = new System.Drawing.Point(82, 15);
            this.btnGet.Name = "btnGet";
            this.btnGet.Size = new System.Drawing.Size(75, 23);
            this.btnGet.TabIndex = 0;
            this.btnGet.Text = "Get GPIO";
            this.btnGet.UseVisualStyleBackColor = true;
            this.btnGet.Click += new System.EventHandler(this.btnGetGPIO_Click);
            // 
            // psCommSimpleWinForms
            // 
            this.psCommSimpleWinForms.EnableBluetooth = false;
            this.psCommSimpleWinForms.EnableSerialPort = false;
            this.psCommSimpleWinForms.Parent = this;
            this.psCommSimpleWinForms.ReceiveStatus += new PalmSens.Comm.StatusEventHandler(this.psCommSimpleWinForms_ReceiveStatus);
            this.psCommSimpleWinForms.StateChanged += new PalmSens.Comm.CommManager.StatusChangedEventHandler(this.psCommSimpleWinForms_StateChanged);
            this.psCommSimpleWinForms.Disconnected += new PalmSens.Core.Simplified.DisconnectedEventHandler(this.psCommSimpleWinForms_Disconnected);
            // 
            // FrmGPIO
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 466);
            this.Controls.Add(this.grpAction);
            this.Controls.Add(this.grpOutput);
            this.Controls.Add(this.grpPinOutput);
            this.Controls.Add(this.grpPinSelection);
            this.Controls.Add(this.grpDevice);
            this.Controls.Add(this.grpConnection);
            this.Name = "FrmGPIO";
            this.Text = "FrmGPIO";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.FrmGPIO_FormClosing);
            this.Load += new System.EventHandler(this.FrmGPIO_Load);
            this.grpConnection.ResumeLayout(false);
            this.grpDevice.ResumeLayout(false);
            this.grpDevice.PerformLayout();
            this.grpPinSelection.ResumeLayout(false);
            this.grpPin8.ResumeLayout(false);
            this.grpPin8.PerformLayout();
            this.grpPin7.ResumeLayout(false);
            this.grpPin7.PerformLayout();
            this.grpPin6.ResumeLayout(false);
            this.grpPin6.PerformLayout();
            this.grpPin5.ResumeLayout(false);
            this.grpPin5.PerformLayout();
            this.grpPin4.ResumeLayout(false);
            this.grpPin4.PerformLayout();
            this.grpPin3.ResumeLayout(false);
            this.grpPin3.PerformLayout();
            this.grpPin2.ResumeLayout(false);
            this.grpPin2.PerformLayout();
            this.grpPin1.ResumeLayout(false);
            this.grpPin1.PerformLayout();
            this.grpPinOutput.ResumeLayout(false);
            this.grpOutputPin8.ResumeLayout(false);
            this.grpOutputPin8.PerformLayout();
            this.grpOutputPin7.ResumeLayout(false);
            this.grpOutputPin7.PerformLayout();
            this.grpOutputPin6.ResumeLayout(false);
            this.grpOutputPin6.PerformLayout();
            this.grpOutputPin5.ResumeLayout(false);
            this.grpOutputPin5.PerformLayout();
            this.grpOutputPin4.ResumeLayout(false);
            this.grpOutputPin4.PerformLayout();
            this.grpOutputPin3.ResumeLayout(false);
            this.grpOutputPin3.PerformLayout();
            this.grpOutputPin2.ResumeLayout(false);
            this.grpOutputPin2.PerformLayout();
            this.grpOutputPin1.ResumeLayout(false);
            this.grpOutputPin1.PerformLayout();
            this.grpOutput.ResumeLayout(false);
            this.grpAction.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private PalmSens.Core.Simplified.WinForms.PSCommSimpleWinForms psCommSimpleWinForms;
        private System.Windows.Forms.GroupBox grpConnection;
        private System.Windows.Forms.ComboBox cmbDevices;
        private System.Windows.Forms.Button btnRefresh;
        private System.Windows.Forms.Button btnConnect;
        private System.Windows.Forms.GroupBox grpDevice;
        private System.Windows.Forms.Label lblStatus;
        private System.Windows.Forms.TextBox tbDeviceStatus;
        private System.Windows.Forms.Label lblCurrentRange;
        private System.Windows.Forms.Label lblCurrent;
        private System.Windows.Forms.TextBox tbCurrent;
        private System.Windows.Forms.Label lblVolt;
        private System.Windows.Forms.TextBox tbPotential;
        private System.Windows.Forms.Label lblPotential;
        private System.Windows.Forms.GroupBox grpPinSelection;
        private System.Windows.Forms.GroupBox grpPinOutput;
        private System.Windows.Forms.RadioButton radioPin1Set;
        private System.Windows.Forms.RadioButton radioPin1Get;
        private System.Windows.Forms.Label lblPin1;
        private System.Windows.Forms.GroupBox grpPin1;
        private System.Windows.Forms.GroupBox grpPin8;
        private System.Windows.Forms.Label lblPin8;
        private System.Windows.Forms.RadioButton radioPin8Set;
        private System.Windows.Forms.RadioButton radioPin8Get;
        private System.Windows.Forms.GroupBox grpPin7;
        private System.Windows.Forms.Label lblPin7;
        private System.Windows.Forms.RadioButton radioPin7Set;
        private System.Windows.Forms.RadioButton radioPin7Get;
        private System.Windows.Forms.GroupBox grpPin6;
        private System.Windows.Forms.Label lblPin6;
        private System.Windows.Forms.RadioButton radioPin6Set;
        private System.Windows.Forms.RadioButton radioPin6Get;
        private System.Windows.Forms.GroupBox grpPin5;
        private System.Windows.Forms.Label lblPin5;
        private System.Windows.Forms.RadioButton radioPin5Set;
        private System.Windows.Forms.RadioButton radioPin5Get;
        private System.Windows.Forms.GroupBox grpPin4;
        private System.Windows.Forms.Label lblPin4;
        private System.Windows.Forms.RadioButton radioPin4Set;
        private System.Windows.Forms.RadioButton radioPin4Get;
        private System.Windows.Forms.GroupBox grpPin3;
        private System.Windows.Forms.Label lblPin3;
        private System.Windows.Forms.RadioButton radioPin3Set;
        private System.Windows.Forms.RadioButton radioPin3Get;
        private System.Windows.Forms.GroupBox grpPin2;
        private System.Windows.Forms.Label lblPin2;
        private System.Windows.Forms.RadioButton radioPin2Set;
        private System.Windows.Forms.RadioButton radioPin2Get;
        private System.Windows.Forms.CheckBox chkPin2SetHigh;
        private System.Windows.Forms.CheckBox chkPin1SetHigh;
        private System.Windows.Forms.CheckBox chkPin8SetHigh;
        private System.Windows.Forms.CheckBox chkPin7SetHigh;
        private System.Windows.Forms.CheckBox chkPin6SetHigh;
        private System.Windows.Forms.CheckBox chkPin5SetHigh;
        private System.Windows.Forms.CheckBox chkPin4SetHigh;
        private System.Windows.Forms.CheckBox chkPin3SetHigh;
        private System.Windows.Forms.GroupBox grpOutput;
        private System.Windows.Forms.ListBox lbConsole;
        private System.Windows.Forms.GroupBox grpAction;
        private System.Windows.Forms.Button btnGet;
        private System.Windows.Forms.Button btnSet;
        private System.Windows.Forms.GroupBox grpOutputPin8;
        private System.Windows.Forms.RadioButton rbHighPin8;
        private System.Windows.Forms.RadioButton rbLowPin8;
        private System.Windows.Forms.GroupBox grpOutputPin7;
        private System.Windows.Forms.RadioButton rbHighPin7;
        private System.Windows.Forms.RadioButton rbLowPin7;
        private System.Windows.Forms.GroupBox grpOutputPin6;
        private System.Windows.Forms.RadioButton rbHighPin6;
        private System.Windows.Forms.RadioButton rbLowPin6;
        private System.Windows.Forms.GroupBox grpOutputPin5;
        private System.Windows.Forms.RadioButton rbHighPin5;
        private System.Windows.Forms.RadioButton rbLowPin5;
        private System.Windows.Forms.GroupBox grpOutputPin4;
        private System.Windows.Forms.RadioButton rbHighPin4;
        private System.Windows.Forms.RadioButton rbLowPin4;
        private System.Windows.Forms.GroupBox grpOutputPin3;
        private System.Windows.Forms.RadioButton rbHighPin3;
        private System.Windows.Forms.RadioButton rbLowPin3;
        private System.Windows.Forms.GroupBox grpOutputPin2;
        private System.Windows.Forms.RadioButton rbHighPin2;
        private System.Windows.Forms.RadioButton rbLowPin2;
        private System.Windows.Forms.GroupBox grpOutputPin1;
        private System.Windows.Forms.RadioButton rbHighPin1;
        private System.Windows.Forms.RadioButton rbLowPin1;
        private System.Windows.Forms.CheckBox chkIsOutputPin1;
        private System.Windows.Forms.CheckBox chkIsOutputPin8;
        private System.Windows.Forms.CheckBox chkIsOutputPin7;
        private System.Windows.Forms.CheckBox chkIsOutputPin6;
        private System.Windows.Forms.CheckBox chkIsOutputPin5;
        private System.Windows.Forms.CheckBox chkIsOutputPin4;
        private System.Windows.Forms.CheckBox chkIsOutputPin3;
        private System.Windows.Forms.CheckBox chkIsOutputPin2;
    }
}