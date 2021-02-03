from .crest import Crest

class TrapCrest(Crest):
    """
    A trap crest.
    """
    def __init__(self):
        self.char_ascii   = "T"
        self.char_unicode = "⊗"
        self.char_emoji   = "⚡"
        super().__init__()

    def add_to_pool(self, pool, multiplier):
        """
        Add the trap crest to pool.
        """
        pool.trap += multiplier
