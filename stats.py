class Player:
    def _init_(self, name: str, starting_position: tuple[int, int]):
        """
        Initialize a player with basic attributes.
        :param name: Name of the player.
        :param starting_position: Starting position (x, y).
        """
        self.name = name  # Player's name
        self.health = 100  # Starting health (initialized as 100)
        self.inventory = []  # Empty inventory at the start
        self.position = starting_position  # Initial position on the map

    def show_stats(self):
        """
        Display the player's current stats.
        """
        stats = f"""
        Player: {self.name}
        Health: {self.health}
        Position: {self.position}
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