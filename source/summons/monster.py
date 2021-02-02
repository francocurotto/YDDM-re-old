from colorama import Fore
from summon import Summon

class Monster(Summon):
    """
    A monster in the board.
    """
    def __init__(self, card):
        # attributes extracted from card
        super().__init__(card)
        self.attack = self.card.attack
        self.defense = self.card.defense
        self.life = self.card.life
        self.ability = self.card.ability

    def attack_monster(self, attacked, defending):
        """
        Attack the attacked monster. The defend flag 
        indicates if the monster is defending or not.
        """
        # case defending monster
        if defending:
            message = self.attack_defending_monster(attacked)
        # case non-defending monster
        else:
            message = self.attack_nondefending_monster(
                attacked)

        return message

    def attack_defending_monster(self, attacked):
        """
        Attack a monster that is defending defending.
        """
        # get the attacking power considering type advanteges
        # (if in the rules)
        power, message = self.get_attacking_power(attacked)
        message += attaker.name + " defends with " + \
            str(attacker.defense) + "."

        # if attack surpass defense, inflict damage in 
        # attaked monster
        if power > attacked.defense:
            damage = power - attacked.defense
            attacked.life -= damage
            message += attacked.name + " received " + \
                str(damage) + " points of damage."

        # if defense surpass attack, get retaliation damage
        # in attacker monster
        elif power < attacked.defense:
            damage = attacked.defense - power
            message += self.get_retaliation_damage(damage)
        
        # attack and defense are equal
        else:
            message += "No damage inflicted."

        return message

    def attack_nondefending_monster(self, attacked):
        """
        Attack a monster that is not defending.
        """
        # get the attacking power considering type advanteges
        # (if in the rules)
        power, message = self.get_attacking_power(attacked)

        # inflict damage in attaked monster
        damage = power
        attacked.life -= damage
        message += attacked.name + " received " + \
            str(damage) + " points of damage."

        return message

    def get_attacking_power(attacked):
        """
        Get attaking power when attacking attacked monster,
        considering types advantages, if in the rules.
        """
        #TODO: implement
        #TODO: apply diferent rules
        pass

    def get_retaliation_damage(self, damage):
        """
        Inflict the damage for attacking a defending monster
        that has higher defense that the attack of the 
        attacker. Note: should consider different rules.
        """
        #TODO: implement
        #TODO: apply different rules

    def is_monster(self):
        return True

    def stringify_short(self):
        """
        Returns a one-liner string version of object.
        """
        # name, cropped at name_crop characters
        string = self.name[:self.card.name_crop]
        # whitespace to fill chars if name is too short
        string = string.ljust(self.card.name_crop+1)
        # summon type icon
        string += self.chars["type"]
        # level value
        string += str(self.level) + " "
        # attack value, styled for buffs and debuffs
        string += get_attr_styled(self.attack, 
            self.card.attack)
        #attack icon
        string += self.chars["attack"] + " "
        # defense value
        string += get_attr_styled(self.defense, 
            self.card.defense)
        # defense icon
        string += self.chars["defense"] + " "
        # life value, current/max
        string += str(self.life) + "/"
        string += str(self.card.life)
        # life icon
        string += self.chars["life"]

        return string

def get_attr_styled(current, original):
    """
    get the string version of an attribute (attack or defense)
    styled in a way to show buff, debuff or normal case.
    """
    if current > original: # buff style
        return Fore.CYAN + str(current).rjust(2)
    elif current < original: # debuff style
        return Fore.red + str(current).rjust(2)
    else: # normal style
        return str(current).rjust(2)
