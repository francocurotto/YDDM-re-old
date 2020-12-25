from crests.crest_creator import CrestCreator

class Side():
    """
    One of the side of a dice.
    """
    def __init__(self, string):
        """
        Creates a side object by parsing a string with the
        side information.
        """
        crest, multiplier = parse_side_string(string)

        self.crest = crest
        self.multiplier = multiplier
        self.crest_creator = CrestCreator()

    def strngify(self):
        """
        Returns a string version of object.
        """
        return self.crest.char + str(self.multiplier)

def parse_side_string(string):
    """
    Parses a string containing the information of a side 
    object.
    """
    # extract crest from first char
    crest = self.crest_creator.create_crest(string[0])

    # extract multiplier from following chars
    if len(string) <= 1:
        multiplier = 1
    else:
        multiplier = int(string[1:])
