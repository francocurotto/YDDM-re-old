from colorama import Fore
from settings import type_adv, retal_dmg
from functions import color
from summon import Summon

class Monster(Summon):
    """
    A monster in the board.
    """
    def __init__(self, card):
        super().__init__(card)
        # attributes extracted from card
        self.attack = self.card.attack
        self.defense = self.card.defense
        self.life = self.card.life
        self.ability = self.card.ability
        self.in_cooldown = False

    def attack_monster(self, attacked, defending):
        """
        Attack the attacked monster. The defend flag 
        indicates if the monster is defending or not.
        """
        # first get attacking power, considering type adv.
        power = self.get_attacking_power(attacked)

        # case defending monster
        if defending:
            message = self.attack_defending_monster(attacked,
                power)
        # case non-defending monster
        else:
            attacked.life -= power
            message = attacked.name + " received " + \
                str(power) + " points of damage."

        # monster enters cooldown
        self.in_cooldown = True

        return message

    def attack_ml(self, opponent):
        """
        Attack the opponent monster lord, directly removing
        one of its hearts.
        """
        # attack monster lord
        opponent.monster_lord.hearts -= 1

        # monster enter cooldown
        self.in_cooldown = True

        # create information string
        string = self.name + " attacked " + opponent.name + \
            " Monster Lord directly.\n"
        string += opponent.monster_lord.stringify()

        return string

    def attack_defending_monster(self, attacked, power):
        """
        Attack a monster that is defending with power attack
        points.
        """
        # defending message
        message = attacked.name + " defends with " + \
            str(attacked.defense) + ".\n"

        # if attack surpass defense, inflict damage in 
        # attacked monster
        if power > attacked.defense:
            damage = power - attacked.defense
            attacked.life -= damage
            message += attacked.name + " received " + \
                str(damage) + " points of damage."

        # if defense surpass attack, get retaliation damage
        # in attacker monster
        elif power < attacked.defense:
            damage = attacked.defense - power
            message += self.inflict_retaliation_damage(
                damage)
        
        # attack and defense are equal
        else:
            message += "No damage inflicted."

        return message

    def get_attacking_power(self, attacked):
        """
        Get attaking power when attacking attacked monster,
        considering type advantages, if in the rules.
        """
        # if type advantage is enabled
        if type_adv:
            # case advantage
            if self.has_advantage(attacked):
                return self.attack + 10
            # case disadvantage
            elif self.has_disadvantage(attacked):
                return self.attack - 10
            # case neutral
            else:
                return self.attack
        # case type advantage is disabled
        else:
            return self.attack

    def inflict_retaliation_damage(self, damage):
        """
        Inflict the damage for attacking a defending monster
        that has higher defense that the attack of the 
        attacker. Note: should consider different rules.
        """
        # case retaliation damage is activated
        if retal_dmg:
            self.life -= damage
            message = self.name + " received " + \
                str(damage) + \
                " points of damage in retaliation."
        # case retaliation damage deactivated
        else:
            message = "No damage inflicted."

        return message
            
    def has_advantage(self, attacked):
        """
        Check if monster has type advantage over attacked 
        monster. This can be implemented easily by checking
        the reverse condition, ie, if the attacked has 
        disadvantage (tht is already implemented).
        """
        return attacked.has_disadvantage(self)

    def is_monster(self):
        return True

    # default advantage functions
    def has_advantage_over_spellcaster(self):
        return False
    def has_advantage_over_warrior(self):
        return False
    def has_advantage_over_undead(self):
        return False
    def has_advantage_over_beast(self):
        return False
    def has_advantage_over_dragon(self):
        return False

    def stringify_prebattle(self, attacked):
        """
        Return a string that describes an attack on an 
        opponent monster so that the opponent can make a 
        decision to defend or not.
        """
        string = ""

        # type advantage information, if in the rules
        if self.has_advantage(attacked) and type_adv:
            string += self.name + " has advantage over " \
                + attacked.name + ".\n"
        if self.has_disadvantage(attacked) and type_adv:
            string += self.name + " has disadvantage over " \
                + attacked.name + ".\n"

        # attaking power information
        power = self.get_attacking_power(attacked)
        string += self.name + " is attacking with " + \
            str(power) + " points."

        return string

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
    get the string version of an attribute (attack or 
    defense) styled in a way to show buff, debuff or normal
    case.
    """
    string = str(current)
    if current > original: # buff style
        string = color(string, Fore.CYAN)
    elif current < original: # debuff style
        string = color(string, Fore.RED)

    return string.rjust(2)
