from math import inf


def divide(first, second):
    result = 0
    if second == 0:
        result = inf
    else:
        result = first / second
    return result