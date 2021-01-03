from .crest import Crest

class MagicCrest(Crest):
    """
    A magic crest.
    """
    def __init__(self):
        super().__init__()          
        self.char_ascii   = "G"
        self.char_unicode = "✡"
        self.char_emoji   = "✡️ "

    def get_pool_slot(self, pool):
        """
        Get the magic crest pool slot.
        """
        return pool.magic
