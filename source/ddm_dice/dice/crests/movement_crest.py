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

    def get_pool_slot(self, pool):
        """
        Get the movement crest pool slot.
        """
        return pool.movement
