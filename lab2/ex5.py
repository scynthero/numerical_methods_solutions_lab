import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cs50


def plotting(num=0):
    x_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)
    y_knots = np.linspace(-3 * np.pi, 3 * np.pi, 201)
    X, Y = np.meshgrid(x_knots, y_knots)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.cos(R) ** 2 * np.exp(((-0.1 - (float(num)) / 400)) * R)
    ax = Axes3D(plt.figure(figsize=(8, 5)))
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
    plt.show()

print("if you don't supply correct type (float), the program will ask again")
plotting(cs50.get_float("number: "))
