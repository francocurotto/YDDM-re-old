#####################
# Main  game script #
#####################
# add necessary folders to path
import sys, glob
dirlist = globglob("*/")
dirlist.remove("__pycache__/")
for dirname in dirlist:
    sys.path.append(dirname)

# imports
import setting
from io_modules import CommandPrompt
from duel import Duel

def main():
    """
    Main game function.
    """
    initialize_game()
    
    # create game elements
    cmd = CommandPrompt()
    duel = Duel()

    # initial display
    message = duel.get_initial_message()
    cmd.display(message)

    # start game loop
    while True:
        command = cmd.get_command()
        result = duel.update(command)
        cmd.display(result["message"])
        if result["finished"]:
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
