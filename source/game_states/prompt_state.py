from command import run_prompt

class PromptState():
    """
    Generic game state that initializes a command prompt.
    """
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.help_text = help_text
        self.finish = False

    def start(self):
        """
        Start prompt state.
        """
        # run action at the start of running the state
        self.run_initial_action()

        # state loop
        while not self.finish:
            command = run_prompt()
            self.parse_command(command)
        
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
        # quit (forfeit) command)
        if command.equals("q"):
            self.player.forfeited = True
            self.finish = True

        # help text command
        elif command.equals("h"):
            print(self.help_text)

        # print command
        elif command.equals_param(0, "p"):
            subcommand = command.subcommand(1)
            self.run_print_command(subcommand)

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
        elif command.equals("oc"): # display op. crest pool
            print(self.opponent.crest_pool.stringify_short())
        elif command.equals("s"): # display summons
            print(self.player.summon_list.stringify())
        elif command.equals("os"): # display op. summons
            print(self.opponent.summon_list.stringify())
        elif command.equals("m"): # display monster lord
            print(self.player.monster_lord.stringify())
        elif command.equals("om"): # display op. monster lord
            print(self.opponent.monster_lord.stringify())
        elif command.equals("g"): # display graveyard
            print(self.player.graveyard.stringify())
        elif command.equals("og"): # display op. graveyard
            print(self.opponent.graveyard.stringify())

help_text = "\
General commands: \n\
    h   : print help \n\
    q   :  forfeit the duel \n\
\n\
Print commands: \n\
    p p : print pool \n\
    p h : print hand \n\
    p c : print crest pool \n\
    p oc: print opponent crest pool \n\
    p s : print summons \n\
    p os: print opponent summons \n\
    p m : print monster lord \n\
    p om: print opponent monster lord \n\
    p g : print graveyard \n\
    p og: print opponent graveyard \n\
\n"
