import math
import numpy as np
import matplotlib.pyplot as plt

# Automatic Differentiation
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

def cos(f):
    if isinstance(f, Dual):
        result = Dual(0,0)
        result.x = math.cos(f.x)
        result.dx = -math.sin(f.x) * f.dx
        return result
    else:
        return math.cos(f)

a = Dual(math.pi / 4, 1)
b = Dual(2, 1)

print(sin(a) * cos(a))  # There is no differentiation
# sin(pi/4) * cos(pi/4) = 1/2 * sin(pi / 2) = 1/2
# sin(a)cos(a) = 1/2 sin(2a) -> 1/2 cos(2a) * 2 = cos(pi/2) = 0

x = np.arange(0, 2*math.pi, 0.001)
f = np.sin(x)

def dsin(x):
    d = Dual(x, 1)
    s = sin(d) # (value, derivative)
    return s.dx

df = [dsin(t) for t in x]

plt.rc("text", usetex=True)
plt.rc("font", family="serif")

plt.figure(figsize=(10, 6), dpi=300)
plt.title(r"Automatic Differentiation of $\sin{x}$")
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.plot(x, f, label=r"$y = \sin{x}$")
plt.plot(x, df, label=r"$y = \frac{d}{dx} \sin{x}$")
plt.grid()
plt.legend()
plt.savefig("sin.png")
