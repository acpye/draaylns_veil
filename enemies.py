import weapons
class Enemy:
    def __init__(self, name, ally=False, attack=0, hitpoints=0, damageRoll=0, stamina=0, staminaRecovery=0, procCoefficient=0, staminaConsumption=0, stun=False, poison=False, bleed=False, weapon="Fists"):
        self.name = name
        self.ally = ally
        self.attack = attack
        self.procCoefficient = procCoefficient
        self.staminaConsumption = staminaConsumption
        self.stun = stun
        self.poison = poison
        self.bleed = bleed
        self.hitpoints = hitpoints
        self.maxHitpoints = hitpoints
        self.damageRoll= damageRoll
        self.stun = stun
        self.bleed = bleed
        self.poison = poison
        self.weapon = weapons.weaponsList[weapon]
        self.stamina = stamina
        self.maxStamina = self.stamina
        self.staminaRecovery = staminaRecovery

enemyList = {
    "Goblin": Enemy(name="Goblin", hitpoints=40, attack=1, stamina=6, staminaRecovery=1),  
}
