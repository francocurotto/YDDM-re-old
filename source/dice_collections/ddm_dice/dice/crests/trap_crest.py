from .crest import Crest

class TrapCrest(Crest):
    """
    A trap crest.
    """
    def __init__(self):
        super().__init__()          
        self.char_ascii   = "T"
        self.char_unicode = "⊗"
        self.char_emoji   = "⚡"

    def get_pool_slot(self, pool):
        """
        Get the trap crest pool slot.
        """
        return pool.trap
