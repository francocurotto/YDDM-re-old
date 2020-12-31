from .crest import Crest

class AttackCrest(Crest):
    """
    An attack crest.
    """
    def __init__(self):
        super().__init__()          
        self.char_ascii   = "A"
        self.char_unicode = "⚔"
        self.char_emoji   = "⚔️ "
