from .crest import Crest

class SummonCrest(Crest):
    """
    A summon crest.
    """
    def __init__(self, print_type):
        super().__init__(print_type)          
        self.char_ascii   = "S"
        self.char_unicode = "★"
        self.char_emoji   = "⭐"

    def is_summon(self):
        """
        Assert summon type.
        """
        return True
