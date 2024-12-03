from dataclasses import dataclass
from LoadMapsDict import coordinates, loadmap
from typing import List


print("Hello there!")
print("Welcome to Hilles Hall where you have Python for lunch and Java for Dinner")
print("You have been programming all night upstairs and you've been locked up")
print("You are looking for keys to get out of the Lab H204")
print("Enter up, down, left or r1ight to move around")

done: bool = False
while not done:
        user_response = input("> ")
        if user_response == "map":
                print(loadmap)


def current_location():
    current = coordinates[(4, 0)]
    if user_response.lower == "west" or "w" or "left" or 'l':
        current = go_west()
        return current

    elif user_response.lower == "east" or "e" or "right" or 'r':
        current = go_east()
        return current

    elif user_response.lower == "north" or "n" or "up" or'u':
        current = go_north()
        return current

    elif user_response.lower == "south" or "s" or "down" or 'd':
        current = go_south()
        return current

def go_west():
    coordinates[(x - 1, y)]
    current_location()


def go_east():
    current_location()  # x+1


def go_north():
    current_location()  # y+1


def go_south():
    current_location()  # y-1









@dataclass #decorater

class Character:
        x: int
        y: int
        name: str

class GameMap:
        map: list
        player: Character
        enemies: list

 #       def can_go_north(self):


