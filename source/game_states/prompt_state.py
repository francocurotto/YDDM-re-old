from command import run_prompt

class PromptState():
    """
    Generic game state that initializes a command prompt.
    """
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.help_text = help_text

    def start(self):
        """
        Start prompt state.
        """
        # run action at the start of running the state
        self.run_initial_action()

        # state loop
        while True:
            command = run_prompt()
            finish = self.parse_command(command)
            if finish:
                break
        
    def run_initial_action(self):
        """
        Dummy initial action.
        """
        pass

    def parse_command(self, command):
        """
        Parse the command obtained from prompt. Return True 
        if player is done with prompt state.
        """
        if command.equals("q"):
            self.player.forfeited = True
            return True

        elif command.equals("h"):
            print(self.help_text)
            return False

        # print command
        elif command.equals_param(0, "p"):
            subcommand = command.subcommand(1)
            self.run_print_command(subcommand)
            return False

    def run_print_command(self, command):
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

help_text = "\
General commands: \n\
    h   : print help \n\
    q   :  forfeit the duel \n\
\n\
Print commands: \n\
    p p : print pool \n\
    p h : print hand \n\
    p c : print crest pool \n\
    p s : print summons \n\
    p oc: print opponent crest pool \n\
    p os: print opponent summons \n\
\n"
