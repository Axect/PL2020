class Rational:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        self.simplify()

    def __str__(self):
        num = self.num
        denom = self.denom
        if self.num < 0 and self.denom < 0:
            num = abs(num)
            denom = abs(denom)
        elif self.num < 0:
            pass
        elif self.denom < 0:
            num = -num
            denom = abs(denom)
        else:
            pass
        return "{}/{}".format(num, denom)

    def __add__(self, other):
        r = Rational(1,1)
        denom1 = abs(self.denom)
        denom2 = abs(other.denom)
        g = gcd(denom1, denom2)
        q1 = int(self.denom / g)
        q2 = int(other.denom / g)
        r.denom = g * q1 * q2
        r.num = self.num * q2 + other.num * q1
        r.simplify()
        return r

    def __sub__(self, other):
        temp = Rational(-other.num, other.denom)
        return self + temp
    
    def __mul__(self, other):
        r = Rational(1, 1)
        r.num = self.num * other.num
        r.denom = self.denom * other.denom
        r.simplify()
        return r

    def __truediv__(self, other):
        temp = Rational(other.denom, other.num)
        return self * temp

    def __pow__(self, n):
        return Rational(self.num ** n, self.denom ** n)

    def simplify(self):
        num = abs(self.num)
        denom = abs(self.denom)
        g = gcd(num, denom)
        if g == 1:
            pass
        else:
            self.num = int(self.num / g)
            self.denom = int(self.denom / g)

# 유클리드 호제법
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

r1 = Rational(1, 3)
r2 = Rational(2, 5)
print("r1", r1)
print("r2", r2)
print()

print("r1+r2=", r1 + r2)
print("r1-r2=", r1 - r2)
print("r1*r2=", r1 * r2)
print("r1/r2=", r1 / r2)
print("r1**2=", r1 ** 2)
