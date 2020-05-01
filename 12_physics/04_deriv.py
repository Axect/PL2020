# 12_physics/04_deriv.py
import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self, f, h=1e-6):
        self.f = f
        self.h = h

    def __call__(self, x):
        return (self.f(x + self.h) - self.f(x)) / self.h

def f(x):
    return x**2 + 2*x

df = Derivative(f)
x = np.arange(-2, 2, 0.1)

plt.figure(figsize=(10, 6), dpi=150)
plt.plot(x, f(x), label='f')
plt.plot(x, df(x), label='df')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.legend()
plt.grid()
plt.savefig("deriv.png")
