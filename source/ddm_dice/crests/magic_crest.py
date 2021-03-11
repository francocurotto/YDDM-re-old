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
        Add the magic crest to pool. Return True if crest
        limit is hit.
        """
        pool.magic += multiplier

        # clip on crest limit
        if pool.magic > pool.crest_limit:
            pool.magic = pool.crest_limit
            return True

        return False

