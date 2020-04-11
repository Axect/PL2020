from random import randint
from math import sqrt

def main():
    # 이차함수 만들기
    (a, b, c) = gen_quad()
    q = Quad(a, b, c)

    # 축 알려주기
    ax = q.axis
    print("축:", ax)

    # p값 입력받기
    p = int(input('>'))

    # 근 찾기
    if p >= ax:
        if q(p) >= 0:
            direc = -1
        else:
            direc = 1
    else:
        if q(p) >= 0:
            direc = 1
        else:
            direc = -1

    move(q, p, 1, direc)

def gen_quad():
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 10)
    if D(a,b,c) < 0:
        return gen_quad()
    return (a, b, c)

def D(a, b, c):
    return b ** 2 - 4 * a * c

#def quad(a, b, c):
#    return lambda x: a*x**2 + b*x + c

class Quad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.axis = - b / (2*a)

    def __str__(self):
        return "{}x^2 + {}x + {}".format(self.a, self.b, self.c)

    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c

    def print_root(self):
        a = self.a
        b = self.b
        c = self.c
        x1 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        print(x1, x2)

def move(q, p, step, direc):
    if step < 1e-15:
        print("근은 대충 {}입니다.".format(p))
        q.print_root()
        exit(1)
    if p >= q.axis:
        if q(p) > 0:
            next_direc = -1
            if direc * next_direc < 0:
                step /= 10
            return move(q, p-step, step, next_direc)
        elif q(p) < 0:
            next_direc = 1
            if direc * next_direc < 0:
                step /= 10
            return move(q, p+step, step, next_direc)
        else:
            print("근은 {}입니다.".format(p))
            q.print_root()
            exit(1)
    else:
        if q(p) > 0:
            next_direc = 1
            if direc * next_direc < 0:
                step /= 10
            return move(q, p+step, step, next_direc)
        elif q(p) < 0:
            next_direc = -1
            if direc * next_direc < 0:
                step /= 10
            return move(q, p-step, step, next_direc)
        else:
            print("근은 {}입니다.".format(p))
            q.print_root()
            exit(1)

if __name__=="__main__":
    main()
