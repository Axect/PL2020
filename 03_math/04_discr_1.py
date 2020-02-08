# Math/04_discr_1.py
def D(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        print("서로 다른 두 실근")
    elif d == 0:
        print("중근")
    else:
        print("서로 다른 두 허근")
        
D(1,2,-3)
D(1,2,1)
D(1,2,3)
