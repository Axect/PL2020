class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"

z1 = Complex(1, 2)
z2 = Complex(1, 0)
z3 = Complex(0, 1)
z4 = Complex(1, -2)

print(z1)
print(z2)
print(z3)
print(z4)
