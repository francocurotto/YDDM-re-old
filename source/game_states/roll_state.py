from prompt_state import PromptState

class RollState(PromptState):
    """
    State when player has to roll its dice hand.
    """
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.help_text = help_text

    def parse_command(self, command):
        """
        Parse the command obtained from prompt.
        """
        # generic commands
        super().parse_command(command)

        # print command
        if command.equals_param.param(0, "p"):
            subcommand = command.subcommand(1)
            self.run_print_command(subcommand)

        # add command
        elif command.equals_param(0, "a"):
            subcommand = command.subcommand(1)
            self.run_add_command(subcommand)

        # get back command
        elif command.equals_param(0, "b"):
            subcommand = command.subcommand(1)
            self.run_getback_command(subcommand)

        # roll command
        elif command.equals_param("r"):
            subcommand = command.subcommand(1)
            success = self.run_roll_command(subcommand)
            return success

    def print_commands(self, command):
        """
        Handles print command.
        """
        if command.equals("p"): # display pool     
            print(self.player.stringify_pool())
        elif command.equals("h"): # display hand
            print(self.player.dice_hand.stringify())
        elif command.equals("c"): # display crest pool
            print(self.player.crest_pool.stringify_short())
        elif command.equals("s"): # display summons
            print(self.player.stringify_summons())
        elif command.equals("oc"): # display op. crest pool
            print(self.opponent.crest_pool.stringify_short())
        elif command.equals("os"): # display op. summons
            print(self.opponent.stringify_summons())

help_text = \
"General commands: \
    h   : print help \
    q   : quit game \
\
Print commands: \
    p p : print pool \
    p h : print hand \
    p c : print crest pool \
    p s : print summons \
    p oc: print opponent crest pool \
    p os: print opponent summons \
\
Hand commands: \
    a # [# #]: add 1/2/3 dice from dice pool at positions \
               # to dice hand \
    b # [# #]: get back 1/2/3 dice from hand at positions # 
               from dice hand to dice pool\
    r        : roll dice hand \
    r # # #  : ignore current dice at dice hand and \
               roll dice at positions # # # \
               (quick roll)\
\n"
