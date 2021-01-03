from .crest import Crest

class DefenseCrest(Crest):
    """
    A defense crest.
    """
    def __init__(self):
        super().__init__()          
        self.char_ascii   = "D"
        self.char_unicode = "⊚"
        self.char_emoji   = "🛡️ "

    def get_pool_slot(self, pool):
        """
        Get the defense crest pool slot.
        """
        return pool.defense
