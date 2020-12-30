import random

import sys
# import for local test
if sys.argv[0] == "test_dice.py":
    from crests.summon_crest import SummonCrest
    from crests.movement_crest import MovementCrest
    from crests.attack_crest import AttackCrest
    from crests.defense_crest import DefenseCrest
    from crests.magic_crest import MagicCrest
    from crests.trap_crest import TrapCrest
else:
    from .crests.summon_crest import SummonCrest
    from .crests.movement_crest import MovementCrest
    from .crests.attack_crest import AttackCrest
    from .crests.defense_crest import DefenseCrest
    from .crests.magic_crest import MagicCrest
    from .crests.trap_crest import TrapCrest

class Side():
    """
    One of the side of a dice.
    """
    def __init__(self, string):
        """
        Creates a side object by parsing a string with the
        side information.
        """
        crest, multiplier = parse_side_string(string)

        self.crest = crest
        self.multiplier = multiplier

    def stringify(self):
        """
        Returns a string version of object.
        """
        if self.multiplier <= 1:
            return self.crest.stringify()

        return self.crest.stringify() + str(self.multiplier)

def parse_side_string(string):
    """
    Parses a string containing the information of a side 
    object.
    """
    # extract crest from first char
    crest = crest_dict[string[0]]()

    # extract multiplier from following chars
    if len(string) <= 1:
        multiplier = 1
    else:
        multiplier = int(string[1:])

    return crest, multiplier

def create_random_nonsummon_side_string():
    """
    Creates a string that represents a random non-summon side.
    The side multiplier can be any from 1 to 9.
    """
    # get the characters that define the crests
    crest_chars = list(crest_dict.keys())

    # select a random non-summon crest
    crest = random.choice(crest_chars[1:])
        
    # select a random multiplier
    multiplier = random.randint(1,9)

    # generate string
    if multiplier <= 1:
        return crest
    
    return crest + str(multiplier)

crest_dict = {"S" : SummonCrest,
              "M" : MovementCrest,
              "A" : AttackCrest,
              "D" : DefenseCrest,
              "G" : MagicCrest,
              "T" : TrapCrest}
