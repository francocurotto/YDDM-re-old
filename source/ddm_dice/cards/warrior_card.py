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
        self.chars_ascii  .update({"type" : "W"})
        self.chars_unicode.update({"type" : "W"})
        self.chars_emoji  .update({"type" : "🥋"})

    def summon(self):
        """
        Return the monster as a summon.
        """
        return Warrior(self)
