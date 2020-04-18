from math import trunc

def a(n):
    if n == 1:
        return 91
    elif n % 2 == 0:
        return a(n-1) + 1
    else:
        return trunc(a(n-1) / 2)

# 1. a_6 = ?
print(a(6))

# 2.
n = 1
while True:
    if a(n) == 1:
        break
    n += 1
print(n)

# 3. S_n
m = 1
s = 0
while True:
    b = a(m)
    if b == 1:
        s += b
        break
    s += b
    m += 1
print(s)

