from dice_library import DiceLibrary
from dice_hand import DiceHand

print("Welcome to the dice hand test.\n\n\
Here you can test summoning a monster using a predefined\n\
dice hand.")

print("\n\
Input dh to display the dice hand.\n\
Input r to roll the dice hand.\n\
Input dr to display the roll result.\n\
Input ds to display the roll summon.\n\
Input q to quit.\n")

library = DiceLibrary("databases/my_database.txt")
hand = DiceHand()

# get a prefined set of dice to the dice hand
hand.add_dice(library.get_dice(N)["dice"])
hand.add_dice(library.get_dice(N)["dice"])
hand.add_dice(library.get_dice(N)["dice"])

#########

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
            result = set.get_dice(dicenum)
            if result["success"]:
                print(result["dice"].stringify() + "\n")
            else:
                print(result["message"] + "\n")

    # add dice to pool
    elif command[0] == "a":
        # get dice number from command
        dicenum = get_dicenum(command[1:])
        if dicenum is None: continue

        # get dice from library
        result = library.get_dice(dicenum)
        if not result["success"]:
            print(result["message"] + "\n")
            continue

        # add dice to pool
        result = pool.add_dice(result["dice"])
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
        result = pool.remove_dice(dicenum)
        if result["success"]:
            print("Dice removed to pool.\n")
        else:
            print(result["message"] + "\n")

    # fill with random dice
    elif command == "f":
        pool.fill_random(library)
        print("Dice pool filled.\n")

print("Bye!")
