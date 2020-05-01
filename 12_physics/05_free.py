# 12_physics/05_free.py
from phys import Phys1D

def a(p):
    return 0

ball = Phys1D(0, 20, a, 1e-3)
while ball.t < 3:
    ball.update()
print(ball.x)
