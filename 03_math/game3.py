import random
from random import randint
from enum import Enum
from time import sleep
from sys import exit
from os import system

def damage_calc(damage, DEF):
    if damage < DEF:
        return 0
    else:
        return damage - DEF

random.seed(None)



# ==============================================================================
# Player
# ==============================================================================
class Player:
    def __init__(self, name):
        self.name = name
        self.HP = 0
        self.ATK = 0
        self.DEF = 0
        self.CRI = 0
        self.DEX = 0

    def __str__(self):
        pass

    def attack(self, enemy):
        print("{}, {} 공격!".format(self.name, enemy.name))
        chance = randint(1, 10)
        if chance <= self.CRI:
            sleep(1)
            print("특수 공격 발동!")
            self.special_attack(enemy)
        else:
            chance2 = randint(1, 10)
            if chance2 <= enemy.DEX:
                sleep(1)
                print("특수 방어 발동!")
                enemy.special_defense(self)
            else:
                enemy.defense(self)
    
    def defense(self, enemy):
        damage = damage_calc(enemy.ATK, self.DEF)
        self.HP -= damage

    def special_attack(self, enemy):
        pass

    def special_defense(self, enemy):
        pass

    def is_dead(self):
        return self.HP <= 0

    def turn(self, enemy):
        system("clear")
        print("="*40)
        print("{}의 차례".format(self.name))
        sleep(1.5)
        self.attack(enemy)
        sleep(1)
        print("현재 상태는 다음과 같습니다.")
        print()
        print(self)
        print()
        print(enemy)
        if enemy.is_dead():
            print()
            print("{}는 사망하셨습니다.".format(enemy.name))
            print("{}의 승리!".format(self.name))
            exit(1)
        elif self.is_dead():
            print()
            print("{}는 사망하셨습니다.".format(self.name))
            print("{}의 승리!".format(enemy.name))
            exit(1)
        print("="*40)
        sleep(1.5)
# ==============================================================================
# Warrior
# ==============================================================================
class Warrior(Player):
    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.ATK = 3
        self.DEF = 2
        self.DEX = 4
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
        enemy.defense(self)

    def special_defense(self, enemy):
        self.DEF += 1
        print("""
            단단해져라! : {}의 방어력이 1만큼 상승합니다.
            현재 방어력: {}
            """.format(self.name, self.DEF)
        )
# ==============================================================================
# Theif
# ==============================================================================
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
            self.ATK += 1
            print("""
                신체포기각서 : {}의 공격력이 부족하므로 체력으로 대체합니다.
                {}의 현재 체력: {}
                {}의 현재 공격력: {}
                """.format(enemy.name, enemy.name, enemy.HP, self.name, self.ATK)
            )
        enemy.defense(self)

    def special_defense(self, enemy):
        print("""
            민첩한 회피! : {}가 회피합니다.
            """.format(self.name)
        )
# ==============================================================================
# Magician
# ==============================================================================
class Element(Enum):
    Fire = 1
    Ice = 2
    Chaos = 3

class Magician(Player):
    def __init__(self, name, element):
        self.name = name
        self.elem = element
        self.HP = 5
        self.MP = 10
        self.DEF = 0
        self.CRI = 9
        self.DEX = 5
        self.SK1 = 6 # Default Skill
        self.SK2 = 3 # Second Skill
        self.SK3 = 1 # Ultimate Skill
        self.ATK = 0
        self.DMG = 2

    def __str__(self):
        return "NAME: {}, JOB: Magician({})\nHP: {}, MP: {}".format(self.name, str(self.elem.name), self.HP, self.MP)

    def recovery(self):
        self.MP += 1
        print("마력을 회복합니다.\n현재 마력: {}".format(self.MP))

    def attack(self, enemy):
        print("{}, {} 공격!".format(self.name, enemy.name))
        chance = randint(1, 10)
        if chance <= self.CRI:
            sleep(1)
            print("특수 공격 발동!")
            self.special_attack(enemy)
        else:
            self.recovery()

    def defense(self, enemy):
        damage = damage_calc(enemy.ATK, self.DEF)
        if damage >= self.HP + self.MP:
            print("{}의 HP, MP가 부족합니다.".format(self.name))
            self.HP -= damage - self.MP
            self.MP = 0
        elif damage >= self.HP:
            print("{}의 HP가 부족하므로 MP로 일정부분 대체합니다.".format(self.name))
            damage -= (self.HP - 1)
            self.HP = 1
            self.MP -= damage
        else:
            self.HP -= damage

    def special_attack(self, enemy):
        skill = randint(1, 10)
        if self.elem == Element.Fire:
            if skill <= self.SK1:
                if self.MP < 1:
                    print("""
                    폭죽을 준비하기 위한 마력이 부족합니다!
                    마나를 회복합니다.
                    """)
                    self.recovery()
                else:
                    damage = self.DMG
                    enemy.HP -= damage_calc(damage, enemy.DEF)
                    enemy.HP -= 1
                    self.MP -= 1
                    print("""
                    폭죽 쏘기! : 마나 1을 소모하여 고정데미지 {}와 화상데미지 1을 입힙니다.
                    현재 마력: {}
                    """.format(damage, self.MP))
            elif skill <= self.SK1 + self.SK2:
                if self.MP < 2:
                    print("폭죽 개량을 위한 마력이 부족합니다!")
                    self.recovery()
                else:
                    self.DMG *= 2
                    self.MP -= 2
                    print("""
                    폭죽 개량! : 마나 2를 소모하여 폭죽을 2배 업그레이드 합니다.
                    폭죽의 현재 공격력: {}
                    """.format(self.DMG))
            else:
                if self.MP < 5:
                    print("여의도 불꽃축제를 위한 마력이 부족합니다!")
                    self.recovery()
                else:
                    self.MP -= 5
                    print("""
                    여의도 불꽃 축제 개최! : 상대방이 불꽃축제에 홀려 3턴동안 쉬게 됩니다.
                    """)
                    sleep(1)
                    self.attack(enemy)
                    sleep(1)
                    self.attack(enemy)
                    sleep(1)
                    self.attack(enemy)

    def special_defense(self, enemy):
        self.MP += enemy.ATK
        print("""
        흡수 실드! : 데미지를 마나로 전환합니다.
        현재 마나: {}
        """.format(self.MP))

p1 = Warrior("윤수")
p2 = Magician("동규", Element.Fire)

coin = randint(1, 2)
if coin == 1:
    pass   
else:
    (p1, p2) = (p2, p1)

system("clear")
print("게임을 시작합니다.")
sleep(2)

for i in range(100):
    p1.turn(p2)
    p2.turn(p1)
