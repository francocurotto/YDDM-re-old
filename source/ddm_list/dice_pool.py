import random
from dice_list import DiceList

class DicePool(DiceList):
    """
    Set of 15 dice used by a player to play the game.
    """
    def __init__(self, print_type="emoji", filename=None):
        super().__init__(15, print_type, filename)
        self.name = "dice pool"
        self.itemname = "dice"
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
            result = dice_library.get_copy(i)
            self.add(result["item"])
