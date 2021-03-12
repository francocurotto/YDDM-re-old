import sys
sys.path.append("../game_states")
sys.path.append("../ddm_dice")
sys.path.append("../summons")
from logger import Logger
from dice_list import DiceLibrary
from dice_pool import DicePool

print("Welcome to the dice pool test.\n\n\
Here you can fill a dice pool with dice from a library, and\n\
display the results.")

print("\n\
Input dl to display the library.\n\
Input dl<number> to display a dice from the library.\n\
Input dp to display the dice pool.\n\
Input dp<number> to display a dice from the dice pool.\n\
Input a<number> to add a dice from the library to the pool.\n\
Input r<number> to remove a dice from the pool.\n\
Input f to fill the dice pool with random dice.\n\
Input q to quit.\n")

log = Logger()
library = DiceLibrary(log)
library.fill_from_file("../databases/my_database.txt")
pool = DicePool(log)

def get_dicenum(string):
    try:
        return int(string)
    except ValueError:
        print("Couldn't interpret the dice number.\n")
        return None

while True:
    command = input(">")
    
    if command == "q":
        break
    
    # display something
    if command[0] == "d":
        if len(command) <= 1: # special case of invalid cmd
            print("\n")
            continue
        if command[1] == "l": # display library
            set = library 
        elif command[1] == "p": # display pool
            set = pool
        else: # skip
            continue
        if len(command) == 2: # print the whole set
            print(set.stringify() + "\n")

        else: # print a specific dice
            dicenum = get_dicenum(command[2:])
            if not dicenum: 
                continue
            dice = set.get(dicenum)
            if dice:
                print(dice.stringify() + "\n")
            else:
                print(set.log.flush())

    # add dice to pool
    elif command[0] == "a":
        # get dice number from command
        dicenum = get_dicenum(command[1:])
        if dicenum is None: 
            continue

        # get dice from library
        dice = library.get_copy(dicenum)
        if not dice:
            print(library.log.flush())
            continue

        # add dice to pool
        success = pool.add(dice)
        if success:
            print("Dice added to pool.\n")
        else:
            print(pool.log.flush())
                
    # remove dice from dice pool
    elif command[0] == "r":
        # get dice number from command
        dicenum = get_dicenum(command[1:])
        if dicenum is None: 
            continue

        # remove dice from pool
        dice = pool.remove_idx(dicenum)
        if dice:
            print("Dice removed to pool.\n")
        else:
            print(pool.log.flush())

    # fill with random dice
    elif command == "f":
        pool.fill_random(library)
        print("Dice pool filled.\n")

print("Bye!")
