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
        self.bonus_damage = 35
        super().attack(opponent)

    def unique_ability_2(self):
        pass
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        #now using max(0,opponent.health) so the health never shows up as a negative number because thats not how it would in a real game
        #added 25% to apply 10 addiontal elemental damage
        if random.randint(1,4) == 1:
            self.bonus_damage =10    
            print(f"\n{self.name} adds void damage to his attack for an additional 10 damage!")

        super().attack(opponent)