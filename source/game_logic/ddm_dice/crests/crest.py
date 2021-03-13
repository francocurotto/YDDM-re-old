from char_functions import select_chars

class Crest():
    """
    A generic crest from a dice's side.
    """
    def __init__(self):
        self.char = select_chars(self.char_ascii, 
            self.char_unicode, self.char_emoji)

    def is_summon(self):
        """
        Negate summon type (overwritten is SummonCrest).
        """
        return False

    def stringify(self):
        """
        Returns a string version of object.
        """
        return self.char
