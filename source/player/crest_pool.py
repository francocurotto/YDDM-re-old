from dice_collections.ddm_dice.dice.crests.movement_crest import MovementCrest
from dice_collections.ddm_dice.dice.crests.attack_crest import AttackCrest
from dice_collections.ddm_dice.dice.crests.defense_crest import DefenseCrest
from dice_collections.ddm_dice.dice.crests.magic_crest import MagicCrest
from dice_collections.ddm_dice.dice.crests.trap_crest import TrapCrest

class CrestPool():
    """
    The crest pool from a player.
    """
    def __init__(self):
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
        if not side.crest.is_summon():
            side.crest.add_to_pool(self, multiplier)

    def stringify(self):
        """
        Returns a string version of object.
        """
        string = ""
        # movement crests
        string += MovementCrest().stringify() + ":"
        string += str(self.movement) + "\n"
        # attack crests
        string += AttackCrests.stringify() + ":"
        string += str(self.attack) + "\n"
        # defense crests
        string += DefenseCrests.stringify() + ":"
        string += str(self.defense) + "\n"
        # magic crests
        string += MagicCrests.stringify() + ":"
        string += str(self.magic) + "\n"
        # trap crests
        string += TrapCrests.stringify() + ":"
        string += str(self.trap) + "\n"
        
        return string

    def stringify_short(self):
        """
        Returns a one-liner string version of object.
        """
        long_string = self.stringify()
        string = long_string.replace("\n"," ")
        return string
