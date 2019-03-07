def factorial(num):
    if num < 0:
        return "error, factorial only for positive numbers"
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


print(factorial(int(input("Provide number to factorialize: "))))
