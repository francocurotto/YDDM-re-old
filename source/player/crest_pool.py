from crests.movement_crest import MovementCrest
from crests.attack_crest import AttackCrest
from crests.defense_crest import DefenseCrest
from crests.magic_crest import MagicCrest
from crests.trap_crest import TrapCrest

class CrestPool():
    """
    The crest pool from a player.
    """
    def __init__(self, print_type):
        self.movement = 0
        self.attack   = 0
        self.defense  = 0
        self.magic    = 0
        self.trap     = 0
        self.print_type = print_type

    def add_crests(self, side):
        """
        Adds the crests from the a dice side to the crest 
        pool.
        """
        side.crest.add_to_pool(self, side.multiplier)

    def stringify(self):
        """
        Returns a string version of object.
        """
        string = ""
        # movement crests
        string += MovementCrest(self.print_type).stringify()
        string += ": " + str(self.movement) + "\n"
        # attack crests
        string += AttackCrest(self.print_type).stringify()
        string += ": " + str(self.attack) + "\n"
        # defense crests
        string += DefenseCrest(self.print_type).stringify()
        string += ": " + str(self.defense) + "\n"
        # magic crests
        string += MagicCrest(self.print_type).stringify()
        string += ": " + str(self.magic) + "\n"
        # trap crests
        string += TrapCrest(self.print_type).stringify()
        string += ": " + str(self.trap) + "\n"
        
        return string

    def stringify_short(self):
        """
        Returns a one-liner string version of object.
        """
        string = self.stringify()
        string = string.replace(": ", ":")  # remove spaces
        string = string.replace(":  ", ":") # after ":"
        string = string.replace("\n"," ")
        string += "\n" # add final line break
        return string
