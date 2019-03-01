def minimal(array = [1,15,23,-8, -12, 56]):
    return min(array), array.index(min(array))
print("Minimal value is: %.2f and it's index is: %d" % minimal())
