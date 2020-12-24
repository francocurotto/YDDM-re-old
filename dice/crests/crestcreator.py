class CrestCreator():
    """
    Creates the appropiates crest given a defining character.
    """
    def __init__(self):
        self.dict = {"S" : SummonCrest,
                     "M" : MovementCrest,
                     "A" : AttackCrest,
                     "D" : DefenseCrest,
                     "G" : MagicCrest,
                     "T" : trapCrest}

    def create_crest(self, char):
        """
        Creates a crest. The char parameter is used both to
        determine the type of crest in the dictionary, and
        as a parameter to the crest itself.
        """
        return self.dict[char](char)

