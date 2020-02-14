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

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(
                self.real * other.real - self.imag * other.imag, 
                self.real * other.imag + self.imag * other.real
        )

z1 = Complex(1, 2)
z2 = Complex(2, -3)
print(z1 + z2)
print(z1 - z2)
print(z1 * z2)
