import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        #added title() to the name, bonus damage 
        self.name = name.title()
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.bonus_damage = 0

    def attack(self, opponent):
        #added an else statement so the health never shows up as a negative number because thats not how it would in a real game
        damage = random.randint(0, self.attack_power) + self.bonus_damage
        self.bonus_damage = 0
        opponent.health -= damage
        if opponent.health <= 0:
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage! {opponent.name} has {0} health left!")
            print(f"{opponent.name} has been defeated!")
        else:
             print(f"{self.name} attacks {opponent.name} for {damage} damage! {opponent.name} has {opponent.health}/{opponent.max_health} health left.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def potion(self, heal):
        self.heal = 20
        self.health += self.heal
        if self.health > self.max_health:
            self.health = self.max_health
            print(f"{self.name} uses a potion to restore themselves to their max health of {self.max_health}.")
        else:
            print(f"{self.name} uses a potion to restore {self.heal} health. Health is now at {self.health}/{self.max_health}.")

    #adds unique abilities to the subclasses 
    def unique_ability_1(self):
        pass

    def unique_ability_2(self):
        pass

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
        self.first_ability = "Warrior's Resolve"
        self.first_ability_description = "Increases your max health by 25 and attack power by 10." #remove the 10 attack power?
        self.second_ability = "Savage Blow"
        self.second_ability_description = f"{self.name} gives out a mighty roar and adds +15 damage to his next attack!"

    # Add your power attack method here
    def unique_ability_1(self):
        self.max_health += 25 #also heal for 25? do i want to make it so this can only be used one time per game?
        self.attack_power += 10
        print(f"{self.name} uses their first special ability: {self.first_ability}")
        print(f"{self.name}'s max health increases to {self.max_health} and attack power increases to {self.attack_power}!")

    def unique_ability_2(self):
        self.bonus_damage = 15  #this doesnt right just yet i need to adjust troubleshoot
        print(f"{self.name} uses their second special ability: {self.second_ability}")
        print(f"{self.second_ability_description}")
        
# Mage class (inherits from Character)
class Mage(Character):
    #need to finish flushing out this class
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power
        self.first_ability = "None"
        self.first_ability_description = "None"
        self.second_ability = "None"
        self.second_ability_description = "None"

    # Add your cast spell method here
    def unique_ability_1(self):
        pass

    def unique_ability_2(self):
        pass

# Archer class (inherits from Charater)
class Archer(Character):
    #need to finish flushing out this class
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        self.first_ability = "None"
        self.first_ability_description = "None"
        self.second_ability = "None"
        self.second_ability_description = "None"

    def unique_ability_1(self):
        pass

    def unique_ability_2(self):
        pass

# Paladin class (inherits from Character)
class Paladin(Character):
    #need to finish flushing out this class
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        self.first_ability = "None"
        self.first_ability_description = "None"
        self.second_ability = "None"
        self.second_ability_description = "None"

    def unique_ability_1(self):
        pass

    def unique_ability_2(self):
        pass

# Dark Knight class (inherits from Character)
class DarkKnight(Character):
    #need to finish flushing out this class
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=40)
        self.first_ability = "None"
        self.first_ability_description = "None"
        self.second_ability = "None"
        self.second_ability_description = "None"

    def unique_ability_1(self):
        pass

    def unique_ability_2(self):
        pass

# Summoner class (inherits from Character)
class Summoner(Character):
    #need to finish flushing out this class
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=10)
        self.first_ability = "None"
        self.first_ability_description = "None"
        self.second_ability = "None"
        self.second_ability_description = "None"

    def unique_ability_1(self):
        pass

    def unique_ability_2(self):
        pass