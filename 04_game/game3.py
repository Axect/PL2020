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
            enemy.defense(self)
    
    def defense(self, enemy):
        damage = damage_calc(enemy.TMP, self.DEF)
        chance2 = randint(1, 10)
        if chance2 <= self.DEX:
            sleep(1)
            print("특수 방어 발동!")
            self.special_defense(enemy)
        else:
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
        input()
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
        self.TMP = self.ATK

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
# Thief
# ==============================================================================
class Thief(Player):
    def __init__(self, name):
        self.name = name
        self.HP = 5
        self.ATK = 3
        self.DEF = 1
        self.DEX = 7
        self.CRI = 3
        self.TMP = self.ATK

    def __str__(self):
        return "NAME: {}, JOB: Thief\nHP: {}".format(self.name, self.HP)

    def special_attack(self, enemy):
        if enemy.ATK > 1:
            enemy.ATK -= 1
            self.ATK += 1
            self.TMP = self.ATK
            print("""
                무기 압수! : {}의 공격력을 1만큼 갈취합니다.
                {}의 현재 공격력: {}
                {}의 현재 공격력: {}
                """.format(enemy.name, enemy.name, enemy.ATK, self.name, self.ATK)
            )
        else:
            enemy.HP -= 1
            self.ATK += 1
            self.TMP = self.ATK
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

class Magician(Player):
    def __init__(self, name, element):
        self.name = name
        self.elem = element
        self.HP = 5
        self.MP = 10
        self.DEF = 0
        self.CRI = 9
        self.DEX = 4
        self.SK1 = 6 # Default Skill
        self.SK2 = 3 # Second Skill
        self.SK3 = 1 # Ultimate Skill
        self.ATK = 0
        self.DMG = 2
        self.TMP = self.DMG
        if self.elem == Element.Ice:
            self.COLD = 0

    def __str__(self):
        return "NAME: {}, JOB: Magician({})\nHP: {}, MP: {}".format(self.name, str(self.elem.name), self.HP, self.MP)

    def recovery(self):
        self.MP += 2
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

    def defense_normal(self, enemy):
        damage = damage_calc(enemy.TMP, self.DEF)
        if damage <= self.MP:
            print("데미지를 MP로 상쇄합니다.")
            self.MP -= damage
        else:
            print("데미지를 MP로 상쇄합니다.")
            (damage, self.MP) = (damage - self.MP, 0)
            self.HP -= damage

    def defense(self, enemy):
        chance2 = randint(1, 10)
        if chance2 <= self.DEX:
            sleep(1)
            print("특수방어 발동!")
            self.special_defense(enemy)
        else:
            self.defense_normal(enemy)

    def special_attack(self, enemy):
        skill = randint(1, 10)
        # ==============================================================================
        # Fire Magician
        # ==============================================================================
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
                    enemy.HP -= 1
                    self.MP -= 1
                    print("""
                    폭죽 쏘기! : 마나 1을 소모하여 고정데미지 {}와 화상데미지 1을 입힙니다.
                    현재 마력: {}
                    """.format(damage, self.MP))
                    self.TMP = damage
                    enemy.defense(self)
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
        # ==============================================================================
        # Ice Magician
        # ==============================================================================
        elif self.elem == Element.Ice:
            if self.COLD >= 10:
                print("""
                추위가 극에 달했습니다.
                {}의 머리가 띵해지면서 2턴 동안 움직이지 못합니다.
                2턴 동안 들어가는 모든 공격은 특수 공격이 됩니다.
                적의 민첩이 1 하락합니다.
                """.format(enemy.name))
                enemy.DEX -= 1
                self.COLD -= 5
                sleep(1)
                self.special_attack(enemy)
                sleep(1)
                self.special_attack(enemy)
            elif skill <= self.SK1:
                if self.MP < 1:
                    print("""
                    고드름을 준비하기 위한 마력이 부족합니다!
                    마나를 회복합니다.
                    """)
                    self.recovery()
                else:
                    damage = 1 if self.COLD < 4 else 2
                    self.MP -= 1
                    self.COLD += 2
                    print("""
                    고드름 쏘기! : 마나 1을 소모하여 방어무시데미지 {}을 입힙니다.
                    날씨가 조금 추워집니다.
                    현재 마력: {}
                    현재 추위: {}
                    """.format(damage, self.MP, self.COLD))
                    self.TMP = damage + enemy.DEF
                    enemy.defense(self)
            elif skill <= self.SK1 + self.SK2:
                if self.MP < 2:
                    print("부장님이 개그를 치기 위한 마력이 부족합니다!")
                    self.recovery()
                else:
                    self.COLD *= 2
                    self.MP -= 1
                    print("""
                    부장님 개그! : 마나 1을 소모하여 부장님이 엄청난 개그를 구사합니다.
                    모두들 웃고 있지만 추위는 2배가 됩니다.
                    현재 추위: {}
                    """.format(self.COLD))
            else:
                if self.MP < 5:
                    print("얼음땡을 위한 마력이 부족합니다!")
                    self.recovery()
                else:
                    self.MP -= 5
                    damage = self.COLD * 2
                    print("""
                    얼음땡! : 현재 추위의 2배 만큼의 데미지를 가합니다.
                    데미지: {}
                    """.format(damage))
                    self.TMP = damage
                    enemy.defense(self)

    def special_defense(self, enemy):
        self.MP += damage_calc(enemy.TMP, self.DEF)
        print("""
        흡수 실드! : 데미지를 마나로 전환합니다.
        현재 마나: {}
        """.format(self.MP))

# ==============================================================================
# Hero
# ==============================================================================
class Item(Enum):
    DualBlade = 1
    Elixir = 2

class Hero(Player):
    def __init__(self, name):
        self.name = name
        self.HP = 6
        self.ATK = 1
        self.DEF = 1
        self.DEX = 9
        self.CRI = 2
        self.TMP = self.ATK
        # unique
        self.EXP = 0
        self.LEVEL = 1
        self.HPMAX = 6
        self.ATKMAX = 1
        self.DEFMAX = 1
        self.CRIMAX = 2
        self.DEXMAX = 3
        self.REQEXP = 3
        self.ITEM = None

    def __str__(self):
        return "NAME: {}, JOB: Hero\nHP: {}, LEVEL: {}, EXP: {}".format(self.name, self.HP, self.LEVEL, self.EXP)

    def level_up(self):
        print("""
            레벨업을 위한 경험치가 모두 준비되었습니다.
            상태이상과 체력이 모두 회복되며 랜덤으로 능력이 향상됩니다.
            LEVEL = {}""".format(self.LEVEL+1))
        stat = randint(1, 7)
        if stat == 1:
            self.HPMAX += 2
            print("""
            체력이 향상됩니다.
            현재 체력 : {}
            """.format(self.HPMAX))
        elif stat == 2:
            self.ATKMAX += 2
            print("""
            공격이 향상됩니다.
            현재 공격력 : {}
            """.format(self.ATKMAX))
        elif stat == 3:
            self.DEFMAX += 2
            print("""
            방어력이 향상됩니다.
            현재 방어력 :{}
            """.format(self.DEFMAX))
        elif stat == 4:
            self.CRIMAX += 1
            print("""
            특수공격 발동률이 향상됩니다.
            특수공격 발동률 : {}
            """.format(self.CRIMAX))
        elif stat == 5:
            self.DEXMAX += 1
            print("""
            회피율이 향상됩니다.
            현재 회피율 : {}
            """.format(self.DEXMAX))
        elif stat == 6:
            self.ITEM = Item.DualBlade
            print("""
            듀얼 블레이드를 획득하였습니다.
            이제 기본공격은 항상 두 번 발동합니다.
            """)
        else:
            self.ITEM = Item.Elixir
            print("""
            엘릭서를 획득하였습니다.
            이제 특수방어를 할 때 마다 체력이 모두 회복됩니다.
            """)
        self.HP = self.HPMAX
        self.ATK = self.ATKMAX
        self.DEF = self.DEFMAX
        self.CRI = self.CRIMAX
        self.DEX = self.DEXMAX
        self.EXP -= self.REQEXP
        self.TMP = self.ATK
        self.REQEXP += self.LEVEL
        sleep(1)
        self.LEVEL += 1

    def attack(self, enemy):
        self.EXP += 1
        if self.EXP >= self.REQEXP:
            self.level_up()
        self.TMP = self.ATK
        super().attack(enemy)
        if self.ITEM == Item.DualBlade:
            print("""
            듀얼 블레이드의 효과로 공격이 한번 더 발동됩니다.
            """)
            super().attack(enemy)

    def defense(self, enemy):
        self.EXP += 1
        super().defense(enemy)

    def special_attack(self, enemy):
        self.TMP *= self.LEVEL
        print("""
            주인공은 동료들의 힘을 받아 공격력의 {}배의 데미지를 줍니다.
            데미지: {}
            """.format(self.LEVEL, self.TMP)
        )
        enemy.defense(self)

    def special_defense(self, enemy):
        print("""
            주인공 보정으로 인해 주인공은 절대 맞지 않습니다.
            """)
        if self.ITEM == Item.Elixir:
            print("""
            엘릭서의 효과로 체력이 모두 회복됩니다.
            """)
            self.HP = self.HPMAX

# ==============================================================================
# Play!
# ==============================================================================
p1 = Hero("A")
p2 = Magician("B", Element.Fire)

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
