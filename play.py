import classes, pyfiglet, winsound, playsound
from time import sleep
from classes import attack

colours = {
    'red': "31",
    'green': "32",
    'yellow': "33",
    'blue': "34",
    'purple': "35",
    'cyan': "36",
    'white': "0",
}


winsound.PlaySound("background.wav", winsound.SND_LOOP + winsound.SND_ASYNC)

def confirm():
    a = ""
    while a not in ["y", "n"]:
        text(words="Confirm? (y/n)", colour='green', sound=True)
        a = input()
    if a.lower() == "y":
        return True
    else:
        return False

def text(words="", delay=0.04, colour='white', sound=False):
    for char in words:
        if sound:
            playsound.playsound(sound="sounds/text.mp3", block=False)
        sleep(delay)
        print(f"\033[1;{colours[colour]};40m{char}", end="", flush=True)
        if char in ".,!?":
            sleep(delay * 5)
    print("\n")

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

while menu:
    text(pyfiglet.figlet_format("Draayln's Veil"), delay=0.005, colour='blue')
    sleep(2)
    break

boolean = True
while boolean:
    text(words="Choose your class:", sound=True)
    options = ["===================", "Barbarian", "Pirate", "Samaurai", "Paladin", "Assassin", "==================="]
    text(words="\n".join(options))
    text(words="Type a name to view more.", sound=True)
    choice = input().capitalize()

    while choice not in options:
        text("Type a name to view more.")
        choice = input().capitalize()

    character = getattr(classes, choice)()
    text(f'\n{character.info}\nWeapon: {character.startingWeapon.name}\n')

    if confirm():
        text(words=f"You've chosen the {choice}.", colour='red', sound=True)
        sleep(2)
        boolean = False

text("Would you like a quick tutorial?")

if confirm():
    while True:
        text("Add tutorial later")
        break
else:
    text("Choose which path")
