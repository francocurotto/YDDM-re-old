import sys
sys.path.append("../ddm_dice")
sys.path.append("../summons")
from dice_list import DiceList
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

library = DiceList(print_type="emoji", 
    filename="../databases/my_database.txt")
pool = DicePool()

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
            print(set.stringify())

        else: # print a specific dice
            dicenum = get_dicenum(command[2:])
            if dicenum is None: continue
            result = set.get(dicenum)
            if result["success"]:
                print(result["item"].stringify() + "\n")
            else:
                print(result["message"] + "\n")

    # add dice to pool
    elif command[0] == "a":
        # get dice number from command
        dicenum = get_dicenum(command[1:])
        if dicenum is None: 
            continue

        # get dice from library
        result = library.get_copy(dicenum)
        if not result["success"]:
            print(result["message"] + "\n")
            continue

        # add dice to pool
        result = pool.add(result["item"])
        if result["success"]:
            print("Dice added to pool.\n")
        else:
            print(result["message"] + "\n")
                
    # remove dice from dice pool
    elif command[0] == "r":
        # get dice number from command
        dicenum = get_dicenum(command[1:])
        if dicenum is None: continue

        # remove dice from pool
        result = pool.remove_idx(dicenum)
        if result["success"]:
            print("Dice removed to pool.\n")
        else:
            print(result["message"] + "\n")

    # fill with random dice
    elif command == "f":
        pool.fill_random(library)
        print("Dice pool filled.\n")

print("Bye!")
