import numpy as np
from math import pi
import matplotlib.pyplot as plt

def polar(theta):
    x = np.cos(theta)
    y = np.sin(theta)
    return (x, y)

def circle(r):
    theta = np.arange(0, 2*pi+0.01, 0.01)
    (x, y) = polar(theta)
    x = r * x
    y = r * y
    return (x, y)

(x, y) = circle(1)

plt.figure(figsize=(10, 10), dpi=300)
plt.title("Circle plot", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.plot(x,y)
plt.savefig("circle.png")
