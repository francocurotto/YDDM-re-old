from functions import grayout
from ddm_list import DdmList

class MonsterList(DdmList):
    """
    List of summoned monsters.
    """
    def __init__(self, log):
        super().__init__("monster list", "monster", log)

    def stringify_short(self, i):
        """
        Adapt stringify_short in order to gray out when a 
        monster is in cooldown state.
        """
        string = super().stringify_short(i)
        if self.list[i].in_cooldown:
            string = grayout(string)

        return string

