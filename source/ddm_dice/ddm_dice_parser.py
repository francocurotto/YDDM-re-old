from cards.spellcaster_card import SpellcasterCard
from cards.warrior_card import WarriorCard
from cards.undead_card import UndeadCard
from cards.beast_card import BeastCard
from cards.dragon_card import DragonCard
from cards.item_card import ItemCard
from ddm_dice import DdmDice

class DdmDiceParser():

    def parse_ddm_dice(self, filename):
        """
        Read a file with a ddm dice database and converts it
        into a list of ddm dice objects.
        """
        ddm_dice_list = []
        params = {}
        with open(filename) as file:
            for line in file:
                if line.startswith("NAME:"):
                    params["name"] = line[5:-1]
                elif line.startswith("TYPE:"):
                    params["type"] = line[5:-1]
                elif line.startswith("LEVL:"):
                    params["level"] = int(line[5:-1])
                elif line.startswith("ATTK:"):
                    params["attack"] = int(line[5:-1])
                elif line.startswith("DEFS:"):
                    params["defense"] = int(line[5:-1])
                elif line.startswith("LIFE:"):
                    params["life"] = int(line[5:-1])
                elif line.startswith("ABTY:"):
                    params["ability"] = line[5:-1]
                elif line.startswith("DICE:"):
                    params["dice"] = line[5:-1]
                    
                    # create ddm dice with parsed information
                    ddm_dice = self.create_ddm_dice(params)
                    ddm_dice_list.append(ddm_dice)
                    params = {}
    
        return ddm_dice_list

    def create_ddm_dice(self, params):
        """
        Creates ddm object from a dictionary of appropiate
        parameters.
        """
        # first get card
        if params["type"] == "Spellcaster":
            card = SpellcasterCard(params)
        elif params["type"] == "Warrior":
            card = WarriorCard(params)
        elif params["type"] == "Undead":
            card = UndeadCard(params)
        elif params["type"] == "Beast":
            card = BeastCard(params)
        elif params["type"] == "Dragon":
            card = DragonCard(params)
        elif params["type"] == "Item":
            card = ItemCard(params)

        # create the ddm dice
        dice_string = params["dice"]
        ddm_dice = DdmDice(dice_string, card)

        return ddm_dice
