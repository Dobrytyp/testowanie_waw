def add(x, y):
    return x+y


def product(x, y):
    return x * y


def kwadrat(a):
    return a*a

import math

def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot by negative")
    if type(r) not in [int, float]:
        raise TypeError("The radius be a non-negative real numbers")

    return math.pi*r**2



