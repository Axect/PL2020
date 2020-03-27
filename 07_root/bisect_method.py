from enum import Enum
from math import sin, cos, tan, log

class Root(Enum):
    Exist = 1
    Fail = 2
    Exact = 3

def is_exist(f, a, b):
    if f(a) * f(b) < 0:
        return Root.Exist
    elif f(a) * f(b) > 0:
        return Root.Fail
    else:
        return Root.Exact

def bisect(f, a, b):
    if abs(b - a) < 1e-7:
        return (a + b) / 2
    ex = is_exist(f, a, b)
    if ex == Root.Fail:
        print("근을 찾지 못하였습니다.")
        exit(1)
    elif ex == Root.Exact:
        if f(a) == 0:
            return a
        else:
            return b
    else:
        c = (a + b) / 2
        ex_a = is_exist(f, a, c)
        ex_b = is_exist(f, c, b)
        if ex_a == Root.Exact and ex_b == Root.Exact:
            return c
        elif ex_a == Root.Exist:
            return bisect(f, a, c)
        else:
            return bisect(f, c, b)
