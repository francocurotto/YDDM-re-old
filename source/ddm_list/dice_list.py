from ddm_list import DdmList
from ddm_dice_parser import DdmDiceParser

class DiceList(DdmList):
    """
    List of dice. Used as parent of dice library, dice pool 
    and dice hand.
    """
    def __init__(self, limit=float("inf"), print_type="emoji",
                 filename=None):
        super().__init__(limit)
        self.print_type = print_type
        
        # fill from file if given
        if filename is not None:
            self.fill_from_file(filename)

    def fill_from_file(self, filename):
        """
        Fill dice list from dice obtained from file.
        """
        # generate list of dice from parser
        parser = DdmDiceParser(self.print_type)
        dice_list = parser.parse_ddm_dice(filename)

        # add dice to dice list
        for dice in dice_list:
            self.add(dice)

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
        position i from the dice list.
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
