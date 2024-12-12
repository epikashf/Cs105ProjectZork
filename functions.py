from map import *
from loadmap import *
from dataclasses import dataclass, field

max_x, max_y, min_x, min_y = 10, 10, 1, 1

hersheys_found = False
onecard_found = False
keys_found = False
focaldead = False
visited = set()




def print_map(map):
    for row in map:
        print(row)
def update_map(map, current, visited):
    current = p1.x, p1.y
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


def current_place():
    """Returns the player's current location."""
    return f"({p1.x}, {p1.y})"

def goal_reached() -> bool:
    """Checks if the player has reached the goal location."""
    goal_x, goal_y = 4, 10
    return (p1.x, p1.y) == (goal_x, goal_y)

def onecard() -> bool:
    """Checks if the player has reached the goal location."""
    onecard_x, onecard_y = 5, 2
    global onecard_found
    if (p1.x, p1.y) == (onecard_x, onecard_y) and not onecard_found:
        onecard_found = True
        return True
    else:
        return False

def hilleskey() -> bool:
    """Checks if the player has reached the goal location."""
    hilleskey_x, hilleskey_y = 9, 2
    global keys_found
    if (p1.x, p1.y) == (hilleskey_x, hilleskey_y) and not keys_found:
        keys_found = True
        return True
    else:
        return False

def hersheys() -> bool:
    """Checks if the player has reached the goal location."""
    hersheys_x, hersheys_y = 5, 3
    global hersheys_found
    if (p1.x, p1.y) == (hersheys_x, hersheys_y) and not hersheys_found:
        hersheys_found = True
        return True
    else:
        return False







# Movement check functions
def can_go_north(currentmap) -> bool:
    """Checks if the player can move north."""
    return min_y < p1.y and currentmap.get((p1.x, p1.y - 1), 1) == 1

def can_go_south(currentmap) -> bool:
    """Checks if the player can move south."""
    return p1.y < max_y and currentmap.get((p1.x, p1.y + 1), 1) == 1

def can_go_east(currentmap) -> bool:
    """Checks if the player can move east."""
    return p1.x < max_x and currentmap.get((p1.x + 1, p1.y), 1) == 1

def can_go_west(currentmap) -> bool:
    """Checks if the player can move west."""
    return min_x < p1.x and currentmap.get((p1.x - 1, p1.y), 1) == 1

# Movement actions
def go_north(currentmap):
    """Moves the player north if possible."""
    if can_go_north(currentmap):
        visited.add((p1.x, p1.y))
        p1.y -= 1
        print(f"You moved north to {current_place()}")
    else:
        print("You can't go north!")

def go_south(currentmap):
    """Moves the player south if possible."""
    if can_go_south(currentmap):
        visited.add((p1.x, p1.y))
        p1.y += 1
        print(f"You moved south to {current_place()}")
        #modify_map(mapdisplay, y, x, "_")

    else:
        print("You can't go south!")

def go_east(currentmap):
    """Moves the player east if possible."""
    if can_go_east(currentmap):
        visited.add((p1.x, p1.y))
        p1.x += 1
        print(f"You moved east to {current_place()}")
        #modify_map(mapdisplay, y, x, "_")

    else:
        print("You can't go east!")

def go_west(currentmap):
    """Moves the player west if possible."""
    if can_go_west(currentmap):
        visited.add((p1.x, p1.y))
        p1.x -= 1
        print(f"You moved west to {current_place()}")
        #modify_map(mapdisplay, y, x, "_")

    else:
        print("You can't go west!")


def linux_cat_game():
    reach_x, reach_y = 4, 9
    global focaldead
    if (p1.x, p1.y) == (reach_x, reach_y) and not focaldead:
        focaldead = True
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
    def show_stats(self):

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

p1 = Player()

