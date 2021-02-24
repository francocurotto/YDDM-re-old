from .monster_card import MonsterCard
from warrior import Warrior

class WarriorCard(MonsterCard):
    """
    A monster card of type warrior.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Warrior"

        # display icons
        self.chars_ascii  ["type"] = "W"
        self.chars_unicode["type"] = "W"
        self.chars_emoji  ["type"] = "🥋"

    def summon(self, log):
        """
        Return the monster as a summon.
        """
        return Warrior(self, log)
