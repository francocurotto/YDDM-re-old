from summon_crest import SummonCrest
from movement_crest import MovementCrest
from attack_crest import AttackCrest
from defense_crest import DefenseCrest
from magic_crest import MagicCrest
from trat_crest import TrapCrest

chars1 = "SMADGT"
chars2 = "★⬆⚔⊚✡⨂"
chars3 = "⭐🔁🗡🛡🔯⚡"

class CrestCreator():
    """
    Creates the appropiates crest given a defining character.
    """
    def __init__(self):
        self.chars = chars1 #TODO: make it selectable
        self.dict = {self.chars[0] : SummonCrest,
                     self.chars[1] : MovementCrest,
                     self.chars[2] : AttackCrest,
                     self.chars[3] : DefenseCrest,
                     self.chars[4] : MagicCrest,
                     self.chars[5] : trapCrest}
        self.revdict = dict([reversed(i) for i in d.items()])

    def create_crest(self, char):
        """
        Creates a crest. The char parameter is used both to
        determine the type of crest in the dictionary, and
        as a parameter to the crest itself.
        """
        return self.dict[char](char)

