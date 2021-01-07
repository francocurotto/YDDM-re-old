import random
from colorama import Fore
from dice_set import DiceSet

class DicePool(DiceSet):
    """
    Set of 15 dice used by a player to play the game.
    """
    def __init__(self, filename=None):
        super().__init__(15, filename)
        self.name = "dice pool"
        self.used = [] # dice used in dice hand

    def fill_random(self, dice_library):
        """
        Fill the dice pool with random dice from a dice 
        library.
        """
        # add random dices until the dice pull is full
        while not self.is_full():
            random_dice = random.choice(dice_library.list)
            self.add_dice(random_dice)

    def use_dice(self, i):
        """
        Return dice at position i and mark it as used. Used to
        fill dice hand.
        """
        result = {}
        try:
            dice = self.list[i]
            self.used.append(dice)
            result["success"] = True
            result["dice"] = dice
        
        except IndexError:
            result["success"] = False
            result["message"] = "Invalid index in " + \
                self.name + "."

        return result

    def release_dice(self, dice):
        """
        Mark dice as not used.
        """
        self.used.remove(dice)

    def stringify_dice_short(self, i):
        """
        Same as dice library, but change style if dice is 
        used.
        """
        string = super().stringify_dice_short(i)
        # if dice is used, stringify as used dice
        if self.list[i] in self.used:
            string = Fore.RED + string

        return string
