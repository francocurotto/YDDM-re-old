 import random
 from dice_set import DiceSet

 class DicePoll(DiceSet):
    """
    Set of 15 dice used by a player to play the game.
    """
    def __init__(self, filename):
        super().__init__(15, filename)

    def fill_random(self, dice_library):
        """
        Fill the dice pool with random dice from a dice 
        library.
        """
        # add random dices until the dice pull is full
        while not self.is_full:
            random_dice = random.choice(dice_library.list)
            self.add_dice(random_dice)


        
