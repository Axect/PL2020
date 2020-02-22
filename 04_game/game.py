from random import randint
from enum import Enum
from time import sleep
from sys import exit

class Job(Enum):
    Thief = 1
    Warrior = 2

class Player:
    def __init__(self, name, job):
        self.name = name
        if job == Job.Thief:
            self.HP = 3
            self.ATK = 3
            self.DEF = 0
            self.DEX = 6
            self.CRI = 3
        elif job == Job.Warrior:
            self.HP = 5
            self.ATK = 2
            self.DEF = 1
            self.DEX = 1
            self.CRI = 3

    def __str__(self):
        return "NAME: {}\nHP: {}".format(self.name, self.HP)

    def attack(self, enemy):
        if self.is_dead():
            print("{} Win!".format(enemy.name))
            exit(1)
        print("{} attack {}".format(self.name, enemy.name))
        lucky1 = randint(1, 10)
        damage = self.ATK
        if lucky1 <= self.CRI:
            print("Critical!")
            damage *= 1.5
        lucky2 = randint(1, 10)
        if lucky2 <= enemy.DEX:
            print("Miss!")
        else:
            total_damage = damage - enemy.DEF
            enemy.HP -= total_damage
            print()

    def is_dead(self):
        return self.HP <= 0

CW = Player("찬우", Job.Thief)
SB = Player("승범", Job.Warrior)

coin = randint(1, 2)
if coin == 1:
    for i in range(10):
        print("=======================================")
        print("찬우 차례")
        sleep(1)
        CW.attack(SB)
        sleep(1)
        print("승범 차례")
        sleep(1)
        SB.attack(CW)
        sleep(1)
        print()
        print("찬우의 상태:")
        print(CW)
        print("승범의 상태:")
        print(SB)
        print("=======================================")
        sleep(2)
else:
    for i in range(10):
        print("=======================================")
        print("승범 차례")
        sleep(1)
        SB.attack(CW)
        sleep(1)
        print("찬우 차례")
        sleep(1)
        CW.attack(SB)
        sleep(1)
        print()
        print("찬우의 상태:")
        print(CW)
        print("승범의 상태:")
        print(SB)
        print("=======================================")
        sleep(2)
