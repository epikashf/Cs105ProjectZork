from map import *
from dataclasses import dataclass, field

visited = set()
max_x, max_y, min_x, min_y = 10, 10, 1, 1
global x, y
x, y = 1, 1
hersheys_found = False
onecard_found = False
keys_found = False


def print_map(map):
    for row in map:
        print(row)
def update_map(map, current, visited):
    current = x, y
    # Create a new map display with updates for visited and current positions
    updated_map = []
    for row_idex, row in enumerate(map, start=1):
        row_list = list(row)  # Convert row string to a list for modification
        for col_idex in range(len(row_list)):
            # Mark previously visited places
            if (col_idex + 1, row_idex) == current:
                row_list[col_idex] = "*"
            elif (row_idex, col_idex + 1) in visited:
                row_list[col_idex] = "_"
            # Mark the current position

        updated_map.append(''.join(row_list))  # Convert back to string
    return updated_map


def modify_map(map, row, col, new_value):
    # Convert the specified row into a list
    row_list = list(map[row - 1])
    # Modify the specific column
    row_list[col - 1] = str(new_value)
    # Convert the row back to a string and update the mapdisplay
    map[row - 1] = ''.join(row_list)

def current_place():
    """Returns the player's current location."""
    return f"({x}, {y})"

def goal_reached() -> bool:
    """Checks if the player has reached the goal location."""
    goal_x, goal_y = 10, 4
    return (x, y) == (goal_x, goal_y)

def onecard() -> bool:
    """Checks if the player has reached the goal location."""
    onecard_x, onecard_y = 5, 2
    global onecard_found
    if (x, y) == (onecard_x, onecard_y) and not onecard_found:
        onecard_found = True
        return True
    else:
        return False

def hilleskey() -> bool:
    """Checks if the player has reached the goal location."""
    hilleskey_x, hilleskey_y = 9, 2
    global keys_found
    if (x, y) == (hilleskey_x, hilleskey_y) and not keys_found:
        keys_found = True
        return True
    else:
        return False

def hersheys() -> bool:
    """Checks if the player has reached the goal location."""
    hersheys_x, hersheys_y = 5, 3
    global hersheys_found
    if (x, y) == (hersheys_x, hersheys_y) and not hersheys_found:
        hersheys_found = True
        return True
    else:
        return False







# Movement check functions
def can_go_north() -> bool:
    """Checks if the player can move north."""
    return min_y < y and mapdict.get((x, y - 1), 1) == 1

def can_go_south() -> bool:
    """Checks if the player can move south."""
    return y < max_y and mapdict.get((x, y + 1), 1) == 1

def can_go_east() -> bool:
    """Checks if the player can move east."""
    return x < max_x and mapdict.get((x + 1, y), 1) == 1

def can_go_west() -> bool:
    """Checks if the player can move west."""
    return min_x < x and mapdict.get((x - 1, y), 1) == 1

# Movement actions
def go_north():
    """Moves the player north if possible."""
    global y
    if can_go_north():
        visited.add((y, x))
        y -= 1
        print(f"You moved north to {current_place()}")
        #modify_map(mapdisplay, y, x, "_")

    else:
        print("You can't go north!")

def go_south():
    """Moves the player south if possible."""
    global y
    if can_go_south():
        visited.add((y, x))
        y += 1
        print(f"You moved south to {current_place()}")
        #modify_map(mapdisplay, y, x, "_")

    else:
        print("You can't go south!")

def go_east():
    """Moves the player east if possible."""
    global x
    if can_go_east():
        visited.add((y, x))
        x += 1
        print(f"You moved east to {current_place()}")
        #modify_map(mapdisplay, y, x, "_")

    else:
        print("You can't go east!")

def go_west():
    """Moves the player west if possible."""
    global x
    if can_go_west():
        visited.add((y, x))
        x -= 1
        print(f"You moved west to {current_place()}")
        #modify_map(mapdisplay, y, x, "_")

    else:
        print("You can't go west!")


def linux_cat_game():
    reach_x, reach_y = 4, 9
    return (x, y) == (reach_x, reach_y)




@dataclass
class Player:
    name: str  = "" # Player's name
    health: int = 80  # Starting health (initialized as 80)
    inventory: list = field(default_factory=list) # Empty inventory at the start
    position = current_place() # Initial position on the map

    def show_stats(self):
        """
        Display the player's current stats.
        """
        stats = f"""
        Player: {self.name}
        Health: {self.health}
        Position: {current_place()}
        Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}
        """
        print(stats)

    def modify_health(self, amount: int):
        """
        Modify the player's health.
        :param amount: Amount to adjust health (positive to heal, negative to damage).
        """
        self.health += amount
        self.health = max(0, self.health)  # Ensure health doesn't drop below 0
        if self.health == 0:
            print(f"{self.name} has perished! Game over :((")
        elif amount > 0:
            print(f"{self.name} gained {amount} health!")
        else:
            print(f"{self.name} lost {abs(amount)} health!")

    def take_damage(self, damage: int):
        """
        Subtract health from the player when attacked.
        :param damage: Amount of damage to deal to the player.
        """
        print(f"{self.name} was attacked and lost {damage} health!")
        self.modify_health(-damage)

    def add_item(self, item: str):
        """
        Add an item to the player's inventory and adjust health if applicable.
        :param item: The item to add.
        """
        self.inventory.append(item)
        print(f"{item} added to inventory.")

        # Adjust health based on the item
        if item.lower() == "water":
            self.modify_health(20)  # Healing item

    def check_inventory(self):
        """
        Display the player's inventory.
        """
        inventory = ", ".join(self.inventory) if self.inventory else "Empty"
        print(f"Inventory: {inventory}")




@dataclass
class Weapon:
    name: str
    valid_choices: list  # Valid choices for health decreases (e.g., [10, 20] for keyboard)

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

def battle(player_health, focal_fossa):
    print \
        ("You were about to leave Hilles Room 204, but in front of you, Focal Fossa: the Linux cat is blocking your way.")
    print("Make sure that Focal Fossa's health goes exactly to zero. If not, you will lose!\n")

    # Weapon selection and rules
    print("Choose which weapon you want to use to fight Focal Fossa.")
    print("1. Keyboard - works for 10 or 20 points.")
    print("2. Wire - works for 10 or 5 points.")
    print("3. Monitor - works for 10 or 30 points.")

    weapon_choice = input("Choose your weapon (1, 2, or 3): ")

    if weapon_choice == "1":
        weapon = Weapon("Keyboard", [10, 20])
    elif weapon_choice == "2":
        weapon = Weapon("Wire", [10, 5])
    elif weapon_choice == "3":
        weapon = Weapon("Monitor", [10, 30])
    else:
        print("Invalid choice! Defaulting to Keyboard (10 or 20 points).")
        weapon = Weapon("Keyboard", [10, 20])

    print(f"\nGood choice! You chose the {weapon.name}. This weapon only works for the following health decreases:")
    print(f"Valid decreases for {weapon.name}: {weapon.valid_choices}")
    print("Now, let's start the battle!\n")

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

        if target_presses not in weapon.valid_choices:
            print \
                (f"Oops! {weapon.name} doesn't work for {target_presses} points. You lose 10 health for the wrong input.")
            player_health -= 10
            continue

        print(f"\nYou need to press {choice} exactly {target_presses} times.")

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
            go_south()
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


