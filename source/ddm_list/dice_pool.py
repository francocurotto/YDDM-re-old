import random
from dice_list import DiceList

class DicePool(DiceList):
    """
    Set of 15 dice used by a player to play the game.
    """
    def __init__(self, filename=None):
        super().__init__("dice pool", 15, filename)

    def fill_random(self, dice_library):
        """
        Fill the dice pool with random dice from a dice 
        library.
        """
        # add random dices until the dice pull is full
        while not self.is_full():
            # random index
            i = random.choice(range(len(dice_library.list)))
            result = dice_library.get_copy(i)
            self.add(result["item"])
