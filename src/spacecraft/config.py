import os
from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).resolve().parent

class PhysicsConfig:
    DT = 0.01                 # Time step in seconds
    MASS = 1.5                # kg
    INERTIA_TENSOR = np.array([
        [1.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, 0.0, 3.0]
    ])
    DIMENSIONS = np.array([0.5, 0.5, 0.5])  # Dimensions of the spacecraft in meters
    DURATION = 5.0            # Simulation duration in seconds
    POSITION = np.array([0.0, 0.0, 0.0])
    LINEAR_VELOCITY = np.array([0.0, 0.0, 0.0])
    ATTITUDE = np.array([1.0, 0.0, 0.0, 0.0])
    ANGULAR_VELOCITY = np.array([0.0, 0.0, 0.0])
    STATE = np.concatenate([POSITION, LINEAR_VELOCITY, ATTITUDE, ANGULAR_VELOCITY])
    TORQUE = np.array([1.0, 0.0, 0.0])
