from math import e, pow


def sigmoid(x, breath=1.0, depth=1.0, moveX = 0.0, moveY=0.0):

    value_upper = float(1.0)
    value_bottom = float(1.0) + float( pow(e, ( -x * depth + moveX ) ) )

    return ((float(value_upper)/float(value_bottom)) * breath) + moveY