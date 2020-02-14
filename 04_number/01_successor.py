# Number/01_successor.py
class Successor:
    def __init__(self, n):
        self.prev = n

    def unwrap(self):
        return self.prev

    def __str__(self):
        return "Successor(" + str(self.prev) + ")"

a = Successor(1)
print(a)
print(a.unwrap())

b = Successor(a)
print(b)
print(b.unwrap().unwrap())
