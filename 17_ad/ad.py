import math

class Dual:
    def __init__(self, x, dx):
        self.x = x
        self.dx = dx

    def __str__(self):
        return "Dual({}, {})".format(self.x, self.dx)

    def __add__(self, other):
        result = Dual(0, 0)
        if isinstance(other, Dual):
            result.x = self.x + other.x
            result.dx = self.dx + other.dx
        else:
            result.x = self.x + other
            result.dx = self.dx
        return result

    def __sub__(self, other):
        result = Dual(0, 0)
        if isinstance(other, Dual):
            result.x = self.x - other.x
            result.dx = self.dx - other.dx
        else:
            result.x = self.x - other
            result.dx = self.dx
        return result

    def __mul__(self, other):
        result = Dual(0, 0)
        if isinstance(other, Dual):
            result.x = self.x * other.x
            result.dx = self.x * other.dx + self.dx * other.x
        else:
            result.x = self.x * other
            result.dx = self.dx * other
        return result


def sin(f):
    if isinstance(f, Dual):
        result = Dual(0,0)
        result.x = math.sin(f.x)
        result.dx = math.cos(f.x) * f.dx
        return result
    else:
        return math.sin(f)


a = Dual(2, 1)
b = Dual(2, 1)

print(sin(sin(sin(sin(sin(a))))))
