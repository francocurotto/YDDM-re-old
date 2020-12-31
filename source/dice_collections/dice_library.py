from ddm_dice.ddm_dice_parser import DdmDiceParser

class DiceLibrary():
    """
    A collection of all dice available for the player to make
    its dice pool (can be all dice in the game).
    """
    def __init__(self, filename):
        self.list = DdmDiceParser().parse_ddm_dices(filename)

    def stringify(self):
        """
        Returns a string version of object.
        """
        string = ""
        for i, dice in enumerate(self.list):
            # add dice number
            string += str(i) + ". "
            # add dice short string
            string += dice.stringify_short() + "\n"

        return string

    def stringify_dice(self, dicenum):
        """
        Return the string version of ddm dice in position
        dicenum from the dice library.
        """
        return self.list[dicenum].stringify()


        
