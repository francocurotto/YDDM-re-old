from dice_nets.pos import Pos

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

        # print command
        elif command.equals_param(0, "ps"):
            subcommand = command.subcommand(1)
            self.log.add(self.get_print_short(subcommand))

    def get_print(self, command):
        """
        Get print message.
        """
        if command.equals("p"): # display pool     
            s = self.duel.player.stringify_pool()
        elif command.equals("h"): # display hand
            s = self.duel.player.dice_hand.stringify()
        elif command.equals("c"): # display crest pool
            s = self.duel.player.crest_pool.stringify_short()
        elif command.equals("oc"): # display op. crest pool
            s = self.duel.opponent.crest_pool.stringify_short()
        elif command.equals("g"): # display graveyard
            s = self.duel.player.graveyard.stringify()
        elif command.equals("og"): # display op. graveyard
            s = self.duel.opponent.graveyard.stringify()
        elif command.equals("d"): # display dungeon
            s = self.duel.dungeon.stringify()
        # display item at pos
        elif pos := Pos.from_string(command.get_param(0)):
            s = self.stringify_dungeon_pos(pos, short=False)
        else: # invalid command
            return ""

        return s + "\n\n"

    def get_print_short(self, command):
        """
        Get short print message.
        """
        # display item at pos
        if pos := Pos.from_string(command.get_param(0)):
            s = self.stringify_dungeon_pos(pos, short=True)
        else: # invalid command
            return ""
        return s + "\n\n"

    def stringify_dungeon_pos(self, pos, short):
        """
        Returns string version of object at position pos in
        dungeon. If short is True, return short version.
        """
        # get tile
        tile = self.duel.dungeon.get_tile(pos)
        if not tile: # no tile => out of bound
            return "Can't print, out of bound."
        
        if short:
            return tile.stringify_short()
        else:
            return tile.stringify()

help_text = "\
General commands: \n\
    h : print help \n\
    q :  forfeit the duel \n\
\n\
Print commands: \n\
    p p    : print pool \n\
    p h    : print hand \n\
    p c    : print crest pool \n\
    p oc   : print opponent crest pool \n\
    p g    : print graveyard \n\
    p og   : print opponent graveyard\n\
    p d    : print dungeon\n\
    p <xy> : print item at position <xy>"
