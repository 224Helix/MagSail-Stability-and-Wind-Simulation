from config import PhysicsConfig
import numpy as np
from scipy.integrate import solve_ivp

DT = PhysicsConfig.DT
DURATION = PhysicsConfig.DURATION
MASS = PhysicsConfig.MASS
INERTIA_TENSOR = PhysicsConfig.INERTIA_TENSOR
INV_INERTIA_TENSOR = np.linalg.inv(INERTIA_TENSOR)
STATE = PhysicsConfig.STATE
FORCE = PhysicsConfig.FORCE
TORQUE = PhysicsConfig.TORQUE
def dynamics(t,state, mass, force, torque, inertia, inv_inertia):
    # Unpack the state vector
    position = state[0:3]
    velocity = state[3:6]
    orientation = state[6:10]
    angular_velocity = state[10:13]

    # Linear physics
    d_pos = velocity
    d_lin_vel = force / mass

    # Angular acceleration
    d_ang_vel = inv_inertia @ (torque - np.cross(angular_velocity, inertia @ angular_velocity))

    # Quaternion derivative
    wx, wy, wz = angular_velocity
    omega = np.array([[0, -wx, -wy, -wz], 
                      [wx, 0, wz, -wy], 
                      [wy, -wz, 0, wx], 
                      [wz, wy, -wx, 0]])
    d_quat = 0.5 * omega @ orientation

    # Combine all derivatives
    d_state = np.concatenate([d_pos, d_lin_vel, d_quat, d_ang_vel])
    return d_state

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

