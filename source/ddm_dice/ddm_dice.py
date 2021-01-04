import logging
from dice import Dice

class DdmDice(Dice):
    """
    A dice from the game behaves as normal dice except it
    also has summon type (monster or item).
    """
    def __init__(self, dice_string, summon, print_type):
        super().__init__(dice_string, print_type)
        self.summon = summon

        if self.level != self.summon.level:
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
