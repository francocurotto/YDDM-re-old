from dice_list import DiceList

class DiceHand(DiceList):
    """
    Set of 3 dice used in a turn to make a roll.
    """
    def __init__(self):
        super().__init__("dice hand", 3)

    def roll(self):
        """
        Make a roll of the dice hand. The returned object is
        a RollResult that report the result of the roll.
        """
        # if hand is not full, return default
        if not self.is_full():
            self.message = "Dice hand not yet completed."
            return RollResult()
       
        else:
            # get the rolled sides
            sides = []
            for dice in self.list:
                sides.append(dice.roll())

            # generate roll result
            roll_result = RollResult(self.list, sides)

        return roll_result

class RollResult():
    """
    Represents the result of a dice roll. As constructor 
    parameters receives the rolled dice and the sides of the 
    rolls in the same order.
    """
    def __init__(self, dices=[], sides=[]):
        self.dices = dices
        self.sides = sides
        self.dimensions = self.get_dimensions()

    def get_dimensions(self):
        """
        Check for dice dimensions from rolled sides of the 
        roll result. Returns a list of possible dice 
        dimensions (clould be an empty list).
        """
        # check for all levels
        for level in range(1,5):
            # dice that rolled a summon crest of a specific 
            # level
            summon_dice = DiceList(3)
            
            # go through dice roll (is expected that dice and 
            # side are in order) 
            for dice, side in zip(self.dices, self.sides):
                if rolled_summon_level(dice, side, level):
                    summon_dice.add(dice)

            # check dimension condition: 2 or more summon 
            # crests of the same level
            if len(summon_dice.list) >= 2:
                # return dice available to dimension
                return summon_dice
                
        # no summon was found
        return DiceList(3)

    def stringify_sides(self):
        """
        Return a string version of sides rolled.
        """
        strlist = [side.stringify() for side in self.sides]
        return " ".join(strlist)
        
def rolled_summon_level(dice, side, level):
    """
    Returns True is dice rolled a summon crest with specified 
    level.
    """
    return side.crest.is_summon() and dice.level == level

