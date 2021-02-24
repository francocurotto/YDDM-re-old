from .monster_card import MonsterCard
from beast import Beast

class BeastCard(MonsterCard):
    """
    A monster card of type beast.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Beast"

        # display icons
        self.chars_ascii  ["type"] = "B"
        self.chars_unicode["type"] = "B"
        self.chars_emoji  ["type"] = "🐺"

    def summon(self, log):
        """
        Return the monster as a summon.
        """
        return Beast(self, log)
