from .summon_card import SummonCard

class ItemCard(SummonCard):
    """
    An item card.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Item"
        self.ability = params["ability"]

        # display icons
        self.chars_ascii  .update({"type" : "I"})
        self.chars_unicode.update({"type" : "⍰"})
        self.chars_emoji  .update({"type" : "❓"})

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
        # name, cropped at name_crop characters
        string = self.name[:self.name_crop]
        # whitespace to fill chars if name is too short
        string = string.ljust(self.name_crop+1)
        # summon type icon
        string += self.chars["type"]
        # level value
        string += str(self.level)
        # whitespace to fill for the atk,def,life
        if self.print_type == "emoji":
            string += 15*" "
        else: 
            string += 12*" "

        return string




