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


def compare(figure1, figure2):
    figure1_field = countField(*figure1)
    figure2_field = countField(*figure2)
    if figure1_field > figure2_field:
        return "The {} has larger field = {:g}".format(figure1[0], figure1_field)
    elif figure1_field == figure2_field:
        return "The fields are equal = {:g}".format(figure1_field)
    else:
        return "The {} has larger field = {:g}".format(figure2[0], figure2_field)


print(compare(["Circle", 6], ["Rhombus", 2, 4]))
