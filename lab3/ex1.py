from math import pi


class Circle:
    def field(*args):
        if len(args) < 2:
            return -1
        else:
            return pi * args[1] ** 2


class Rectangle:
    def field(*args):
        if len(args) < 3:
            return -1
        else:
            return args[1] * args[2]


class Triangle:
    def field(*args):
        if len(args) < 3:
            return -1
        else:
            return (args[1] * args[2]) / 2


class Rhombus:
    def field(*args):
        if len(args) < 3:
            return -1
        else:
            return (args[1] * args[2]) / 2


def countField(figure=0, *args):
    if figure not in globals():
        return None
    else:
        return globals()[figure]().field(*args)


def compare(figure1=0, figure2=0, *args):
    if figure1 == 0 or figure2 == 0:
        return ("Missing arguments")
    elif len(args) > 0:
        return ("To many arguments given")
    else:
        figure1_field = countField(*figure1)
        figure2_field = countField(*figure2)
        if figure1_field == -1 or figure2_field == -1:
            return ("Error, wrong number of arguments given")
        elif figure1_field == None or figure2_field == None:
            return ("Wrong figure name")
        elif figure1_field > figure2_field:
            return "The {} has larger field = {:g}".format(figure1[0], figure1_field)
        elif figure1_field == figure2_field:
            return "The fields are equal = {:g}".format(figure1_field)
        else:
            return "The {} has larger field = {:g}".format(figure2[0], figure2_field)


print(compare())
