import random
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

    def stringify(self):
        """
        Returns a string version of object.
        """
        if self.multiplier <= 1:
            return self.crest.char

        return self.crest.char + str(self.multiplier)

def parse_side_string(string):
    """
    Parses a string containing the information of a side 
    object.
    """
    # extract crest from first char
    crest = CrestCreator().create_crest(string[0])

    # extract multiplier from following chars
    if len(string) <= 1:
        multiplier = 1
    else:
        multiplier = int(string[1:])

    return crest, multiplier

def create_random_nonsummon_side_string():
    """
    Creates a string that represents a random non-summon side.
    The side multiplier can be any from 1 to 9.
    """
    # get the summon character from a crest creator
    crest_chars = CrestCreator().chars

    # select a random non-summon crest
    crest = random.choice(crest_chars[1:])
        
    # select a random multiplier
    multiplier = random.randint(1,9)

    # generate string
    if multiplier <= 1:
        return crest
    
    return crest + str(multiplier)
