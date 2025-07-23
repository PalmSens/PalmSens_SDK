from . import techniques


def cyclic_voltammetry(**kwargs):
    """Alias for CyclicVoltammetry for backwards compatibility"""
    cv = techniques.CyclicVoltammetryParameters(**kwargs)
    return cv.to_dotnet_method()
