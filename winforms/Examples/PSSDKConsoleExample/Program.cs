using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using PalmSens;
using PalmSens.Comm;
using PalmSens.Devices;
using PalmSens.Plottables;
using PalmSens.Techniques;
using PalmSens.Windows;
using PalmSens.Windows.Devices;

namespace PSSDKConsoleExample
{
    class Program
    {
        static void Main(string[] args)
        {
            //Initiate the SDKs core dependencies
            CoreDependencies.Init();

            Console.WriteLine("");
            Console.WriteLine("Discovering connected devices...");
            Console.WriteLine("");

            //Discover connected devices
            Device[] connectedDevices = null;
            while (connectedDevices == null || connectedDevices.Length == 0)
                connectedDevices = DiscoverConnectedDevices();

            Console.WriteLine("");
            Console.WriteLine($"Found {connectedDevices.Length} connected devices.");
            Console.WriteLine("");

            //List connected devices
            for (int i = 0; i < connectedDevices.Length; i++)
                Console.WriteLine($"{i + 1}. {connectedDevices[i].ToString()}");
            Console.WriteLine("");

            int deviceIndex = 0;
            if (connectedDevices.Length > 1)
            {
                //Prompt user which device to connect to
                string msg = $"Specify which device to connect to (a number between 1 and {connectedDevices.Length}):";
                while (true)
                {
                    Console.WriteLine(msg);
                    string input = Console.ReadLine();
                    int index;
                    if (int.TryParse(input, out index) && index > 0 && index <= connectedDevices.Length)
                    {
                        deviceIndex = index - 1;
                        break;
                    }
                }
            }

            Device connectedDevice = connectedDevices[deviceIndex];
            Console.WriteLine("");
            Console.WriteLine($"Connecting to {connectedDevice.ToString()}.");
            Console.WriteLine("");

            //Connect to device
            Connect(connectedDevice);

            //Get potential (threadsafe example of getting a single reading from the commmanager)
            float potential = CommInvokeThreadSafe(() => { return _comm.Potential; });
            Console.WriteLine($"Potential {potential.ToString("e2")}");

            //Subscribe to events
            _comm.BeginMeasurement += _comm_BeginMeasurement;
            _comm.BeginReceiveCurve += _comm_BeginReceiveCurve;
            _comm.EndMeasurement += _comm_EndMeasurement;

            //Define a chronoamperometry method
            AmperometricDetection method = new AmperometricDetection();
            method.Potential = 1f; //Sets a potential of 1 volt
            method.RunTime = 5f; //For a duration of 5 seconds
            method.IntervalTime = 0.1f; //Measures the current 10 times per second

            method.EquilibrationTime = 1f; //Equilabrates the cell at the defined potential for 1 second before starting the measurement
            method.Ranging.StartCurrentRange = new CurrentRange(CurrentRanges.cr1uA); //Starts equilabration in the 1µA current range
            method.Ranging.MinimumCurrentRange = new CurrentRange(CurrentRanges.cr10nA); //Min current range 10nA
            method.Ranging.MaximumCurrentRange = new CurrentRange(CurrentRanges.cr1mA); //Max current range 1mA

            //Start the measurement
            string errors = CommInvokeThreadSafe(() => { return _comm.Measure(method); });

            if (!string.IsNullOrEmpty(errors))
            {
                Console.WriteLine($"Measurement failed: {errors}");
                //Unsubscribe from the CommManager's events to avoid memory leaks
                _comm.BeginMeasurement -= _comm_BeginMeasurement;
                _comm.BeginReceiveCurve -= _comm_BeginReceiveCurve;
                _comm.EndMeasurement -= _comm_EndMeasurement;
                _comm.Dispose();
            }

            //Prevent program from terminating immediately after starting the measurement
            Console.ReadKey();
        }

        /// <summary>
        /// Thread safe invoker for CommManager.
        /// </summary>
        /// <typeparam name="T">The specified value type the delegate returns</typeparam>
        /// <param name="del">The delegate function (has to return a value).</param>
        /// <returns>The value</returns>
        private static T CommInvokeThreadSafe<T>(Func<T> del)
        {
            Task<T> t = _comm.ClientConnection.Run<T>(new Task<T>(del));
            t.Wait();
            return t.Result;
        }

        /// <summary>
        /// Thread safe invoker for CommManager.
        /// </summary>
        /// <param name="action">The action.</param>
        private static void CommInvokeThreadSafe(Action action)
        {
            _comm.ClientConnection.Run(action).Wait();
        }

        /// <summary>
        /// The connected devices CommManager
        /// </summary>
        public static CommManager _comm;

        /// <summary>
        /// The active curve containing the measurements results
        /// </summary>
        public static Curve _curve;

        /// <summary>
        /// Discovers the Emstat and PalmSens devices connected via USB.
        /// </summary>
        /// <returns>An array of the connected devices</returns>
        public static Device[] DiscoverConnectedDevices()
        {
            //Determine which devices to discover
            List<DeviceList.DiscoverDevicesFunc> discFuncs = new List<DeviceList.DiscoverDevicesFunc>(); //List of device discovery delegates
            discFuncs.Add(USBCDCDevice.DiscoverDevices); //Adds the delegate for discovering connected PalmSens 4 devices
            discFuncs.Add(FTDIDevice.DiscoverDevices); //Adds the delegate for discovering connected Emstat & PalmSens 3 devices

            //Discover the specified devices
            string errors;
            Device[] devices = new DeviceList(discFuncs).GetAvailableDevices(out errors);

            //Check whether errors occurred during discovery
            if (!string.IsNullOrEmpty(errors))
            {
                Console.WriteLine(errors);
                return null;
            }

            return devices;
        }

        /// <summary>
        /// Connects with the specified device.
        /// </summary>
        /// <param name="device">The device.</param>
        public static void Connect(Device device)
        {
            //Connect to device
            try
            {
                device.Open(); //Open the device to allow a connection
                _comm = new CommManager(device); //Connect to the device
                Console.WriteLine($"Connected to {_comm.Device.ToString()}, {_comm.DeviceSerial.ToString()}");
            }
            catch (Exception ex)
            {
                device.Close();
                Console.WriteLine($"Could not connect: {ex.Message} in {ex.Source}");
                return;
            }
        }

        #region events
        /// <summary>
        /// Raised when the measurement has begun.
        /// </summary>
        /// <param name="sender">The sender.</param>
        /// <param name="newMeasurement">The new measurement.</param>
        private static void _comm_BeginMeasurement(object sender, ActiveMeasurement newMeasurement)
        {
            Console.WriteLine("");
            Console.WriteLine($"Measurement started.");
            Console.WriteLine("");
        }

        /// <summary>
        /// Raised when the curve containing the measurements results is created 
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="CurveEventArgs"/> instance containing the event data.</param>
        private static void _comm_BeginReceiveCurve(object sender, CurveEventArgs e)
        {
            _curve = e.GetCurve(); //Gets the reference to the active curve
            //subscribe to the curves events to write the data to the console
            _curve.NewDataAdded += _curve_NewDataAdded;
            _curve.Finished += _curve_Finished;

            Console.WriteLine("");
            Console.WriteLine($"Curve received.");
            Console.WriteLine("");
        }

        /// <summary>
        /// Raised when new data is added to the curve
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="PalmSens.Data.ArrayDataAddedEventArgs"/> instance containing the event data.</param>
        private static void _curve_NewDataAdded(object sender, PalmSens.Data.ArrayDataAddedEventArgs e)
        {
            int startIndex = e.StartIndex; //the index of the first new data point added to the curve
            int count = e.Count; //the number of new data points added to the curve

            //Write the current readings to the console
            string xUnit = _curve.XUnit.ToString();
            string yUnit = _curve.YUnit.ToString();

            for (int i = startIndex; i < startIndex + count; i++)
            {
                double xValue = _curve.GetXValue(i);
                double yValue = _curve.GetYValue(i);
                Console.WriteLine($"index = {i + 1}, {xValue.ToString("F1")} {xUnit}, {yValue.ToString("e3")} {yUnit}");
            }
        }

        /// <summary>
        /// Raised when the curve has finished receiving data
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private static void _curve_Finished(object sender, EventArgs e)
        {
            //Unsubscribe from the curves events to avoid memory leaks
            _curve.NewDataAdded -= _curve_NewDataAdded;
            _curve.Finished -= _curve_Finished;

            Console.WriteLine("");
            Console.WriteLine($"Curve finished.");
            Console.WriteLine("");
        }

        /// <summary>
        /// Raised when the measurement has ended
        /// </summary>
        /// <param name="sender">The source of the event.</param>
        /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
        private static void _comm_EndMeasurement(object sender, EventArgs e)
        {
            Console.WriteLine("");
            Console.WriteLine($"Measurement completed, {_curve.NPoints} data points received.");

            //Unsubscribe from the CommManager's events to avoid memory leaks
            _comm.BeginMeasurement -= _comm_BeginMeasurement;
            _comm.BeginReceiveCurve -= _comm_BeginReceiveCurve;
            _comm.EndMeasurement -= _comm_EndMeasurement;

            //Dispose data
            _curve.Dispose();
            _comm.Dispose();

            Console.WriteLine("Press any key to exit");
        }
        #endregion
    }
}
