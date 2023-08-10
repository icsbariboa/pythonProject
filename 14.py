try:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    print(a / b)
except ZeroDivisionError as e:
    print("You tried to divide by zero, nu nu nu")
    print(e.args)
except ValueError as e:
    print("Bad input")
    print(e.args)
except BaseException as e:
    print(e.args)
print("aviel")
