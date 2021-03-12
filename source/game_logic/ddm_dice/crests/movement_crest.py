from .crest import Crest

class MovementCrest(Crest):
    """
    A movement crest.
    """
    def __init__(self):
        self.char_ascii   = "M"
        self.char_unicode = "⬆" 
        self.char_emoji   = "⬆️ " 
        super().__init__()

    def add_to_pool(self, pool, multiplier):
        """
        Add the movement crest to pool. Return True if crest
        limit is hit.
        """
        pool.movement += multiplier

        # clip on crest limit
        if pool.movement > pool.crest_limit:
            pool.movement = pool.crest_limit
            return True

        return False

