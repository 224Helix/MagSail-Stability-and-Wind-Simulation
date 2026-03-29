""" 
This file uses the Ornstein-Uhlenbeck process to generate random clump objects. 
These are smooth perturbations in density and velocity that are then advected with the mean wind flow.
The OU process is a continuous-time stochastic process that is mean-reverting, making it suitable for modeling physical phenomena like turbulence.
"""

import numpy as np
from scipy.ndimage import gaussian_filter
from wind.velocity import velocity
from wind.density import mean_density

def ou_3d(
    t,
    positions,          # (Nx, Ny, Nz, 3) grid of spatial coordinates
    v_fluct,            # (Nx, Ny, Nz, 3) velocity fluctuations
    rho_fluct,          # (Nx, Ny, Nz) density fluctuations
    dt,
    params
):
    """
    3D Ornstein-Uhlenbeck turbulence model.
    Injects correlated stochastic fluctuations at the inflow boundary,
    advects them with the mean wind field, and applies exponential decay.
    """
    
    # Step 1 — Compute Mean Fields
    v_mean = velocity(t, positions)
    # The existing mean_density function in density.py takes 3 arguments: t, position, density.
    # We follow the spec but adapt to the existing signature by passing None for the unused argument.
    rho_mean = mean_density(t, positions, None)
    
    # Step 2 — Determine Inflow Boundary
    # Compute domain-averaged mean velocity vector
    v_mean_avg = np.mean(v_mean, axis=(0, 1, 2))
    
    nx, ny, nz = v_fluct.shape[:3]
    dx, dy, dz = params["dx"], params["dy"], params["dz"]
    
    # Determine dominant flow direction (largest component)
    abs_v_avg = np.abs(v_mean_avg)
    dominant_axis = np.argmax(abs_v_avg)
    
    # Step 3 — Advect Fluctuations
    # Use integer grid shift (first-order upwind approximation)
    shift_x = int(v_mean_avg[0] * dt / dx)
    shift_y = int(v_mean_avg[1] * dt / dy)
    shift_z = int(v_mean_avg[2] * dt / dz)
    
    v_fluct = np.roll(v_fluct, shift_x, axis=0)
    v_fluct = np.roll(v_fluct, shift_y, axis=1)
    v_fluct = np.roll(v_fluct, shift_z, axis=2)
    
    rho_fluct = np.roll(rho_fluct, shift_x, axis=0)
    rho_fluct = np.roll(rho_fluct, shift_y, axis=1)
    rho_fluct = np.roll(rho_fluct, shift_z, axis=2)
    
    # Step 4 — Apply OU Decay
    v_fluct *= np.exp(-params["theta_v"] * dt)
    rho_fluct *= np.exp(-params["theta_rho"] * dt)
    
    # Step 5 — Inject Boundary Turbulence
    def generate_correlated_noise(shape, sigma, dt, corr_length):
        # 5.1 Generate Gaussian noise
        noise = np.random.randn(*shape)
        # Apply spatial smoothing kernel (Gaussian filter)
        # sigma in gaussian_filter is the standard deviation in pixels/grid units
        smoothed_noise = gaussian_filter(noise, sigma=corr_length)
        # 5.2 Scale noise: noise MUST scale with np.sqrt(dt)
        return smoothed_noise * sigma * np.sqrt(dt)

    # 5.3 Apply only to boundary slice based on flow direction
    if dominant_axis == 0:
        # x-axis dominant
        idx = -1 if v_mean_avg[0] > 0 else 0
        v_fluct[idx, :, :, :] += generate_correlated_noise((ny, nz, 3), params["sigma_v"], dt, params["corr_length"])
        rho_fluct[idx, :, :] += generate_correlated_noise((ny, nz), params["sigma_rho"], dt, params["corr_length"])
    elif dominant_axis == 1:
        # y-axis dominant
        idx = -1 if v_mean_avg[1] > 0 else 0
        v_fluct[:, idx, :, :] += generate_correlated_noise((nx, nz, 3), params["sigma_v"], dt, params["corr_length"])
        rho_fluct[:, idx, :] += generate_correlated_noise((nx, nz), params["sigma_rho"], dt, params["corr_length"])
    else:
        # z-axis dominant
        idx = -1 if v_mean_avg[2] > 0 else 0
        v_fluct[:, :, idx, :] += generate_correlated_noise((nx, ny, 3), params["sigma_v"], dt, params["corr_length"])
        rho_fluct[:, :, idx] += generate_correlated_noise((nx, ny), params["sigma_rho"], dt, params["corr_length"])

    # Step 6 — Output
    v_full = v_mean + v_fluct
    rho_full = rho_mean + rho_fluct
    
    return v_full, rho_full, v_fluct, rho_fluct

