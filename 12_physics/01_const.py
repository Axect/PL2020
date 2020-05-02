# 12_physics/01_const.py
def s_gen(v0):
    return lambda t: v0 * t
  
s = s_gen(20)
print(s(3))