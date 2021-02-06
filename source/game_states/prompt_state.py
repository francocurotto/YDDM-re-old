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
        self.skip_newline = False

    def start(self):
        """
        Start prompt state.
        """
        # run action at the start of running the state
        self.run_initial_action()
        print("")

        # state loop
        while not self.finish:
            command = run_prompt()
            valid = self.parse_command(command)
            if valid and not self.skip_newline:
                print("")
        
    def parse_command(self, command):
        """
        Parse the command obtained from prompt. Return True 
        if player command is valid.
        """
        # quit (forfeit) command)
        if command.equals("q"):
            self.player.forfeited = True
            self.finish = True
            print(self.player.name + " forfeited.")

        # help text command
        elif command.equals("h"):
            print(self.help_text)

        # print command
        elif command.equals_param(0, "p"):
            subcommand = command.subcommand(1)
            self.run_print_command(subcommand)
        
        # invalid command
        else:
            return False

        # valid command
        return True

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
            print(self.player.stringify_summons())
        elif command.equals("os"): # display op. summons
            print(self.opponent.stringify_summons())
        elif command.equals("m"): # display monsters
            print(self.player.monster_list.stringify())
        elif command.equals("om"): # display op. monsters
            print(self.opponent.monster_list.stringify())
        elif command.equals("i"): # display items
            print(self.player.item_list.stringify())
        elif command.equals("oi"): # display op. items
            print(self.opponent.item_list.stringify())
        elif command.equals("ml"): # display monster lord
            print(self.player.monster_lord.stringify())
        elif command.equals("oml"): # display op. monster lord
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
    p p  : print pool \n\
    p h  : print hand \n\
    p c  : print crest pool \n\
    p oc : print opponent crest pool \n\
    p s  : print summons \n\
    p os : print opponent summons \n\
    p m  : print monsters \n\
    p om : print opponent monsters \n\
    p i  : print items \n\
    p oi : print opponent items \n\
    p ml : print monster lord \n\
    p oml: print opponent monster lord \n\
    p g  : print graveyard \n\
    p og : print opponent graveyard"
