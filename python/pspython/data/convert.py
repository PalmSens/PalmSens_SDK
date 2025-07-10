from .curve import Curve
from .measurement import Measurement


def convert_to_measurement(
    m,
) -> Measurement:
    """
    Get collection of arrays in the dataset with the exception of the potential and current arrays.

    Arrays contain a single value stored in the Value field.

    Please note that measurements can contain multiple arrays of the same type,
    i.e. for CVs or Mux measurements
    """
    measurement = Measurement(dotnet_measurement=m)
    return measurement


def convert_to_curves(m):
    curves = []

    curves_net = m.GetCurveArray()
    for dotnet_curve in curves_net:
        curves.append(Curve(dotnet_curve=dotnet_curve))

    return curves
