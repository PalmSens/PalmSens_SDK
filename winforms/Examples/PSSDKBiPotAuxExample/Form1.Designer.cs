namespace PSSDKBiPotAuxExample
{
    partial class Form1
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
            this.cmbDevices = new System.Windows.Forms.ComboBox();
            this.btnRefresh = new System.Windows.Forms.Button();
            this.btnConnect = new System.Windows.Forms.Button();
            this.btnMeasureBiPot = new System.Windows.Forms.Button();
            this.grpConnection = new System.Windows.Forms.GroupBox();
            this.grpDevice = new System.Windows.Forms.GroupBox();
            this.cmbStatusExtraValue = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.tbExtraValue = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.tbDeviceStatus = new System.Windows.Forms.TextBox();
            this.lblCurrentRange = new System.Windows.Forms.Label();
            this.lblCurrent = new System.Windows.Forms.Label();
            this.tbCurrent = new System.Windows.Forms.TextBox();
            this.lblVolt = new System.Windows.Forms.Label();
            this.tbPotential = new System.Windows.Forms.TextBox();
            this.lblPotential = new System.Windows.Forms.Label();
            this.grpMeasurement = new System.Windows.Forms.GroupBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btnMeasureAux = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.label2 = new System.Windows.Forms.Label();
            this.tbBiPotPotential = new System.Windows.Forms.TextBox();
            this.cmbBiPotMode = new System.Windows.Forms.ComboBox();
            this.dgvMeasurement = new System.Windows.Forms.DataGridView();
            this.grpConsole = new System.Windows.Forms.GroupBox();
            this.lbConsole = new System.Windows.Forms.ListBox();
            this.psCommSimpleWinForms = new PalmSens.Core.Simplified.WinForms.PSCommSimpleWinForms(this.components);
            this.lblExtaValueUnit = new System.Windows.Forms.Label();
            this.grpConnection.SuspendLayout();
            this.grpDevice.SuspendLayout();
            this.grpMeasurement.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvMeasurement)).BeginInit();
            this.grpConsole.SuspendLayout();
            this.SuspendLayout();
            // 
            // cmbDevices
            // 
            this.cmbDevices.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbDevices.FormattingEnabled = true;
            this.cmbDevices.Location = new System.Drawing.Point(6, 19);
            this.cmbDevices.Name = "cmbDevices";
            this.cmbDevices.Size = new System.Drawing.Size(155, 21);
            this.cmbDevices.TabIndex = 0;
            // 
            // btnRefresh
            // 
            this.btnRefresh.Location = new System.Drawing.Point(6, 46);
            this.btnRefresh.Name = "btnRefresh";
            this.btnRefresh.Size = new System.Drawing.Size(75, 23);
            this.btnRefresh.TabIndex = 1;
            this.btnRefresh.Text = "Refresh";
            this.btnRefresh.UseVisualStyleBackColor = true;
            this.btnRefresh.Click += new System.EventHandler(this.btnRefresh_Click);
            // 
            // btnConnect
            // 
            this.btnConnect.Enabled = false;
            this.btnConnect.Location = new System.Drawing.Point(86, 46);
            this.btnConnect.Name = "btnConnect";
            this.btnConnect.Size = new System.Drawing.Size(75, 23);
            this.btnConnect.TabIndex = 2;
            this.btnConnect.Text = "Connect";
            this.btnConnect.UseVisualStyleBackColor = true;
            this.btnConnect.Click += new System.EventHandler(this.btnConnect_Click);
            // 
            // btnMeasureBiPot
            // 
            this.btnMeasureBiPot.Enabled = false;
            this.btnMeasureBiPot.Location = new System.Drawing.Point(86, 45);
            this.btnMeasureBiPot.Name = "btnMeasureBiPot";
            this.btnMeasureBiPot.Size = new System.Drawing.Size(75, 23);
            this.btnMeasureBiPot.TabIndex = 3;
            this.btnMeasureBiPot.Text = "Measure";
            this.btnMeasureBiPot.UseVisualStyleBackColor = true;
            this.btnMeasureBiPot.Click += new System.EventHandler(this.btnMeasureBiPot_Click);
            // 
            // grpConnection
            // 
            this.grpConnection.Controls.Add(this.cmbDevices);
            this.grpConnection.Controls.Add(this.btnRefresh);
            this.grpConnection.Controls.Add(this.btnConnect);
            this.grpConnection.Location = new System.Drawing.Point(12, 10);
            this.grpConnection.Name = "grpConnection";
            this.grpConnection.Size = new System.Drawing.Size(171, 79);
            this.grpConnection.TabIndex = 4;
            this.grpConnection.TabStop = false;
            this.grpConnection.Text = "Connection";
            // 
            // grpDevice
            // 
            this.grpDevice.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpDevice.Controls.Add(this.lblExtaValueUnit);
            this.grpDevice.Controls.Add(this.cmbStatusExtraValue);
            this.grpDevice.Controls.Add(this.label3);
            this.grpDevice.Controls.Add(this.tbExtraValue);
            this.grpDevice.Controls.Add(this.label1);
            this.grpDevice.Controls.Add(this.tbDeviceStatus);
            this.grpDevice.Controls.Add(this.lblCurrentRange);
            this.grpDevice.Controls.Add(this.lblCurrent);
            this.grpDevice.Controls.Add(this.tbCurrent);
            this.grpDevice.Controls.Add(this.lblVolt);
            this.grpDevice.Controls.Add(this.tbPotential);
            this.grpDevice.Controls.Add(this.lblPotential);
            this.grpDevice.Location = new System.Drawing.Point(190, 10);
            this.grpDevice.Name = "grpDevice";
            this.grpDevice.Size = new System.Drawing.Size(374, 99);
            this.grpDevice.TabIndex = 5;
            this.grpDevice.TabStop = false;
            this.grpDevice.Text = "Device Status";
            // 
            // cmbStatusExtraValue
            // 
            this.cmbStatusExtraValue.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbStatusExtraValue.Enabled = false;
            this.cmbStatusExtraValue.FormattingEnabled = true;
            this.cmbStatusExtraValue.Items.AddRange(new object[] {
            "BiPot",
            "Aux"});
            this.cmbStatusExtraValue.Location = new System.Drawing.Point(203, 71);
            this.cmbStatusExtraValue.Name = "cmbStatusExtraValue";
            this.cmbStatusExtraValue.Size = new System.Drawing.Size(87, 21);
            this.cmbStatusExtraValue.TabIndex = 10;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(7, 74);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(64, 13);
            this.label3.TabIndex = 9;
            this.label3.Text = "Extra Value:";
            // 
            // tbExtraValue
            // 
            this.tbExtraValue.Location = new System.Drawing.Point(77, 71);
            this.tbExtraValue.Name = "tbExtraValue";
            this.tbExtraValue.ReadOnly = true;
            this.tbExtraValue.Size = new System.Drawing.Size(70, 20);
            this.tbExtraValue.TabIndex = 8;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(200, 22);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(40, 13);
            this.label1.TabIndex = 7;
            this.label1.Text = "Status:";
            // 
            // tbDeviceStatus
            // 
            this.tbDeviceStatus.Location = new System.Drawing.Point(246, 19);
            this.tbDeviceStatus.Name = "tbDeviceStatus";
            this.tbDeviceStatus.ReadOnly = true;
            this.tbDeviceStatus.Size = new System.Drawing.Size(87, 20);
            this.tbDeviceStatus.TabIndex = 6;
            // 
            // lblCurrentRange
            // 
            this.lblCurrentRange.AutoSize = true;
            this.lblCurrentRange.Location = new System.Drawing.Point(153, 48);
            this.lblCurrentRange.Name = "lblCurrentRange";
            this.lblCurrentRange.Size = new System.Drawing.Size(44, 13);
            this.lblCurrentRange.TabIndex = 5;
            this.lblCurrentRange.Text = "* 10 mA";
            // 
            // lblCurrent
            // 
            this.lblCurrent.AutoSize = true;
            this.lblCurrent.Location = new System.Drawing.Point(7, 48);
            this.lblCurrent.Name = "lblCurrent";
            this.lblCurrent.Size = new System.Drawing.Size(44, 13);
            this.lblCurrent.TabIndex = 4;
            this.lblCurrent.Text = "Current:";
            // 
            // tbCurrent
            // 
            this.tbCurrent.Location = new System.Drawing.Point(77, 45);
            this.tbCurrent.Name = "tbCurrent";
            this.tbCurrent.ReadOnly = true;
            this.tbCurrent.Size = new System.Drawing.Size(70, 20);
            this.tbCurrent.TabIndex = 3;
            // 
            // lblVolt
            // 
            this.lblVolt.AutoSize = true;
            this.lblVolt.Location = new System.Drawing.Point(153, 22);
            this.lblVolt.Name = "lblVolt";
            this.lblVolt.Size = new System.Drawing.Size(14, 13);
            this.lblVolt.TabIndex = 2;
            this.lblVolt.Text = "V";
            // 
            // tbPotential
            // 
            this.tbPotential.Location = new System.Drawing.Point(77, 19);
            this.tbPotential.Name = "tbPotential";
            this.tbPotential.ReadOnly = true;
            this.tbPotential.Size = new System.Drawing.Size(70, 20);
            this.tbPotential.TabIndex = 1;
            // 
            // lblPotential
            // 
            this.lblPotential.AutoSize = true;
            this.lblPotential.Location = new System.Drawing.Point(7, 22);
            this.lblPotential.Name = "lblPotential";
            this.lblPotential.Size = new System.Drawing.Size(51, 13);
            this.lblPotential.TabIndex = 0;
            this.lblPotential.Text = "Potential:";
            // 
            // grpMeasurement
            // 
            this.grpMeasurement.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpMeasurement.Controls.Add(this.groupBox1);
            this.grpMeasurement.Controls.Add(this.groupBox2);
            this.grpMeasurement.Controls.Add(this.dgvMeasurement);
            this.grpMeasurement.Location = new System.Drawing.Point(190, 115);
            this.grpMeasurement.Name = "grpMeasurement";
            this.grpMeasurement.Size = new System.Drawing.Size(374, 284);
            this.grpMeasurement.TabIndex = 6;
            this.grpMeasurement.TabStop = false;
            this.grpMeasurement.Text = "Measurement";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.btnMeasureAux);
            this.groupBox1.Location = new System.Drawing.Point(184, 19);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(108, 48);
            this.groupBox1.TabIndex = 9;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Aux Measurement";
            // 
            // btnMeasureAux
            // 
            this.btnMeasureAux.Enabled = false;
            this.btnMeasureAux.Location = new System.Drawing.Point(27, 17);
            this.btnMeasureAux.Name = "btnMeasureAux";
            this.btnMeasureAux.Size = new System.Drawing.Size(75, 23);
            this.btnMeasureAux.TabIndex = 10;
            this.btnMeasureAux.Text = "Measure";
            this.btnMeasureAux.UseVisualStyleBackColor = true;
            this.btnMeasureAux.Click += new System.EventHandler(this.btnMeasureAux_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.tbBiPotPotential);
            this.groupBox2.Controls.Add(this.btnMeasureBiPot);
            this.groupBox2.Controls.Add(this.cmbBiPotMode);
            this.groupBox2.Location = new System.Drawing.Point(10, 19);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(168, 73);
            this.groupBox2.TabIndex = 9;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Bipot Measurement";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(147, 22);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(14, 13);
            this.label2.TabIndex = 9;
            this.label2.Text = "V";
            // 
            // tbBiPotPotential
            // 
            this.tbBiPotPotential.Location = new System.Drawing.Point(84, 19);
            this.tbBiPotPotential.Name = "tbBiPotPotential";
            this.tbBiPotPotential.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.tbBiPotPotential.Size = new System.Drawing.Size(60, 20);
            this.tbBiPotPotential.TabIndex = 8;
            this.tbBiPotPotential.Text = "0";
            this.tbBiPotPotential.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // cmbBiPotMode
            // 
            this.cmbBiPotMode.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbBiPotMode.FormattingEnabled = true;
            this.cmbBiPotMode.Items.AddRange(new object[] {
            "Constant",
            "Offset"});
            this.cmbBiPotMode.Location = new System.Drawing.Point(6, 19);
            this.cmbBiPotMode.Name = "cmbBiPotMode";
            this.cmbBiPotMode.Size = new System.Drawing.Size(72, 21);
            this.cmbBiPotMode.TabIndex = 7;
            // 
            // dgvMeasurement
            // 
            this.dgvMeasurement.AllowUserToAddRows = false;
            this.dgvMeasurement.AllowUserToDeleteRows = false;
            this.dgvMeasurement.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.dgvMeasurement.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvMeasurement.EditMode = System.Windows.Forms.DataGridViewEditMode.EditProgrammatically;
            this.dgvMeasurement.Location = new System.Drawing.Point(7, 98);
            this.dgvMeasurement.Name = "dgvMeasurement";
            this.dgvMeasurement.ReadOnly = true;
            this.dgvMeasurement.RowHeadersVisible = false;
            this.dgvMeasurement.Size = new System.Drawing.Size(361, 178);
            this.dgvMeasurement.TabIndex = 4;
            // 
            // grpConsole
            // 
            this.grpConsole.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
            this.grpConsole.Controls.Add(this.lbConsole);
            this.grpConsole.Location = new System.Drawing.Point(12, 96);
            this.grpConsole.Name = "grpConsole";
            this.grpConsole.Size = new System.Drawing.Size(172, 303);
            this.grpConsole.TabIndex = 7;
            this.grpConsole.TabStop = false;
            this.grpConsole.Text = "Console";
            // 
            // lbConsole
            // 
            this.lbConsole.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
            this.lbConsole.FormattingEnabled = true;
            this.lbConsole.Location = new System.Drawing.Point(7, 19);
            this.lbConsole.Name = "lbConsole";
            this.lbConsole.Size = new System.Drawing.Size(154, 277);
            this.lbConsole.TabIndex = 0;
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
            // lblExtaValueUnit
            // 
            this.lblExtaValueUnit.AutoSize = true;
            this.lblExtaValueUnit.Location = new System.Drawing.Point(153, 74);
            this.lblExtaValueUnit.Name = "lblExtaValueUnit";
            this.lblExtaValueUnit.Size = new System.Drawing.Size(44, 13);
            this.lblExtaValueUnit.TabIndex = 11;
            this.lblExtaValueUnit.Text = "* 10 mA";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(576, 411);
            this.Controls.Add(this.grpConsole);
            this.Controls.Add(this.grpMeasurement);
            this.Controls.Add(this.grpDevice);
            this.Controls.Add(this.grpConnection);
            this.Name = "Form1";
            this.Text = "Form1";
            this.grpConnection.ResumeLayout(false);
            this.grpDevice.ResumeLayout(false);
            this.grpDevice.PerformLayout();
            this.grpMeasurement.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvMeasurement)).EndInit();
            this.grpConsole.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private PalmSens.Core.Simplified.WinForms.PSCommSimpleWinForms psCommSimpleWinForms;
        private System.Windows.Forms.Button btnMeasureBiPot;
        private System.Windows.Forms.Button btnConnect;
        private System.Windows.Forms.Button btnRefresh;
        private System.Windows.Forms.ComboBox cmbDevices;
        private System.Windows.Forms.GroupBox grpConnection;
        private System.Windows.Forms.GroupBox grpDevice;
        private System.Windows.Forms.GroupBox grpMeasurement;
        private System.Windows.Forms.DataGridView dgvMeasurement;
        private System.Windows.Forms.GroupBox grpConsole;
        private System.Windows.Forms.ListBox lbConsole;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tbDeviceStatus;
        private System.Windows.Forms.Label lblCurrentRange;
        private System.Windows.Forms.Label lblCurrent;
        private System.Windows.Forms.TextBox tbCurrent;
        private System.Windows.Forms.Label lblVolt;
        private System.Windows.Forms.TextBox tbPotential;
        private System.Windows.Forms.Label lblPotential;
        private System.Windows.Forms.ComboBox cmbBiPotMode;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox tbBiPotPotential;
        private System.Windows.Forms.Button btnMeasureAux;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tbExtraValue;
        private System.Windows.Forms.ComboBox cmbStatusExtraValue;
        private System.Windows.Forms.Label lblExtaValueUnit;
    }
}

