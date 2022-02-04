# リアルタイムで振り子の角度とかをプロット
# 未完成

from pendulum_sim import state_vector, do_simulation, init_setup
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111)
timestep = 10000

def animate_pendulum(frame):
    do_simulation(sim, 0, 1)
    x = np.arange(timestep)
    y = state_vector(sim)
    ax.plot(x[frame],y[1], "o")

sim, viewer = init_setup()
animation = FuncAnimation(fig, animate_pendulum, frames=range(128), interval=1000)
animation.save("test.gif", writer="pillow")
plt.close()