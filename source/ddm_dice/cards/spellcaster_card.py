from .monster_card import MonsterCard
from spellcaster import Spellcaster

class SpellcasterCard(MonsterCard):
    """
    A monster card of type spellcaster.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Spellcaster"

        # display icons
        self.chars_ascii  ["type"] = "S"
        self.chars_unicode["type"] = "S"
        self.chars_emoji  ["type"] = "🧙"
    
    def summon(self, log):
        """
        Return the monster as a summon.
        """
        return Spellcaster(self, log)
