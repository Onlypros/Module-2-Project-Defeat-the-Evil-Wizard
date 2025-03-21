import random

from Characters import Character

class EvilWizard(Character): # EvilWizard class (inherits from Character)
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power. Not sure why this was created in the starter code but leaving the dmg as is for balancing.
        self.first_ability = "Summon minions"
        self.second_ability = "None"

    def unique_ability_1(self, opponent):
        #added 12.5% chance for wizard to summon minions for more damage
        print(f"{self.name} casts {self.first_ability}")
        attack_message = (f"\n{self.name} screams with rage and casts {self.first_ability}\n"
        f"The minions swarm {opponent.name} overwhelming them and deal 35 damage!")
        opponent.health = max(0, opponent.health -35)
        super().attack_ability(attack_message, opponent)

    # def unique_ability_2(self):
    #     pass add later?
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health = min(self.health + 5, self.max_health)  # Lower regeneration amount. Not sure why this was created in the starter code but leaving the regen as is for balancing.
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}/{self.max_health}.")

    def attack(self, opponent):
        #now using max(0,opponent.health) so the health never shows up as a negative number because thats not how it would in a real game
        #added 25% to apply 10 addiontal elemental damage
        if random.randint(1,4) == 1:
            self.bonus_damage =10    
            print(f"{self.name} channels his evil powers, adding void damage to his attack (+10 bonus damage)!")
        super().attack(opponent)
        #todo extra blank like when he adds void damage and when the attack then happens after it bothers me