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
            print(f"{self.name} attacks {opponent.name} for {damage} damage! {opponent.name} has {0} health left!")
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
        self.max_health += 25
        self.attack_power += 10
        print(f"{self.name} uses their first special ability: {self.first_ability}.")
        print(f"{self.name}'s max health increases to {self.max_health} and attack power increases to {self.attack_power}!")

    def unique_ability_2(self):
        self.bonus_damage = 15
        print(f"{self.name} uses their second special ability: {self.second_ability}.")
        print(f"{self.second_ability_description}")
        
# Mage class (inherits from Character)
class Mage(Character):
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
            print(f"{opponent.name} has {opponent.health} health left!")
            print(f"{opponent.name} has been defeated!")
        else:
            print(f"{opponent.name} now has {opponent.health}/{opponent.max_health} health left.")

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

# Function to create player character based on user input
def create_character():
    # class_choice now correctly only accepts valid inputs
    print("\nChoose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin 
    
    while True:
        class_choice = input("\nEnter the number of your class choice: ").strip()
        if class_choice in ('1', '2', '3', '4'):
            break
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
        
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        # Add Archer class here
        pass
    elif class_choice == '4':
        # Add Paladin class here
        pass
        
# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print(f"2. Unique ability #1 {player.first_ability} - {player.first_ability_description}")
        print(f"3. Unique ability #2 {player.second_ability} - {player.second_ability_description}")
        print("4. Use a potion to heal 20 health")
        print("5. View Stats")
        
        choice = input("\nChoose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Call the special ability here
            player.unique_ability_1()
            pass  # Implement this
        elif choice == '3':
            # Call the special ability here
            player.unique_ability_2()
            pass  # Implement this
        elif choice == '4':
            # Call the heal method here
            player.potion(player)
            # pass  # Implement this
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            random_ability_1 = random.randint(1, 8)
            wizard.regenerate()
            #added 12.5% chance for wizard to summon minions for more damage
            if random_ability_1 == 1:
                wizard.unique_ability_1(player)
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()