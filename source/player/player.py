from colorama import Fore, Style
from dice_pool import DicePool
from dice_hand import DiceHand
from dice_list import DiceList
from summon_list import SummonList
from crest_pool import CrestPool
from monster_lord import MonsterLord

class Player():
    """
    A player in the game.
    """
    summon_limit = 10

    def __init__(self, name, print_type="emoji"):
        self.name = name
        self.color = None
        self.dice_pool = DicePool(print_type)
        self.dice_hand = DiceHand(print_type)
        self.dice_bin = DiceList(print_type)
        self.crest_pool = CrestPool(print_type)
        self.summon_list = SummonList(print_type)
        self.monster_lord = MonsterLord()
        self.forfeited = False

    def add_dice_to_hand(self, i):
        """
        Add dice at position i in dice pool to dice hand.
        """
        # first get dice
        result = self.dice_pool.get(i)
        if not result["success"]:
            return result
        
        dice = result["item"]

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
        result = self.dice_hand.add(dice)

        return result

    def add_dice_to_hand_quick(self, i1, i2, i3):
        """
        Add three dice to hand hand given three index to from 
        dice in dice pool to roll. Must check if index are 
        correct and if necessary empty the hand if it already 
        hace dice in it.
        """
        indeces = [i1, i2, i3]

        # get the dice
        for i in indeces:
            result = self.dice_pool.get(i)
            
            # check if the indeces are correct
            if not result["success"]:
                return result

            # check that the dice are not dimensioned yet
            if result["item"] in self.dice_bin.list:
                result = {}
                result["success"] = False
                result["message"] = \
                    "Dice already dimensioned."
                return result

        # empty hand
        self.empty_hand()

        # fill dice hand with dice indeces
        for i in indeces:
            self.add_dice_to_hand(i)

        return {"success" : True}

    def roll_hand(self):
        """
        Roll dice in hand, and add roll to crest poll.
        """
        result = self.dice_hand.roll()

        if not result["success"]: # roll failed
            return result

        # is success add roll to crest pool
        self.add_roll_to_crest_pool(result["sides"])

        return result

    def dimension_dice(self, dice):
        """
        Dimension dice from dice hand. It involves:
        1. creating a summon from dice
        2. discarting dice to the dice bin
        3. empty dice hand
        """
        # summon card from dice
        summon = dice.card.summon()
        self.summon_list.add(summon)

        # discard summoned dice into dice bin
        self.dice_bin.add(dice)

        # empty dice hand
        self.empty_hand()

    def empty_hand(self):
        """
        Remove all dice from hand and release them in dice 
        pool.
        """
        while True:
            result = self.dice_hand.remove_idx(0)
            
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

    def get_monster(self, i):
        """
        Get a monster from player summon list. If index is
        for a item, ignore procedure and return message.
        """
        result = self.summon_list.get(i)
        
        # check for successful get
        if not result["success"]:
            return result

        # check if summon is monster
        if result["item"].is_item():
            result = {}
            result["message"] = "Summon selected is not a \
                                 monster"
            result["success"] = False
            return result

        # successfull operation
        return result

    def has_monsters(self):
        """
        Return true if player has at least one monster 
        summoned.
        """
        # if not summons at all return false
        if self.summon_list.is_empty():
            return False

        # iterate through summons
        for summon in self.summon_list.list:
            if summon.is_monster():
                return True

        # if not summon found return false
        return False

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
