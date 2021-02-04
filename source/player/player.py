from colorama import Fore, Style
from dice_pool import DicePool
from dice_hand import DiceHand
from dice_list import DiceList
from ddm_list import MonsterList
from ddm_list import ItemList
from ddm_list import Graveyard
from crest_pool import CrestPool
from monster_lord import MonsterLord

class Player():
    """
    A player in the game.
    """
    summon_limit = 10

    def __init__(self, name):
        self.name = name
        self.color = None
        self.dice_pool = DicePool()
        self.dice_hand = DiceHand()
        self.dice_bin = DiceList()
        self.crest_pool = CrestPool()
        self.monster_list = MonsterList()
        self.item_list = ItemList()
        self.graveyard = Graveyard()
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
        if summon.is_monster():
            self.monster_list.add(summon)
        elif summon.is_item():
            self.item_list.add(summon)

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

    def decooldown_monsters(self):
        """
        Used when a turn starts, all monsters that were in
        cooldown, reset its state.
        """
        for monster in self.monster_list.list:
            monster.is_cooldown = False

    def check_for_casualities():
        """
        Iterates through monsters and check if any monster is
        dead. For every dead monster, send it to the,
        graveyard and add a message to the return string.
        """
        string = ""

        for monster in self.monster_list.list:
            # check if monster is dead
            if monster.life <= 0:
                self.send_to_graveyard(monster)
                string += monster.name + " is dead.\n"

        return string

    def send_to_graveyard(self, monster):
        """
        Remove monster from summoned list and send it to 
        graveyard. It is assumed that the monster is in the 
        summoned list.
        """
        self.monster_list.remove(monster)
        self.graveryard.add(monster)

    def stringify_pool(self):
        """
        Return string version of dice pool, colorized to
        distinguish between used dice (dimensioned), dice in 
        the dice hand, and normal pool dice.
        """
        string = ""
        for i, dice in enumerate(self.dice_pool.list):
            dice_str = self.dice_pool.stringify_short(i)
            
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
        Returns a string version of player summons, that is,
        simply a combinations of player monsters and player
        items.
        """
        string = ""
        string += "Monsters:\n"
        string += self.monster_list.stringify()
        string += "\n"
        string += "Items:\n"
        string += self.item_list.stringify()
        return string

