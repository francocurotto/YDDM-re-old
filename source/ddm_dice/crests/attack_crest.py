from .crest import Crest

class AttackCrest(Crest):
    """
    An attack crest.
    """
    def __init__(self):
        self.char_ascii   = "A"
        self.char_unicode = "⚔"
        self.char_emoji   = "⚔️ "
        super().__init__()

    def add_to_pool(self, pool, multiplier):
        """
        Add the attack crest to pool. Return True if crest
        limit is hit.
        """
        pool.attack += multiplier

        # clip on crest limit
        if pool.attack > pool.crest_limit:
            pool.attack = pool.crest_limit
            return True

        return False
