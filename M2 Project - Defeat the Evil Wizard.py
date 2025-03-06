import random

from Characters import Warrior, Mage, Archer, Paladin, DarkKnight
from Evilwizard import EvilWizard

# Function to create player character based on user input
def create_character():
    # class_choice now correctly only accepts valid inputs
    print("\nChoose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin 
    print("5. Dark Knight") #add dark knight
    print("6. Summoner") #add summoner
    
    while True:
        class_choice = input("\nEnter the number of your class choice: ").strip()
        if class_choice in ('1', '2', '3', '4', '5', '6'):
            break
        print("Invalid choice. Please enter 1-6.")
        
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    elif class_choice == '5':
        return DarkKnight(name)
    elif class_choice == '6':
        # add summoner class here
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
        
        choice = input("\nChoose an action: ").strip()

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if player.first_ability in ["Fireball", "Sheep", "Full Draw", "Evade", "Smite"]:
                player.unique_ability_1(wizard)
            else:
                player.unique_ability_1()
        elif choice == '3':
            if player.second_ability in ["Warrior's Resolve", "Savage Blow", "Divine Protection"]:
                player.unique_ability_2()
            else:
                player.unique_ability_2(Wizard)
        elif choice == '4':
            # Call the heal method here
            player.potion()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.miss == True:
            print(f"{player.miss_message}")
            wizard.miss = False
            continue
        elif wizard.health > 0:
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