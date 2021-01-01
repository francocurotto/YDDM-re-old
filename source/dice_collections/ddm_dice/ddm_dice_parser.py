try:  # relative import for standard use
    from .summon.spellcaster import Spellcaster
    from .summon.warrior import Warrior
    from .summon.undead import Undead
    from .summon.beast import Beast
    from .summon.dragon import Dragon
    from .summon.item import Item
    from .ddm_dice import DdmDice
except ImportError: # absolute import for local test
    from summon.spellcaster import Spellcaster
    from summon.warrior import Warrior
    from summon.undead import Undead
    from summon.beast import Beast
    from summon.dragon import Dragon
    from summon.item import Item
    from ddm_dice import DdmDice

class DdmDiceParser():

    def parse_ddm_dices(self, filename):
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
                else: # create ddm dice with parsed information
                    ddm_dice = self.create_ddm_dice(params)
                    ddm_dice_list.append(ddm_dice)
                    params = {}
    
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
        elif params["type"] == "Dragon":
            summon = Dragon(params)
        elif params["type"] == "Item":
            summon = Item(params)

        # create the ddm dice
        ddm_dice = DdmDice(params["dice"], summon)

        return ddm_dice
