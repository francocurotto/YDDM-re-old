from .crest import Crest

class MagicCrest(Crest):
    """
    A magic crest.
    """
    def __init__(self):
        self.char_ascii   = "G"
        self.char_unicode = "✡"
        self.char_emoji   = "✡️ "
        super().__init__()

    def add_to_pool(self, pool, multiplier):
        """
        Add the magic crest to pool.
        """
        pool.magic += multiplier
