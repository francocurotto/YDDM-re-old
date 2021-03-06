from dungeon_object import DungeonObject

class Summon(DungeonObject):
    """
    Summon generated from a dice dimension.
    """
    def __init__(self, card, color, log):
        # attributes extracted from card
        self.name = card.name
        self.level = card.level
        self.chars = card.chars
        self.ability = card.ability
        self.card = card
        self.color = color
        self.log = log

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

