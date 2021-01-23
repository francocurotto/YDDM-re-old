from itertools import cycle
import sys
sys.path.append("../dice_collections")
sys.path.append("../ddm_dice")
sys.path.append("../summons")
from player import Player
from dice_library import DiceLibrary

print("Welcome to the player test.\n\
Here two players will alternate turns filling their dice\n\
hand, rolling their dice hands, getting crests for their\n\
crest pool, and summoning monsters. Their dice pool will\n\
be generated randomly.\n\n\
Input h for a list of available commands at any given\n\
time.\n")

# geterate dice library in order to fill the dice pools
print_type = "emoji"
#print_type = "ascii"
lib_filename = "../databases/my_database.txt"
library = DiceLibrary(lib_filename, print_type)

# generate players
player1 = Player("Player 1", print_type)
player2 = Player("Player 2", print_type)

# generate random dice pools randomly
player1.dice_pool.fill_random(library)
player2.dice_pool.fill_random(library)

# create player list
player_list = [player1, player2]

def main():
    """
    Main loop.
    """
    # main loop
    i = False # player index
    while True:
        # sort out current and opponent player
        player   = player_list[i]
        opponent = player_list[not i]
        print(player.name + " turn.")

        # call player loop
        print(player.stringify_pool())
        player_loop(player, opponent)

        # check win condition
        if len(player.summons) >= player.summon_limit:
            break

        # update player index
        i = not i

    # declare winner
    print(player.name + " is the winner!\n" + \
        "He/She summoned " + str(player.summon_limit) + \
        " monsters/items")
    
def player_loop(player, opponent):
    """
    Loops throught the turn of a player. Return a dictionary
    with the result of the loop.
    """
    help_text = \
    "General commands:\n" + \
    "    h   : print help\n" + \
    "    q   : quit game\n\n" + \
    "Print commands:\n" + \
    "    p p : display pool\n" + \
    "    p h : display hand\n" + \
    "    p c : display crest pool\n" + \
    "    p s : display summons\n" + \
    "    p oc: display opponent crest pool\n" + \
    "    p os: display opponent summons\n\n" + \
    "Hand commands:\n" + \
    "    a #    : add dice from dice pool at position\n" + \
    "             # to dice hand\n" + \
    "    d #    : remove dice from hand at position #\n" + \
    "    r      : roll dice hand\n" + \
    "    r # # #: ignore current dice at dice hand and\n" + \
    "             roll dice at positions # # #\n" + \
    "             (quick roll)\n\n"

    while True:
        try:
            command = input(">")
        except:
            command = "q"
        cmd_list = command.split()

        # no command
        if command == "":
            continue

        # help text
        if command == "h":
            print(help_text)
        
        # quit game
        elif command == "q":
            print("Bye!")
            exit()

        # print case
        elif cmd_list[0] == "p" and len(cmd_list) == 2:
            dsp_cmd = cmd_list[1]
            print_commands(player, opponent, dsp_cmd)

        # hand case
        elif cmd_list[0] in ["a","d"] and len(cmd_list) == 2:
            try: # convert indext into int
                i = int(cmd_list[1]) # dice index
                hand_commands(player, cmd_list[0], i)
            except ValueError:
                continue
       
        # roll dice hand
        elif command == "r":
            success = roll_command(player)

            # if successful roll, finish turn
            if success:
                break

        # quick roll dice
        elif cmd_list[0] == "r":
            try: # convert indeces into int
                i1 = int(cmd_list[1])
                i2 = int(cmd_list[2])
                i3 = int(cmd_list[3])
            except (ValueError, IndexError):
                continue

            success = quickroll_command(player, i1, i2, i3)

            # if successful roll, finish turn
            if success:
                break

def hand_commands(player, command, i):
    """
    Handles commands that add and remove dice from dice hand.
    """
    # add dice from dice pool to dice hand
    if command == "a":
        result = player.add_dice_to_hand(i)
        if not result["success"]:
            print(result["message"])
        print("")
                
    # remove dice from dice hand
    elif command == "d":
        result = player.dice_hand.remove_dice_idx(i)
        if not result["success"]:
            print(result["message"])
        print("")

def roll_command(player):
    """
    Handles a roll command.
    """
    result = player.roll_hand()
    
    if not result["success"]: # roll failed
        print(result["message"] + "\n")
        return False

    # roll succeded
    print("Roll result:" + result["string"] + "\n")

    # check for summon
    dimensions = result["dimensions"]
    if not dimensions.is_empty():
        summon_command(player, dimensions)

    return True

def quickroll_command(player, i1, i2, i3):
    """
    Handles quick roll command.
    """
    # add dice to hand
    result = player.add_dice_to_hand_quick(i1, i2, i3)
    if not result["success"]:
        print(result["message"] + "\n")
        return False

    # roll dice
    success = roll_command(player)

    return success

def summon_command(player, dimensions):
    """
    State for summoning a monster/item.
    """
    print("Available summons:")
    print(dimensions.stringify())

    # selection loop
    while True:
        print("Select a dice to dimension [q to quit].")
        command = input(">")

        # quit without summon
        if command == "q":
            print("")
            break
        
        # get dice index
        try:
            i = int(command)
        except ValueError:
            continue

        # get the summoned dice
        print("")
        result = dimensions.get_dice(i)
        if not result["success"]:
            print(result["message"])
            continue

        # summon dice
        player.dimension_dice(result["dice"])
        break

def print_commands(player, opponent, command):        
    """
    Handles print commands.
    """
    if command == "p": # display pool     
        print(player.stringify_pool())
    elif command == "h": # display hand
        print(player.dice_hand.stringify())
    elif command == "c": # display crest pool
        print(player.crest_pool.stringify_short())
    elif command == "s": # display summons
        print(player.stringify_summons())
    elif command == "oc": # display opponent crest pool
        print(opponent.crest_pool.stringify_short())
    elif command == "os": # display opponent summons
        print(opponent.stringify_summons())

if __name__ == "__main__":
    main()
