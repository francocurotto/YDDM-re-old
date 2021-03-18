from cards.spellcaster_card import SpellcasterCard
from cards.warrior_card import WarriorCard
from cards.undead_card import UndeadCard
from cards.beast_card import BeastCard
from cards.dragon_card import DragonCard
from cards.item_card import ItemCard
from ddm_dice import DdmDice

class DdmDiceParser():
    def create_ddm_dice(self, params):
        """
        Creates ddm object from a dictionary of appropiate
        parameters.
        """
        # first get card
        if params["TYPE"] == "SPELLCASTER":
            card = SpellcasterCard(params)
        elif params["TYPE"] == "WARRIOR":
            card = WarriorCard(params)
        elif params["TYPE"] == "UNDEAD":
            card = UndeadCard(params)
        elif params["TYPE"] == "BEAST":
            card = BeastCard(params)
        elif params["TYPE"] == "DRAGON":
            card = DragonCard(params)
        elif params["TYPE"] == "ITEM":
            card = ItemCard(params)

        # create the ddm dice
        dice_string = params["DICE"]
        ddm_dice = DdmDice(dice_string, card)

        return ddm_dice
