class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b

    def __str__(self):
        if self.imag >= 0:
            return str(self.real) + " + " + str(self.imag) + "i"
        else:
            return str(self.real) + " - " + str(-self.imag) + "i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

z1 = Complex(1, 2)
z2 = Complex(2, -3)
z = z1 + z2
print(z)
