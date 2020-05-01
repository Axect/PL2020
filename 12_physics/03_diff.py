# 12_physics/03_diff.py
def diff(f, a, h=1e-6):
    return (f(a+h) - f(a)) / h

def f(x):
    return x**2 + 2*x
  
print(diff(f, 1))
print(diff(f, 1, 1e-8))
print(diff(f, 1, 1e-15))
