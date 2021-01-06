from .monster_card import MonsterCard

class SpellcasterCard(MonsterCard):
    """
    A monster card of type spellcaster.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Spellcaster"

        # display icons
        self.chars_ascii  .update({"type" : "S"})
        self.chars_unicode.update({"type" : "S"})
        self.chars_emoji  .update({"type" : "🧙"})
