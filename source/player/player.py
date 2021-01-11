from dice_pool import DicePool
from dice_hand import DiceHand
from crest_pool import CrestPool

class Player():
    """
    A player in the game.
    """
    def __init__(self, name, print_type="emoji"):
        self.name = name
        self.dice_pool = DicePool()
        self.dice_hand = DiceHand()
        self.crest_pool = CrestPool(print_type)
        self.summons = []

    def stringify_summons(self):
        """
        Return a string version of summon list.
        """
        string = ""
        for summon in self.summons:
            string += summon.strinigy_short()

        return string
