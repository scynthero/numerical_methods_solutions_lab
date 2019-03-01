from sys import argv
import numpy
import matplotlib.pyplot

if len(argv) != 1:
    matplotlib.pyplot.plot([0, argv[1]], [0, 0]) # x and y
matplotlib.pyplot.show()
