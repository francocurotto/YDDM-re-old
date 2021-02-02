import sys
sys.path.append("..")

class Crest():
    """
    A generic crest from a dice's side.
    """
    def is_summon(self):
        """
        Negate summon type (overwritten is SummonCrest).
        """
        return False

    def stringify(self):
        """
        Returns a string version of object.
        """
        # weird import here so that the print_type parameter
        # can be changed at runtime
        from settings import print_type

        if print_type == "ascii":
            return self.char_ascii
        elif print_type == "unicode":
            return self.char_unicode
        elif print_type == "emoji":
            return self.char_emoji
