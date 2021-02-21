class DuelSubstate():
    """
    Generic duel substate.
    """
    def __init__(self, duel, log):
        self.duel = duel
        self.log = log
        self.help_text = help_text
        self.start_message = ""

    def log_start_message(self):
        """
        Log the starting message and reset.
        """
        self.log.add(self.start_message)
        self.start_message = ""

    def update(self, command):
        """
        Update state given command.
        """
        # quit (forfeit) command
        if command.equals("q"):
            self.duel.player.forfeited = True

        # help text command
        elif command.equals("h"):
            self.log.add(self.help_text + "\n\n")

        # print command
        elif command.equals_param(0, "p"):
            subcommand = command.subcommand(1)
            self.log.add(self.get_print(subcommand))

    def get_print(self, command):
        """
        Get asked print message.
        """
        if command.equals("p"): # display pool     
            s = self.duel.player.stringify_pool()
        elif command.equals("h"): # display hand
            s = self.duel.player.dice_hand.stringify()
        elif command.equals("c"): # display crest pool
            s = self.duel.player.crest_pool.stringify_short()
        elif command.equals("oc"): # display op. crest pool
            s = self.duel.opponent.crest_pool.stringify_short()
        elif command.equals("s"): # display summons
            s = self.duel.player.stringify_summons()
        elif command.equals("os"): # display op. summons
            s = self.duel.opponent.stringify_summons()
        elif command.equals("m"): # display monsters
            s = self.duel.player.monster_list.stringify()
        elif command.equals("om"): # display op. monsters
            s = self.duel.opponent.monster_list.stringify()
        elif command.equals("i"): # display items
            s = self.duel.player.item_list.stringify()
        elif command.equals("oi"): # display op. items
            s = self.duel.opponent.item_list.stringify()
        elif command.equals("ml"): # display monster lord
            s = self.duel.player.monster_lord.stringify()
        elif command.equals("oml"): # display op. monster lord
            s = self.duel.opponent.monster_lord.stringify()
        elif command.equals("g"): # display graveyard
            s = self.duel.player.graveyard.stringify()
        elif command.equals("og"): # display op. graveyard
            s = self.duel.opponent.graveyard.stringify()
        else: # invalid command
            return ""

        return s + "\n\n"

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
