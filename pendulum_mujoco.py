import mujoco_py
import numpy as np
model = mujoco_py.load_model_from_path("pendulum_3.xml")
sim = mujoco_py.MjSim(model, nsubsteps=2)

viewer = mujoco_py.MjViewer(sim)

def do_simulation(ctrl, n_frames):
    sim.data.ctrl[:] = ctrl
    for _ in range(n_frames):
        sim.step()

def state_vector():
    return np.concatenate([
        sim.data.qpos.flat,
        sim.data.qvel.flat
    ])
    
def is_healthy():
    state = state_vector()
    min_z, max_z = (0.4, 1.0)
    is_healthy = (np.isfinite(state).all() and min_z <= state[2] <= max_z)
    return is_healthy

def set_state(qpos, qvel):
    old_state = sim.get_state()
    new_state = mujoco_py.MjSimState(old_state.time, qpos, qvel,
                                     old_state.act, old_state.udd_state)
    sim.set_state(new_state)
    sim.forward()

# 初期位置，速度
init_qpos = sim.data.qpos.ravel().copy()
init_qvel = sim.data.qvel.ravel().copy()

for step in range(1000):
    viewer.render()
    do_simulation(0, 1)
    print("position", sim.data.qpos.flat.copy()) # [スライダ-, hinge1, hinge2, hinge...]の位置, ヒンジは[-π, π]
    print("velocity", sim.data.qvel.flat.copy())

viewer = None
