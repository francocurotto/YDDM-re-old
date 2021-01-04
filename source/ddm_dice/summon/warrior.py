from .monster import Monster

class Warrior(Monster):
    """
    A monster of type warrior.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Warrior"

        # display icons
        self.chars_ascii  .update({"type" : "W"})
        self.chars_unicode.update({"type" : "W"})
        self.chars_emoji  .update({"type" : "🥋"})
