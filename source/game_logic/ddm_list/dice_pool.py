import random
from library_functions import get_library
from dice_list import DiceList, create_ddm_dice

class DicePool(DiceList):
    """
    Set of 15 dice used by a player to play the game.
    """
    def __init__(self, log):
        super().__init__("dice pool", log, 15)

    def fill_random(self, library):
        """
        Fill the dice pool with random dice from a dice 
        library.
        """
        library_items = list(library.items())
        # add random dices until the dice pull is full
        while not self.is_full():
            # random index
            dice_id, params = random.choice(library_items)
            dice = create_ddm_dice(params)
            self.add(dice)

    def fill_from_ids(self, id_list, library):
        """
        Fill dice pool from id an id list. The dice is 
        extracted from the dice library with the same ids.
        """
        keys = library.keys()
        for id in id_list:
            if id in keys:
                params = library[id]
            else:
                self.log.add("Invalid dice ID " + str(id) +
                    ", skipping.\n")
                continue
            dice = create_ddm_dice(params)
            self.add(dice)

