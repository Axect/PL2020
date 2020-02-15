# Math/01_positive_root.py
from math import sqrt

def positive_root(a, b, c):
    return (-b + sqrt(b**2 - 4*a*c)) / (2*a)
  
print(positive_root(1, 2, 1))
print(positive_root(1, 2, -3))
