from wind import turbulence, evolution, wr_params
from spacecraft.dynamics import dynamics
from spacecraft import magsail
from coupling import forces, torques
from simulation import monte_carlo, stability
from utils import visualization, validation, io
import spacecraft.config as config
import numpy as np
from scipy.integrate import solve_ivp

if __name__ == "__main__":
    MASS = config.PhysicsConfig.MASS
    INERTIA_TENSOR = config.PhysicsConfig.INERTIA_TENSOR
    INV_INERTIA_TENSOR = np.linalg.inv(INERTIA_TENSOR)
    DT = config.PhysicsConfig.DT
    DURATION = config.PhysicsConfig.DURATION
    STATE = config.PhysicsConfig.STATE
    FORCE = config.PhysicsConfig.FORCE
    TORQUE = config.PhysicsConfig.TORQUE
    sol = solve_ivp(
        dynamics,
        t_span=(0, DURATION),
        y0=STATE,
        args=(MASS, FORCE, TORQUE, INERTIA_TENSOR, INV_INERTIA_TENSOR),
        t_eval=np.linspace(0, DURATION, int(DURATION/DT)+1),
        method='RK45'
    )

    # Extract the solution
    solution = sol.y
    for i, t in enumerate(sol.t):
        current_state = solution[:, i]
        pos = current_state[:3]
        quat = current_state[6:10]
        quat = quat / np.linalg.norm(quat)  # Normalize quaternion to ensure it's a valid rotation

        print(f"Time: {t}, Position: {pos}, Orientation (Quaternion): {quat}")
    
