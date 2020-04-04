def a(n):
    return 3 * n - 1

def s(n, a):
    s = 0
    for i in range(1,n+1):
        s += a(i)
    return s

print(a(79))
print(s(79, a))

def b(n):
    if n == 1:
        return 2
    else:
        return 2 * b(n-1) - 1

print(b(14))
print(s(14, b))
