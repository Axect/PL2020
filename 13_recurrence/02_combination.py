def a(n,r):
    if r == 0:
        return 1
    else:
        return (n - (r-1)) / r * a(n,r-1)

print(a(10, 3))
