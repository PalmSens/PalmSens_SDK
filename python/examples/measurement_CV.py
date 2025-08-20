import pypalmsens
from pypalmsens.methods import CyclicVoltammetry, CURRENT_RANGE


def new_data_callback(new_data):
    for point in new_data:
        print(point)


available_instruments = pypalmsens.discover()
print('connecting to ' + available_instruments[0].name)

with pypalmsens.connect(available_instruments[0]) as manager:
    print('connection established')

    manager.callback = new_data_callback

    serial = manager.get_instrument_serial()
    print(serial)

    method = CyclicVoltammetry(
        current_ranges={
            'max': CURRENT_RANGE.cr_1_A,  # 1 A range
            'min': CURRENT_RANGE.cr_1_uA,  # 1 µA range
            'start': CURRENT_RANGE.cr_1_mA,  # 1 mA range
        },
        equilibration_time=2,  # seconds
        begin_potential=-2,  # V
        vertex1_potential=-2,  # V
        vertex2_potential=3,  # V
        step_potential=0.05,  # V
        scanrate=5,  # V/s
        n_scans=3,  # number of scans
    )

    measurement = manager.measure(method)

    if measurement is not None:
        print('measurement finished')
    else:
        print('failed to start measurement')
