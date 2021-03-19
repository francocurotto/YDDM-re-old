import sys
sys.path.append("../..")
sys.path.append("../../functions")
sys.path.append("../game_states")
sys.path.append("../ddm_dice")
sys.path.append("../dungeon_objects")
import settings
from logger import Logger
from dice_list import DiceList
from dice_hand import DiceHand, RollResult

print("Welcome to the dice hand test.\n\n\
Here you can test summoning a monster using a predefined\n\
dice hand.")

print("\n\
Input dh to display the dice hand.\n\
Input r to roll the dice hand.\n\
Input dr to display the roll result.\n\
Input q to quit.\n")

log = Logger()
library = DiceList("library", log)
settings.library_path = ("../../databases/library.yaml")
library.fill_from_library()
hand = DiceHand(log)

# get a prefined set of dice to the dice hand
hand.add(library.get(1))
hand.add(library.get(3))
hand.add(library.get(7))

roll_result = RollResult(log)
while True:
    command = input(">")
    
    if command == "q":
        break

    # display hand
    elif command == "dh":
        print(hand.stringify()+ "\n")

    # roll
    elif command == "r":
        roll_result = hand.roll()
        print("Hand rolled\n")

    if command == "dr":
        if not roll_result.sides:
            print("Hand not rolled yet.\n")
        else:
            print("Roll results:")
            print("Sides:")
            print(roll_result.stringify_sides())
            print("\nAvailable summons:")
            print(roll_result.dimensions.stringify())

print("Bye!")
