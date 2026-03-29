"""
This function will take as input the OU fluctuations onto the mean values, and will now add transient activity.
The transient activity is modeled as a Poisson process, which generates random events (flares) in space and time.
The Poisson process is characterized by a rate parameter (lambda) that controls the average number of events per unit time and space.
This rate parameter will be obtained from the average period between flares.
The function will add the generated flares to the existing OU fluctuations, creating a combined effect of both processes.
"""

import numpy as np
from wind.config import WindConfig

def add_poisson_flares(
    t,
    positions,          # (Nx, Ny, Nz, 3) grid of spatial coordinates
    v_full,             # (Nx, Ny, Nz, 3) full velocity field (mean + OU)
    rho_full,           # (Nx, Ny, Nz) full density field (mean + OU)
    dt
):
    
    RATE = 1.0 / WindConfig.FLARE_PERIOD  # Average flares per second
    # Step 1 — Compute Flare Probability
    flare_prob = RATE * dt  # Probability of at least one flare in this time step
    # Step 2 — Generate Poisson Events
    flare_events = np.random.rand(*positions.shape[:-1]) < flare_prob  # (Nx, Ny, Nz) boolean array
    # Step 3 — Add Flare Perturbations
    # The flare perturbations will have Gaussian amplitudes and a spatial extent defined by a Gaussian kernel.
    flare_amplitude = 5.0  # m/s for velocity, kg/m^3 for density (tunable parameter)
    flare_extent = 10000.0  # meters (10 km, tunable parameter)
    # Create a Gaussian kernel for spatial smoothing
    def gaussian_kernel(size, sigma):
        ax = np.arange(-size // 2 + 1., size // 2 + 1.)
        xx, yy, zz = np.meshgrid(ax, ax, ax)
        kernel = np.exp(-(xx**2 + yy**2 + zz**2) / (2. * sigma**2))
        return kernel / np.sum(kernel)
    kernel_size = int(3 * flare_extent / min(WindConfig.VIEWPORT_DIMENSIONS))  # Ensure kernel covers the flare extent
    kernel = gaussian_kernel(kernel_size, flare_extent / 3)
    # Apply flare perturbations to velocity and density fields
    for i in range(3):  # For each velocity component
        v_full[..., i] += flare_events * flare_amplitude * np.random.randn(*flare_events.shape)
        v_full[..., i] = np.convolve(v_full[..., i], kernel, mode='same')  # Smooth the perturbations
        
    rho_full += flare_events * flare_amplitude * np.random.randn(*flare_events.shape)
    rho_full = np.convolve(rho_full, kernel, mode='same')  # Smooth the perturbations
    return v_full, rho_full