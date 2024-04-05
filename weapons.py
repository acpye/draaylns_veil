class Weapon:
    def __init__(self, name, damage=0, procCoefficient=0, staminaConsumption=0, stun=False, poison=False, bleed=False):
        self.name = name
        self.damage = damage
        self.procCoefficient = procCoefficient
        self.staminaConsumption = staminaConsumption

weaponsList = [
    Weapon(name="Greatsword", damage=0, procCoefficient=0, staminaConsumption=0),
    Weapon(name="Hammer", damage=0, procCoefficient=0, staminaConsumption=0, stun=True),
    Weapon(name="Battleaxe", damage=0, procCoefficient=0, staminaConsumption=0),
    Weapon(name="Morning Star", damage=0, procCoefficient=0, staminaConsumption=0),
    Weapon(name="Sword", damage=0, procCoefficient=0, staminaConsumption=0),
    Weapon(name="Katana", damage=0, procCoefficient=0, staminaConsumption=0, bleed=True),
    Weapon(name="Quarterstaff", damage=0, procCoefficient=0, staminaConsumption=0),
    Weapon(name="Club", damage=0, procCoefficient=0, staminaConsumption=0, stun=True),
    Weapon(name="Dagger", damage=0, procCoefficient=0, staminaConsumption=0, bleed=True),
    Weapon(name="Poison-Tipped Dagger", damage=0, procCoefficient=0, staminaConsumption=0, poison=True),
    Weapon(name="Hook", damage=0, procCoefficient=0, staminaConsumption=0, bleed=True)
]

# procCoefficient is there for things like poison or stuns








