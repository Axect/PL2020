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
        pass
    
    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __pow__(self, n):
        pass

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

r1 = Rational(1, 27)
r2 = Rational(2, 27)
print(r1)
print(r2)

print(r1 + r2)
