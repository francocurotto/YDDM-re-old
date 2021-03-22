from library_functions import get_library
from ddm_list import DdmList

class DiceList(DdmList):
    """
    List of dice. Used as parent of dice library, dice pool 
    and dice hand.
    """
    def __init__(self, name, log, limit=float("inf")):
        super().__init__(name, "dice", log, limit)

    def fill_from_library(self):
        """
        Fill dice list with whole library content.
        """
        library = get_library()
        for id, params in library.items():
            self.add(create_ddm_dice(params))

from cards.spellcaster_card import SpellcasterCard
from cards.warrior_card import WarriorCard
from cards.undead_card import UndeadCard
from cards.beast_card import BeastCard
from cards.dragon_card import DragonCard
from cards.item_card import ItemCard
from ddm_dice import DdmDice

def create_ddm_dice(params):
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
