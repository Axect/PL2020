import numpy as np

# 행렬
a = np.matrix("1 2; 3 4")
print(a)

print(a[0,0])
print(a[0,1])
print(a[1,0])
print(a[1,1])

for i in range(0, 2):
    for j in range(0, 2):
        print("{}행, {}열 = {}".format(i, j, a[i,j]))
