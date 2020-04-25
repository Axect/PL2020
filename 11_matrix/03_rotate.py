import numpy as np
from math import pi, cos, sin

def rotate(n):
    rad = n * pi / 180
    a = np.zeros((2, 2))
    a[0,0] = cos(rad)
    a[0,1] = -sin(rad)
    a[1,0] = sin(rad)
    a[1,1] = cos(rad)
    return a

a = rotate(30)
b = np.matrix("1;0")

for i in range(1, 13):
    print("{}번째 회전".format(i))
    b = a * b
    print(b)

