# python3 pendulum_sim.py --xmlfile pendulum_2 --exportcsv result_pendulum2 --timestep 10000
import mujoco_py
import numpy as np
import csv
import argparse


def init_setup(xmlfile):
    model = mujoco_py.load_model_from_path("xml/" + xmlfile + ".xml")
    sim = mujoco_py.MjSim(model, nsubsteps=2)
    viewer = mujoco_py.MjViewer(sim)
    return sim, viewer

def do_simulation(sim, ctrl, n_frames):
    sim.data.ctrl[:] = ctrl
    for _ in range(n_frames):
        sim.step()

# 状態をまとめて取得する
def state_vector(sim):
    return np.concatenate([
        sim.data.qpos.flat,
        sim.data.qvel.flat
    ])
# 初期状態をセットする
# def set_state(sim, qpos, qvel):
#     old_state = sim.get_state()
#     new_state = mujoco_py.MjSimState(old_state.time, qpos, qvel,
#                                      old_state.act, old_state.udd_state)
#     sim.set_state(new_state)
#     sim.forward()
# 初期位置，速度
# init_qpos = sim.data.qpos.ravel().copy()
# init_qvel = sim.data.qvel.ravel().copy()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--xmlfile", type=str, default="pendulum_2")
    parser.add_argument("--exportcsv", type=str, default="test")
    parser.add_argument("--timestep", type=int, default=10000)

    args = parser.parse_args()


    sim, viewer = init_setup(args.xmlfile)
    observations = []
    for step in range(args.timestep):
        viewer.render()
        # 特に自分からカートを動かさないのでctrlには0を入れる
        do_simulation(sim, 0, 1)
        print(step, " timestep")
        print("position", sim.data.qpos.flat.copy(), "velocity", sim.data.qvel.flat.copy()) # [スライダ-, hinge1, hinge2, hinge...]の位置, ヒンジは[-π, π]
        observations.append(state_vector(sim).tolist())

    # csvファイルに出力する
    with open(args.exportcsv + ".csv", 'a', newline='') as f:
        w = csv.writer(f)
        w.writerows(observations)
    viewer = None
