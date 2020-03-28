from copy import deepcopy

class Polynomial:
    def __init__(self, coef):
        self.coef = coef

    def __str__(self):
        coef = self.coef
        l = len(coef)
        n = l-1
        
        # 첫번째
        result = ""
        tmp = term(n, coef[0])[3:]
        if coef[0] < 0:
            tmp = "-" + tmp
        result += tmp
        
        # 나머지
        for i in range(1, l):
            if coef[i] == 0:
                continue
            else:
                result += term(n-i, coef[i])

        if abs(coef[l-1]) == 1:
            result += "1"

        return result

    def __add__(self, other):
        coef1 = deepcopy(self.coef)
        coef2 = deepcopy(other.coef)

        coef1.reverse()
        coef2.reverse()

        coef3 = zip_with(lambda x, y: x + y, coef1, coef2)
        coef3.reverse()

        return Polynomial(coef3)

    def __sub__(self, other):
        other2 = Polynomial(list(map(lambda x: -x, other.coef)))
        return self + other2

    def __mul__(self, other):
        coef1 = self.coef
        coef2 = other.coef

        coef = []

        pass

def term(n, value):
    if value == 0:
        return None
    
    result = " "
    op = "+" if value > 0 else "-"
    result += op
    result += " "
    if abs(value) != 1:
        result += str(abs(value))
    if n == 1:
        result += "x"
    elif n == 0:
        pass
    else:
        result += "x^{}".format(n)
    return result

def zip_with(f, v1, v2):
    v = []
    for i in range(min(len(v1), len(v2))):
        v.append(f(v1[i],v2[i]))
    if len(v1) > len(v2):
        v += v1[len(v):]
    elif len(v2) > len(v1):
        v += v2[len(v):]
    return v
