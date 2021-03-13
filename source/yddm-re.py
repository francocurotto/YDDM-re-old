#####################
# Main  game script #
#####################
# add necessary folders to path
import sys
from functions.module_functions import get_all_modules
modlist = get_all_modules()
[sys.path.append(modname) for modname in modlist]
    
# imports
import settings
from command_prompt import CommandPrompt
from curses_io import CursesIO
from duel_state import DuelState

def main():
    """
    Main game function.
    """
    iom = initialize_game()
    
    # create game elements
    duel_state = DuelState()

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

def initialize_game():
    """
    Do all the necessary tasks when initializing the game.
    """
    # expected command line inputs
    print_types = {"ascii", "unicode", "emoji"}
    iomodules = {"cmd", "curses"}

    # get print type
    print_type = set(sys.argv) & print_types
    if len(print_type) == 1:
        settings.print_type = print_type.pop()

    # get io module
    iomodule = set(sys.argv) & iomodules
    if len(iomodule) == 1:
        iomodule = get_iomodule(iomodule.pop())
    else: # default io module
        iomodule = CommandPrompt()

    return iomodule

def get_iomodule(module_name):
    """
    Get the appropiate iomodule from name.
    """
    if module_name == "cmd":
        return CommandPrompt()
    elif module_name == "curses":
        return CursesIO()

if __name__ == "__main__":
    main()
