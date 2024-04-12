import classes, pyfiglet, winsound, playsound, enemies, fight, random
from time import sleep

#Colour codes for the text function
colours = {
    'red': "31",
    'green': "32",
    'yellow': "33",
    'blue': "34",
    'purple': "35",
    'cyan': "36",
    'white': "0",
}

#This function types characters out one at a time, and can colour/play sound
def text(words="", delay=0.04, colour='white', sound=False):
    for char in words:
        if sound:
            playsound.playsound(sound="sounds/text.mp3", block=False) #playsound function needs to be downloaded, type "pip install playsound" into your terminal
        sleep(delay)
        print(f"\033[1;{colours[colour]};40m{char}", end="", flush=True) #DO NOT TOUCH THIS, IT WILL BREAK THE WHOLE FUNCTION
        if char in ".,!?:;": #Makes the text wait a little longer once it encounters puncuation. Makes text flow nicer
            sleep(delay * 5)
    print("\n") #Printing an empty line at the end just makes the writing easier to read, giving space between lines

menu = True
while menu: # Will have a save/load function hopefully, for now just a title screen.
    text(pyfiglet.figlet_format("Draayln's Veil"), delay=0.005, colour='blue') #may need to pip install pyfiglet, im not too sure but if it doesnt work then yes do it
    sleep(2)
    break

winsound.PlaySound("sounds/background.wav", winsound.SND_LOOP + winsound.SND_ASYNC) #winsound function needs to be downloaded, type "pip install playsound" into your terminal

def confirm(): #This just saves writing a confirm loop everytime someone needs to answer a y/n question
    a = ""
    while a not in ["y", "n"]:
        text(words="(y/n)", colour='green', sound=True)
        a = input()
    if a.lower() == "y":
        return True
    else:
        return False

while True: #This loop lets the user pick the speed of the text
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
            scrollSpeed = float(f"0.0{n}") #if someone typed '1' for the fastest speed, scrollSpeed = 0.01, which is the delay between characters being typed (100 characters/second)
            text(words="This is a sample text for you to see your target speed. If you would like to change your choice, type 'n'. Otherwise, type 'y' to confirm.", delay=scrollSpeed, sound=True) #If sound == True, noises play as text is typed out. also slows down the speed of the text slightly.
            if confirm(): #this means confirm() == True
                scrollSpeed = float(f"0.0{n}")
                break
            else:
                continue # (else: continue) just repeats the loop, so if confirm() == False (which means someone typed 'n' in the confirm function), itll ask for scroll speed again. This idea will be used for many (y/n) questions  
    except Exception:
        continue

def text(words="", delay=scrollSpeed, colour='white', sound=False): #have to repeat the function to allow for the scrollSpeed to be initialised into the text function. can try find a fix later.
    for char in words:
        if sound:
            playsound.playsound(sound="sounds/text.mp3", block=False)
        sleep(delay)
        print(f"\033[1;{colours[colour]};40m{char}", end="", flush=True)
        if char in ".,!?":
            sleep(delay * 5)
    sleep(delay * 5)
    print("\n")

while True:
    text(words="Choose your class:", sound=True)
    options = ["===================", "Barbarian", "Pirate", "Samurai", "Paladin", "Assassin", "==================="] # more will be added here. can be soft coded but not for now.
    text(words="\n".join(options))
    text(words="Type a name to view more.", sound=True)
    choice = input().capitalize() #inputting names is case-insensitive using the .capitalize() function

    while choice not in options:
        text("Type a name to view more.")
        choice = input().capitalize()

    character = getattr(classes, choice)()
    text(f'\n{character.info}\nWeapon: {character.weapon.name}\n') #Gives some info on the class you typed

    if confirm():
        text(words=f"You've chosen the {choice}.", colour='red', sound=True)
    else:
        continue
    while True:
        text("Please enter your character's name.")
        name = input()
        if name == "":
            text("Your name can't be blank.")
            continue
        else:
            text(f"Are you sure you want the name '{name}'")
        if confirm():
            character.name = name
            text(f"Your name is {character.name}, the {choice}")
            sleep(1)
            break
        else:
            continue
    break

characterList = [character] #Adds your character to a list that will eventually have up to 4 characters inside.

text("Would you like a quick tutorial?")

if confirm():

    while True:
        winsound.PlaySound(None, winsound.SND_FILENAME) #This is how to stop the original song
        text("Time for your first battle...", delay=0.06, sound=True)
        winsound.PlaySound("sounds/Battle.wav", winsound.SND_LOOP + winsound.SND_ASYNC) #This starts the battle theme
        monsterList = [enemies.Goblin(), enemies.Goblin()] #This can be randomised, for now is hardcoded as its a tutorial

        for monster in monsterList:
            text(f"A {monster.name} approaches!")

        text("Hit enter to do a basic attack with your weapon!")
        enemies_dead = False
        characters_dead = False

        while len(characterList) != 0 and len(monsterList) != 0: #Due to perma death, the fight continues until either the list of enemies or the list of characters is empty.
            entities = monsterList + characterList #Puts every active member of the fight together
            order = sorted(entities, key=lambda x: x.stamina) #Uses lambda to sort by stamina for whos turn it is 
            attacker = order[-1] # order[-1] is the highest stamina currently
            sleep(1)

            if attacker in characterList: #If the highest stamina is in your party
                text(f"Its {attacker.name}'s turn!")
                print(f"Tap to attack. 'f' to flee.")
                text(f"{attacker.name}'s Stamina: {character.stamina}/{character.maxStamina}", colour='green')
                a = input()

                if a == "":
                    while True:
                        try:
                            text("Attack who? (Type the NUMBER of the enemy)")
                            i = 0
                            for monster in monsterList:
                                i = i + 1
                                if monster.hitpoints / monster.maxHitpoints < 0.25: #if hp < 25%: their name is red
                                    text(f"{i} = {monster.name}", colour='red')
                                elif monster.hitpoints / monster.maxHitpoints < 0.5: #if hp < 50%: their name is yellow
                                    text(f"{i} = {monster.name}", colour='yellow')
                                else:
                                    text(f"{i} = {monster.name}")
                            pick = int(input())
                            target = monsterList[pick - 1]
                            fight.attack(attacker, target)
                            if monsterList[pick - 1].hitpoints == 0:
                                text(f"The {target.name} is defeated!")
                                monsterList.pop(pick - 1) #Remove dead enemies from the list
                            break
                        except Exception:
                            continue
                elif a == "f":
                    text("This is a tutorial, fight!")
                        
            else:
                text(f"It is the {attacker.name}'s turn")
                target = random.choice(characterList) #Party is attacked at random
                sleep(1)
                fight.attack(attacker, target)
                fight.healthBar(target.hitpoints, target.maxHitpoints, 25) #Displays health bar
                if target.hitpoints == 0:
                    text(f"{target.name} has died!")
                    characterList.remove(target.name) #removes dead party member - permadeath
                print()
        text("All enemies have been defeated!")
        break
else:
    text("Choose which path")
