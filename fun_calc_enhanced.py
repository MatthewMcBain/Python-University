# Simple calculator using functions

def choose_integer(output):
    integer_valid = False

    while integer_valid is False:
        try:
            integer = int(input(output))
            integer_valid = True

        except ValueError:
            print("You need to enter an integer")

    return integer


def add(int1, int2):
    print(int1, "+", int2, "=", int1 + int2)


def subtract(int1, int2):
    print(int1, "-", int2, "=", int1 - int2)


def multiply(int1, int2):
    print(int1, "*", int2, "=", int1 * int2)


def divide(int1, int2):
    try:
        print(int1, "/", int2, "=", int1 // int2)

    except ZeroDivisionError:
        print("Divisor cannot be zero")


def remainder(int1, int2):
    try:
        print(int1, "%", int2, "=", int1 % int2)

    except ZeroDivisionError:
        print("Divisor cannot be zero")


integer1 = choose_integer("Enter integer 1: ")
integer2 = choose_integer("Enter integer 2: ")
print("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Remainder")
operation = choose_integer("Select option: ")

while not (1 <= operation <= 5):
    print("Value needs to be between 1 and 5")
    operation = choose_integer("Select option: ")

if operation == 1:
    add(integer1, integer2)
elif operation == 2:
    subtract(integer1, integer2)
elif operation == 3:
    multiply(integer1, integer2)
elif operation == 4:
    divide(integer1, integer2)
elif operation == 5:
    remainder(integer1, integer2)
else:
    print("Invalid operator")
