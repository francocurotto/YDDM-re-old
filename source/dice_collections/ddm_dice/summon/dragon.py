from .monster import Monster

class Dragon(Monster):
    """
    A monster of type dragon.
    """
    def __init__(self, params):
        super().__init__(params)
        self.type = "Dragon"

        # display icons
        self.chars_ascii  .update({"type" : "D"})
        self.chars_unicode.update({"type" : "D"})
        self.chars_emoji  .update({"type" : "🐲"})
