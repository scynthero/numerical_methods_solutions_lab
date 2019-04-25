from matplotlib.pyplot import *
from numpy import *


def Euler(a=1,T=3,h=0.1):
    initial_x = 1
    t = arange(0, T, h)
    x = zeros(t.shape)
    x[0] = initial_x

    for i in range(t.size - 1):
        x[i + 1] = x[i] + h * (1 * x[i])
    plot(t, x, '-')
    show()


Euler()
