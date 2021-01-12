"""
Script for testing the dice object and its internal attributes.
"""
from dice import Dice, create_random_dice_string

print("Welcome to the dice test.\n\n\
Here you can create a random dice, roll it and see the\n\
result of the roll. At any time you can press q to quit\n\
the test.")

input_str = "\n\
Press c to create a new dice. Press r to roll current dice.\n\
Press s to show current dice. Press q to quit.\n>"

dice = None
while True:
    command = input(input_str)

    if command == "q":
        break

    if command == "c": # create random dice
        dice_string = create_random_dice_string()
        dice = Dice(dice_string, "emoji")
        print("Dice created: " + dice.stringify())
        print("Dice level: " + str(dice.level))

    if command == "r": # roll created dice
        if dice is None:
            print("No dice created yet.")
            continue
        rolled_side = dice.roll()
        print("Roll result: " + rolled_side.stringify())

    if command == "s":
        if dice is None:
            print("No dice created yet.")
            continue
        print("Current dice: " + dice.stringify())
        print("Dice level: " + str(dice.level))
        
print("\nBye!")
