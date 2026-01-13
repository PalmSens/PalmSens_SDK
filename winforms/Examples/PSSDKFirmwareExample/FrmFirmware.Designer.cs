
namespace PSSDKFirmwareExample
{
    partial class FrmFirmware
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
            this.grpConsole = new System.Windows.Forms.GroupBox();
            this.lbConsole = new System.Windows.Forms.ListBox();
            this.grpDevice = new System.Windows.Forms.GroupBox();
            this.txtFirmware = new System.Windows.Forms.TextBox();
            this.grpConnection = new System.Windows.Forms.GroupBox();
            this.cmbDevices = new System.Windows.Forms.ComboBox();
            this.btnRefresh = new System.Windows.Forms.Button();
            this.grpBoxFirmwareNew = new System.Windows.Forms.GroupBox();
            this.btnUpload = new System.Windows.Forms.Button();
            this.btnLoadFile = new System.Windows.Forms.Button();
            this.txtFileLocation = new System.Windows.Forms.TextBox();
            this.pgsBarUpload = new System.Windows.Forms.ProgressBar();
            this.grpProgress = new System.Windows.Forms.GroupBox();
            this.lblCurrentStatus = new System.Windows.Forms.Label();
            this.psCommSimpleWinForms = new PalmSens.Core.Simplified.WinForms.PSCommSimpleWinForms(this.components);
            this.grpConsole.SuspendLayout();
            this.grpDevice.SuspendLayout();
            this.grpConnection.SuspendLayout();
            this.grpBoxFirmwareNew.SuspendLayout();
            this.grpProgress.SuspendLayout();
            this.SuspendLayout();
            // 
            // grpConsole
            // 
            this.grpConsole.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpConsole.Controls.Add(this.lbConsole);
            this.grpConsole.Location = new System.Drawing.Point(12, 254);
            this.grpConsole.Name = "grpConsole";
            this.grpConsole.Size = new System.Drawing.Size(560, 151);
            this.grpConsole.TabIndex = 10;
            this.grpConsole.TabStop = false;
            this.grpConsole.Text = "Console";
            // 
            // lbConsole
            // 
            this.lbConsole.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lbConsole.FormattingEnabled = true;
            this.lbConsole.Location = new System.Drawing.Point(3, 16);
            this.lbConsole.Name = "lbConsole";
            this.lbConsole.Size = new System.Drawing.Size(554, 132);
            this.lbConsole.TabIndex = 0;
            // 
            // grpDevice
            // 
            this.grpDevice.Controls.Add(this.txtFirmware);
            this.grpDevice.Location = new System.Drawing.Point(281, 12);
            this.grpDevice.Name = "grpDevice";
            this.grpDevice.Size = new System.Drawing.Size(291, 164);
            this.grpDevice.TabIndex = 9;
            this.grpDevice.TabStop = false;
            this.grpDevice.Text = "Firmware Information";
            // 
            // txtFirmware
            // 
            this.txtFirmware.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtFirmware.Location = new System.Drawing.Point(3, 16);
            this.txtFirmware.Multiline = true;
            this.txtFirmware.Name = "txtFirmware";
            this.txtFirmware.ReadOnly = true;
            this.txtFirmware.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtFirmware.Size = new System.Drawing.Size(285, 145);
            this.txtFirmware.TabIndex = 0;
            // 
            // grpConnection
            // 
            this.grpConnection.Controls.Add(this.cmbDevices);
            this.grpConnection.Controls.Add(this.btnRefresh);
            this.grpConnection.Location = new System.Drawing.Point(12, 12);
            this.grpConnection.Name = "grpConnection";
            this.grpConnection.Size = new System.Drawing.Size(263, 79);
            this.grpConnection.TabIndex = 8;
            this.grpConnection.TabStop = false;
            this.grpConnection.Text = "Connection";
            // 
            // cmbDevices
            // 
            this.cmbDevices.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.cmbDevices.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbDevices.FormattingEnabled = true;
            this.cmbDevices.Location = new System.Drawing.Point(6, 19);
            this.cmbDevices.Name = "cmbDevices";
            this.cmbDevices.Size = new System.Drawing.Size(247, 21);
            this.cmbDevices.TabIndex = 0;
            this.cmbDevices.SelectedIndexChanged += new System.EventHandler(this.cmbDevices_SelectedIndexChanged);
            // 
            // btnRefresh
            // 
            this.btnRefresh.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnRefresh.Location = new System.Drawing.Point(178, 46);
            this.btnRefresh.Name = "btnRefresh";
            this.btnRefresh.Size = new System.Drawing.Size(75, 23);
            this.btnRefresh.TabIndex = 1;
            this.btnRefresh.Text = "Refresh";
            this.btnRefresh.UseVisualStyleBackColor = true;
            this.btnRefresh.Click += new System.EventHandler(this.btnRefresh_Click);
            // 
            // grpBoxFirmwareNew
            // 
            this.grpBoxFirmwareNew.Controls.Add(this.btnUpload);
            this.grpBoxFirmwareNew.Controls.Add(this.btnLoadFile);
            this.grpBoxFirmwareNew.Controls.Add(this.txtFileLocation);
            this.grpBoxFirmwareNew.Location = new System.Drawing.Point(12, 97);
            this.grpBoxFirmwareNew.Name = "grpBoxFirmwareNew";
            this.grpBoxFirmwareNew.Size = new System.Drawing.Size(263, 79);
            this.grpBoxFirmwareNew.TabIndex = 11;
            this.grpBoxFirmwareNew.TabStop = false;
            this.grpBoxFirmwareNew.Text = "Firmware";
            // 
            // btnUpload
            // 
            this.btnUpload.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnUpload.Location = new System.Drawing.Point(206, 49);
            this.btnUpload.Name = "btnUpload";
            this.btnUpload.Size = new System.Drawing.Size(51, 23);
            this.btnUpload.TabIndex = 2;
            this.btnUpload.Text = "Upload";
            this.btnUpload.UseVisualStyleBackColor = true;
            this.btnUpload.Click += new System.EventHandler(this.btnUpload_Click);
            // 
            // btnLoadFile
            // 
            this.btnLoadFile.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnLoadFile.Location = new System.Drawing.Point(206, 16);
            this.btnLoadFile.Name = "btnLoadFile";
            this.btnLoadFile.Size = new System.Drawing.Size(51, 23);
            this.btnLoadFile.TabIndex = 1;
            this.btnLoadFile.Text = "Open";
            this.btnLoadFile.UseVisualStyleBackColor = true;
            this.btnLoadFile.Click += new System.EventHandler(this.btnLoadFile_Click);
            // 
            // txtFileLocation
            // 
            this.txtFileLocation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtFileLocation.Location = new System.Drawing.Point(6, 18);
            this.txtFileLocation.Name = "txtFileLocation";
            this.txtFileLocation.ReadOnly = true;
            this.txtFileLocation.Size = new System.Drawing.Size(194, 20);
            this.txtFileLocation.TabIndex = 0;
            // 
            // pgsBarUpload
            // 
            this.pgsBarUpload.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pgsBarUpload.Location = new System.Drawing.Point(6, 19);
            this.pgsBarUpload.Name = "pgsBarUpload";
            this.pgsBarUpload.Size = new System.Drawing.Size(548, 23);
            this.pgsBarUpload.TabIndex = 12;
            // 
            // grpProgress
            // 
            this.grpProgress.Controls.Add(this.lblCurrentStatus);
            this.grpProgress.Controls.Add(this.pgsBarUpload);
            this.grpProgress.Location = new System.Drawing.Point(12, 182);
            this.grpProgress.Name = "grpProgress";
            this.grpProgress.Size = new System.Drawing.Size(560, 66);
            this.grpProgress.TabIndex = 13;
            this.grpProgress.TabStop = false;
            this.grpProgress.Text = "Progress";
            // 
            // lblCurrentStatus
            // 
            this.lblCurrentStatus.AutoSize = true;
            this.lblCurrentStatus.Location = new System.Drawing.Point(6, 45);
            this.lblCurrentStatus.Name = "lblCurrentStatus";
            this.lblCurrentStatus.Size = new System.Drawing.Size(69, 13);
            this.lblCurrentStatus.TabIndex = 14;
            this.lblCurrentStatus.Text = "Current State";
            this.lblCurrentStatus.TextAlign = System.Drawing.ContentAlignment.TopRight;
            // 
            // psCommSimpleWinForms
            // 
            this.psCommSimpleWinForms.EnableBluetooth = false;
            this.psCommSimpleWinForms.EnableSerialPort = false;
            this.psCommSimpleWinForms.Parent = this;
            this.psCommSimpleWinForms.Disconnected += new PalmSens.Core.Simplified.DisconnectedEventHandler(this.psCommSimpleWinForms_Disconnected);
            // 
            // FrmFirmware
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(584, 409);
            this.Controls.Add(this.grpProgress);
            this.Controls.Add(this.grpBoxFirmwareNew);
            this.Controls.Add(this.grpConsole);
            this.Controls.Add(this.grpDevice);
            this.Controls.Add(this.grpConnection);
            this.Name = "FrmFirmware";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.FrmFirmware_Load);
            this.grpConsole.ResumeLayout(false);
            this.grpDevice.ResumeLayout(false);
            this.grpDevice.PerformLayout();
            this.grpConnection.ResumeLayout(false);
            this.grpBoxFirmwareNew.ResumeLayout(false);
            this.grpBoxFirmwareNew.PerformLayout();
            this.grpProgress.ResumeLayout(false);
            this.grpProgress.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox grpConsole;
        private System.Windows.Forms.ListBox lbConsole;
        private System.Windows.Forms.GroupBox grpDevice;
        private System.Windows.Forms.GroupBox grpConnection;
        private System.Windows.Forms.ComboBox cmbDevices;
        private System.Windows.Forms.Button btnRefresh;
        private PalmSens.Core.Simplified.WinForms.PSCommSimpleWinForms psCommSimpleWinForms;
        private System.Windows.Forms.GroupBox grpBoxFirmwareNew;
        private System.Windows.Forms.Button btnLoadFile;
        private System.Windows.Forms.TextBox txtFileLocation;
        private System.Windows.Forms.TextBox txtFirmware;
        private System.Windows.Forms.Button btnUpload;
        private System.Windows.Forms.GroupBox grpProgress;
        private System.Windows.Forms.ProgressBar pgsBarUpload;
        private System.Windows.Forms.Label lblCurrentStatus;
    }
}

