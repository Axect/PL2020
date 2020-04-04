class Fib:
    def __init__(self, a, b):
        self.curr = a
        self.next = b

    def iter(self):
        temp = self.curr + self.next
        self.curr = self.next
        self.next = temp

    def pick(self):
        return self.curr

    def __str__(self):
        return "{}, {}".format(self.curr, self.next)

f = Fib(1, 1)
for _i in range(99):
    f.iter()

print(f.pick())
