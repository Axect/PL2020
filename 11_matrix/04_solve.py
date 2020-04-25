import numpy as np

a = np.matrix("2 -1; 1 1")
b = np.matrix("1;2")

x = np.linalg.inv(a) * b

print(x)

a2 = np.matrix("1 -1 2; 2 -1 -1; -1 2 -3")
b2 = np.matrix("2;3;-5")

x2 = np.linalg.inv(a2) * b2

print(x2)

a3 = np.matrix("1 1;2 2")
b3 = np.matrix("2;3")

x3 = np.linalg.inv(a3) * b3

print(x3)
