# a_n = a_{n-1} + 2, a_1 = 3
# a_n = 2n + 1

def a(n):
    if n == 1:
        return 3
    else:
        return a(n-1) + 2 # 재귀

print(a(3))
# a(3) = a(2) + 2
# a(2) = a(1) + 2
# a(1) = a(0) + 2
# a(0) = a(-1) + 2
# ...
