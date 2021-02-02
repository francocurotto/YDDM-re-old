from .crest import Crest

class AttackCrest(Crest):
    """
    An attack crest.
    """
    def __init__(self):
        self.char_ascii   = "A"
        self.char_unicode = "⚔"
        self.char_emoji   = "⚔️ "

    def add_to_pool(self, pool, multiplier):
        """
        Add the attack crest to pool.
        """
        pool.attack += multiplier
