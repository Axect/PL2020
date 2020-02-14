from math import sqrt

class Quad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
  
    def D(self):
    	return self.b**2 - 4*self.a*self.c
  
    def root(self):
    	D = self.D()
    	(a, b, c) = (self.a, self.b, self.c)
    	if D > 0:
      	    return ((-b + sqrt(D)) / (2*a), (-b - sqrt(D)) / (2*a))
    	elif D == 0:
      	    return -b / (2*a)
    	else:
      	    return "No root"
  
    def print_root(self):
    	print(self.root())

q1 = Quad(1,2,3)
q2 = Quad(1,2,1)
q3 = Quad(1,2,-1)

q1.print_root()
q2.print_root()
q3.print_root()
