from dice_set import DiceSet
from ddm_dice.dicd.crests.summon_crest import SummonCrest

class DiceHand(DiceSet):
    """
    Set of 3 dice used in a turn to make a roll.
    """
    def __init__(self):
        super().__init__(3)
        self.name = "dice hand"

    def roll(self):
        """
        Make a roll of the dice hand. The returned object is
        a dictionary with the following format.
        result = {
        "success" : (bool) True if roll was performed
                    successfully.
        "sides"   : (list) list of sides rolled.
        "summons" : (list) list of resulting summons.
        "message" : (str) Relevant print string, usually for
                    when the roll is unsuccessful.}
        """
        result = {}
        if not self.is_full():
            result["success"] = False
            result["message"] = "Dice hand not yet completed."
       
        else:
            # get the rolled sides
            result["sides"] = []
            for dice in self.list:
                results["sides"].append(dice.roll())

            # get possible summons
            summons = self.get_summons(result["sides"])
            result["summons"] = summons

            results["success"] = True

        return results

    def get_summons(self, sides):
        """
        Check for summons from rolled sides of the dice hand.
        This should never be called with an incompleted dice
        hand, and the sides and dice from the dice hand
        should be in the same order. Returns a list of 
        possible summons (clould be an empty list).
        """
        # zip combining dice with rolled side
        ds_zip = zip(self.list, sides)

        # check for all levels
        for level in range(1,5):
            # generate filter function
            f = lambda ds_pair : rolled_lvl_x(ds_pair, level)
            
            # filter ds_pairs to be summon crests of current
            # level
            filt_ds_pairs = filter(f, ds_zip)

            # check summon condition: 2 or more summon crests
            # of the same level
            if len(filt_ds_pairs) >= 2:
                # return list of summons if condition is met
                summons = []
                for ds_pair in filt_ds_pairs:
                    dice = ds_pair[0]
                    summons.append(dice.summon)
                return summons
                
        # no summon was found
        return []
        
def rolled_lvl_x(ds_pair, x):
    """
    Returns True is dice rolled a summon crest with level x.
    ds_pair is a pair of a dice and a rolled side of the dice.
    """
    # check if side is a summon crest
    summon_char = SummonCrest().char_ascii
    rolled_char = side.crest.char_ascii
    is_summon = summon_char == rolled_char

    # check if level is x
    is_level_x = dice.level == x

    return is_summon and is_level_x

