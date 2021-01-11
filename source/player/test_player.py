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
    # main loop
    i = False # player index
    while True:
        # sort out current and opponent player
        player   = player_list[i]
        opponent = player_list[not i]
        print(player.name + " turn.")

        # call player loop
        result = player_loop(player, opponent)

        # update player index
        i = not i
    
def player_loop(player, opponent):
    """
    Loops throught the turn of a player. Return a dictionary
    with the result of the loop.
    """
    help_text = "\
    General commands:\n\
    \th   : print help\n\
    \tq   : quit game\n\n\
    Display commands:\n\
    \td p : display pool\n\
    \td h : display hand\n\
    \td c : display crest pool\n\
    \td s : display summons\n\
    \td oc: display opponent crest pool\n\
    \td os: display opponent summons\n\n\
    Hand commands:\n\
    \th a #: add dice from dice pool at position # to dice\n\
             hand.\n\
    \th d #: remove dice from hand at position #.\n\
    \th r  : roll dice hand\n"

    while True:
        command = input(">")
        cmd_list = command.split()

        # help text
        if command == "h":
            print(help_text)
        
        # quit game
        elif command == "q":
            print("Bye!")
            exit()

        # display case
        elif cmd_list[0] == "d" and len(cmd_list) == 2:
            dsp_cmd = cmd_list[1]
            display_commands(player, opponent, dsp_cmd)

        # hand case
        elif cmd_list[0] == "h" and len(cmd_list) == 3:
            try: # convert indext into int
                i = int(cmd_list[2]) # dice index
                hand_commands(player, cmd_list[1], i)
            except ValueError:
                continue
       
        # roll dice hand
        elif cmd_list[0] == "h" andlen(cmd_list) == 2:
            if cmd_list[1] == "r":
                success = roll_command(player, opponent)

                # if successful roll, finish turn
                if success:
                    break

def hand_command(player, command, i):
    # add dice from dice pool to dice hand
    if cmd_list[1] == "a":
        result = player.add_dice_to_hand(i)
        if not result["success"]:
            print(result["message"])
                
    # remove dice from dice hand
    elif cmd_list[1] == "d":
        result = player.remove_dice_from_hand(i)
        if not result["success"]:
            print(result["message"])
            
def roll_command(player, opponent):
    result == player.dice_hand.roll()
    
    if result["success"]: # roll succeded
        print("Roll result:")
        for side in result["sides"]:
            print(side.stringify())
            player.add_roll_to_crest_pool(result["sides"])

        # check for summon
        if result["dimension"]: # is not empty
            dimension = result["dimension"]
            summon_command(player, opponent, dimension)

        return True

    else: # roll failed
        print(result["message"])
        return False

def summon_command(player, opponent, dimension):
    pass # TODO

def display_commands(player, opponent, command):        
    if command == "p": # display pool     
        print(player.dice_pool.stringify())
    elif command == "h": # display hand
        print(player.dice_hand.stringify())
    elif command == "c": # display crest pool
        print(player.crest_pool.stringify())
    elif command == "s": # display summons
        print(player.stringify_summons())
    elif command == "oc": # display opponent crest pool
        print(opponent.crest_pool.stringify())
    elif command == "os": # display opponent summons
        print(opponent.stringify_summons())

if __name__ == "__main__":
    main()
