from pspython import pspyinstruments, pspymethods


def new_data_callback(new_data):
    for point in new_data:
        for type, value in point.items():
            print(type + ' = ' + str(value))
    return


manager = pspyinstruments.InstrumentManager(new_data_callback=new_data_callback)
available_instruments = pspyinstruments.discover_instruments()
print('connecting to ' + available_instruments[0].name)
success = manager.connect(available_instruments[0])

if success != 1:
    print('connection failed')
    exit()

print('connection established')

n_multiplexer_channels = manager.initialize_multiplexer(2)
manager.set_mux8r2_settings()

for channel in range(n_multiplexer_channels):
    manager.set_multiplexer_channel(channel)

# When measuring alternatingly the selection is restricted to the first n channels
altnernating_multiplexer_method = pspymethods.chronoamperometry(
    interval_time=0.5,  # seconds
    e=1.0,  # volts
    run_time=5.0,  # seconds
    set_mux_mode=1,  # -1 = disabled, 0 = sequential, 1 = alternating
    set_mux_channels=[
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
    ],  # 8 channels, 1 and 2 are enabled
    set_mux8r2_settings=pspymethods.get_mux8r2_settings(
        connect_sense_to_working_electrode=False,
        combine_reference_and_counter_electrodes=False,
        use_channel_1_reference_and_counter_electrodes=False,  # use the reference and counter electrodes of channel 1 for all channels
        set_unselected_channel_working_electrode=0,  # working electrode of the unselected channels are disconnected/floating
    ),
)
measurement = manager.measure(altnernating_multiplexer_method)

if measurement is not None:
    print('measurement finished')
else:
    print('failed to start measurement')

consecutive_multiplexer_method = pspymethods.square_wave_voltammetry(
    equilibrium_time=0,  # seconds
    begin_potential=-0.5,  # volts
    end_potential=0.5,  # volts
    step_potential=0.01,  # volts
    amplitude=0.1,  # volts
    frequency=10,  # hertz
    set_mux_mode=0,  # -1 = disabled, 0 = sequential, 1 = alternating
    set_mux_channels=[
        True,
        True,
        False,
        False,
        False,
        False,
        True,
        True,
    ],  # 8 channels, 1, 2, 7 and 8 are enabled
    set_mux8r2_settings=pspymethods.get_mux8r2_settings(
        connect_sense_to_working_electrode=False,
        combine_reference_and_counter_electrodes=False,
        use_channel_1_reference_and_counter_electrodes=False,  # use the reference and counter electrodes of channel 1 for all channels
        set_unselected_channel_working_electrode=0,  # working electrode of the unselected channels are disconnected/floating
    ),
)

measurement = manager.measure(consecutive_multiplexer_method)

if measurement is not None:
    print('measurement finished')
else:
    print('failed to start measurement')

success = manager.disconnect()

if success == 1:
    print('disconnected')
else:
    print('error while disconnecting')
