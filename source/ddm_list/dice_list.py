from ddm_list import DdmList
from ddm_dice_parser import DdmDiceParser

class DiceList(DdmList):
    """
    List of dice. Used as parent of dice library, dice pool 
    and dice hand.
    """
    def __init__(self, name="dicelist", limit=float("inf")):
        super().__init__(name, "dice", limit)
        
    def fill_from_file(self, filename):
        """
        Fill dice list from dice obtained from file.
        """
        # generate list of dice from parser
        parser = DdmDiceParser()
        dice_list = parser.parse_ddm_dice(filename)

        # add dice to dice list
        for dice in dice_list:
            self.add(dice)
