# 12_physics/phys.py
class Phys1D:
    def __init__(self, x, v, f, h=1e-6):
        self.x = x      # Value
        self.v = v      # Value
        self.accel = f  # Function
        self.t = 0      # Value
        self.a = 0      # Value
        self.h = h      # Value

    def calc_accel(self):
        self.a = self.accel(self)

    def update(self):
        self.calc_accel()
        self.x += self.v * self.h
        self.v += self.a * self.h
        self.t += self.h
