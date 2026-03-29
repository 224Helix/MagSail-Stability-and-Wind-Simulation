import sys
import os
import numpy as np

# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'src')))

try:
    from wind.ou import ou_3d
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

def test_ou_3d():
    nx, ny, nz = 10, 10, 10
    positions = np.zeros((nx, ny, nz, 3))
    v_fluct = np.zeros((nx, ny, nz, 3))
    rho_fluct = np.zeros((nx, ny, nz))
    dt = 1.0
    params = {
        "theta_v": 0.1,
        "theta_rho": 0.1,
        "sigma_v": 1.0,
        "sigma_rho": 0.1,
        "corr_length": 2.0,
        "dx": 10.0,
        "dy": 10.0,
        "dz": 10.0
    }
    
    # Run one step
    v_full, rho_full, v_f_new, rho_f_new = ou_3d(0.0, positions, v_fluct, rho_fluct, dt, params)
    
    print(f"v_full shape: {v_full.shape}")
    print(f"rho_full shape: {rho_full.shape}")
    print(f"v_full mean: {np.mean(v_full, axis=(0,1,2))}")
    print(f"rho_full mean: {np.mean(rho_full)}")
    
    # Check shapes
    assert v_full.shape == (nx, ny, nz, 3)
    assert rho_full.shape == (nx, ny, nz)
    assert v_f_new.shape == (nx, ny, nz, 3)
    assert rho_f_new.shape == (nx, ny, nz)
    
    # Check that fluctuations are non-zero after injection
    # Injected only at one slice
    print(f"Non-zero elements in v_f_new: {np.count_nonzero(v_f_new)}")
    assert np.any(v_f_new != 0)
    assert np.any(rho_f_new != 0)
    
    # Since we are using np.roll with v_mean_avg=[10, 10, 10] and dt=1, dx=10, 
    # shift_x = int(10 * 1 / 10) = 1.
    # So the fluctuations should be shifted.
    
    print("Test passed!")

if __name__ == "__main__":
    test_ou_3d()
