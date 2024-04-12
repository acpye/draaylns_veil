import weapons
class Enemy:
    def __init__(self, name, ally=False, attack=0, hitpoints=0, stamina=0, staminaRecovery=0, weapon="Fists"):
        self.name = name
        self.ally = ally
        self.attack = attack
        self.hitpoints = hitpoints
        self.maxHitpoints = hitpoints
        self.weapon = weapons.weaponsList[weapon]
        self.stamina = stamina
        self.maxStamina = self.stamina
        self.staminaRecovery = staminaRecovery

class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", attack=1, hitpoints=25, stamina=18)

class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", attack=15, hitpoints=100, stamina=20)
        
