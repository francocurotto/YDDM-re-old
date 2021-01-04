from .crest import Crest

class TrapCrest(Crest):
    """
    A trap crest.
    """
    def __init__(self, print_type):
        super().__init__(print_type)          
        self.char_ascii   = "T"
        self.char_unicode = "⊗"
        self.char_emoji   = "⚡"

    def get_pool_slot(self, pool):
        """
        Get the trap crest pool slot.
        """
        return pool.trap
