import numpy as np
from wind.config import WindConfig
import sys

MEAN_WIND_VELOCITY =  WindConfig.MEAN_WIND_VELOCITY
VIEWPORT_DIMENSIONS = WindConfig.VIEWPORT_DIMENSIONS
def velocity(t):
    """
    Compute the wind vector field at a given time.
    """
    CELL_SIZE = 5 # km^3
    dim_x = int(VIEWPORT_DIMENSIONS[0] / CELL_SIZE)
    dim_y = int(VIEWPORT_DIMENSIONS[1] / CELL_SIZE)
    dim_z = int(VIEWPORT_DIMENSIONS[2] / CELL_SIZE)
    v_field = initialize_v_field(dim_x, dim_y, dim_z)
    if v_field is None:
        sys.exit(1)  # Exit if initialization failed due to memory issues
    
    # Example: Set mean wind velocity in the entire field
    v_field[:, :, :, 0] = MEAN_WIND_VELOCITY[0]  # Vx
    v_field[:, :, :, 1] = MEAN_WIND_VELOCITY[1]  # Vy
    v_field[:, :, :, 2] = MEAN_WIND_VELOCITY[2]  # Vz


def initialize_v_field(dim_x, dim_y, dim_z):
    # Calculate expected memory usage in GB (for float32, 3 components)
    gb_required = (dim_x * dim_y * dim_z * 3 * 4) / (1024**3)
    print(f"Initializing {dim_x}x{dim_y}x{dim_z} grid...")
    print(f"Estimated RAM requirement: {gb_required:.2f} GB")
    
    try:
        # We use (X, Y, Z, 3) where 3 is [Vx, Vy, Vz]
        v_field = np.zeros((dim_x, dim_y, dim_z, 3), dtype=np.float32)
        print("Initialization successful.")
        return v_field
    except MemoryError:
        print("CRITICAL: Not enough RAM. Try reducing grid size or using float16.")
        return None

    
