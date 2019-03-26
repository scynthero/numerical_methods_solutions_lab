import cs50
import math
print("if you don't supply correct type (float), the program will ask again")
x = cs50.get_float("x: ")
y = cs50.get_float("y: ")
print("Perimeter of first circle is {:.4f}, and it's field is {:.4f}. "
      "Perimeter of second circle is {:.4f}, and it's field is {:.4f}."
      .format(2 * math.pi * x, math.pi * x ** 2, 2 * math.pi * y, math.pi * y ** 2))
