class Crest():
    """
    A generic crest from a dice's side.
    """
    def __init__(self, print_type="ascii"):
        self.print_type = print_type

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
        if self.print_type == "ascii":
            return self.char_ascii
        elif self.print_type == "unicode":
            return self.char_unicode
        elif self.print_type == "emoji":
            return self.char_emoji
