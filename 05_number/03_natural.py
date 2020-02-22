# Number/03_natural.py
# You should write Successor, One before natural number
class Successor:
    def __init__(self, n):
        self.prev = n

    def unwrap(self):
        return self.prev

    def __str__(self):
        if self.prev == None:
            return "1"
        else:
            return "Successor(" + str(self.prev) + ")"

class OneIsNotSuccessor(Exception):
    def __str__(self):
        return "One is not successor"

class One(Successor):
    def __init__(self):
        self.prev = None

    def unwrap(self):
        raise OneIsNotSuccessor()

    def __str__(self):
        return "1"

class NegativeOrZero(Exception):
    def __str__(self):
        return "Natural number is not negative or zero"

def natural(n):
    if n <= 0:
        raise NegativeOrZero()
    elif n == 1:
        return One()
    else:
        result = One()
        for _i in range(n-1):
            result = Successor(result)
        return result

a = natural(10)
print(a)
