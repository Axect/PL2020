from random import randint
from enum import Enum
from time import sleep
from sys import exit
from os import system

class Player:
    def __init__(self, name):
        self.name = name
        self.HP = 0

    def __str__(self):
        pass

    def attack(self, enemy):
        print("{}, {} 공격!".format(self.name, enemy.name))
        chance = randint(1, 10)
        if chance <= self.CRI:
            print("특수 공격 발동!")
            self.special_attack(enemy)
        else:
            chance2 = randint(1, 10)
            if chance2 <= enemy.DEX:
                print("특수 방어 발동!")
                enemy.special_defense(self)
            else:
                damage = self.ATK - enemy.DEF
                enemy.HP -= damage

    def special_attack(self, enemy):
        pass

    def special_defense(self, enemy):
        pass

    def is_dead(self):
        return self.HP <= 0

class Warrior(Player):
    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.ATK = 3
        self.DEF = 2
        self.DEX = 5
        self.CRI = 3

    def __str__(self):
        return "NAME: {}, JOB: Warrior\nHP: {}".format(self.name, self.HP)

    def special_attack(self, enemy):
        enemy.DEF -= 1
        print("""
            물렁해져라! : {}의 방어력이 1만큼 감소합니다.
            현재 방어력: {}
            """.format(enemy.name, enemy.DEF)
        )
        damage = self.ATK - enemy.DEF
        enemy.HP -= damage

    def special_defense(self, enemy):
        self.DEF += 1
        print("""
            단단해져라! : {}의 방어력이 1만큼 상승합니다.
            현재 방어력: {}
            """.format(self.name, self.DEF)
        )

class Thief(Player):
    def __init__(self, name):
        self.name = name
        self.HP = 5
        self.ATK = 3
        self.DEF = 1
        self.DEX = 8
        self.CRI = 3

    def __str__(self):
        return "NAME: {}, JOB: Thief\nHP: {}".format(self.name, self.HP)

    def special_attack(self, enemy):
        if enemy.ATK > 1:
            enemy.ATK -= 1
            self.ATK += 1
            print("""
                무기 압수! : {}의 공격력을 1만큼 갈취합니다.
                {}의 현재 공격력: {}
                {}의 현재 공격력: {}
                """.format(enemy.name, enemy.name, enemy.ATK, self.name, self.ATK)
            )
        else:
            enemy.HP -= 1
            self.HP += 1
            print("""
                신체포기각서 : {}의 공격력이 부족하므로 체력을 1만큼 갈취합니다.
                {}의 현재 체력: {}
                {}의 현재 체력: {}
                """.format(enemy.name, enemy.name, enemy.HP, self.name, self.HP)
            )
        damage = self.ATK - enemy.DEF
        enemy.HP -= damage

    def special_defense(self, enemy):
        print("""
            민첩한 회피! : {}가 회피합니다.
            """.format(self.name)
        )
################################################################
def turn(p1, p2):
    print("====================================================")
    print("{}의 차례".format(p1.name))
    sleep(2)
    p1.attack(p2)
    print("현재 상태")
    print()
    print(p1)
    print()
    print(p2)
    ####################################################
    if p2.is_dead():
        print("{}는 사망하셨습니다.".format(p2.name))
        print("{}의 승리!".format(p1.name))
        exit(1)
    ####################################################
    sleep(2)
    system("clear")
    print("====================================================")
    print("{}의 차례".format(p2.name))
    sleep(2)
    p2.attack(p1)
    print("현재 상태")
    print()
    print(p1)
    print()
    print(p2)
    ####################################################
    if p1.is_dead():
        print("{}는 사망하셨습니다.".format(p1.name))
        print("{}의 승리!".format(p2.name))
        exit(1)
    print("====================================================")
    sleep(2)
    system("clear")

p1 = Thief("윤수")
p2 = Warrior("동규")

coin = randint(1, 2)
if coin == 1:
    pass   
else:
    (p1, p2) = (p2, p1)

print("게임을 시작합니다.")

for i in range(100):
    turn(p1, p2)
