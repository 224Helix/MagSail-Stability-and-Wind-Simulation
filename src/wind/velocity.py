import numpy as np
from wind.config import WindConfig

MEAN_WIND_VELOCITY =  WindConfig.MEAN_WIND_VELOCITY
def velocity(t, position):
    """
    Compute the mean wind velocity at a given time and position.
    
    For now, it will simply return a constant velocity vector"""

    MEAN_WIND_VELOCITY =  WindConfig.MEAN_WIND_VELOCITY

    return MEAN_WIND_VELOCITY # Example: constant wind of 10 m/s in the x-direction

