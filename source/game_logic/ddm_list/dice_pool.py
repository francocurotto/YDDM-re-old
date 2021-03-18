import random
from dice_list import DiceList
from ddm_dice_parser import DdmDiceParser

class DicePool(DiceList):
    """
    Set of 15 dice used by a player to play the game.
    """
    def __init__(self, log):
        super().__init__("dice pool", log, 15)

    def fill_random(self, dice_library):
        """
        Fill the dice pool with random dice from a dice 
        library.
        """
        parser = DdmDiceParser() 
        library_items = list(dice_library.items())
        # add random dices until the dice pull is full
        while not self.is_full():
            # random index
            i = random.choice(range(len(library_items)))
            id, params = library_items[i]
            dice = parser.create_ddm_dice(params)
            self.add(dice)
