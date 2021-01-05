from .crest import Crest

class MagicCrest(Crest):
    """
    A magic crest.
    """
    def __init__(self, print_type):
        super().__init__(print_type)          
        self.char_ascii   = "G"
        self.char_unicode = "✡"
        self.char_emoji   = "✡️ "

    def add_to_pool(self, pool, multiplier):
        """
        Add the magic crest to pool.
        """
        pool.magic += multiplier
