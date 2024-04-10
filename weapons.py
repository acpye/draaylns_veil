class Weapon:
    def __init__(self, name, damage=0, damageRoll=0, procCoefficient=0, staminaConsumption=0, stun=False, poison=False, bleed=False):
        self.name = name
        self.damage = damage
        self.procCoefficient = procCoefficient
        self.staminaConsumption = staminaConsumption
        self.stun = stun
        self.poison = poison
        self.bleed = bleed

weaponsList = {
    "Greatsword": Weapon(name = "Greatsword", damage=10, damageRoll=6, procCoefficient=0, staminaConsumption=5),
    "Battleaxe": Weapon(name="Battleaxe", damage=8, damageRoll=6, procCoefficient=0, staminaConsumption=4),
    "Hammer": Weapon(name="Hammer", damage=7, damageRoll=4, procCoefficient=0, staminaConsumption=4, stun=True),
    "Morning Star": Weapon(name="Morning Star", damage=7, damageRoll=7, procCoefficient=0, staminaConsumption=4),
    "Sword": Weapon(name="Sword", damage=6, damageRoll=5, procCoefficient=0, staminaConsumption=3),
    "Katana": Weapon(name="Katana", damage=5, damageRoll=3, procCoefficient=0, staminaConsumption=3, bleed=True),
    "Quaterstaff": Weapon(name="Quarterstaff", damage=5, damageRoll=6, procCoefficient=0, staminaConsumption=3),
    "Club": Weapon(name="Club", damage=4, damageRoll=4, procCoefficient=0, staminaConsumption=3, stun=True),
    "Dagger": Weapon(name="Dagger", damage=3, damageRoll=2, procCoefficient=0, staminaConsumption=2, bleed=True),
    "Poison-Tipped Dagger": Weapon(name="Poison-Tipped Dagger", damage=0, damageRoll=2, procCoefficient=0, staminaConsumption=1, poison=True),
    "Hook": Weapon(name="Hook", damage=0, damageRoll=2, procCoefficient=0, staminaConsumption=2, bleed=True),   
}
