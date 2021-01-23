from functools import cache

def c(n, r):
    if r == 0 or n == r:
        return 1
    else:
        return c(n-1,r-1) + c(n-1,r)

@cache
def c_cache(n, r):
    if r == 0 or n == r:
        return 1
    else:
        return c_cache(n-1,r-1) + c_cache(n-1,r)


print(c_cache(300, 150))
#print(c(40, 10))
