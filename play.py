import classes, pyfiglet, winsound, playsound, enemies, fight, random
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


def text(words="", delay=0.04, colour='white', sound=False):
    for char in words:
        if sound:
            playsound.playsound(sound="sounds/text.mp3", block=False)
        sleep(delay)
        print(f"\033[1;{colours[colour]};40m{char}", end="", flush=True)
        if char in ".,!?:;":
            sleep(delay * 5)
    print("\n")

menu = True
while menu:
    text(pyfiglet.figlet_format("Draayln's Veil"), delay=0.005, colour='blue')
    sleep(2)
    break

winsound.PlaySound("sounds/background.wav", winsound.SND_LOOP + winsound.SND_ASYNC)

def confirm():
    a = ""
    while a not in ["y", "n"]:
        text(words="Confirm? (y/n)", colour='green', sound=True)
        a = input()
    if a.lower() == "y":
        return True
    else:
        return False

while True:
    try:
        text("Choose your scroll speed:")
        print("1 (FASTEST)")
        print("2 (FASTER)")
        print("3 (FAST)")
        print("4 (NORMAL)")
        print("5 (SLOW)")
        print("6 (SLOWER)")
        print("7 (SLOWEST)")
        n = int(input())
        if n >= 1 and n <= 7:
            scrollSpeed = float(f"0.0{n}")
            text(words="This is a sample text for you to see your chosen speed. If you would like to change your choice, type 'n'. Otherwise, type 'y' to confirm.", delay=scrollSpeed, sound=True)
            a = confirm()
            if a:
                scrollSpeed = float(f"0.0{n}")
                break
            else:
                continue
    except ValueError:
        continue

def text(words="", delay=scrollSpeed, colour='white', sound=False):
    for char in words:
        if sound:
            playsound.playsound(sound="sounds/text.mp3", block=False)
        sleep(delay)
        print(f"\033[1;{colours[colour]};40m{char}", end="", flush=True)
        if char in ".,!?":
            sleep(delay * 5)
    sleep(delay * 5)
    print("\n")

menu = True

boolean = True
while boolean:
    text(words="Choose your class:", sound=True)
    options = ["===================", "Barbarian", "Pirate", "Samurai", "Paladin", "Assassin", "==================="]
    text(words="\n".join(options))
    text(words="Type a name to view more.", sound=True)
    choice = input().capitalize()

    while choice not in options:
        text("Type a name to view more.")
        choice = input().capitalize()

    character = getattr(classes, choice)()
    text(f'\n{character.info}\nWeapon: {character.weapon.name}\n')

    if confirm():
        text(words=f"You've chosen the {choice}.", colour='red', sound=True)
    else:
        continue
    while True:
        text("Please enter your character's name.")
        name = input()
        if confirm():
            character.name = name
            text(f"Your character is {character.name}, the {choice}")
            sleep(1)
            break
    boolean = False

characterList = [character]

text("Would you like a quick tutorial?")
a = enemies.enemyList["Goblin"]
if confirm():

    while True:
        winsound.PlaySound(None, winsound.SND_FILENAME)
        text("Time for your first battle...", delay=0.06, sound=True)
        winsound.PlaySound("sounds/Battle.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
        monsterList = [a]
        i = 0
        for monster in monsterList:
            text(f"A {monster.name} approaches!")
            i = i + 1

        text("Hit enter to do a basic attack with your weapon!")
        entities = monsterList + characterList
        enemies_dead = False
        characters_dead = False

        #while characters_dead == False and enemies_dead == False: 
        while character.hitpoints != 0 and monster[0].hitpoints != 0:
            turn = sorted(entities, key=lambda x: x.stamina)
            attacker = turn[-1]
            print(f"It is {attacker.name}'s turn")
            text(f" Stamina: {character.stamina}/{character.maxStamina}", colour='green')

            if attacker in characterList:
                text(f"Its {attacker.name}'s turn!")
                print(f"Tap to attack. 'r' to recover stamina. 'f' to flee.")
                a = input()

                if a == "":
                    while True:
                        try:
                            text("Attack who? (Type the NUMBER of the enemy)")
                            for monster in monsterList:
                                if monster.hitpoints / monster.maxHitpoints < 0.2:
                                    text(monster.name, colour='red')
                                elif monster.hitpoints / monster.maxHitpoints < 0.5:
                                    text(monster.name, colour='yellow')
                                else:
                                    text(monster.name)
                            pick = int(input())
                            fight.attack(attacker, monsterList[pick - 1])
                            break
                        except:
                            continue
                        
            else:
                fight.attack(attacker, random.choice(characterList))
            for entity in entities:
                entity.stamina += entity.staminaRecovery

        break
else:
    text("Choose which path")
