from dataclasses import dataclass


print("Hello there!")
print("Welcome to Hilles Hall where you have Python for lunch and Java for Dinner")
print("You have been programming all night upstairs and you've been locked up")
print("You are looking for keys to get out of the library")


while True:
    user = input("Press any key to continue")
    user = input("Enter Up, Down, Left or Right to move around")



def main():
        done: bool = False
        while not done:
                user_response = input(">")




@dataclass #decorater

class Character:
        x: int
        y: int
        name: str

class GameMap:
        map: list[list[str]] = []
        player: Character
        enemies: list[Character]

        def can_go_north(self):


