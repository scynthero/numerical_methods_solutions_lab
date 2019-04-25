import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import differential_evolution
from scipy.optimize import fmin

x_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)
y_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)

X, Y = np.meshgrid(x_knots, y_knots)

R = np.sqrt(X ** 2 + Y ** 2)
Z = -np.cos(R) ** 2 * np.exp(-0.1 * R)

ax = Axes3D(plt.figure(figsize=(8, 5)))

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)


def f(x):
    r = np.sqrt(x[0] ** 2 + x[1] ** 2)
    z = -np.cos(r) ** 2 * np.exp(-0.1 * r)
    return z


bounds = [(-5, 5), (-5, 5)]
result = differential_evolution(f, bounds)
ax.plot([result.x[0]], [result.x[1]], [result.fun], marker='o', markersize=8, color='k')
x0 = [-7,-7]
local_min = fmin(f,x0)
local_min_val = f(local_min)
ax.plot([local_min[0]],[local_min[1]],[local_min_val], marker='o', markersize=8, color='y')
ax.plot([x0[0]], [x0[1]], [f(x0)], color='g', marker='o', markersize=5, label='initial')
plt.show()
