import cs50
print("if you don;t supply correct type (int), the progam will ask again")
x = cs50.get_int("x: ")
y = cs50.get_int("y: ")
if y == 0:
    print("can't divide by zero")
else:
    print("X is divisible by Y" if x % y == 0 else "X is not divisible by Y")
