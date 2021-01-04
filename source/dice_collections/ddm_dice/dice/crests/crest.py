class Crest():
    """
    A generic crest from a dice's side.
    """
    def __init__(self):
        self.print_type = 1 # 1: print as ascii
                            # 2: print as unicode
                            # 3: print as emoji

    def add_to_pool(self, pool, multiplier):
        """
        Add the appropiate number of crests to the 
        corresponding crest pool slot.
        """
        slot = self.get_pool_slot(pool)
        slot += multiplier

    def is_summon(self):
        """
        Negate summon type (overwritten is SummonCrest).
        """
        return False

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
