import random

from Characters import Character

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
        self.first_ability = "Summon minions"
        self.second_ability = "None"

    def unique_ability_1(self, opponent):
        #added 12.5% chance for wizard to summon minions for more damage
        print(f"{self.name} casts {self.first_ability}")
        print(f"The minions swarm {opponent.name} overwhelming them and deal 35 damage!")
        opponent.health -= 35
        opponent.health = max (0, opponent.health)

        if opponent.health == 0:
            print(f"\n{opponent.name} has {opponent.health} health left!")
            print(f"{opponent.name} has been defeated!")
        else:
            print(f"\n{opponent.name} now has {opponent.health}/{opponent.max_health} health left.")

    def unique_ability_2(self):
        pass
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        #now using max(0,opponent.health) so the health never shows up as a negative number because thats not how it would in a real game
        random_element = random.randint(1, 4)
        # print(f"random element {random_element}")

        if random_element == 1:
            self.bonus_damage = 10
        else:
            self.bonus_damage = 0

        if self.bonus_damage == 10:
            print(f"\n{self.name} adds void damage to his attack for an additional 10 damage!")

        damage = random.randint(0, self.attack_power) 
        total_damage = damage + self.bonus_damage
        # print(f"damamge - bonus power {damage} + {self.bonus_damage}")
        opponent.health -= total_damage
        opponent.health = max (0, opponent.health)

        attack_message = f"{self.name} attacks {opponent.name} for {total_damage} damage! "
        if opponent.health == 0:
            print(f"{attack_message}{opponent.name} has {opponent.health} health left!")
            print(f"{opponent.name} has been defeated!")
        else:
            print(f"{attack_message}{opponent.name} has {opponent.health}/{opponent.max_health} health left.")