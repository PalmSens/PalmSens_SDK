from pypalmsens import instruments
from pypalmsens.methods import ChronoAmperometryParameters

method = ChronoAmperometryParameters(
    interval_time=0.01,
    potential=1.0,
    run_time=10.0,
)

with instruments.connect() as manager:
    measurement = manager.measure(method)
