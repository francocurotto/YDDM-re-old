class DuelSubstate():
    """
    Generic duel substate.
    """
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.help_text = help_text

    def update(self, command):
        """
        Update state given command.
        """
        # quit (forfeit) command
        if command.equals("q"):
            self.player.forfeited = True

        # help text command
        elif command.equals("h"):
            self.message = self.help_text + "\n\n"

        # print command
        elif command.equals_param(0, "p"):
            subcommand = command.subcommand(1)
            self.message = self.get_print(subcommand)

    def get_print(self, command):
        """
        Get asked print message.
        """
        if command.equals("p"): # display pool     
            msg = self.player.stringify_pool()
        elif command.equals("h"): # display hand
            msg = self.player.dice_hand.stringify()
        elif command.equals("c"): # display crest pool
            msg = self.player.crest_pool.stringify_short()
        elif command.equals("oc"): # display op. crest pool
            msg = self.opponent.crest_pool.stringify_short()
        elif command.equals("s"): # display summons
            msg = self.player.stringify_summons()
        elif command.equals("os"): # display op. summons
            msg = self.opponent.stringify_summons()
        elif command.equals("m"): # display monsters
            msg = self.player.monster_list.stringify()
        elif command.equals("om"): # display op. monsters
            msg = self.opponent.monster_list.stringify()
        elif command.equals("i"): # display items
            msg = self.player.item_list.stringify()
        elif command.equals("oi"): # display op. items
            msg = self.opponent.item_list.stringify()
        elif command.equals("ml"): # display monster lord
            msg = self.player.monster_lord.stringify()
        elif command.equals("oml"): # display op. monster lord
            msg = self.opponent.monster_lord.stringify()
        elif command.equals("g"): # display graveyard
            msg = self.player.graveyard.stringify()
        elif command.equals("og"): # display op. graveyard
            msg = self.opponent.graveyard.stringify()
        else: # invalid command
            return ""

        return msg + "\n\n"

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
