import cs50
print("if you don't supply correct type (int), the program will ask again")
x = cs50.get_float("x: ")
y = cs50.get_float("y: ")
while( y == 0):
    print("can't divide by zero")
    y = cs50.get_float("y: ")

print("X is divisible by Y and result is {:.2f}".format((x / y)+0 ) if x % y == 0 else "X is not divisible by Y")
