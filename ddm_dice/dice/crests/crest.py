class Crest():
    """
    A generic crest from a dice's side.
    """
    def __init__(self):
        self.print_type = 3 # 1: print as ascii
                            # 2: print as unicode
                            # 3: print as emoji

    def stringify(self):
        """
        Returns a string version of object.
        """
        if self.print_type == 1:
            return self.char_ascii
        elif self.print_type == 2:
            return self.char_unicode
        elif self.print_type == 3:
            return self.char_emoji
