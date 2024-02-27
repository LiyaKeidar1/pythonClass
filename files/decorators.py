# decorator that takes two parameters, type of parameters of function,
# and answer if the parameters of the function don't fit the type
def decorator(typee, defu):
    def inside(func):
        def inner_function(*args):
            for x in args:
                if isinstance(x, typee):
                    continue
                else:
                    return defu
            return func(*args)
        return inner_function
    return inside

@decorator(int, -1)
def lol(a, b):
    return a+b

def parmValidation(*restrictions):
    def callFunction(func):
        def inner(*parameters):
            for i in range(len(restrictions)):
                if restrictions[i] is None:
                    continue

                if restrictions[i][0] is not None and type(parameters[i]) is not restrictions[i][0]:
                    if type(restrictions[i][0]) is tuple and type(parameters[i]) not in restrictions[i][0]:
                        raise Exception(f"{parameters[i]}'s type is bad")
                    elif type(restrictions[i][0]) is not tuple:
                        raise Exception(f"{parameters[i]}'s type is bad")

                if restrictions[i][1] is not None and parameters[i] < restrictions[i][1]:
                    raise Exception(f"{parameters[i]} is out of range")

                if restrictions[i][2] is not None and parameters[i] > restrictions[i][2]:
                    raise Exception(f"{parameters[i]} is out of range")

            return func(*parameters)
        return inner
    return callFunction

@parmValidation((int, -20, 20), ((int, str), None, 20), None)
def drawPoint(x, y, cnt):
    print(f"Those are the coordinates: {x}, {y}")



print(drawPoint(10, 14, 0))




class NotANumber(Exception):
    def __init__(self):
        super().__init__("Not a Number")


    def __str__(self):
        return "Not a Number"
class BIsAZero(Exception):
    def __init__(self):
        super().__init__("Division by zero")

    def __str__(self):
        return "Division by zero"

def decoratorOfException(func):
    def inside(a, b):
        if b == 0:
            raise BIsAZero("b is zero")
        if type(a) != int or type(b) != int:
            raise NotANumber("those aren't numbers")
        func(a, b)

    return inside
@decoratorOfException
def divide(a, b):
    return a / b



