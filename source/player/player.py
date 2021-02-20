from colorama import Fore
from functions import color, grayout
from dice_pool import DicePool
from dice_hand import DiceHand
from dice_list import DiceList
from monster_list import MonsterList
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
        self.message = ""

    def add_dice_to_hand(self, i):
        """
        Add dice at position i in dice pool to dice hand.
        If operation fails return False.
        """
        # first get dice
        dice = self.dice_pool.get(i)
        if not dice:
            self.message = self.dice_pool.message
            return False
        
        # check if dice is in bin
        if dice in self.dice_bin.list:
            self.message = "Dice already dimensioned."
            return False

        # check if dice is in hand already
        if dice in self.dice_hand.list:
            self.message = "Dice already in hand."
            return False

        # finally, add dice to hand
        success = self.dice_hand.add(dice)
        self.message = self.dice_hand.message

        return success

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
            dice = self.dice_pool.get(i)
            
            # check if the indeces are correct
            if not dice:
                self.message = self.dice_pool.message
                return False

            # check that the dice are not dimensioned yet
            if dice in self.dice_bin.list:
                self.message = "Dice already dimensioned."
                return False

        # empty hand
        self.empty_hand()

        # fill dice hand with dice indeces
        for i in indeces:
            self.add_dice_to_hand(i)

        return True

    def roll_hand(self):
        """
        Roll dice in hand, and add roll to crest poll.
        """
        roll_result = self.dice_hand.roll()

        if not roll_result.sides: # roll failed
            self.message = self.dice_hand.message

        # is success add roll to crest pool
        self.add_roll_to_crest_pool(roll_result)

        return roll_result

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
            dice = self.dice_hand.remove_idx(0)
            
            # remove will fail when there are no more dice
            # in dice hand
            if not dice:
                break

    def add_roll_to_crest_pool(self, roll_result):
        """
        Add the roll result to the crest pool.
        """
        for side in roll_result.sides:
            self.crest_pool.add_crests(side)

    def hit_dimension_limit(self):
        """
        Check if player has hit the dimension limit.
        """
        total_summons  = len(self.monster_list.list)
        total_summons += len(self.item_list.list)
        total_summons += len(self.graveyard.list)

        return total_summons >= self.summon_limit

    def prepare_attack(self, i):
        """
        Prepares for an attack by:
            1. getting the monster at index i
            2. checking that monster is not in cooldown
            3. checking that player has attack crests,
                and substract crest in that case.
        Returns attacker monster.
        """
        # 1. get monster
        attacker = self.monster_list.get(i)
        if not attacker:
            self.message = self.monster_list.message
            return None

        # 2. check if monster is in cooldown
        if attacker.in_cooldown:
            self.message = attacker.name + " has " + \
                "already attacked."
            return None
        
        # 3. verify attack crest
        if self.crest_pool.attack == 0:
            self.message = self.name + " has no attack " + \
                "crests."
            return None

        # if everything is ok, return attacker
        return attacker

    def decooldown_monsters(self):
        """
        Used when a turn starts, all monsters that were in
        cooldown, reset its state.
        """
        for monster in self.monster_list.list:
            monster.in_cooldown = False

    def check_for_casualties(self):
        """
        Iterates through monsters and check if any monster is
        dead. For every dead monster, send it to the,
        graveyard and add a message to the return string.
        """
        # check if monster is dead
        strlist = []
        for monster in self.monster_list.list:
            if monster.life <= 0:
                self.send_to_graveyard(monster)
                strlist.append(monster.name + " is dead.")
            
        self.message = "\n".join(strlist)

    def send_to_graveyard(self, monster):
        """
        Remove monster from summoned list and send it to 
        graveyard. It is assumed that the monster is in the 
        summoned list.
        """
        self.monster_list.remove(monster)
        # set dead monster life to zero for consistency
        monster.life = 0
        self.graveyard.add(monster)

    def stringify_pool(self):
        """
        Return string version of dice pool, colorized to
        distinguish between used dice (dimensioned), dice in 
        the dice hand, and normal pool dice.
        """
        strlist = []
        for i, dice in enumerate(self.dice_pool.list):
            dice_str = self.dice_pool.stringify_short(i)
            
            # case in hand
            if dice in self.dice_hand.list:
                dice_str = color(dice_str, Fore.GREEN)

            # case dimensioned
            elif dice in self.dice_bin.list:
                dice_str = grayout(dice_str)

            strlist.append(dice_str)

        string = "\n".join(strlist)
        
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
