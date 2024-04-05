import classes
import weapons
import skills

def confirm():
    a = input()
    while a not in ["y", "n"]:
        print("Confirm? (y/n)")
        a = input()
    return a

print("Choose your class:")
options = ["===================", "Barbarian", "Pirate", "Samaurai", "Paladin", "Assassin", "==================="]
print("\n".join(options))
print("Type a name to view more.\n")
choice = input().capitalize()

while choice not in options:
    print("Type a name to view more.")
    choice = input().capitalize()

choice = getattr(classes, choice)()
print("\n" + choice.info + "\n")

print("Confirm your class? (y/n)")
a = confirm()
print(a)