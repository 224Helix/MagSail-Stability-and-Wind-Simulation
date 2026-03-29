import numpy as np
from wind.velocity import velocity
from wind.density import density


def force(t, position, collision_area):
    """
    Compute the mean wind force exerted due to ram pressure at a given time and position.
    
    For now, it will simply return the product of mean wind velocity and density"""
    v = velocity.mean_wind(t, position)
    rho = density.mean_density(t, position, None)  # Density function can be extended to use more parameters
    return rho * collision_area * np.linalg.norm(v) * v # This is the ram pressure force for incompressible flow