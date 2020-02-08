class Character:
    def __init__(self, kind):
        if kind == "Warrior":
            self.HP = 10
            self.ATK = 2
            self.DEF = 1
            self.INT = 0
        elif kind == "Thief":
            self.HP = 5
            self.ATK = 3
            self.DEF = 0
            self.INT = 1

    def attack(self, enemy):
        damage = self.ATK - enemy.DEF
        enemy.HP -= damage

    def is_alive(self):
        return self.HP > 0

sb = Character("Thief")
dg = Character("Warrior")

while sb.is_alive():
    sb.attack(dg)
    dg.attack(sb)
    print("HP: SB {}, DG {}".format(str(sb.HP), str(dg.HP)))
    print()
