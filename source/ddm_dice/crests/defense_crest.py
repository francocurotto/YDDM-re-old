from .crest import Crest

class DefenseCrest(Crest):
    """
    A defense crest.
    """
    def __init__(self):
        self.char_ascii   = "D"
        self.char_unicode = "⊝"
        self.char_emoji   = "🛡️ "
        super().__init__()

    def add_to_pool(self, pool, multiplier):
        """
        Add the attack defense to pool.
        """
        pool.defense += multiplier
