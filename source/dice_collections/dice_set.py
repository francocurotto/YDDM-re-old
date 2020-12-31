import copy
from dice_library import DiceLibrary


class DiceSet(DiceSet):
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
                self.print_creation_from_file_warning()
        else: # create empty list
            self.list = []

    def add_dice(self, dice):
        """
        Add a ddm-dice into the dice set. If the dice set
        is full, ignore the dice and print a message.
        """
        if not self.is_full():
            # use copy to avoid tampering with original dice
            copy_dice = copy.deepcopy(dice)
            self.list.append(dice_copy)
        else:
            print(self.name + " full.")

    def remove_dice(self, i):
        """
        Remove dice from dice set with index i. If index is
        not valid, ignore dice and print a message.
        """
        try:
            del(self.list[i])
        except IndexError:
            print("Invalid index in " + self.name + ".")

    def is_full(self):
        """
        Check if dice set is full.
        """
        return len(self.list) >= self.limit
            
    def print_creating_from_file_warning(self):
        print("WARNING: Dice set created from file, but " +
        "the number of dice is different than expected for " +
        "set (" + str(self.limit) "). Reverting to empty set.")
