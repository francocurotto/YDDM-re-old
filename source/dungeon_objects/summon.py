from functions import color_bg
from dungeon_object import DungeonObject

class Summon(DungeonObject):
    """
    Summon generated from a dice dimension.
    """
    def __init__(self, card, color, log):
        # attributes extracted from card
        self.name = card.name
        self.level = card.level
        self.ability = card.ability
        self.chars = card.chars
        self.card = card
        self.color = color
        self.log = log

        self.chars_emoji = {"tile" : \
            color_bg(self.card.chars_emoji["type"], color)}
        self.chars.update(self.select_chars())

    def stringify(self):
        """
        Returns a string version of object.
        """
        return self.card.stringify()

    def stringify_short(self):
        """
        Returns one-liner string version of object.
        """
        return self.card.stringify_short()
