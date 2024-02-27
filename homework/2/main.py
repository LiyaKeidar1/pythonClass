


def isSumIn(list: list[int], num: int):
    xs = list.copy()
    sum = 0
    while len(xs) > 1:
        for x in xs:
            sum = xs[-1] + x
            if sum == num:
                return True
            if sum > num:
                continue
        xs.pop()
    return False

# decoratetor takes two parameters, type of parameters of function,
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


def paramsValidator(*val):
    def inside(func):
        def inner_func(*args):
            answer = False
            for i in range(len(val)):

                if val[i] is None:
                    answer = True
                    continue

                elif (type(val[i][0]) == type(args[i])\
                        or val[i][0] is None\
                        or (type(val[i][0]) == tuple and type(args[i]) in val[i][0])):
                    if ((args[i] > val[i][1] or val[i][1] is None)\
                            and (args[i] <val[i][2] or val[i][2] is None)):
                        answer = True
                        continue
                return answer
            return func(*args)
        return inner_func
    return inside




@paramsValidator((int, -20, 20), ((int, float), None, 30), None)
def drawPoint(x, y, cnt):
    pass



print(drawPoint(10, 14, 0))


@decorator(int, -1)
def lol(a, b):
    return a+b







def sumList(xs: list):
    sum = 0
    for x in xs:
        if isinstance(x, int):
            sum += x

        elif isinstance(x, tuple) or isinstance(x, set) or isinstance(x,list):
            sum += sumList(x)
    return sum


# print(sumList((1,2,(3,4,{5,6}),[7, 8], 9, 10)))