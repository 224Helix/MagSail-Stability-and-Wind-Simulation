import numpy as np
from wind.config import WindConfig

def mean_density(t, position, density):
    """
    Compute the mean wind density at a given time and position.
    
    For now, it will simply return a constant density value but it will be replaced with a Parker spiral model in the future."""
    return WindConfig.MEAN_WIND_DENSITY  # kg/m^3, standard sea level density

