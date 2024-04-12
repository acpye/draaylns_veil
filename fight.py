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

def healthBar(hitpoints, maxHitpoints, length):
    dashConvert = int(maxHitpoints / length)
    currentDashes = int(hitpoints / dashConvert)
    remaininghitpoints = length - currentDashes

    hitpointsDisplay = '█' * currentDashes
    remainingDisplay = ' ' * remaininghitpoints
    
    print("|" + hitpointsDisplay + remainingDisplay + "|")  # Print out healthbar
    print(f"HP: {hitpoints}/{maxHitpoints}")


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

def attack(attacker, target):

    text(f"{attacker.name} Attacks!")
    if attacker.stamina > 0:
        attacker.stamina -= attacker.weapon.staminaConsumption
        damage = (attacker.attack + attacker.weapon.damage + random.randint(1, attacker.weapon.damageRoll))
        if attacker.stamina < 0:
            damage = damage // 2
            text("They are too tired for a strong attack...", colour='blue')

        acc = random.randint(1, 100)
        if acc < attacker.weapon.accuracy:
            crit = random.randint(1, 100)
            if crit < attacker.weapon.critChance:
                target.hitpoints -= round(damage * 1.75)
                target.hitpoints = max(target.hitpoints, 0)
                if target.ally:
                    return text(f"The {attacker.name} landed a critical hit!\nThe {target.name} takes {int(damage * 1.5)} damage!", colour='red')
                else:
                    return text(f"{attacker.name} landed a critical hit!\nThe {target.name} takes {int(damage * 1.5)} damage!", colour='red')
            else:
                target.hitpoints -= damage
                target.hitpoints = max(target.hitpoints, 0)
                if target.ally:
                    return text(f"{target.name} takes {damage} damage!", colour='red')
                else:
                    return text(f"The {target.name} takes {damage} damage!", colour='red')
        else:
            if attacker.ally:
                return text(f"{attacker.name} missed.")
            else:
                return text(f"The {attacker.name} missed.")
    else:
        return text("But they're exhausted...", colour='blue')
