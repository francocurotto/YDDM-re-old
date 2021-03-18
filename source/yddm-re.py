#####################
# Main  game script #
#####################
# add necessary folders to path
import sys
from functions.module_functions import get_all_modules
modlist = get_all_modules()
[sys.path.append(modname) for modname in modlist]
    
# imports
import argparse
import settings
import char_functions
from command_prompt import CommandPrompt
from curses_io import CursesIO
from duel_state import DuelState

def main():
    """
    Main game function.
    """
    args = parse_args()
    if args.test_chars:
        test_chars()

    iom = get_iomodule(args.io_module)
    
    # create game elements
    duel_state = DuelState(args.pool1, args.pool2)

    # initial display
    iom.display(duel_state)

    # start game loop
    while True:
        command = iom.get_command()
        duel_state.update(command)
        iom.display(duel_state)
        if duel_state.finished:
            break

    # finish game gracefully
    iom.terminate()

def parse_args():
    """
    Parse user command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Yugioh Dungeon Dice Monsters " +
            "reimplementation.")
    # display arguments
    parser.add_argument("-pt", "--print_type", 
        choices=["ascii", "unicode", "emoji"], 
        default="emoji",
        help="Type of character to do the 'graphics'")
    parser.add_argument("-io", "--io_module", 
        choices=["cmd", "curses"],
        default="curses",
        help="Input/output method for the game")
    parser.add_argument("-tc", "--test_chars",  
        action="store_true",
        help="Test for the proper display of characters " +
            "in the game and exit")
    # duel arguments
    parser.add_argument("-p1", "--pool1",
        default=None,
        help="File with Player 1's dice pool. If not " +
            "given use random pool")
    parser.add_argument("-p2", "--pool2",
        default=None,
        help="File with Player 2's dice pool. If not " +
            "given use random pool")
    args = parser.parse_args()
    args = parser.parse_args()

    # process some arguments
    settings.print_type = args.print_type

    return args

def get_iomodule(module_name):
    """
    Get the appropiate iomodule from name.
    """
    if module_name == "cmd":
        settings.verbose = True
        return CommandPrompt(module_name)
    elif module_name == "curses":
        settings.verbose = False
        return CursesIO(module_name)

def test_chars():   
    """
    Instead of running the game, test for the proper display
    of the characters.
    """
    char_functions.test_chars(settings.print_type)
    exit()
    
if __name__ == "__main__":
    main()
