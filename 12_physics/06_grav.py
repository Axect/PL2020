# 12_physics/06_grav.py
from phys import Phys1D

def a(p):
    return -10

ball = Phys1D(20, 0, a)
while ball.x > 0:
    ball.update()
    print("{:.6f}\t{:.6f}\t{:.6f}".format(ball.x, ball.v, ball.t))
