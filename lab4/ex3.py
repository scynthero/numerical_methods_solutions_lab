from matplotlib.pyplot import *
from scipy.integrate import *
from numpy import *
from mpl_toolkits.mplot3d import *
s = 10
b = 8/3
r = 28
h = 0.001
start = 0
stop = 100
time = arange(start,stop,h)
init = (1,1,1)
def func (param, time):
    dx = [0,0,0]
    dx[0] = s * (param[1] - param[0])
    dx[1] = -1 * param[0] * param [2] + r * param[0] - param[1]
    dx[2] = param[0] * param[1] - b * param[2]
    return dx
returned_values = odeint(func, init, time)
#plot(time,returned_values)
show()
Axes3D(figure()).plot(returned_values[:,0],returned_values[:,1], returned_values[:,2])
show()