# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        #added title() to the name
        self.name = name.title()
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        #added an else statement so the health never shows up as a negative number because thats not how it would in a real game
        opponent.health -= self.attack_power
        if opponent.health <= 0:
            print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage! {opponent.name} has {0} health left!")
            print(f"{opponent.name} has been defeated!")
        else:
             print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage! {opponent.name} has {opponent.health}/{opponent.max_health} health left.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def potion(self, heal):
        self.heal = 20
        self.health += self.heal
        if self.health >= self.max_health:
            print(f"{self.name} uses a potion to restore themselves to their max health of {self.max_health}.")
        else:
            print(f"{self.name} uses a potion to restore {self.heal} health. Health is now at {self.health}/{self.max_health}.")

    def unique_ability_1(self):
        pass

    def unique_ability_2(self):
        pass

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here
    def unique_ability_1(self):
        #added the first unique ability for this class
        self.first_ability = "Warrior's Resolve"
        self.max_health += 25
        self.attack_power += 10
        print(f"{self.name} uses their first special ability: {self.first_ability}.")
        print(f"{self.name}'s max health increases to {self.max_health} and attack power increases to {self.attack_power}!")

    def savage_blow(self):
        pass


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Add your cast spell method here


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin 
    
    class_choice = input("\nEnter the number of your class choice: ")
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
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use 1st Special Ability")
        print("3. Use 2nd Special Ability")
        print("4. Heal")
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
            wizard.regenerate()
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