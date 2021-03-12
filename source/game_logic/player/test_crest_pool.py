import sys
sys.path.append("../ddm_dice")
sys.path.append("../game_states")
from dice import Dice, create_random_dice_string
from crest_pool import CrestPool
from logger import Logger

print("Welcome to the crest pool test.\n\n\
Here you can create a random dice, roll the dice, and\n\
check how the crestpool updates after every roll.")

print("\n\
Input c to create a new dice.\n\
Input dd to display the dice information.\n\
Input r to roll the dice.\n\
Input dc to display the crest pool.\n\
Input ds to display the crest pool in short format.")

# create an initial random dice and crest pool
dice = Dice(create_random_dice_string())
log  = Logger() 
pool = CrestPool(log)

while True:
    print("")
    command = input(">")

    if command == "q":
        break

    elif command == "c": # create new random dice
        dice = Dice(create_random_dice_string())

    elif command == "dd":
        print("Dice: " + dice.stringify())

    elif command == "r":
        rolled_side = dice.roll()
        print("Rolled side: " + rolled_side.stringify())
        pool.add_crests(rolled_side)
        print(log.flush(),end="")

    elif command == "dc":
        print("Crest pool:")
        print(pool.stringify())

    elif command == "ds":
        print("Crest pool:")
        print(pool.stringify_short())

print("\nBye!")
