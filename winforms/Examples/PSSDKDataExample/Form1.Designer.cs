namespace PSSDKDataExample
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
            this.grpMeasurement = new System.Windows.Forms.GroupBox();
            this.grpDataOperations = new System.Windows.Forms.GroupBox();
            this.lblStep8 = new System.Windows.Forms.Label();
            this.lblStep7 = new System.Windows.Forms.Label();
            this.lblStep6 = new System.Windows.Forms.Label();
            this.lblStep5 = new System.Windows.Forms.Label();
            this.lblStep4 = new System.Windows.Forms.Label();
            this.lblStep3 = new System.Windows.Forms.Label();
            this.lblStep2 = new System.Windows.Forms.Label();
            this.lblStep1 = new System.Windows.Forms.Label();
            this.btnPerformOperation = new System.Windows.Forms.Button();
            this.plot = new SDKPlot.WinForms.Plot();
            this.grpConsole = new System.Windows.Forms.GroupBox();
            this.lbConsole = new System.Windows.Forms.ListBox();
            this.grpMeasurement.SuspendLayout();
            this.grpDataOperations.SuspendLayout();
            this.grpConsole.SuspendLayout();
            this.SuspendLayout();
            // 
            // grpMeasurement
            // 
            this.grpMeasurement.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpMeasurement.Controls.Add(this.grpDataOperations);
            this.grpMeasurement.Controls.Add(this.plot);
            this.grpMeasurement.Location = new System.Drawing.Point(12, 12);
            this.grpMeasurement.Name = "grpMeasurement";
            this.grpMeasurement.Size = new System.Drawing.Size(757, 551);
            this.grpMeasurement.TabIndex = 6;
            this.grpMeasurement.TabStop = false;
            this.grpMeasurement.Text = "Plot";
            // 
            // grpDataOperations
            // 
            this.grpDataOperations.Controls.Add(this.lblStep8);
            this.grpDataOperations.Controls.Add(this.lblStep7);
            this.grpDataOperations.Controls.Add(this.lblStep6);
            this.grpDataOperations.Controls.Add(this.lblStep5);
            this.grpDataOperations.Controls.Add(this.lblStep4);
            this.grpDataOperations.Controls.Add(this.lblStep3);
            this.grpDataOperations.Controls.Add(this.lblStep2);
            this.grpDataOperations.Controls.Add(this.lblStep1);
            this.grpDataOperations.Controls.Add(this.btnPerformOperation);
            this.grpDataOperations.ForeColor = System.Drawing.SystemColors.ControlText;
            this.grpDataOperations.Location = new System.Drawing.Point(7, 20);
            this.grpDataOperations.Name = "grpDataOperations";
            this.grpDataOperations.Size = new System.Drawing.Size(744, 126);
            this.grpDataOperations.TabIndex = 6;
            this.grpDataOperations.TabStop = false;
            this.grpDataOperations.Text = "Data Operations";
            // 
            // lblStep8
            // 
            this.lblStep8.AutoSize = true;
            this.lblStep8.ForeColor = System.Drawing.SystemColors.ControlDark;
            this.lblStep8.Location = new System.Drawing.Point(6, 107);
            this.lblStep8.Name = "lblStep8";
            this.lblStep8.Size = new System.Drawing.Size(210, 13);
            this.lblStep8.TabIndex = 14;
            this.lblStep8.Text = "8. Display Bode Plot of EIS Measurement...";
            // 
            // lblStep7
            // 
            this.lblStep7.AutoSize = true;
            this.lblStep7.ForeColor = System.Drawing.SystemColors.ControlDark;
            this.lblStep7.Location = new System.Drawing.Point(6, 94);
            this.lblStep7.Name = "lblStep7";
            this.lblStep7.Size = new System.Drawing.Size(116, 13);
            this.lblStep7.TabIndex = 13;
            this.lblStep7.Text = "7. Differentiate Curve...";
            // 
            // lblStep6
            // 
            this.lblStep6.AutoSize = true;
            this.lblStep6.ForeColor = System.Drawing.SystemColors.ControlDark;
            this.lblStep6.Location = new System.Drawing.Point(6, 81);
            this.lblStep6.Name = "lblStep6";
            this.lblStep6.Size = new System.Drawing.Size(168, 13);
            this.lblStep6.TabIndex = 12;
            this.lblStep6.Text = "6. New Charge over Time Curve...";
            // 
            // lblStep5
            // 
            this.lblStep5.AutoSize = true;
            this.lblStep5.ForeColor = System.Drawing.SystemColors.ControlDark;
            this.lblStep5.Location = new System.Drawing.Point(6, 68);
            this.lblStep5.Name = "lblStep5";
            this.lblStep5.Size = new System.Drawing.Size(93, 13);
            this.lblStep5.TabIndex = 11;
            this.lblStep5.Text = "5. Detect Peaks...";
            // 
            // lblStep4
            // 
            this.lblStep4.AutoSize = true;
            this.lblStep4.ForeColor = System.Drawing.SystemColors.ControlDark;
            this.lblStep4.Location = new System.Drawing.Point(6, 55);
            this.lblStep4.Name = "lblStep4";
            this.lblStep4.Size = new System.Drawing.Size(111, 13);
            this.lblStep4.TabIndex = 10;
            this.lblStep4.Text = "4. Subtract Baseline...";
            // 
            // lblStep3
            // 
            this.lblStep3.AutoSize = true;
            this.lblStep3.ForeColor = System.Drawing.SystemColors.ControlDark;
            this.lblStep3.Location = new System.Drawing.Point(6, 42);
            this.lblStep3.Name = "lblStep3";
            this.lblStep3.Size = new System.Drawing.Size(200, 13);
            this.lblStep3.TabIndex = 9;
            this.lblStep3.Text = "3. Determine Moving Average Baseline...";
            // 
            // lblStep2
            // 
            this.lblStep2.AutoSize = true;
            this.lblStep2.ForeColor = System.Drawing.SystemColors.ControlDark;
            this.lblStep2.Location = new System.Drawing.Point(6, 29);
            this.lblStep2.Name = "lblStep2";
            this.lblStep2.Size = new System.Drawing.Size(95, 13);
            this.lblStep2.TabIndex = 8;
            this.lblStep2.Text = "2. Smooth Curve...";
            // 
            // lblStep1
            // 
            this.lblStep1.AutoSize = true;
            this.lblStep1.Location = new System.Drawing.Point(6, 16);
            this.lblStep1.Name = "lblStep1";
            this.lblStep1.Size = new System.Drawing.Size(125, 13);
            this.lblStep1.TabIndex = 7;
            this.lblStep1.Text = "1. Load PSSession File...";
            // 
            // btnPerformOperation
            // 
            this.btnPerformOperation.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnPerformOperation.Location = new System.Drawing.Point(631, 97);
            this.btnPerformOperation.Name = "btnPerformOperation";
            this.btnPerformOperation.Size = new System.Drawing.Size(107, 23);
            this.btnPerformOperation.TabIndex = 6;
            this.btnPerformOperation.Text = "Perform Operation";
            this.btnPerformOperation.UseVisualStyleBackColor = true;
            this.btnPerformOperation.Click += new System.EventHandler(this.btnPerformOperation_Click);
            // 
            // plot
            // 
            this.plot.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.plot.BackColor = System.Drawing.Color.White;
            this.plot.Location = new System.Drawing.Point(7, 152);
            this.plot.MarkerSize = 5;
            this.plot.MarkerType = OxyPlot.MarkerType.Circle;
            this.plot.Name = "plot";
            this.plot.Size = new System.Drawing.Size(744, 392);
            this.plot.TabIndex = 4;
            this.plot.Title = null;
            this.plot.XAxisLabel = null;
            this.plot.XAxisType = SDKPlot.AxisType.Linear;
            this.plot.YAxisLabel = null;
            this.plot.YAxisSecondaryLabel = null;
            this.plot.YAxisSecondaryType = SDKPlot.AxisType.Linear;
            this.plot.YAxisType = SDKPlot.AxisType.Linear;
            // 
            // grpConsole
            // 
            this.grpConsole.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.grpConsole.Controls.Add(this.lbConsole);
            this.grpConsole.Location = new System.Drawing.Point(775, 12);
            this.grpConsole.Name = "grpConsole";
            this.grpConsole.Size = new System.Drawing.Size(311, 551);
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
            this.lbConsole.Size = new System.Drawing.Size(297, 524);
            this.lbConsole.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1091, 575);
            this.Controls.Add(this.grpConsole);
            this.Controls.Add(this.grpMeasurement);
            this.Name = "Form1";
            this.Text = "Form1";
            this.grpMeasurement.ResumeLayout(false);
            this.grpDataOperations.ResumeLayout(false);
            this.grpDataOperations.PerformLayout();
            this.grpConsole.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.GroupBox grpMeasurement;
        private System.Windows.Forms.GroupBox grpConsole;
        private System.Windows.Forms.ListBox lbConsole;
        private SDKPlot.WinForms.Plot plot;
        private System.Windows.Forms.GroupBox grpDataOperations;
        private System.Windows.Forms.Button btnPerformOperation;
        private System.Windows.Forms.Label lblStep8;
        private System.Windows.Forms.Label lblStep7;
        private System.Windows.Forms.Label lblStep6;
        private System.Windows.Forms.Label lblStep5;
        private System.Windows.Forms.Label lblStep4;
        private System.Windows.Forms.Label lblStep3;
        private System.Windows.Forms.Label lblStep2;
        private System.Windows.Forms.Label lblStep1;
    }
}

