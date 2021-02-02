import sys
sys.path.append("../ddm_dice")
sys.path.append("../summons")
from dice_list import DiceList
from dice_hand import DiceHand

print("Welcome to the dice hand test.\n\n\
Here you can test summoning a monster using a predefined\n\
dice hand.")

print("\n\
Input dh to display the dice hand.\n\
Input r to roll the dice hand.\n\
Input dr to display the roll result.\n\
Input q to quit.\n")

library = DiceList(filename="../databases/my_database.txt")
hand = DiceHand()

# get a prefined set of dice to the dice hand
hand.add(library.get(1)["item"])
hand.add(library.get(3)["item"])
hand.add(library.get(7)["item"])

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
            print(roll_result["dimensions"].stringify())

print("Bye!")
