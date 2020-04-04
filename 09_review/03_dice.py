from random import randint
import matplotlib.pyplot as plt

# 주사위 한 번 던지기
def roll():
    return randint(1, 6)

# 주사위 n 번 던지기
def roll_and_roll(n):
    a = []
    for _i in range(n):
        a.append(roll())
    return a

# lst(배열)에 3이 몇 개 있는지 세기
def count(lst):
    c = 0
    for x in lst:
        if x == 3:
            c += 1
    return c

# 1번 : 주사위 10번 던졌을 때 3이 몇 번 나오는가
lst1 = roll_and_roll(10)
print(count(lst1) / 10)

# 2번 : 주사위 100번 던졌을 때 3이 몇 번 나오는가
lst2 = roll_and_roll(100)
print(count(lst2) / 100)

# 3번 : 주사위 10000번 던졌을 때 3이 몇 번 나오는가
lst3 = roll_and_roll(10000)
print(count(lst3) / 10000)

# 4번 : 10000번까지 다 기록하고 그림 그리기
c = 0
n = 0
ns = []
ps = []
for x in lst3:
    n += 1
    if x == 3:
        c += 1
    ns.append(n)
    ps.append(c / n)

plt.figure(figsize=(10, 6), dpi=300)
plt.title("Monte Carlo Simulation")
plt.xlabel("n")
plt.ylabel("p")
plt.plot(ns, ps)
plt.grid()
plt.savefig("dice.png")
