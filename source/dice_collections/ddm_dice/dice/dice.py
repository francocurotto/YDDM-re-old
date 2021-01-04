import random

try: # relative import for standard use
    from .side import Side
    from .side import create_random_nonsummon_side_string
    from .side import crest_dict
except ImportError: # absolute import for local test
    from side import Side
    from side import create_random_nonsummon_side_string
    from side import crest_dict

class Dice():
    """
    A dice that a player rolls in the game to perform 
    summonings and collect crests.
    NOTE: I use singular dice instead of die because it's just
    most natural for me. Sorry for all the affected.
    """
    def __init__(self, string):
        """
        Creates a dice object by parsing a string with the
        dice information.
        """
        self.sides = parse_dice_string(string)
        self.level = self.get_level()

    def get_level(self):
        """
        Get the dice level from the dice sides.
        """
        summon_crests = 0
        for side in self.sides:
            if side.crest.is_summon():
                summon_crests += 1

        return 5 - summon_crests

    def roll(self):
        """
        Simulates a dice roll by selecting a random element
        from the dice sides list.
        """
        return random.choice(self.sides)

    def stringify(self):
        """
        Returns a string version of object.
        """
        return "".join([s.stringify() for s in self.sides])

def parse_dice_string(string):
    """
    Parses a string containing the information of a dice
    object, and produces a list of the sides of the dice.
    """
    # get the crest characters for a crest dict
    crest_chars = list(crest_dict.keys())

    # first break the string into a list of side strings
    side_strings = []
    for char in string:
        if char in crest_chars:
            side_strings.append(char)
        else: # expected to be a digit
            side_strings[-1] = side_strings[-1] + char
    
    # then convert the side strings into side objects
    side_list = []
    for side_string in side_strings:
        side_list.append(Side(side_string))

    return side_list

def create_random_dice_string():
    """
    Creates a string that represents a random (legal) dice. 
    Summon level can be any from 1 to 4. The rest of the sides
    are random non-summon crests with random multipliers from
    1 to 9.
    """
    string = ""
    
    # first define the dice level
    level = random.randint(1,4)
    summon_sides = 5 - level
    
    # get the summon character from a crest dict
    summon_char = list(crest_dict.keys())[0]
    
    # add the summon characters
    string += summon_char * summon_sides

    # add the rest of the sides
    for _ in range(6 - summon_sides):
        side_string = create_random_nonsummon_side_string()
        string += side_string

    return string
