import cs50

x = cs50.get_float("x: ")
y = cs50.get_float("y: ")
print("X is divisible by Y" if round(x, 2) % round(y, 2) == 0 else "X is not divisible by Y")
