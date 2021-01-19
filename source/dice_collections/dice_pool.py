import random
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
            # random index
            i = random.choice(range(len(dice_library.list)))
            result = dice_library.get_dice_copy(i)
            self.add_dice(result["dice"])

    def use_dice(self, i):
        """
        Return dice at position i and mark it as used. Used 
        to fill dice hand. Return dictionary format:
        result = {
        "success" : (bool) True if action was performed
                    successfully.
        "dice"    : (dice) dice used.
        "message" : (str) Relevant print string, usually 
                    for when the action is unsuccessful.}
        }
        """
        # get dice
        result = self.get_dice(i)
        if not result["success"]:
            return result

        # check if dice is already used
        dice = result["dice"]
        result = {}
        if dice in self.used:
            result["success"] = False
            result["message"] = "Dice already used."
            return result

        # if not used marked as used now
        self.used.append(dice)
        result["success"] = True
        result["dice"] = dice

        return result

    def release_dice(self, dice):
        """
        Mark dice as not used.
        """
        self.used.remove(dice)

    #def stringify_dice_short(self, i):
    #    """
    #    Same as dice library, but change style if dice is 
    #    used.
    #    """
    #    string = super().stringify_dice_short(i)
    #    # if dice is used, stringify as used dice
    #    if self.list[i] in self.used:
    #        string = Fore.RED + string + Style.RESET_ALL

    #    return string
