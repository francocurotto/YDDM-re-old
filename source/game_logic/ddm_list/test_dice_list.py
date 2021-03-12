import sys
sys.path.append("../game_states")
sys.path.append("../ddm_dice")
sys.path.append("../summons")
from logger import Logger
from dice_list import DiceLibrary

print("Welcome to the dice list test.\n\n\
Here you can display a whole dice library in short version,\n\
or a single dice from the library in long version. The\n\
specific library is harcoded as a filename in the test.")

print("\n\
Input d to display the whole library.\n\
Input d<number> to display a specific dice.\n\
Input q to quit.\n")

log = Logger()
library = DiceLibrary(log)
library.fill_from_file("../databases/my_database.txt")

while True:
    command = input(">")
    
    if command == "q":
        break

    if command == "d": # print the whole library
        print(library.stringify() + "\n")

    elif command[0] == "d": # print a specific dice
        try:
            dicenum = int(command[1:])
        except ValueError:
            print("Couldn't interpret the dice number.\n")
            continue
        dice = library.get(dicenum)
        if dice:
            print(dice.stringify() + "\n")
        else:
            print(library.log.flush())

print("Bye!")
