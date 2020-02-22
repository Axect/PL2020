class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b

    def __str__(self):
        if self.imag >= 0:
            return str(self.real) + " + " + str(self.imag) + "i"
        else:
            return str(self.real) + " - " + str(-self.imag) + "i"

z = Complex(1, -3)
print(z)
