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
    DURATION = 5.0            # Simulation duration in seconds
    POSITION = np.array([0.0, 0.0, 0.0])
    LINEAR_VELOCITY = np.array([0.0, 0.0, 0.0])
    ATTITUDE = np.array([1.0, 0.0, 0.0, 0.0])
    ANGULAR_VELOCITY = np.array([0.0, 0.0, 0.0])
    STATE = np.concatenate([POSITION, LINEAR_VELOCITY, ATTITUDE, ANGULAR_VELOCITY])
    FORCE = np.array([0.0, 0.0, 15.0])
    TORQUE = np.array([1.0, 0.0, 0.0])
