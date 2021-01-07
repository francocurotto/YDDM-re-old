from .crest import Crest

class MovementCrest(Crest):
    """
    A movement crest.
    """
    def __init__(self, print_type):
        super().__init__(print_type)          
        self.char_ascii   = "M"
        self.char_unicode = "⬆" 
        self.char_emoji   = "⬆️ " 

    def add_to_pool(self, pool, multiplier):
        """
        Add the movement crest to pool.
        """
        pool.movement += multiplier