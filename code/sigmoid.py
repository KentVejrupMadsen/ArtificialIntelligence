from math import e, pow


def __one():
    return float(1)


def __sigmoid_expo(x):
    return pow(e, x)


def __calc_exponent(x, moveX, xLimit):
    ix = -x

    return ix * xLimit + moveX


def __sigmoid_upper():
    return __one()


def __sigmoid_bottom(x, moveX, xLimit):
    value = __one() + __sigmoid_expo(__calc_exponent(float(x), float(moveX), float(xLimit)))
    return float( value )


def sigmoid(x, y_limit=1.0, x_limit=1.0, moveX = 0.0, moveY=0.0):
    return (__sigmoid_upper()/(__sigmoid_bottom(x, moveX, x_limit))) * y_limit + moveY
