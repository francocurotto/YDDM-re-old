from ddm_list import DdmList
from ddm_dice_parser import DdmDiceParser

class DiceList(DdmList):
    """
    List of dice. Used as parent of dice library, dice pool 
    and dice hand.
    """
    def __init__(self, name, log, limit=float("inf")):
        super().__init__(name, "dice", log, limit)
