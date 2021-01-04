import sys
sys.path.append("../ddm_dice")
from dice_library import DiceLibrary
from dice_hand import DiceHand

print("Welcome to the dice hand test.\n\n\
Here you can test summoning a monster using a predefined\n\
dice hand.")

print("\n\
Input dh to display the dice hand.\n\
Input r to roll the dice hand.\n\
Input dr to display the roll result.\n\
Input q to quit.\n")

library = DiceLibrary("../databases/my_database.txt")
hand = DiceHand()

# get a prefined set of dice to the dice hand
hand.add_dice(library.get_dice(1)["dice"])
hand.add_dice(library.get_dice(3)["dice"])
hand.add_dice(library.get_dice(7)["dice"])

roll_result = None
while True:
    command = input(">")
    
    if command == "q":
        break

    # display hand
    elif command == "dh":
        print(hand.stringify())

    # roll
    elif command == "r":
        roll_result = hand.roll()
        print("Hand rolled\n")

    if command == "dr":
        if roll_result is None:
            print("Hand not rolled yet.\n")
        else:
            print("Roll results:")
            print("Sides:")
            for side in roll_result["sides"]:
                print(side.stringify())
            print("\nAvailable summons:")
            for summon in roll_result["summons"]:
                print(summon.stringify()+"\n")

print("Bye!")
