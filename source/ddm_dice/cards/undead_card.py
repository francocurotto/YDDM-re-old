from .monster_card import MonsterCard
from undead import Undead

class UndeadCard(MonsterCard):
    """
    A monster card of type undead.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Undead"

        # display icons
        self.chars_ascii  .update({"type" : "U"})
        self.chars_unicode.update({"type" : "U"})
        self.chars_emoji  .update({"type" : "🧟"})

    def summon(self):
        """
        Return the monster as a summon.
        """
        return Undead(self)
