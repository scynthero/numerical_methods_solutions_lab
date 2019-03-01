def minimal(array = [1,15,23,-8, -12, 56]):
    return min(array), array.index(min(array))
print("Minimal value is: {0[0]} and it's index is: {0[1]}".format(minimal()))
