# 12_physics/02_unif.py
def s_gen(a, v0):
    return lambda t: v0 * t + 0.5 * a * t**2
  
s = s_gen(10, 0)
t = 0
while s(t) < 20:
  t += 0.1
print(t, s(t))
