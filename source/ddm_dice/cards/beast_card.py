from .monster_card import MonsterCard

class BeastCard(MonsterCard):
    """
    A monster card of type beast.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Beast"

        # display icons
        self.chars_ascii  .update({"type" : "B"})
        self.chars_unicode.update({"type" : "B"})
        self.chars_emoji  .update({"type" : "🐺"})
