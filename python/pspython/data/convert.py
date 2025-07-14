from .curve import Curve


def convert_to_curves(m):
    curves = []

    curves_net = m.GetCurveArray()
    for dotnet_curve in curves_net:
        curves.append(Curve(dotnet_curve=dotnet_curve))

    return curves
