'''
def minimal(array=[-12, 15, 23, -8, -12, 56]):
    return min(array), array.index(min(array))

'''


def minimal(array=[-12, 15, 23, -8, -12, 56, -14.5]):
    mini = min(array)
    collect_mini = []
    for x in range(len(array)):
        if array[x] == mini:
            print(x)
            collect_mini.append(x)

    return mini, collect_mini


print("Minimal value is: {0[0]} and it's index is: {0[1]}".format(minimal()))
