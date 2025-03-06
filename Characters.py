import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name.title() #added title() to the name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.bonus_damage = 0  #added bonus damage to use in unique abilites
        self.miss = False
        self.miss_message = ""
        self.reduced_damage = 1

    def attack(self, opponent):
        damage = random.randint(0, self.attack_power)# randomizes the damage
        # print(f"damage = {damage}")
        total_damage = (damage + self.bonus_damage) * self.reduced_damage 
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
        self.reduced_damage = 0 #adds the ability to reduce damamge
        # print(f"self bonus damage after 2 = {self.bonus_damage}")

    def attack_ability(self, attack_message, opponent):
        if opponent.health == 0:
            print(f"{attack_message} {opponent.name} has {opponent.health} health left!")
            print(f"{opponent.name} has been defeated!")
        else:
            print(f"{attack_message} {opponent.name} has {opponent.health}/{opponent.max_health} health left.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def potion(self):  # created a basic healing ability using potions
        heal_amount = 20
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

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
        self.first_ability = "Warrior's Resolve 1/1"
        self.first_ability_description = "Increases your max health by 25." #remove the 10 attack power?
        self.second_ability = "Savage Blow"
        self.second_ability_description = f"{self.name} gives out a mighty roar and adds +15 damage to your next attack!"
#todo i want to make both of these abilites a one time use since they boost stats it would be broken if not
    # Add your power attack method here
    def unique_ability_1(self):
        self.max_health += 25 #also heal for 25? do i want to make it so this can only be used one time per game?
        # self.attack_power += 10
        # if 
        print(f"\n{self.name} uses their first special ability: {self.first_ability}")
        print(f"{self.name}'s max health increases to {self.max_health} and attack power increases to {self.attack_power}!")
        #  self.first_ability = "Warrior's Resolve 0/1"
        #  self.first_ability_description = "is no longer avaiable"

    def unique_ability_2(self):
        self.bonus_damage = 25
        print(f"{self.name} uses their second special ability: {self.second_ability}")
        print(f"{self.second_ability_description}")
        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power
        self.first_ability = "Fireball"
        self.first_ability_description = f"Casts a fireball hitting the Evil Wizard for 40 damage"
        self.second_ability = "Sheep"
        self.second_ability_description = f"Turns your target into a sheep for one turn."

    # Add your cast spell method here
    def unique_ability_1(self, opponent):
        attack_message = f"\n{self.name} casts {self.first_ability} and deals 40 damage to {opponent.name}!"
        opponent.health = max(0, opponent.health - 40)
        self.attack_ability(attack_message, opponent)

    def unique_ability_2(self, opponent):
        opponent.miss = True
        opponent.miss_message = f"{opponent.name} is unable to attack while in sheep form."
        print(f"\n{self.name} casts {self.second_ability}. Turning {opponent.name} into a sheep for one turn!"
        f"\n{opponent.name} has {opponent.health}/{opponent.max_health} health left.")

# Archer class (inherits from Charater)
class Archer(Character):
    #need to finish flushing out this class
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.first_ability = "Full Draw"
        self.first_ability_description = "Draw your bow near its limit and do 40 damage. "
        self.second_ability = "Evade"
        self.second_ability_description = "Evade the next attack."

    def unique_ability_1(self, opponent):
        attack_message = f"\n{self.name} draws with all their might and releases a mighty arrow!"
        opponent.health = max(0, opponent.health - 40)
        self.attack_ability(attack_message, opponent)

    def unique_ability_2(self, opponent):
        opponent.miss = True
        print(f"\n{self.name} uses their heighted relaxes to evade the incoming attack!")
        opponent.miss_message = f"{opponent.name} misses his attack." 
        # print(f"{self.name} uses {self.second_ability}")
        print(f"\n{opponent.name} has {opponent.health}/{opponent.max_health} health left.")
        
# Paladin class (inherits from Character)
class Paladin(Character):
    #need to finish flushing out this class
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)
        self.first_ability = "Smite"
        self.first_ability_description = "Unleash you holy powers to deal 20 bonus damage"
        self.second_ability = "Divine Protection"
        self.second_ability_description = "Reduce the next attack by 50%"

    def unique_ability_1(self, opponent):
        attack_message = f"\n{self.name} casts {self.first_ability} to deal 20 bonus damage to {opponent.name}!"
        self.bonus_damage = 20
        self.attack(opponent)

    def unique_ability_2(self):
        self.reduced_damage = 0.5
        print(f"{self.name} casts {self.second_ability}.")
        print(f"{self.second_ability_description}")

# Dark Knight class (inherits from Character)
class DarkKnight(Character):
    #need to finish flushing out this class
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=30)
        self.first_ability = "None"
        self.first_ability_description = "None"
        self.second_ability = "None"
        self.second_ability_description = "None"

    def unique_ability_1(self):
        #drain life
        pass

    def unique_ability_2(self):
        #blood pact
        pass

# Summoner class (inherits from Character)
class Summoner(Character):
    #need to finish flushing out this class
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