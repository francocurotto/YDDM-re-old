#####################
# Main  game script #
#####################
# add necessary folders to path
import sys, glob
dirlist = glob.glob("*/")
dirlist.remove("__pycache__/")
for dirname in dirlist:
    sys.path.append(dirname)

# imports
import settings
from command_prompt import CommandPrompt
from duel_state import DuelState

def main():
    """
    Main game function.
    """
    initialize_game()
    
    # create game elements
    cmd = CommandPrompt()
    duel_state = DuelState()

    # initial display
    cmd.display(duel_state.message)

    # start game loop
    while True:
        command = cmd.get_command()
        duel_state.update(command)
        cmd.display(duel_state.message)
        if duel_state.finished:
            break

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
