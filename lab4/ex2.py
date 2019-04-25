from matplotlib.pyplot import *
from numpy import *


def Euler():
    a = 1
    T = 3
    h = 0.1

    initial_x = 1
    t = arange(0, T, h)
    x = zeros(t.shape)
    x[0] = initial_x

    for i in range(t.size - 1):
        x[i + 1] = x[i] + h * (1 * x[i])

    h = 0.001
    initial_y = 1
    r = arange(0, T, h)
    y = zeros(r.shape)
    y[0] = initial_y
    for i in range(r.size - 1):
        y[i + 1] = y[i] + h * (1 * y[i])
    line, = plot(t, x, '-',label="not approximated")
    line, = plot(r, y, 'g-',label="ideal")
    legend()
    show()


Euler()
