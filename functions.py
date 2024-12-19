from mapdisplay import *
from loadmap import *
# from graphics import demo
from dataclasses import dataclass, field

max_x, max_y, min_x, min_y = 10, 10, 1, 1

hersheys_found = False
onecard_found = False
keys_found = False
focaldead = False
focaldeadmap2 = False




def print_map(map):
    for row in map:
        print(row)
def update_map(map, current, visited):

    # Create a new map display with updates for visited and current positions
    updated_map = []
    for row_idex, row in enumerate(map, start=1):
        row_list = list(row)  # Convert row string to a list for modification
        for col_idex in range(len(row_list)):
            # Mark previously visited places
            if (col_idex + 1, row_idex) == current:
                row_list[col_idex] = "*"
            elif (col_idex + 1, row_idex) in visited:
                row_list[col_idex] = "_"
            # Mark the current position

        updated_map.append(''.join(row_list))  # Convert back to string
    return updated_map


def current_place(player):
    return f"({player.x}, {player.y})"

def goal_reachedmap1(player) -> bool:
    goal_x, goal_y = 4, 10
    if (player.x, player.y) == (goal_x, goal_y):
        if not keys_found or not onecard_found:
            print("You can't exit Map 1 without the key and the OneCard!\nGo back to"
                  "look for what you are missing.")
            return False
        return True
    return False

def goal_reachedmap2(player) -> bool:
    goal_x, goal_y = 1, 10
    return (player.x, player.y) == (goal_x, goal_y)



def goal_reachedmap3(player) -> bool:
    goal_x, goal_y = 4, 10
    return (player.x, player.y) == (goal_x, goal_y)



def onecard(player) -> bool:
    onecard_x, onecard_y = 5, 2
    global onecard_found
    if (player.x, player.y) == (onecard_x, onecard_y) and not onecard_found:
        onecard_found = True
        return True
    else:
        return False

def hilleskey(player) -> bool:
    hilleskey_x, hilleskey_y = 9, 2
    global keys_found
    if (player.x, player.y) == (hilleskey_x, hilleskey_y) and not keys_found:
        keys_found = True
        return True
    else:
        return False

def hersheys(player) -> bool:
    hersheys_x, hersheys_y = 5, 3
    global hersheys_found
    if (player.x, player.y) == (hersheys_x, hersheys_y) and not hersheys_found:
        hersheys_found = True
        return True
    else:
        return False


def reset_visited(visited):
    visited.clear()



# Movement check functions
def can_go_north(currentmap, player) -> bool:
    return min_y < player.y and currentmap.get((player.x, player.y - 1), 1) == 1

def can_go_south(currentmap,player) -> bool:
    return player.y < max_y and currentmap.get((player.x, player.y + 1), 1) == 1

def can_go_east(currentmap, player) -> bool:
    return player.x < max_x and currentmap.get((player.x + 1, player.y), 1) == 1

def can_go_west(currentmap, player) -> bool:
    return min_x < player.x and currentmap.get((player.x - 1, player.y), 1) == 1

# Movement actions
def go_north(currentmap, player, visited):
    if can_go_north(currentmap, player):
        visited.add((player.x, player.y))
        player.y -= 1
        print(f"You moved north to {current_place(player)}")
    else:
        print("You can't go north!")

def go_south(currentmap, player, visited):
    if can_go_south(currentmap, player):
        visited.add((player.x, player.y))
        player.y += 1
        print(f"You moved south to {current_place(player)}")

    else:
        print("You can't go south!")

def go_east(currentmap, player, visited):
    if can_go_east(currentmap, player):
        visited.add((player.x, player.y))
        player.x += 1
        print(f"You moved east to {current_place(player)}")

    else:
        print("You can't go east!")

def go_west(currentmap, player, visited):
    if can_go_west(currentmap, player):
        visited.add((player.x, player.y))
        player.x -= 1
        print(f"You moved west to {current_place(player)}")

    else:
        print("You can't go west!")


def linux_cat_game(player):
    reach_x, reach_y = 4, 9
    global focaldead
    if (player.x, player.y) == (reach_x, reach_y) and not focaldead:
        focaldead = True
        return True
    else:
        return False


def linux_cat_gamemap2(player):
    reach_x, reach_y = 4, 7
    global focaldeadmap2
    if (player.x, player.y) == (reach_x, reach_y) and not focaldeadmap2:
        focaldeadmap2 = True
        return True
    else:
        return False



@dataclass
class Player:
    name: str  = "" # Player's name
    health: int = 80  # Starting health (initialized as 80)
    inventory: list = field(default_factory=list) # Empty inventory at the start
    x: int = 1  # Initial position on the map
    y: int = 1

    def reset_position(self):
        self.x = 1
        self.y = 1  # Reset to default position

    def show_stats(self):

        stats = f"""
        Player: {self.name}
        Health: {self.health}
        Position: {self.x, self.y}
        Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}
        """
        print(stats)

    def modify_health(self, amount: int):

        self.health += amount
        self.health = max(0, self.health)  # Ensure health doesn't drop below 0
        if self.health == 0:
            print(f"{self.name} has perished! Game over :((")
        elif amount > 0:
            print(f"{self.name} gained {amount} health!")
        else:
            print(f"{self.name} lost {abs(amount)} health!")

    def take_damage(self, damage: int):

        print(f"{self.name} was attacked and lost {damage} health!")
        self.modify_health(-damage)

    def add_item(self, item: str):

        self.inventory.append(item)
        print(f"{item} added to inventory.")

        # Adjust health based on the item
        if item.lower() == "water":
            self.modify_health(20)  # Healing item

    def check_inventory(self):

        inventory = ", ".join(self.inventory) if self.inventory else "Empty"
        print(f"Inventory: {inventory}")


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

focal_fossa = Enemy(name="Focal Fossa", health=100)

def battlemap1(player_health, focal_fossa):
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
                return battlemap1(100, Enemy(name="Focal Fossa", health=100))
            else:
                print("You chose not to restart. Game over!")
                break
                exit()
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
            return battlemap1(100, Enemy(name="Focal Fossa", health=100))
        else:
            print("You chose not to restart. Game over!")
            return

    return player_health, focal_fossa


import random

def focal_fossa_battlemap2(player_health):
    print("\n--- Focal Fossa Battle ---")
    print("Focal Fossa challenges you again! Strategically counter its attacks.")
    print("Survive by making correct choices. Each wrong or invalid choice costs energy!")
    print("Successfully counter 5 attacks to win, or lose if energy drops to 0 :(\n")

    # Player resources
    tools = {"Debugger": 2, "Firewall": 2, "Encryption Key": 2}
    successful_counters = 0  # Tracks the number of successful defenses

    # Define possible attacks and required tools
    attack_tool_mapping = {
        "Firewall Breach": "Firewall",
        "Encrypted Puzzle": "Encryption Key",
        "Corrupted Code": "Debugger",
        "Logic Overload": "Debugger",
        "Malware Injection": "Firewall"
    }

    # Track the count of each attack
    attack_counts = {attack: 0 for attack in attack_tool_mapping.keys()}
    max_attacks_per_type = 1  # Limit each attack type to appear no more than twice

    # Keep playing until energy is 0 or all 5 attacks are countered
    while player_health > 0 and successful_counters < 5:
        # Randomly select an attack, ensuring it hasn't been used more than twice
        available_attacks = [attack for attack, count in attack_counts.items() if count < max_attacks_per_type]
        if not available_attacks:
            print("No more valid attacks left. Ending the game!")
            break

        attack = random.choice(available_attacks)
        attack_counts[attack] += 1

        print(f"Focal Fossa uses {attack}!")
        print("Choose a tool to counter the attack:")
        print("1: Debugger")
        print("2: Firewall")
        print("3: Encryption Key")

        # Player's choice
        choice = input("Enter your choice (1, 2, or 3): ")
        choice_mapping = {"1": "Debugger", "2": "Firewall", "3": "Encryption Key"}
        selected_tool = choice_mapping.get(choice, None)

        # Handle invalid input or depleted tools
        if selected_tool is None:
            print("Invalid choice! Please choose a valid tool.")
            player_health -= 20
        elif tools[selected_tool] == 0:
            print(f"No uses left for {selected_tool}!")
            player_health -= 20
        elif selected_tool == attack_tool_mapping[attack]:
            print(f"Well done! The {selected_tool} counters the {attack}!")
            tools[selected_tool] -= 1
            successful_counters += 1
        else:
            print(f"Wrong choice! The {attack} damages you!")
            player_health -= 20

        print(f"\n--- Current Status ---\nEnergy: {player_health}\nTools: {tools}\n")

    # Determine game outcome
    if successful_counters == 5:
        print("Congratulations! You've successfully countered all of Focal Fossa's attacks and won!")

    if player_health <= 0:
        print("You have died. Focal Fossa overwhelmed you. Game over!")
        restart = input("Press 'r' to restart: ")
        if restart.lower().strip() == 'r':
            return focal_fossa_battlemap2(80)
        else:
            print("You chose not to restart. Game over!")
            exit()




