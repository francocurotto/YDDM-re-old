from .summon_card import SummonCard

class MonsterCard(SummonCard):
    """
    Generic typeless monster card.
    """
    def __init__(self, params):
        super().__init__(params)
        self.attack = params["attack"]
        self.defense = params["defense"]
        self.life = params["life"]
        self.ability = params["ability"]

        # display icons
        self.chars_ascii  .update({"attack"  : "A",
                                   "defense" : "D",
                                   "life"    : "L"})
        self.chars_unicode.update({"attack"  : "⚔",
                                   "defense" : "⊚",
                                   "life"    : "❤"})
        self.chars_emoji  .update({"attack"  : "⚔️ ",
                                   "defense" : "🛡️ ",
                                   "life"    : "❤️ "})

    def stringify(self):
        """
        Returns a string version of object.
        """
        string  = "NAME:    " + self.name + "\n"
        string += "TYPE:    " + self.type + "\n"
        string += "LEVEL:   " + str(self.level) + "\n"
        string += "ATTACK:  " + str(self.attack) + "\n"
        string += "DEFENSE: " + str(self.defense) + "\n"
        string += "LIFE:    " + str(self.life) + "\n"
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
        string += str(self.level) + " "
        # attack value
        string += str(self.attack).rjust(2)
        #attack icon
        string += self.chars["attack"] + " "
        # defense value
        string += str(self.defense).rjust(2)
        # defense icon
        string += self.chars["defense"] + " "
        # life value
        string += str(self.life) 
        # life icon
        string += self.chars["life"]

        return string
