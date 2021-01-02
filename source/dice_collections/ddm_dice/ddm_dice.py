import logging
try:  # relative import for standard use
    from .dice.dice import Dice
except ImportError: # absolute import for local test
    from dice.dice import Dice

class DdmDice(Dice):
    """
    A dice from the game behaves as normal dice except it
    also has summon type (monster or item).
    """
    def __init__(self, string, summon):
        super().__init__(string)
        self.summon = summon

        if self.level != summon.level:
            logging.warning("dice level doesn't match with" +
                " summon level for " + summon.name)

    def stringify(self):
        """
        Returns a string version of object.
        """
        string  = self.summon.stringify() + "\n"
        string += "DICE:    " + super().stringify()

        return string

    def stringify_short(self):
        """
        Returns a one-liner string version of object.
        """
        string  = self.summon.stringify_short() + " "
        string += super().stringify() 

        return string
