from ddm_list import DdmList

class SummonList(DdmList):
    """
    List of summons that a player summons during the game.
    """
    def __init__(self, name="summon list"):
        super().__init__(name, "summon")
        
    def stringify(self):
        """
        Returns a string version of object.
        """
        string = ""
        for i in range(len(self.list)):
            string += self.stringify_summon_short(i)

        return string

    def stringify_summon_short(self, i):
        """
        Return the short string version of ddm dice in 
        position i from the dice list.
        """
        # add summon number
        string = str(i).rjust(3) + ". "
        # add dice short string
        string += self.list[i].stringify_short() + "\n"

        return string

    def stringify_summon(self, i):
        """
        Return the string version of summon in position
        i from the dice library.
        """
        return self.list[i].stringify()
