import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from amuse.plot import *

# plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

# fig = plt.figure(figsize=(8,8))                                # <-- reduce DPI later for speed
# ax = fig.add_subplot(111, projection="3d")
# ax.axes.set(xlim=(-1000,1000), ylim=(-1000,1000), zlim=(-1000,1000))
# ax.scatter(binary.x.value_in(u.RSun), binary.y.value_in(u.RSun), binary.z.value_in(u.RSun), s=binary.radius.value_in(u.RSun), label = "Schwarzschild radius", alpha = 0.5, c="green")
# ax.scatter(binary.x.value_in(u.RSun), binary.y.value_in(u.RSun), binary.z.value_in(u.RSun),  alpha=0.5, c="blue" )
# ax.scatter(gas.x.value_in(u.RSun), gas.y.value_in(u.RSun), gas.z.value_in(u.RSun), c="yellow", alpha=0.2)
# ax.scatter(core.x.value_in(u.RSun), core.y.value_in(u.RSun), core.z.value_in(u.RSun), c="red")
# # ax.scatter(binary.center_of_mass().x.value_in(u.AU), binary.center_of_mass().y, marker="x", label="center of mass")
# plt.legend()
# fig, ax = plt.subplots(figsize=(6,6))
# sph_particles_plot(gas, max_size=500)
# scatter(core.x,core.y, c="white", s=core.radius.value_in(u.RSun)*1000, marker="o", label="Core")