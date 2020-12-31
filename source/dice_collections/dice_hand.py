from dice_set import DiceSet

class DiceHand(DiceSet):
    """
    Set of 3 dice used in a turn to make a roll.
    """
    def __init__(self):
        super().__init__(3)

    def roll(self, crest_pool):
        """
        Make a roll of the dice hand. Add the rolled crests
        to the given crest pool. Also return possible summons
        from roll.
        """
