# 12_physics/06_grav.py
from phys import Phys1D

def a(p):
    return -10

ball = Phys1D(20, 0, a, 1e-3)
while ball.x > 0:
    ball.update()
print(ball.x, ball.t)
