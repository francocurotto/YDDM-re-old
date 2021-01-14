import logging
from dice_library import DiceLibrary

class DiceSet(DiceLibrary):
    """
    Set of dice with a limit in the number of dice. Used as
    parent of dice pool and dice hand.
    """
    def __init__(self, limit, filename=None):
        self.limit = limit

        if filename is not None: # create list from filename
            super().__init__()
            # if limit is not respeted, revert to empty list
            if self.list != self.limit: 
                self.limit =[]
                self.creating_from_file_warning()
        else: # create empty list
            self.list = []

    def add_dice(self, dice):
        """
        Add a ddm-dice into the dice set. If the dice set
        is full, ignore the dice and print a message.
        Return dictionary format:
        result = {
        "success" : (bool) True if action was performed
                    successfully.
        "message" : (str) Relevant print string, usually 
                    for when the action is unsuccessful.}
        }
        """
        result = {}
        if not self.is_full():
            self.list.append(dice)
            result["success"] = True

        else:
            result["success"] = False
            result["message"] = self.name + " full."

        return result

    def remove_dice(self, i):
        """
        Remove dice from dice set with index i. If index is
        not valid, ignore it and add a message to result.
        Return dictionary format:
        result = {
        "success" : (bool) True if action was performed
                    successfully.
        "message" : (str) Relevant print string, usually 
                    for when the action is unsuccessful.}
        }
        """
        result = self.get_dice(i)
        if not result["success"]:
            return result

        # get dice index
        dice = result["dice"]
        i = self.list.index(dice)
        
        # remove dice
        del(self.list[i])
        result["success"] = True
        result["dice"] = dice

        return result

    def is_full(self):
        """
        Check if dice set is full.
        """
        return len(self.list) >= self.limit

    def is_empty(self):
        """
        Check if dice set is empty.
        """
        return len(self.list) == 0
            
    def creating_from_file_warning(self):
        logging.warning("Dice set created from file, but " + \
        "the number of dice is different than expected " + \
        "for set (" + str(self.limit) + "). Reverting to" + \
        "empty set.")
