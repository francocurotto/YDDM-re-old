from .crest import Crest

class DefenseCrest(Crest):
    """
    A defense crest.
    """
    def __init__(self, print_type):
        super().__init__(print_type)          
        self.char_ascii   = "D"
        self.char_unicode = "⊚"
        self.char_emoji   = "🛡️ "

    def add_to_pool(self, pool, multiplier):
        """
        Add the attack defense to pool.
        """
        pool.defense += multiplier
