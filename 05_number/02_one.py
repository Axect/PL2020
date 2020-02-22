# Number/02_one.py
# You should write Successor before write One
class Successor:
    def __init__(self, n):
        self.prev = n

    def unwrap(self):
        return self.prev

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

a = One()
print(a)
a.unwrap()
print(1+1)
