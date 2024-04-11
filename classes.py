import weapons
from health import HealthBar

class Barbarian(object):

    def __init__(self, name="Barbarian"):
        self.ally = True
        self.name = name
        self.info = "The Barbarian is a kilt-clad warrior hungry for destruction. Big damage and health numbers, little stamina."
        self.maxHitpoints = 115
        self.hitpoints = self.maxHitpoints
        self.defence = 0 # Armour value can override this
        self.strength = 0
        self.attack = 0 # If we set this to something low it can act as fists if player lacks weapon - weapon damage can just override this
        self.agility = 0
        self.evasion = 0 # Should stay relatively low by default with few skills that can affect - maybe armour can also affect?
        self.luck = 0 # will affect proc chance. affects chance of increased level up rewards? affects victory drop rates?
        self.skill = "Bloodrage" # We need to make sure certain skills do not turn up in the random roll so should probably assign them here instead
        self.weapon = weapons.weaponsList["Battleaxe"]
        self.healthBar = HealthBar(self, color="green")
        self.stamina = 10
        self.maxStamina = self.stamina
        self.staminaRecovery = 2

class Samurai(object):

    def __init__(self, name="Samurai"):
        self.ally = True
        self.name = name
        self.info = "The Samurai is a disciplined killer, adept and honourable."
        self.maxHitpoints = 95
        self.hitpoints = self.maxHitpoints
        self.defence = 0
        self.strength = 0
        self.attack = 0
        self.agility = 0
        self.evasion = 0
        self.luck = 0
        self.skill = "Withhold"
        self.weapon = weapons.weaponsList["Katana"]
        self.healthBar = HealthBar(self, color="green")
        self.stamina = 10
        self.maxStamina = self.stamina
        self.staminaRecovery = 2

class Pirate(object):

    def __init__(self, name="Pirate"):
        self.ally = True
        self.name = name
        self.info = "The Pirate is a plundering outlaw, experienced with combat and their cutlass."
        self.maxHitpoints = 105
        self.hitpoints = self.maxHitpoints
        self.defence = 0
        self.strength = 0
        self.attack = 0
        self.agility = 0
        self.evasion = 0
        self.luck = 0
        self.skill = "Plunder"
        self.weapon = weapons.weaponsList["Hook"]
        self.healthBar = HealthBar(self, color="green")
        self.stamina = 10
        self.maxStamina = self.stamina
        self.staminaRecovery = 2

class Paladin(object):

    def __init__(self, name="Paladin"):
        self.ally = True
        self.name = name
        self.info = "The Paladin is the King's loyal subject, a strong and stoic knight"
        self.maxHitpoints = 125
        self.hitpoints = self.maxHitpoints
        self.defence = 0
        self.strength = 0
        self.attack = 0
        self.agility = 0
        self.evasion = 0
        self.luck = 0
        self.skill = "Barrier"
        self.weapon = weapons.weaponsList["Hammer"]
        self.healthBar = HealthBar(self, color="green")
        self.stamina = 10
        self.maxStamina = self.stamina
        self.staminaRecovery = 2

class Assassin(object):

    def __init__(self, name="Assassin"):
        self.ally = True
        self.name = name
        self.info = "The Assassin is a lethal and deadly hunter. Fast attacks with a high chance for critical hits."
        self.maxHitpoints = 80
        self.hitpoints = self.maxHitpoints
        self.defence = 0
        self.strength = 0
        self.attack = 0
        self.agility = 0
        self.evasion = 0
        self.luck = 0
        self.skill = "Backstab"
        self.weapon = weapons.weaponsList["Dagger"]
        self.healthBar = HealthBar(self, color="green")
        self.stamina = 10
        self.maxStamina = self.stamina
        self.staminaRecovery = 2
    
# need death function (i think permadeath as can recruit more allies - if og character dies should STILL continue on with allies)
