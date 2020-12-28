class DdmDiceParser():

    def parse_ddm_dices(filename):
        """
        Read a file with a ddm dice database and converts it
        into a list of ddm dice objects.
        """
        ddm_dice_list = []
        with open(filename) as file:
            for line in file:
                if line.startswith("NAME:"):
                    name = line[5:-1]
                elif line.startswith("TYPE:"):
                    type = line[5:-1]
                elif line.startswith("LEVL:"):
                    level = int(line[5:-1])
                elif line.startswith("ATTK:"):
                    attack = int(line[5:-1])
                elif line.startswith("DEFS:"):
                    defense = int(line[5:-1])
                elif line.startswith("LIFE:"):
                    life = int(line[5:-1])
                elif line.startswith("ABTY:"):
                    ability = line[5:-1]
                elif line.startswith("DICE:"):
                    dice = Dice(line[5:-1])
                else: # create ddm dice with parsed information
                    self.create_dice(name, type, level, 
                        attack, defense, life, ability, dice)



