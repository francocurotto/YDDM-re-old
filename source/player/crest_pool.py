from crests.movement_crest import MovementCrest
from crests.attack_crest import AttackCrest
from crests.defense_crest import DefenseCrest
from crests.magic_crest import MagicCrest
from crests.trap_crest import TrapCrest

class CrestPool():
    """
    The crest pool from a player.
    """
    crest_limit = 99
    def __init__(self, log):
        self.log = log
        self.movement = 0
        self.attack   = 0
        self.defense  = 0
        self.magic    = 0
        self.trap     = 0

    def add_crests(self, side):
        """
        Adds the crests from the a dice side to the crest 
        pool.
        """
        crest = side.crest
        multiplier = side.multiplier
        hit_limit = crest.add_to_pool(self, multiplier)
        
        # clip on crest limit
        if hit_limit:
            self.log.add("Crest limit reached.\n")
            
    def stringify(self):
        """
        Returns a string version of object.
        """
        string = ""
        # movement crests
        string += MovementCrest().stringify()
        string += ":" + str(self.movement).rjust(2) + "\n"
        # attack crests
        string += AttackCrest().stringify()
        string += ":" + str(self.attack).rjust(2) + "\n"
        # defense crests
        string += DefenseCrest().stringify()
        string += ":" + str(self.defense).rjust(2) + "\n"
        # magic crests
        string += MagicCrest().stringify()
        string += ":" + str(self.magic).rjust(2) + "\n"
        # trap crests
        string += TrapCrest().stringify()
        string += ":" + str(self.trap).rjust(2)
        
        return string

    def stringify_short(self):
        """
        Returns a one-liner string version of object.
        """
        string = self.stringify()
        string = string.replace("\n","|")
        return string
