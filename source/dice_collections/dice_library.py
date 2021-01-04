from ddm_dice_parser import DdmDiceParser

class DiceLibrary():
    """
    A collection of all dice available for the player to make
    its dice pool (can be all dice in the game).
    """
    def __init__(self, filename):
        self.list = DdmDiceParser().parse_ddm_dices(filename)

    def get_dice(self, i):
        """
        Get the dice at index i.
        """
        result = {}
        try:
            ddm_dice = self.list[i]
            result["dice"] = ddm_dice
            result["success"] = True

        except IndexError:
            result["success"] = False
            result["message"] = "Invalid index for library."

        return result

    def stringify(self):
        """
        Returns a string version of object.
        """
        string = ""
        for i in range(len(self.list)):
            string += self.stringify_dice_short(i)

        return string

    def stringify_dice_short(self, i):
        """
        Return the short string version of ddm dice in 
        position i from the dice library.
        """
        # add dice number
        string = str(i).rjust(3) + ". "
        # add dice short string
        string += self.list[i].stringify_short() + "\n"

        return string

    def stringify_dice(self, i):
        """
        Return the string version of ddm dice in position
        i from the dice library.
        """
        return self.list[i].stringify()
