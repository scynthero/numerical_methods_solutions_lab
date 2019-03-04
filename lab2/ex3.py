import cs50

x = cs50.get_int("x: ")
y = cs50.get_int("y: ")
print("X is divisible by Y" if x % y == 0 else "X is not divisible by Y")
