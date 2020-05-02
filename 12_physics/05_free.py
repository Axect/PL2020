# 12_physics/05_free.py
from phys import Phys1D

def a(p):
    return 0

ball = Phys1D(0, 20, a, 1e-3)
while ball.t < 3:
    ball.update()
    print("{:.6f}\t{:.6f}\t{:.6f}".format(ball.x, ball.v, ball.t))
print(ball.x)
