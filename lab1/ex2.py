import cs50


def factorial(num):
    if num < 0:
        return "error, factorial only for positive numbers"
    if num == 0:
        return 1
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


print(factorial(cs50.get_int("Provide number to factorialize: ")))
