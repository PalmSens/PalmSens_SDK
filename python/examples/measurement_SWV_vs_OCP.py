import pypalmsens
from pypalmsens.methods import SquareWaveVoltammetry


def new_data_callback(new_data):
    for point in new_data:
        print(point)


available_instruments = pypalmsens.discover()

with pypalmsens.connect(available_instruments[0]) as manager:
    print('connection established')

    manager.callback = new_data_callback

    method = SquareWaveVoltammetry(
        conditioning_potential=2.0,  # V
        conditioning_time=2,  # seconds
        versus_ocp_mode=3,  # versus begin and end potential
        versus_ocp_max_ocp_time=1,  # seconds
        begin_potential=-0.5,  # V
        end_potential=0.5,  # V
        step_potential=0.01,  # V
        amplitude=0.08,  # V
        frequency=10,  # Hz
    )

    method.frequency = 50

    measurement = manager.measure(method)

    print(f'ocp: {measurement.curves[0].pscurve.OCPValue}')
