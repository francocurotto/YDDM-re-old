from .crest import Crest

class MovementCrest(Crest):
    """
    A movement crest.
    """
    def __init__(self):
        super().__init__()          
        self.char_ascii   = "M"
        self.char_unicode = "⬆" 
        self.char_emoji   = "⬆️ " 

    def get_pool_slot(self, pool):
        """
        Get the movement crest pool slot.
        """
        return pool.movement
