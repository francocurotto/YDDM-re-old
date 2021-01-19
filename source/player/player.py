import copy
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

    def add_dice_to_hand(self, i):
        """
        Add dice at position i in dice pool to dice hand.
        Handles case of index error in dice pool.
        """
        result = self.dice_pool.use_dice(i)
        if not result["success"]:
            return result
        
        dice = result["dice"]
        result = self.dice_hand.add_dice(dice)

        return result

    def remove_dice_from_hand(self, i):
        """
        Remove dice at position i in dice hand and make it 
        available in dice pool again. 
        """
        # remove dice from hand
        result = self.dice_hand.remove_dice_idx(i)
        if not result["success"]:
            return result

        # release dice in dice pool
        self.dice_pool.release_dice(result["dice"])
        result = {"success" : True}
        
        return result

    def empty_hand(self):
        """
        Remove all dice from hand and release them in dice 
        pool.
        """
        while True:
            result = self.remove_dice_from_hand(0)
            
            # remove will fail when there are no more dice
            # in dice hand
            if not result["success"]:
                break

    def add_roll_to_crest_pool(self, sides):
        """
        Add the roll result to the crest pool.
        """
        for side in sides:
            self.crest_pool.add_crests(side)

    def stringify_summons(self):
        """
        Return a string version of summon list.
        """
        string = ""
        for summon in self.summons:
            string += summon.stringify_short()

        return string
