class Barbarian(object):

    def __init__(self):
        self.info = "The Barbarian is a kilt-clad warrior hungry for destruction. Big damage and health numbers, little stamina."
        self.maxHitpoints = 0
        self.hitpoints = maxHitpoints
        self.defence = 0 # Armour value can override this
        self.strength = 0
        self.attack = 0 # If we set this to something low it can act as fists if player lacks weapon - weapon damage can just override this
        self.agility = 0
        self.evasion = 0 # Should stay relatively low by default with few skills that can affect - maybe armour can also affect?
        self.luck = 0 # will affect proc chance. affects chance of increased level up rewards? affects victory drop rates?
        self.skill = # We need to make sure certain skills do not turn up in the random roll so should probably assign them here instead

class Ninja(object):

    def __init__(self):
        self.info = "The Ninja is an agile and talented warrior. Can attack often and fast, at the cost of health."
        self.maxHitpoints = 0
        self.hitpoints = maxHitpoints
        self.defence = 0
        self.strength = 0
        self.attack = 0
        self.agility = 0
        self.evasion = 0
        self.luck = 0
        self.skill = ""


class Pirate(object):

    def __init__(self):
        self.info = "The Pirate is a plundering outlaw, experienced with combat and their cutlass."
        self.maxHitpoints = 0
        self.hitpoints = maxHitpoints
        self.defence = 0
        self.strength = 0
        self.attack = 0
        self.agility = 0
        self.evasion = 0
        self.luck = 0
        self.skill = ""

class Paladin(object):

    def __init__(self):
        self.info = "The Paladin is the King's loyal subject, a strong and stoic knight"
        self.maxHitpoints = 0
        self.hitpoints = maxHitpoints
        self.defence = 0
        self.strength = 0
        self.attack = 0
        self.agility = 0
        self.evasion = 0
        self.luck = 0
        self.skill = ""

class Assassin(object):

    def __init__(self):
        self.info = "The Assassin is a lethal and deadly hunter. Fast attacks with a high chance for critical hits."
        self.maxHitpoints = 0
        self.hitpoints = maxHitpoints
        self.defence = 0
        self.strength = 0
        self.attack = 0
        self.agility = 0
        self.evasion = 0
        self.luck = 0
        self.skill = ""

# need stamina function (need to decide which model to use as will affect rest of code + balancing)
# need death function (i think permadeath as can recruit more allies - if og character dies should STILL continue on with allies)
# need run away function (potentially affected by luck or agility? more likely agility)