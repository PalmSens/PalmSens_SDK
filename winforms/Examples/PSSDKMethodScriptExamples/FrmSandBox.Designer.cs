
namespace PSSDKMethodScriptExamples
{
    partial class FrmSandBox
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
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.grpConnection = new System.Windows.Forms.GroupBox();
            this.cmbDevices = new System.Windows.Forms.ComboBox();
            this.btnRefresh = new System.Windows.Forms.Button();
            this.btnConnect = new System.Windows.Forms.Button();
            this.grpDevice = new System.Windows.Forms.GroupBox();
            this.label1 = new System.Windows.Forms.Label();
            this.tbDeviceStatus = new System.Windows.Forms.TextBox();
            this.lblCurrentRange = new System.Windows.Forms.Label();
            this.lblCurrent = new System.Windows.Forms.Label();
            this.tbCurrent = new System.Windows.Forms.TextBox();
            this.lblVolt = new System.Windows.Forms.Label();
            this.tbPotential = new System.Windows.Forms.TextBox();
            this.lblPotential = new System.Windows.Forms.Label();
            this.groupBoxOptions = new System.Windows.Forms.GroupBox();
            this.lblUse = new System.Windows.Forms.Label();
            this.rbSetter = new System.Windows.Forms.RadioButton();
            this.rbGetter = new System.Windows.Forms.RadioButton();
            this.rbSandBox = new System.Windows.Forms.RadioButton();
            this.btnRun = new System.Windows.Forms.Button();
            this.lblMethod = new System.Windows.Forms.Label();
            this.cmbMethod = new System.Windows.Forms.ComboBox();
            this.groupBoxMeasure = new System.Windows.Forms.GroupBox();
            this.dgvMeasurement = new System.Windows.Forms.DataGridView();
            this.grpOutput = new System.Windows.Forms.GroupBox();
            this.lbConsole = new System.Windows.Forms.ListBox();
            this.groupBoxScript = new System.Windows.Forms.GroupBox();
            this.txtScript = new System.Windows.Forms.TextBox();
            this.psCommSimpleWinForms = new PalmSens.Core.Simplified.WinForms.PSCommSimpleWinForms(this.components);
            this.chkEnableBluetooth = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            this.grpConnection.SuspendLayout();
            this.grpDevice.SuspendLayout();
            this.groupBoxOptions.SuspendLayout();
            this.groupBoxMeasure.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvMeasurement)).BeginInit();
            this.grpOutput.SuspendLayout();
            this.groupBoxScript.SuspendLayout();
            this.SuspendLayout();
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.FixedPanel = System.Windows.Forms.FixedPanel.Panel1;
            this.splitContainer1.IsSplitterFixed = true;
            this.splitContainer1.Location = new System.Drawing.Point(0, 0);
            this.splitContainer1.Name = "splitContainer1";
            this.splitContainer1.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.grpConnection);
            this.splitContainer1.Panel1.Controls.Add(this.grpDevice);
            this.splitContainer1.Panel1.Controls.Add(this.groupBoxOptions);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.groupBoxMeasure);
            this.splitContainer1.Panel2.Controls.Add(this.grpOutput);
            this.splitContainer1.Panel2.Controls.Add(this.groupBoxScript);
            this.splitContainer1.Size = new System.Drawing.Size(880, 450);
            this.splitContainer1.SplitterDistance = 86;
            this.splitContainer1.TabIndex = 0;
            // 
            // grpConnection
            // 
            this.grpConnection.Controls.Add(this.chkEnableBluetooth);
            this.grpConnection.Controls.Add(this.cmbDevices);
            this.grpConnection.Controls.Add(this.btnRefresh);
            this.grpConnection.Controls.Add(this.btnConnect);
            this.grpConnection.Location = new System.Drawing.Point(12, 3);
            this.grpConnection.Name = "grpConnection";
            this.grpConnection.Size = new System.Drawing.Size(257, 79);
            this.grpConnection.TabIndex = 5;
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
            this.grpDevice.Controls.Add(this.label1);
            this.grpDevice.Controls.Add(this.tbDeviceStatus);
            this.grpDevice.Controls.Add(this.lblCurrentRange);
            this.grpDevice.Controls.Add(this.lblCurrent);
            this.grpDevice.Controls.Add(this.tbCurrent);
            this.grpDevice.Controls.Add(this.lblVolt);
            this.grpDevice.Controls.Add(this.tbPotential);
            this.grpDevice.Controls.Add(this.lblPotential);
            this.grpDevice.Location = new System.Drawing.Point(581, 3);
            this.grpDevice.Name = "grpDevice";
            this.grpDevice.Size = new System.Drawing.Size(296, 79);
            this.grpDevice.TabIndex = 9;
            this.grpDevice.TabStop = false;
            this.grpDevice.Text = "Device Status";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(189, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(40, 13);
            this.label1.TabIndex = 7;
            this.label1.Text = "Status:";
            // 
            // tbDeviceStatus
            // 
            this.tbDeviceStatus.Location = new System.Drawing.Point(192, 45);
            this.tbDeviceStatus.Name = "tbDeviceStatus";
            this.tbDeviceStatus.ReadOnly = true;
            this.tbDeviceStatus.Size = new System.Drawing.Size(98, 20);
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
            // groupBoxOptions
            // 
            this.groupBoxOptions.Controls.Add(this.lblUse);
            this.groupBoxOptions.Controls.Add(this.rbSetter);
            this.groupBoxOptions.Controls.Add(this.rbGetter);
            this.groupBoxOptions.Controls.Add(this.rbSandBox);
            this.groupBoxOptions.Controls.Add(this.btnRun);
            this.groupBoxOptions.Controls.Add(this.lblMethod);
            this.groupBoxOptions.Controls.Add(this.cmbMethod);
            this.groupBoxOptions.Location = new System.Drawing.Point(275, 3);
            this.groupBoxOptions.Name = "groupBoxOptions";
            this.groupBoxOptions.Size = new System.Drawing.Size(300, 79);
            this.groupBoxOptions.TabIndex = 0;
            this.groupBoxOptions.TabStop = false;
            this.groupBoxOptions.Text = "Options";
            // 
            // lblUse
            // 
            this.lblUse.AutoSize = true;
            this.lblUse.Location = new System.Drawing.Point(7, 49);
            this.lblUse.Name = "lblUse";
            this.lblUse.Size = new System.Drawing.Size(29, 13);
            this.lblUse.TabIndex = 8;
            this.lblUse.Text = "Use:";
            // 
            // rbSetter
            // 
            this.rbSetter.AutoSize = true;
            this.rbSetter.Location = new System.Drawing.Point(185, 47);
            this.rbSetter.Name = "rbSetter";
            this.rbSetter.Size = new System.Drawing.Size(53, 17);
            this.rbSetter.TabIndex = 7;
            this.rbSetter.Text = "Setter";
            this.rbSetter.UseVisualStyleBackColor = true;
            // 
            // rbGetter
            // 
            this.rbGetter.AutoSize = true;
            this.rbGetter.Location = new System.Drawing.Point(125, 47);
            this.rbGetter.Name = "rbGetter";
            this.rbGetter.Size = new System.Drawing.Size(54, 17);
            this.rbGetter.TabIndex = 6;
            this.rbGetter.Text = "Getter";
            this.rbGetter.UseVisualStyleBackColor = true;
            // 
            // rbSandBox
            // 
            this.rbSandBox.AutoSize = true;
            this.rbSandBox.Checked = true;
            this.rbSandBox.Location = new System.Drawing.Point(48, 47);
            this.rbSandBox.Name = "rbSandBox";
            this.rbSandBox.Size = new System.Drawing.Size(71, 17);
            this.rbSandBox.TabIndex = 5;
            this.rbSandBox.TabStop = true;
            this.rbSandBox.Text = "Sand Box";
            this.rbSandBox.UseVisualStyleBackColor = true;
            // 
            // btnRun
            // 
            this.btnRun.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnRun.Location = new System.Drawing.Point(251, 44);
            this.btnRun.Name = "btnRun";
            this.btnRun.Size = new System.Drawing.Size(37, 23);
            this.btnRun.TabIndex = 4;
            this.btnRun.Text = "Run";
            this.btnRun.UseVisualStyleBackColor = true;
            this.btnRun.Click += new System.EventHandler(this.btnRun_Click);
            // 
            // lblMethod
            // 
            this.lblMethod.AutoSize = true;
            this.lblMethod.Location = new System.Drawing.Point(7, 20);
            this.lblMethod.Name = "lblMethod";
            this.lblMethod.Size = new System.Drawing.Size(93, 13);
            this.lblMethod.TabIndex = 1;
            this.lblMethod.Text = "Method Template:";
            // 
            // cmbMethod
            // 
            this.cmbMethod.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.cmbMethod.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbMethod.FormattingEnabled = true;
            this.cmbMethod.Location = new System.Drawing.Point(106, 17);
            this.cmbMethod.Name = "cmbMethod";
            this.cmbMethod.Size = new System.Drawing.Size(182, 21);
            this.cmbMethod.TabIndex = 0;
            this.cmbMethod.SelectedIndexChanged += new System.EventHandler(this.cmbMethod_SelectedIndexChanged);
            // 
            // groupBoxMeasure
            // 
            this.groupBoxMeasure.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBoxMeasure.Controls.Add(this.dgvMeasurement);
            this.groupBoxMeasure.Location = new System.Drawing.Point(607, 3);
            this.groupBoxMeasure.Name = "groupBoxMeasure";
            this.groupBoxMeasure.Size = new System.Drawing.Size(270, 354);
            this.groupBoxMeasure.TabIndex = 10;
            this.groupBoxMeasure.TabStop = false;
            this.groupBoxMeasure.Text = "Measure";
            // 
            // dgvMeasurement
            // 
            this.dgvMeasurement.AllowUserToAddRows = false;
            this.dgvMeasurement.AllowUserToDeleteRows = false;
            this.dgvMeasurement.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvMeasurement.Dock = System.Windows.Forms.DockStyle.Fill;
            this.dgvMeasurement.EditMode = System.Windows.Forms.DataGridViewEditMode.EditProgrammatically;
            this.dgvMeasurement.Location = new System.Drawing.Point(3, 16);
            this.dgvMeasurement.Name = "dgvMeasurement";
            this.dgvMeasurement.ReadOnly = true;
            this.dgvMeasurement.RowHeadersVisible = false;
            this.dgvMeasurement.Size = new System.Drawing.Size(264, 335);
            this.dgvMeasurement.TabIndex = 5;
            // 
            // grpOutput
            // 
            this.grpOutput.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpOutput.Controls.Add(this.lbConsole);
            this.grpOutput.Location = new System.Drawing.Point(355, 3);
            this.grpOutput.Name = "grpOutput";
            this.grpOutput.Size = new System.Drawing.Size(246, 351);
            this.grpOutput.TabIndex = 8;
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
            this.lbConsole.Size = new System.Drawing.Size(240, 332);
            this.lbConsole.TabIndex = 0;
            // 
            // groupBoxScript
            // 
            this.groupBoxScript.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBoxScript.Controls.Add(this.txtScript);
            this.groupBoxScript.Location = new System.Drawing.Point(0, 3);
            this.groupBoxScript.Name = "groupBoxScript";
            this.groupBoxScript.Size = new System.Drawing.Size(349, 354);
            this.groupBoxScript.TabIndex = 0;
            this.groupBoxScript.TabStop = false;
            this.groupBoxScript.Text = "Script";
            // 
            // txtScript
            // 
            this.txtScript.AcceptsReturn = true;
            this.txtScript.AutoCompleteCustomSource.AddRange(new string[] {
            "var",
            "store_var",
            "copy_var",
            "add_var",
            "sub_var",
            "mul_var",
            "div_var",
            "set_e wait",
            "set_int",
            "await_int",
            "loop",
            "endloop",
            "meas",
            "meas_loop_lsv",
            "meas_loop_cv",
            "meas_loop_dpv",
            "meas_loop_swv",
            "meas_loop_npv",
            "meas_loop_ca",
            "meas_loop_pad",
            "meas_loop_ocp",
            "meas_loop_eis",
            "meas_loop_cp",
            "meas_loop_lsp",
            "set_range",
            "set_autoranging",
            "set_range_minmax",
            "pck_start",
            "pck_add",
            "pck_end",
            "set_max_bandwidth",
            "set_cr",
            "cell_on",
            "cell_off",
            "set_pgstat_mode",
            "send_string",
            "set_gpio_cfg",
            "set_gpio_pullup",
            "set_gpio",
            "get_gpio",
            "set_pot_range",
            "set_pgstat_chan",
            "set_poly_we_mode",
            "if",
            "elseif",
            "else",
            "endif",
            "get_time",
            "timer_start",
            "timer_get",
            "breakloop",
            "array",
            "array_get",
            "array_set",
            "file_open",
            "file_close",
            "set_script_output",
            "i2c_config",
            "i2c_write",
            "i2c_write_byte",
            "i2c_read",
            "i2c_read_byte",
            "i2c_write_read",
            "hibernate",
            "abort",
            "poly_we",
            "nscans",
            "meta_msk",
            "on_finished"});
            this.txtScript.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.SuggestAppend;
            this.txtScript.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.CustomSource;
            this.txtScript.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtScript.Location = new System.Drawing.Point(3, 16);
            this.txtScript.Multiline = true;
            this.txtScript.Name = "txtScript";
            this.txtScript.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtScript.Size = new System.Drawing.Size(343, 335);
            this.txtScript.TabIndex = 0;
            this.txtScript.WordWrap = false;
            // 
            // psCommSimpleWinForms
            // 
            this.psCommSimpleWinForms.EnableBluetooth = false;
            this.psCommSimpleWinForms.EnableSerialPort = false;
            this.psCommSimpleWinForms.Parent = this;
            this.psCommSimpleWinForms.ReceiveStatus += new PalmSens.Comm.StatusEventHandler(this.psCommSimpleWinForms_ReceiveStatus);
            this.psCommSimpleWinForms.MeasurementStarted += new System.EventHandler(this.psCommSimpleWinForms_MeasurementStarted);
            this.psCommSimpleWinForms.MeasurementEnded += new System.EventHandler<System.Exception>(this.psCommSimpleWinForms_MeasurementEnded);
            this.psCommSimpleWinForms.SimpleCurveStartReceivingData += new PalmSens.Core.Simplified.PSCommSimple.SimpleCurveStartReceivingDataHandler(this.psCommSimpleWinForms_SimpleCurveStartReceivingData);
            this.psCommSimpleWinForms.StateChanged += new PalmSens.Comm.CommManager.StatusChangedEventHandler(this.psCommSimpleWinForms_StateChanged);
            this.psCommSimpleWinForms.Disconnected += new PalmSens.Core.Simplified.DisconnectedEventHandler(this.psCommSimpleWinForms_Disconnected);
            // 
            // chkEnableBluetooth
            // 
            this.chkEnableBluetooth.AutoSize = true;
            this.chkEnableBluetooth.Location = new System.Drawing.Point(6, 47);
            this.chkEnableBluetooth.Name = "chkEnableBluetooth";
            this.chkEnableBluetooth.Size = new System.Drawing.Size(71, 17);
            this.chkEnableBluetooth.TabIndex = 3;
            this.chkEnableBluetooth.Text = "Bluetooth";
            this.chkEnableBluetooth.UseVisualStyleBackColor = true;
            // 
            // FrmSandBox
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(880, 450);
            this.Controls.Add(this.splitContainer1);
            this.Name = "FrmSandBox";
            this.Text = "FrmSandBox";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.FrmSandBox_FormClosing);
            this.Load += new System.EventHandler(this.FrmSandBox_Load);
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            this.grpConnection.ResumeLayout(false);
            this.grpConnection.PerformLayout();
            this.grpDevice.ResumeLayout(false);
            this.grpDevice.PerformLayout();
            this.groupBoxOptions.ResumeLayout(false);
            this.groupBoxOptions.PerformLayout();
            this.groupBoxMeasure.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dgvMeasurement)).EndInit();
            this.grpOutput.ResumeLayout(false);
            this.groupBoxScript.ResumeLayout(false);
            this.groupBoxScript.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.GroupBox groupBoxOptions;
        private System.Windows.Forms.GroupBox groupBoxScript;
        private System.Windows.Forms.TextBox txtScript;
        private System.Windows.Forms.Button btnRun;
        private System.Windows.Forms.Label lblMethod;
        private System.Windows.Forms.ComboBox cmbMethod;
        private System.Windows.Forms.GroupBox grpConnection;
        private System.Windows.Forms.ComboBox cmbDevices;
        private System.Windows.Forms.Button btnRefresh;
        private System.Windows.Forms.Button btnConnect;
        private PalmSens.Core.Simplified.WinForms.PSCommSimpleWinForms psCommSimpleWinForms;
        private System.Windows.Forms.GroupBox grpOutput;
        private System.Windows.Forms.ListBox lbConsole;
        private System.Windows.Forms.GroupBox grpDevice;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tbDeviceStatus;
        private System.Windows.Forms.Label lblCurrentRange;
        private System.Windows.Forms.Label lblCurrent;
        private System.Windows.Forms.TextBox tbCurrent;
        private System.Windows.Forms.Label lblVolt;
        private System.Windows.Forms.TextBox tbPotential;
        private System.Windows.Forms.Label lblPotential;
        private System.Windows.Forms.GroupBox groupBoxMeasure;
        private System.Windows.Forms.DataGridView dgvMeasurement;
        private System.Windows.Forms.RadioButton rbSandBox;
        private System.Windows.Forms.Label lblUse;
        private System.Windows.Forms.RadioButton rbSetter;
        private System.Windows.Forms.RadioButton rbGetter;
        private System.Windows.Forms.CheckBox chkEnableBluetooth;
    }
}