from ddm_dice_parser import DdmDiceParser

class DdmDice():
    """
    A dice from the game cosisting in a normal dice plus a
    summon type (monster or item).
    """
    def __init__(self, dice, summon):
        self.dice = dice
        self.summon = summon

        if dice.level != summon.level:
            print("WARNING: dice level doesn't match with \
                summon level.")

