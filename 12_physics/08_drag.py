# 12_physics/07_drag.py
from phys import Phys1D

def a(p):
    return -10 + 0.1 * p.v**2

ball = Phys1D(20, 0, a, 1e-6)
while ball.x >= 0:
    ball.update()
    print("{:.6f}\t{:.6f}\t{:.6f}".format(ball.x, ball.v, ball.t))
