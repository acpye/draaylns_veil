import random, playsound
from time import sleep

colours = {
    'red': "31",
    'green': "32",
    'yellow': "33",
    'blue': "34",
    'purple': "35",
    'cyan': "36",
    'white': "0",
}

def text(words="", delay=0.015, colour='white', sound=False):
    for char in words:
        if sound:
            playsound.playsound(sound="sounds/text.mp3", block=False)
        sleep(delay)
        print(f"\033[1;{colours[colour]};40m{char}", end="", flush=True)
        if char in ".,!?:;":
            sleep(delay * 5)
    print("\n")



def block():
    return True

def attack(self, target):

    text(f"{self.name} Attacks!")
    if self.stamina > 0:
        self.stamina -= self.weapon.staminaConsumption
        damage = (self.attack + self.weapon.damage + random.randint(1, self.weapon.damageRoll))
        if self.stamina < 0:
            damage = damage // 2
            text("They are too tired for a strong attack...", colour='blue')

        acc = random.randint(1, 100)
        if acc < self.weapon.accuracy:
            crit = random.randint(1, 100)
            if crit < self.weapon.critChance:
                target.hitpoints -= round(damage * 1.75)
                target.hitpoints = max(target.hitpoints, 0)
                if self.ally:
                    return text(f"{self.name} landed a critical hit!\nThe {target.name} takes {int(damage * 1.5)} damage!\nHP: {target.hitpoints}/{target.maxHitpoints}", colour='red')
                else:
                    return text(f"The {self.name} landed a critical hit!\nThe {target.name} takes {int(damage * 1.5)} damage!\nHP: {target.hitpoints}/{target.maxHitpoints}", colour='red')
            else:
                target.hitpoints -= damage
                target.hitpoints = max(target.hitpoints, 0)
                if target.ally:
                    return text(f"{target.name} takes {damage} damage!\nHP: {target.hitpoints}/{target.maxHitpoints}", colour='red')
                else:
                    return text(f"The {target.name} takes {damage} damage!\nHP: {target.hitpoints}/{target.maxHitpoints}", colour='red')
        else:
            if self.ally:
                return text(f"{self.name} missed.")
            else:
                return text(f"The {self.name} missed.")
    else:
        return text("But they're exhausted...", colour='blue')
