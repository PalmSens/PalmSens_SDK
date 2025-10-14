﻿using OxyPlot;
using OxyPlot.Axes;
using OxyPlot.Series;
using PalmSens;
using PalmSens.Comm;
using PalmSens.Core.Simplified;
using PalmSens.Core.Simplified.Data;
using PalmSens.Techniques;
using PalmSensLivePlot.Services;
using System.Collections.ObjectModel;
using Device = PalmSens.Devices.Device;

namespace PalmSensLivePlot
{
    public partial class MainPage : ContentPage
    {
        private IReadOnlyList<Device> _availableDevices;
        private Device _selectedDevice;
        private readonly PSCommSimple _psCommSimple;

        public MainPage(PSCommSimple psCommSimple)
        {
            InitializeComponent();
            BindingContext = this;
            this._psCommSimple = psCommSimple;

            _psCommSimple.StateChanged += OnStateChanged;
            _psCommSimple.ReceiveStatus += OnReceiveStatus;
            _psCommSimple.MeasurementStarted += OnMeasurementStarted;
            _psCommSimple.MeasurementEnded += OnMeasurementEnded;
            _psCommSimple.SimpleCurveStartReceivingData += OnSimpleCurveStartReceivingData;
            _psCommSimple.Disconnected += OnDisconnected;
        }

        private SimpleMeasurement _activeMeasurement = null;

        public ObservableCollection<string> Log
        {
            get { return _log; }
            set { _log = value; }
        }

        private ObservableCollection<string> _log = [];

        public IReadOnlyList<Device> AvailableDevices
        {
            get => _availableDevices;
            set
            {
                _availableDevices = value;
                OnPropertyChanged();
            }
        }

        public Device? SelectedDevice
        {
            get => _selectedDevice;
            set
            {
                _selectedDevice = value;
                OnPropertyChanged();
            }
        }
        private Method InitMethod()
        {
            Method method = new CyclicVoltammetry
            {
                BeginPotential = -.5f,
                Vtx1Potential = -.5f,
                Vtx2Potential = .5f,
                StepPotential = 0.05f,
                Scanrate = 1f,
                nScans = 3,
                EquilibrationTime = 5f,
            };

            method.Ranging.StartCurrentRange = new CurrentRange(CurrentRanges.cr1uA);
            method.Ranging.MinimumCurrentRange = new CurrentRange(CurrentRanges.cr10nA);
            method.Ranging.MaximumCurrentRange = new CurrentRange(CurrentRanges.cr1mA);

            return method;
        }

        private async void DiscoverClicked(object? sender, EventArgs e)
        {
            DiscoverBtn.IsEnabled = false;
            try
            {
                AvailableDevices = await _psCommSimple.GetAvailableDevicesAsync();
                SelectedDevice = AvailableDevices.FirstOrDefault();
            }
            finally
            {
                DiscoverBtn.IsEnabled = true;
                ConnectBtn.IsEnabled = true;
            }
        }

        private async void ConnectClicked(object? sender, EventArgs e)
        {
            Log.Add($"Connecting to {SelectedDevice}...");


            if (_psCommSimple.Connected)
            {
                await _psCommSimple.DisconnectAsync();

            }
            else
            {
                try
                {
                    await _psCommSimple.ConnectAsync(SelectedDevice);
                }
                catch (Exception ex)
                {
                    Log.Add(ex.Message);
                }
            }

            MeasureBtn.IsEnabled = _psCommSimple.Connected;
            ConnectBtn.Text = _psCommSimple.Connected ? "Disconnect" : "Connect";
            Log.Add(_psCommSimple.Connected ? $"Connected to {_psCommSimple.ConnectedDevice}" : "Nothing is connected");
        }

        private async void MeasureClicked(object? sender, EventArgs e)
        {
            Method method = InitMethod();

            if (_psCommSimple.DeviceState == PalmSens.Comm.CommManager.DeviceState.Idle)
            {
                Log.Add($"Starting measurement...");
                try
                {
                    _activeMeasurement = await _psCommSimple.MeasureAsync(method);
                }
                catch (Exception ex)
                {
                    Log.Add(ex.Message);
                }
            }
            else
            {
                Log.Add($"Aborting measurement...");
                try
                {
                    await _psCommSimple.AbortMeasurementAsync();
                }
                catch (Exception ex)
                {
                    Log.Add(ex.Message);
                }
            }
        }
        private void OnReceiveStatus(object sender, PalmSens.Comm.StatusEventArgs e)
        {
            Status status = e.GetStatus();

            double potential = status.PotentialReading.Value;
            double currentInRange = status.CurrentReading.ValueInRange;

            PalmSens.Comm.ReadingStatus currentStatus = status.CurrentReading.ReadingStatus;
            CurrentRange cr = status.CurrentReading.CurrentRange;

            PotentialValue.Text = $"{potential:F3} V";
            CurrentValue.Text = $"{currentInRange:F3} * {cr}";
        }

        private void OnStateChanged(object sender, PalmSens.Comm.CommManager.DeviceState CurrentState)
        {
            StatusValue.Text = $"{CurrentState}";

            var isIdle = CurrentState == PalmSens.Comm.CommManager.DeviceState.Idle;
            var isEnabled = isIdle;

            ConnectBtn.IsEnabled = isEnabled;
            DiscoverBtn.IsEnabled = isEnabled;

            MeasureBtn.Text = isIdle ? "Measure" : "Abort";
        }

        private void OnMeasurementStarted(object sender, EventArgs e)
        {
            Log.Add("Measurement started");
        }

        private void OnMeasurementEnded(object sender, Exception e)
        {
            Log.Add("Measurement ended");
        }

        private void OnDisconnected(object sender, Exception exception)
        {
            if (exception != null)
            {
                Log.Add(exception.Message);
            }
            else
            {
                Log.Add("Disconnected");
            }

            ConnectBtn.Text = "Connect";
            ConnectBtn.IsEnabled = true;
            MeasureBtn.Text = "Measure";
        }

        private void OnSimpleCurveStartReceivingData(object sender, SimpleCurve activeSimpleCurve)
        {
            // `CorePlot.AddSimpleCurve()` subscribes to the `NewDataAdded` event and auto-updates the plot
            plotView1.CorePlot.AddSimpleCurve(activeSimpleCurve);

            activeSimpleCurve.CurveFinished += OnCurveFinished;

            Log.Add("Curve is receiving new data...");
        }

        private void OnNewDataAdded(object sender, PalmSens.Data.ArrayDataAddedEventArgs e)
        {
            if (MauiPlatformInvoker.InvokeIfRequired(() => OnNewDataAdded(sender, e)))
            {
                return;
            }

            SimpleCurve activeSimpleCurve = sender as SimpleCurve;
            int startIndex = e.StartIndex;
            int count = e.Count;

            for (int i = startIndex; i < startIndex + count; i++)
            {
                double xValue = activeSimpleCurve.XAxisValue(i);
                double yValue = activeSimpleCurve.YAxisValue(i);
            }

            PotentialValue.Text = $"{activeSimpleCurve.XAxisValue(startIndex + count - 1):F3}";
            CurrentValue.Text = $"{activeSimpleCurve.YAxisValue(startIndex + count - 1):F3}";
        }

        private void OnCurveFinished(object sender, EventArgs e)
        {
            SimpleCurve activeSimpleCurve = sender as SimpleCurve;

            activeSimpleCurve.CurveFinished -= OnCurveFinished;

            CurveFinished(activeSimpleCurve);
        }

        private void CurveFinished(SimpleCurve activeSimpleCurve)
        {
            if (MauiPlatformInvoker.InvokeIfRequired(() => CurveFinished(activeSimpleCurve)))
            {
                return;
            }

            int nDataPointsReceived = activeSimpleCurve.NDataPoints;
            Log.Add($"{nDataPointsReceived} data point(s) received");
        }
    }
}
