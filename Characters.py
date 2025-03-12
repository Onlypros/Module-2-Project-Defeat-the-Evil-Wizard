import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name.title() #added title() to the name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.bonus_damage = 0  #added bonus damage to use in unique abilites
        self.miss = False # added to make miss/evades work
        self.miss_message = "" # added to make miss/evades work
        self.reduced_damage = 1 #added to allow damage reduction buffs
        self.ability_1_cooldown = 0 #added cooldowns for more rpg reaslism and balancing 
        self.ability_2_cooldown = 0 #added cooldowns for more rpg reaslism and balancing 
        self.potion_cooldown = 0 #potion spamming would be too cheap cooldown added for balancing

    def attack(self, opponent):
        damage = random.randint(0, self.attack_power)# randomizes the damage
        # print(f"damage = {damage} and reduced damage = {self.reduced_damage}")
        total_damage = round((damage + self.bonus_damage) * opponent.reduced_damage)
        # print(f"total damage = {total_damage}")
        # print(f"self bonus damage before = {self.bonus_damage}")
        opponent.health -= total_damage
        # print(f"self bonus damage after = {self.bonus_damage}")
        opponent.health = max (0, opponent.health) #makes sure health never shows a negative number like a real game

        #reworked attack messaging to make it more precise
        attack_message = f"\n{self.name} attacks {opponent.name} for {total_damage} damage!"
        if opponent.health == 0:
            print(f"{attack_message} {opponent.name} has {opponent.health} health left!")
            print(f"{opponent.name} has been defeated!")
        else:
            print(f"{attack_message} {opponent.name} has {opponent.health}/{opponent.max_health} health left.")

        self.bonus_damage = 0 #added bonus damage to use in unique abilites
        opponent.reduced_damage = 1 #adds the ability to reduce damamge
        # print(f"self bonus damage after 2 = {self.bonus_damage}")

    def attack_ability(self, attack_message, opponent):
        if opponent.health == 0:
            print(f"{attack_message} {opponent.name} has {opponent.health} health left!")
            print(f"{opponent.name} has been defeated!")
        else:
            print(f"{attack_message} {opponent.name} has {opponent.health}/{opponent.max_health} health left.")

    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def potion(self):  # created a basic healing ability using potions
        heal_amount = 25
        self.health += heal_amount
        if self.health > self.max_health: #cant health past max health
            self.health = self.max_health
            print(f"\n{self.name} uses a potion to restore themselves to their max health of {self.max_health}.")
        else:
            print(f"\n{self.name} uses a potion to restore {heal_amount} health. Health is now at {self.health}/{self.max_health}.")

    #adds unique abilities to the subclasses 
    def unique_ability_1(self):
        pass

    def unique_ability_2(self):
        pass

class Warrior(Character): # Warrior class (inherits from Character)
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power. Not sure why starter code says that. Left as it for my game balancing.
        self.first_ability = "Warrior's Resolve"
        self.first_ability_description = "Increases your max health by 15 and attack power by 5."
        self.second_ability = "Savage Blow"
        self.second_ability_description = f"{self.name} gives out a mighty roar and adds +30 damage to your next attack!"
    
    def unique_ability_1(self):
        self.health += 15
        self.max_health += 15
        self.attack_power += 5
        print(f"\n{self.name} uses {self.first_ability}")
        print(f"{self.name}'s max health increases to {self.max_health} and attack power increases to {self.attack_power}!")
        
    def unique_ability_2(self):
        self.bonus_damage = 30
        print(f"\n{self.name} uses {self.second_ability}")
        print(f"{self.second_ability_description}")
        
class Mage(Character): # Mage class (inherits from Character)
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power. Not sure why starter code says that. Left as it for my game balancing.
        self.first_ability = "Fireball"
        self.first_ability_description = f"Casts a fireball hitting the Evil Wizard for 40 damage."
        self.second_ability = "Sheep"
        self.second_ability_description = f"Turns your target into a sheep for one turn."

    def unique_ability_1(self, opponent):
        attack_message = f"\n{self.name} casts {self.first_ability} and deals 40 damage to {opponent.name}!"
        opponent.health = max(0, opponent.health - 40)
        self.attack_ability(attack_message, opponent)

    def unique_ability_2(self, opponent):
        opponent.miss = True
        opponent.miss_message = f"{opponent.name} is unable to attack while in sheep form."
        print(f"\n{self.name} casts {self.second_ability}. Turning {opponent.name} into a sheep for one turn!")
        print(f"\n{opponent.name} has {opponent.health}/{opponent.max_health} health left.")

class Archer(Character): # Archer class (inherits from Charater)
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.first_ability = "Full Draw"
        self.first_ability_description = "Draw your bow near its limit and do 40 damage. "
        self.second_ability = "Evade"
        self.second_ability_description = "Evade the next attack."

    def unique_ability_1(self, opponent):
        attack_message = f"\n{self.name} draws with all their might and releases a mighty arrow dealing 40 damage!"
        opponent.health = max(0, opponent.health - 40)
        self.attack_ability(attack_message, opponent)

    def unique_ability_2(self, opponent):
        opponent.miss = True
        print(f"\n{self.name} uses their heightened relexes to evade the incoming attack!")
        opponent.miss_message = f"{opponent.name} misses his attack." 
        # print(f"{self.name} uses {self.second_ability}")
        print(f"\n{opponent.name} has {opponent.health}/{opponent.max_health} health left.")
        
class Paladin(Character): # Paladin class (inherits from Character)
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
        self.first_ability = "Smite"
        self.first_ability_description = "Unleash your holy powers to deal 25 bonus damage."
        self.second_ability = "Divine Protection"
        self.second_ability_description = "Reduce the next attack by 75%."

    def unique_ability_1(self, opponent):
        print(f"\n{self.name} casts {self.first_ability} to deal 25 bonus holy damage!")
        self.bonus_damage = 25
        self.attack(opponent)
        
    def unique_ability_2(self):
        self.reduced_damage = 0.25
        print(f"\n{self.name} casts {self.second_ability}.")
        print(f"{self.second_ability_description}")

class DarkKnight(Character): # Dark Knight class (inherits from Character)
    #need to finish flushing out this class
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=30)
        self.first_ability = "Drain Life"
        self.first_ability_description = "Drains 25 health from target and heals you for 20 health."
        self.second_ability = "Blood Pact"
        self.second_ability_description = "Sacrifice 25 health to empower your attack with 35 bonus damage."

    def unique_ability_1(self, opponent):
        attack_message = f"\n{self.name} casts {self.first_ability}, draining 25 health from The Evil Wizard and healing for 20 health."
        opponent.health = max(0, opponent.health - 25)
        self.health += 20
        if self.health > self.max_health:
            self.health = self.max_health

        self.attack_ability(attack_message, opponent)
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}.")

    def unique_ability_2(self, opponent):
        print(f"{self.name} casts {self.second_ability} sacrificing 25 health to empower their attack with 35 blood damage!")
        self.health -= 25
        self.bonus_damage = 30
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}.")
        self.attack(opponent)

class Summoner(Character): # Summoner class (inherits from Character)
    #can add in the future
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)
        self.first_ability = "None"
        self.first_ability_description = "None"
        self.second_ability = "None"
        self.second_ability_description = "None"

    def unique_ability_1(self):
        # offensive summon
        pass

    def unique_ability_2(self):
        # defensive summon
        pass