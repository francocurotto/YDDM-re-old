class DdmDice():
    """
    A dice from the game cosisting in a normal dice plus a
    summon type (monster or item).
    """
    def __init__(self, summon, dice):
        self.summon = summon
        self.dice = dice

        if summon.level != dice.level:
            
            print("WARNING: dice level doesn't match with" +
                " summon level.")

    def roll(self):
        """
        Roll the dice from the ddm-dice.
        """
        return self.dice.roll()

    def stringify(self):
        """
        Returns a string version of object.
        """
        string  = self.summon.stringify() + "\n"
        string += "DICE:    " + self.dice.stringify()

        return string

    def stringify_short(self):
        """
        Returns a one-liner string version of object.
        """
        string  = self.summon.stringify_short() + " "
        string += self.dice.stringify() 

        return string
