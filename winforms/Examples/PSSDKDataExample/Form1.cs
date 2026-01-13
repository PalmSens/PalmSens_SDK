using System;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;
using PalmSens.Core.Simplified.Data;
using System.Collections.Generic;
using PalmSens.Core.Simplified.WinForms;

namespace PSSDKDataExample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            InitPlot(); //Resets and initiates the plot control
        }

        /// <summary>
        /// Initializes the plot control.
        /// </summary>
        private void InitPlot()
        {
            plot.ClearAll(); //Clear all curves and data from plot
            //Set the Axis labels
            plot.XAxisLabel = "V";
            plot.YAxisLabel = "µA";
            plot.MarkerSize = 3;
            plot.AddData("", new double[0], new double[0]); //Add a empty data array to draw an empty plot
        }

        /// <summary>
        /// The next data operation to perform (always start with loading the data)
        /// </summary>
        private Steps _nextStep = Steps.LoadData;

        private enum Steps
        {
            LoadData = 1,
            Smooth = 2,
            MovingAverageBaseline = 3,
            SubtractBaseline = 4,
            DetectPeaks = 5,
            NewChargeCurve = 6,
            DifferntiateCurve = 7,
            DisplayBodePlot = 8
        }

        /// <summary>
        /// List that will hold references to the measurements in the Example PSSession file
        /// </summary>
        private List<SimpleMeasurement> _measurements;

        /// <summary>
        /// The active SimpleMeasurement
        /// </summary>
        private SimpleMeasurement _activeMeasurement;

        /// <summary>
        /// The active SimpleCurve
        /// </summary>
        private SimpleCurve _activeCurve;

        /// <summary>
        /// The baseline SimpleCurve
        /// </summary>
        private SimpleCurve _baselineCurve;

        /// <summary>
        /// Handles the Click event of the btnPerformOperation control.
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private void btnPerformOperation_Click(object sender, EventArgs e)
        {
            PerformOperation();
        }

        /// <summary>
        /// Performs the pending operation.
        /// </summary>
        private void PerformOperation()
        {
            if (_nextStep == Steps.LoadData)
            {
                //Load measurements from the Example PSSession File
                _measurements = SimpleLoadSaveFunctions.LoadMeasurements("Example.pssession");
                if (_measurements.Count == 4)
                {
                    lbConsole.Items.Add("Example.pssession succesfully loaded.");
                }
                else
                {
                    lbConsole.Items.Add("Example file empty...");
                    lbConsole.Items.Add("Please make sure the Example.pssession file is present in the project folder.");
                    return;
                }

                //Get the measurement named DPV Example
                //Also possible without LINQ: SimpleMeasurement dpvExample = _measurements[2]
                SimpleMeasurement dpvExample = _measurements.Where(meas => meas.Title == "DPV Example").FirstOrDefault();
                _activeMeasurement = dpvExample;

                //Plot the first and only curve in the dpvExample measurement
                _activeCurve = dpvExample.SimpleCurveCollection[0];
                plot.AddSimpleCurve(_activeCurve);

                lblStep1.Text += " DONE";
                lblStep1.ForeColor = SystemColors.ControlDark;
                lblStep2.ForeColor = SystemColors.ControlText;
                IncrementStep(); //Increment the _nextStep property
            }
            else if (_nextStep == Steps.Smooth)
            {
                //Smooth the active SimpleCurve defined in the previous step
                //Smoothes the data on the Y-axis with the Savitzky-Golay filter.
                SimpleCurve smoothedCurve = _activeCurve.Smooth(SmoothLevel.High);

                lbConsole.Items.Add("Curve Smoothed.");

                //Add the smoothed curve to the plot
                plot.AddSimpleCurve(smoothedCurve);

                lblStep2.Text += " DONE";
                lblStep2.ForeColor = SystemColors.ControlDark;
                lblStep3.ForeColor = SystemColors.ControlText;
                IncrementStep(); //Increment the _nextStep property
            }
            else if (_nextStep == Steps.MovingAverageBaseline)
            {
                plot.ClearAll(); //Clear the plot

                //Get the measurement named SWV Example
                //Also possible without LINQ: SimpleMeasurement dpvExample = _measurements[3]
                SimpleMeasurement swvExample = _measurements.Where(meas => meas.Title == "SWV Example").FirstOrDefault();
                _activeMeasurement = swvExample;

                //Get the first and only curve in the SWV Example measurement
                _activeCurve = swvExample.SimpleCurveCollection[0];
                plot.AddSimpleCurve(_activeCurve);

                //Determine and plot the moving average baseline curve
                _baselineCurve = _activeCurve.MovingAverageBaseline();
                plot.AddSimpleCurve(_baselineCurve);

                lbConsole.Items.Add("SWV Example Curve Moving Average Baseline Determined.");

                lblStep3.Text += " DONE";
                lblStep3.ForeColor = SystemColors.ControlDark;
                lblStep4.ForeColor = SystemColors.ControlText;
                IncrementStep(); //Increment the _nextStep property
            }
            else if (_nextStep == Steps.SubtractBaseline)
            {
                //Subtract the baseline from the measurement and plot the result
                _activeCurve = _activeCurve.Subtract(_baselineCurve); //Replace the activeCurve reference with the result
                plot.AddSimpleCurve(_activeCurve);

                lbConsole.Items.Add("Baseline Curve Subtracted From SWV Example Curve.");

                lblStep4.Text += " DONE";
                lblStep4.ForeColor = SystemColors.ControlDark;
                lblStep5.ForeColor = SystemColors.ControlText;
                IncrementStep(); //Increment the _nextStep property
            }
            else if (_nextStep == Steps.DetectPeaks)
            {
                plot.ClearAll(); //Clear the plot

                //Add the last step's result to the plot and detect its peaks
                plot.AddSimpleCurve(_activeCurve);
                _activeCurve.DetectPeaks();

                lbConsole.Items.Add("Peaks Detected in the Baseline Corrected Curve.");

                lblStep5.Text += " DONE";
                lblStep5.ForeColor = SystemColors.ControlDark;
                lblStep6.ForeColor = SystemColors.ControlText;
                IncrementStep(); //Increment the _nextStep property
            }
            else if (_nextStep == Steps.NewChargeCurve)
            {
                plot.ClearAll(); //Clear the plot

                //Get the measurement named CV Example
                //Also possible without LINQ: SimpleMeasurement dpvExample = _measurements[0]
                SimpleMeasurement cvExample = _measurements.Where(meas => meas.Title == "CV Example").FirstOrDefault();
                _activeMeasurement = cvExample;

                //Get Charge over Time curves from the measurement and plot them
                List<SimpleCurve> chargeCurves = cvExample.NewSimpleCurve(PalmSens.Data.DataArrayType.Time, PalmSens.Data.DataArrayType.Charge, "Charge/Potential");
                plot.AddSimpleCurves(chargeCurves);
                _activeCurve = chargeCurves[0];

                lbConsole.Items.Add("Obtained Charge over Time curve for each");
                lbConsole.Items.Add("scan in the CV Example.");

                lblStep6.Text += " DONE";
                lblStep6.ForeColor = SystemColors.ControlDark;
                lblStep7.ForeColor = SystemColors.ControlText;
                IncrementStep(); //Increment the _nextStep property
            }
            else if (_nextStep == Steps.DifferntiateCurve)
            {
                plot.ClearAll(); //Clear the plot

                //Plot the first charge over time scan from the previous step
                plot.AddSimpleCurve(_activeCurve);

                //Differentiate and plot the result on the secondary y-axis
                SimpleCurve diffCharge = _activeCurve.Differentiate();
                plot.AddSimpleCurve(diffCharge, true); //Plot on the secondary y-axis
                plot.YAxisSecondaryLabel = "dC(µC)/dt(s)"; //Set the unit for the secondary Y-Axis

                lbConsole.Items.Add("Differentiated the curve");

                lblStep7.Text += " DONE";
                lblStep7.ForeColor = SystemColors.ControlDark;
                lblStep8.ForeColor = SystemColors.ControlText;
                IncrementStep(); //Increment the _nextStep property
            }
            else if (_nextStep == Steps.DisplayBodePlot)
            {
                plot.ClearAll(); //Clear the plot

                //Get the measurement named EIS Example
                //Also possible without LINQ: SimpleMeasurement dpvExample = _measurements[3]
                SimpleMeasurement eisExample = _measurements.Where(meas => meas.Title == "EIS Example").FirstOrDefault();
                _activeMeasurement = eisExample;

                //Get the curves for the bode plot from the measurement
                SimpleCurve impedance = (eisExample.NewSimpleCurve(PalmSens.Data.DataArrayType.Frequency, PalmSens.Data.DataArrayType.Z, "Impedance"))[0];
                SimpleCurve phase = (eisExample.NewSimpleCurve(PalmSens.Data.DataArrayType.Frequency, PalmSens.Data.DataArrayType.Phase, "-Phase"))[0];

                //Plot the curves on the primary and secondary y-axes and set the x-axis to logarithmic display mode
                plot.AddSimpleCurve(impedance);
                plot.AddSimpleCurve(phase, true); //Plot on the secondary y-axis
                //Set the axis to logarithmic display mode
                plot.XAxisType = SDKPlot.AxisType.Logarithmic;
                plot.YAxisType = SDKPlot.AxisType.Logarithmic;

                lblStep8.Text += " DONE";
                lblStep8.ForeColor = SystemColors.ControlDark;
                lbConsole.Items.Add("Completed Example.");
                btnPerformOperation.Enabled = false;
            }
        }

        /// <summary>
        /// Increments the next step property.
        /// </summary>
        private void IncrementStep()
        {
            int nextStepIndex = (int)_nextStep + 1;
            _nextStep = (Steps)nextStepIndex;
        }
    }
}