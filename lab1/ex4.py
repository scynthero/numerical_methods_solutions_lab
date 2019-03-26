from sys import argv
import numpy
import matplotlib.pyplot

if len(argv) != 1:
    '''
    if type(argv[1]) != float or int:
        print("must be a number")
    else:
        if int(argv[1]) < 0:
            print("Error, length can't be negative")
        else:
    '''
    matplotlib.pyplot.plot([0, argv[1]], [0, 0]) # x and y
matplotlib.pyplot.show()
