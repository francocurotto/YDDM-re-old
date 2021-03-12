#####################
# Main  game script #
#####################
# add necessary folders to path
import sys
from functions import get_all_modules
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
    initialize_game()
    
    # create game elements
    iom = CommandPrompt()
    #iom = CursesIO()
    duel_state = DuelState()

    # initial display
    iom.display(duel_state)

    # start game loop
    while True:
    #while False:
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
    # set print type if given as commandline input
    print_types = ["ascii", "unicode", "emoji"]
    if len(sys.argv) >= 2 and sys.argv[1] in print_types:
        settings.print_type = sys.argv[1]

if __name__ == "__main__":
    main()
