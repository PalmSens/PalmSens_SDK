from . import techniques


def cyclic_voltammetry(**kwargs):
    """Alias for CyclicVoltammetry for backwards compatibility"""
    cv = techniques.CyclicVoltammetryParameters(**kwargs)
    return cv.to_dotnet_method()


def linear_sweep_voltammetry(**kwargs):
    """Alias for LinearSweep for backwards compatibility"""
    lsv = techniques.LinearSweepParameters(**kwargs)
    return lsv.to_dotnet_method()
