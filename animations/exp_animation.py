"""
==================
Animated line plot
==================

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')
ln, = plt.plot([], [], 'r', mfc='none')
plt.xlabel('Time (s)')


Vcc  = 3
tmax = 3
tmin = 0
ymin = 0
ymax = Vcc 


def init():
    ax.set_xlim(tmin,tmax)
    ax.set_ylim(ymin, ymax)
    return ln,

def yfunk(t):
    return Vcc*(1-np.exp(-t))

def update(frame):
    xdata.append(frame)
    ydata.append(yfunk(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, tmax, 25),
                    init_func=init,interval=50, repeat=False,blit=False)
# repeat_delay=1000,

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
