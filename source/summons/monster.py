from colorama import Fore
from summon import Summon

class Monster(Summon):
    """
    A monster in the board.
    """
    def __init__(self, card):
        # attributes extracted from card
        super().__init__(card)
        self.attack = self.card.attack
        self.defense = self.card.defense
        self.life = self.card.life
        self.ability = self.card.ability

    def attack_monster(self, attacked, result):
        """
        """
        pass
        #TODO

    def stringify_short(self):
        """
        Returns a one-liner string version of object.
        """
        # name, cropped at name_crop characters
        string = self.name[:self.card.name_crop]
        # whitespace to fill chars if name is too short
        string = string.ljust(self.name_crop+1)
        # summon type icon
        string += self.chars["type"]
        # level value
        string += str(self.level) + " "
        # attack value, styled for buffs and debuffs
        string += get_attr_styled(self.attack, 
            self.card.attack)
        #attack icon
        string += self.chars["attack"] + " "
        # defense value
        string += get_attr_styled(self.defense, 
            self.card.defense)
        # defense icon
        string += self.chars["defense"] + " "
        # life value, current/max
        string += str(self.life) + "/"
        string += str(self.card.life)
        # life icon
        string += self.chars["life"]

def get_attr_styled(current, original):
    """
    get the string version of an attribute (attack or defense)
    styled in a way to show buff, debuff or normal case.
    """
    if current > original: # buff style
        return Fore.CYAN + str(current).rjust(2)
    elif current < original: # debuff style
        return Fore.red + str(current).rjust(2)
    else: # normal style
        return str(current).rjust(2)
