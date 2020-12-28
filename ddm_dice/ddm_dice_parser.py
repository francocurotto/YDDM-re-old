from summon.summon import Summon
from dice.dice import Dice

class DdmDiceParser():

    def parse_ddm_dices(self, filename):
        """
        Read a file with a ddm dice database and converts it
        into a list of ddm dice objects.
        """
        ddm_dice_list = []
        with open(filename) as file:
            for line in file:
                params = {}
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
                    params["dice"] = Dice(line[5:-1])
                else: # create ddm dice with parsed information
                    ddm_dice = self.create_ddm_dice(params)
                    ddm_dice_list.append(ddm_dice)
    
            # get the last dice
            ddm_dice = self.create_ddm_dice(params)
            ddm_dice_list.append(ddm_dice)
        
        return ddm_dice_list

    def create_ddm_dice(self, params):
        """
        Creates ddm object from a dictionary of appropiate
        parameters.
        """
        # first get summon
        if params["type"] == "Spellcaster":
            summon = Spellcaster(params)
        elif params["type"] == "Warrior":
            summon = Warrior(params)
        elif params["type"] == "Undead":
            summon = Undead(params)
        elif params["type"] == "Beast":
            summon = Beast(params)
        elif param["type"] == "Dragon":
            summon = Dragon(params)
        elif params["type"] = "Item":
            summon = Item(params)

        # next get dice
        dice = Dice(params["dice"])

        # create the ddm dice
        ddm_dice = DdmDice(summon, dice)

        return ddm_dice
