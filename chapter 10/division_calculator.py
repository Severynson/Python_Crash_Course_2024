def divide(divided, divisor):
    "Divide a number provided in the first argument per number in a second argument."
    try:
        print(divided / divisor)
    except ZeroDivisionError:
        print("You can not divided by zero")


divide(4, 2)
divide(100, 0)
