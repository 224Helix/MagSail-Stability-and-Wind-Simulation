import os
from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).resolve().parent

class WindConfig:
    MEAN_WIND_VELOCITY = np.array([10.0, 10.0, 10.0])  # m/s
    MEAN_WIND_DENSITY = 1.225  # kg/m^3
    VIEWPORT_DIMENSIONS = np.array([1000000.0, 1000000.0, 1000000.0])  # 1000 km x 1000 km x 1000 km
    FLARE_PERIOD = 20526.0 # seconds (about 5.7 hours)