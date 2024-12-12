from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    damage: int


@dataclass
class Enemy:
    name: str
    health: int

    def take_damage(self, damage: int):
        self.health -= damage
        print(f"{self.name}'s health is now {self.health}")

    def is_alive(self):
        return self.health > 0


def battle(player_health, focal_fossa):
    print(
        "You were about to leave Hilles Room 204, but in front of you, Focal Fossa: the Linux cat is blocking your way.")
    print("Make sure that Focal Fossa's health goes exactly to zero. If not, you will lose!\n")

    # Weapon selection
    print("Choose which weapon you want to use to fight Focal Fossa.")
    print("1. Keyboard - to bang it on its head")
    print("2. Wire - to strangle Focal Fossa")
    print("3. Monitor - to hit Focal Fossa")

    weapon_choice = input("Choose your weapon (1, 2, or 3): ")

    if weapon_choice == "1":
        weapon = Weapon("Keyboard", 10)
    elif weapon_choice == "2":
        weapon = Weapon("Wire", 15)
    elif weapon_choice == "3":
        weapon = Weapon("Monitor", 12)
    else:
        print("Invalid choice! Defaulting to Keyboard.")
        weapon = Weapon("Keyboard", 10)

    print(f"Good choice! You chose the {weapon.name}. Now, let's start the battle!\n")

    while player_health > 0 and focal_fossa.is_alive():
        print(f"\nYour health: {player_health}")
        print(f"{focal_fossa.name}'s health: {focal_fossa.health}")

        # Prompt the player for their action
        print("\nNow, choose a number to press according to the health decrease:")
        print("Press 1 for a decrease of 10 points.")
        print("Press 2 for a decrease of 20 points.")
        print("Press 3 for a decrease of 30 points.")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice not in ["1", "2", "3"]:
            print("Invalid choice! You lose 10 health for the wrong input.")
            player_health -= 10
            continue

        target_presses = int(choice)  # The number the player needs to press

        print(f"\nNow press {choice} exactly {target_presses} times on different lines.")

        # Player needs to press the correct number the right number of times
        number_presses = 0
        while number_presses < target_presses:
            player_input = input("Press the number: ")

            if player_input == choice:
                number_presses += 1
            else:
                print(f"You pressed the wrong key! You lose 10 health.")
                player_health -= 10
                break

        if number_presses == target_presses:
            damage = target_presses * 10
            print(f"Good job! Focal Fossa's health decreases by {damage} points.")
            focal_fossa.take_damage(damage)

        # Check if the health of Focal Fossa goes negative and the player did not manage to hit exactly 0
        if focal_fossa.health < 0:
            print("Uh-oh! You made a mistake. Focal Fossa's health did not reach exactly zero!")
            print("Since you didn't exactly get to 0, you lose the game. Press 'r' to restart.")
            restart = input("Press 'r' to restart: ")
            if restart.lower() == 'r':
                return battle(100, Enemy(name="Focal Fossa", health=100))
            else:
                print("You chose not to restart. Game over!")
                break

        # Check if the health is exactly zero and the player wins
        if focal_fossa.health == 0:
            print("\nYou have defeated Focal Fossa!")
            break

        # Check if the player loses
        if player_health <= 0:
            print("Game Over! You have been defeated by Focal Fossa!")
            break

    # Restart prompt if the player loses
    if player_health <= 0:
        print("\nGame Over! Press 'r' to restart.")
        restart = input("Press 'r' to restart: ")
        if restart.lower() == 'r':
            return battle(100, Enemy(name="Focal Fossa", health=100))
        else:
            print("You chose not to restart. Game over!")
            return

    return player_health, focal_fossa


# Initialize player health and Focal Fossa's health
player_health = 100
focal_fossa = Enemy(name="Focal Fossa", health=100)

# Start the battle
player_health, focal_fossa = battle(player_health, focal_fossa)