import sys
sys.path.append("..")
from .summon_card import SummonCard
from item import Item

class ItemCard(SummonCard):
    """
    An item card.
    """
    # display icons
    chars_ascii   = {"type" : "I"}
    chars_unicode = {"type" : "I"}
    chars_emoji   = {"type" : "❓"}

    def __init__(self, params):
        super().__init__(params)
        self.type = "Item"
        self.ability = params["ability"]

    def summon(self, log):
        """
        Return the monster as a summon.
        """
        return Item(self, log)

    def stringify(self):
        """
        Returns a string version of object.
        """
        string  = "NAME: " + self.name + "\n"
        string += "TYPE: " + self.type + "\n"
        string += "LEVEL: " + str(self.level) + "\n"
        string += "ABILITY: " + self.ability

        return string

    def stringify_short(self):
        """
        Returns a one-liner string version of object.
        """
        # weird import here so that the print_type parameter
        # can be changed at runtime
        from settings import print_type
        
        # name, cropped at name_crop characters
        string = self.name[:self.name_crop]
        # whitespace to fill chars if name is too short
        string = string.ljust(self.name_crop+1)
        # summon type icon
        string += self.chars["type"]
        # level value
        string += str(self.level)
        # whitespace to fill for the atk,def,life
        if print_type == "emoji":
            string += 15*" "
        else: 
            string += 12*" "

        return string
