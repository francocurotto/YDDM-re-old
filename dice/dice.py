import random

class Dice():
    """
    A dice that a player rolls in the game to perform 
    summonings and collect crests.
    NOTE: I use singular dice instead of die because it's just
    most natural for me. Sorry for all the affected.
    """
    def __init__(self, string):
        """
        Creates a dice object by parsing a string with the
        dice information.
        """
        self.sides = parse_dice_string(string)

    def roll(self):
        """
        Simulates a dice roll by selecting a random element
        from the dice sides list.
        """
        return random.choice(self.sides)

def parse_dice_string(string):
    """
    Parses a string containing the information of a dice
    object.
    """
