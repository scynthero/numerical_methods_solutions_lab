for x in range(-19, 20):
    for y in range(-19, 20):
        if y == 0:
            continue
        if x % 2 != 0 or y % 2 !=0:
            continue
        if x % y == 0:
            print(x, y)
