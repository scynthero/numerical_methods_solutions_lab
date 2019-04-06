from math import pi


class Circle:
    def field(*args):
        return pi * args[1] ** 2


class Rectangle:
    def field(*args):
        return args[1] * args[2]


class Triangle:
    def field(*args):
        return (args[1] * args[2]) / 2


class Rhombus:
    def field(*args):
        return (args[1] * args[2]) / 2


def countField(figure, *args):
    return globals()[figure]().field(*args)


def compare(*args):
    cmpr = []
    for i in range(len(args)):
        if len(args[i]) == 2:
            cmpr.append([args[i][0], countField(args[i][0], args[i][1])])
        else:
            cmpr.append([args[i][0], countField(args[i][0], args[i][1], args[i][2])])

    if cmpr[0][1] > cmpr[1][1]:
        return "The {} has larger field = {:g}".format(cmpr[0][0], cmpr[0][1])
    elif cmpr[0][1] == cmpr[1][1]:
        return "The fields are equal = {:g}".format(cmpr[0][1])
    else:
        return "The {} has larger field = {:g}".format(cmpr[1][0], cmpr[1][1])

    '''
    if countField(args[0][0], args[0][1:]) > countField(args[1][0],args[1][1:]):
        return "The {} has larger field".format(args[0][0])
    else:
        return "The {} has larger field".format(args[1][0])
    '''


print(compare(["Circle", 4], ["Rhombus", 2, 4]))
