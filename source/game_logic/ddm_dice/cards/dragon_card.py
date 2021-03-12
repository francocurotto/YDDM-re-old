from .monster_card import MonsterCard
from dragon import Dragon

class DragonCard(MonsterCard):
    """
    A monster card of type dragon.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Dragon"

        # display icons
        self.chars_ascii  ["type"] = "D"
        self.chars_unicode["type"] = "D"
        self.chars_emoji  ["type"] = "🐲"

    def summon(self, chars, log):
        """
        Return the monster as a summon.
        """
        return Dragon(self, chars, log)
