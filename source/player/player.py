from colorama import Fore, Style
from dice_pool import DicePool
from dice_hand import DiceHand
from dice_set import DiceSet
from crest_pool import CrestPool

class Player():
    """
    A player in the game.
    """
    summon_limit = 10

    def __init__(self, name, print_type="emoji"):
        self.name = name
        self.color = None
        self.dice_pool = DicePool()
        self.dice_hand = DiceHand()
        self.dice_bin = DiceSet(self.summon_limit)
        self.crest_pool = CrestPool(print_type)
        self.summons = []

    def add_dice_to_hand(self, i):
        """
        Add dice at position i in dice pool to dice hand.
        Handles case of index error in dice pool.
        """
        # first get dice
        result = self.dice_pool.get_dice(i)
        if not result["success"]:
            return result
        
        dice = result["dice"]

        # check if dice is in bin
        if dice in self.dice_bin.list:
            result["success"] = False
            result["message"] = "Dice already dimensioned."
            return result

        # check if dice is in hand already
        if dice in self.dice_hand.list:
            result["success"] = False
            result["message"] = "Dice already in hand."
            return result

        # finally, add dice to hand
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

    def stringify_pool(self):
        """
        Return string version of dice pool, colorized to
        distinguish between used dice (dimensioned), dice in 
        the dice hand, and normal pool dice.
        """
        string = ""
        for i, dice in enumerate(self.dice_pool.list):
            dice_str = self.dice_pool.stringify_dice_short(i)
            
            # case in hand
            if dice in self.dice_hand.list:
                dice_str = Fore.GREEN + dice_str
                dice_str = dice_str + Style.RESET_ALL

            # case dimensioned
            elif dice in self.dice_bin.list:
                dice_str = Fore.BLACK + dice_str
                dice_str = Style.BRIGHT + dice_str
                dice_str = dice_str + Style.RESET_ALL

            string += dice_str
        
        return string

    def stringify_summons(self):
        """
        Return a string version of summon list.
        """
        string = ""
        for summon in self.summons:
            string += summon.stringify_short() + "\n"

        return string
