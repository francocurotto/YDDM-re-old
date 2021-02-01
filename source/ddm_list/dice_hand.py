from dice_list import DiceList

class DiceHand(DiceList):
    """
    Set of 3 dice used in a turn to make a roll.
    """
    def __init__(self, print_type="emoji"):
        super().__init__(print_type, 3)
        self.name = "dice hand"

    def roll(self):
        """
        Make a roll of the dice hand. The returned object is
        a dictionary with the following format.
        result = {
        "success"   : (bool) True if roll was performed
                      successfully.
        "sides"     : (list) list of sides rolled.
        "string"    : (str) string version of roll result.
        "dimension" : (DiceList) set of dice available to 
                      dimension.
        "message"   : (str) Relevant print string, usually 
                      for when the roll is unsuccessful.}
        """
        result = {}
        if not self.is_full():
            result["success"] = False
            result["message"] = "Dice hand not yet " + \
                "completed."
       
        else:
            # get the rolled sides
            result["sides"] = []
            string = ""
            for dice in self.list:
                side = dice.roll()
                result["sides"].append(side)
                string += side.stringify() + " "
            result["string"] = string

            # get possible summons
            dimensions = self.get_dimensions(result["sides"])
            result["dimensions"] = dimensions
            result["success"] = True

        return result

    def get_dimensions(self, sides):
        """
        Check for dice dimensions from rolled sides of the 
        dice hand. This should never be called with an 
        incompleted dice hand, and the sides and dice from 
        the dice hand should be in the same order. Returns a 
        list of possible dice dimensions (clould be an empty 
        list).
        """
        # check for all levels
        for level in range(1,5):
            # dice that rolled a summon crest of a specific 
            # level
            summon_dice = DiceList(3)
            
            # go through dice roll (is expected that dice and 
            # side are in order) 
            for dice, side in zip(self.list, sides):
                if rolled_summon_level(dice, side, level):
                    summon_dice.add(dice)

            # check dimension condition: 2 or more summon 
            # crests of the same level
            if len(summon_dice.list) >= 2:
                # return dice available to dimension
                return summon_dice
                
        # no summon was found
        return DiceList(3)
        
def rolled_summon_level(dice, side, level):
    """
    Returns True is dice rolled a summon crest with specified 
    level.
    """
    return side.crest.is_summon() and dice.level == level

