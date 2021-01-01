from dice_library import DiceLibrary

print("Welcome to the dice library test.\n\n\
Here you can display a whole dice library in short version,\n\
or a single dice from the library in long version. The\n\
specific library is harcoded as a filename in the test.")

print("\n\
Input d to display the whole library.\n\
Input d<number> to display a specific dice.\n\
Input q to quit.\n")

library = DiceLibrary("ddm_dice/test_monsters.txt")

while True:
    command = input(">")
    
    if command == "q":
        break

    if command == "d": # print the whole library
        print(library.stringify())

    elif command[0] == "d": # print a specific dice
        try:
            dicenum = int(command[1:])
        except ValueError:
            print("Couldn't interpret the dice number.\n")
            continue
        result = library.get_dice(dicenum)
        if result["success"]:
            print(result["dice"].stringify() + "\n")
        else:
            print(result["message"] + "\n")

print("Bye!")
