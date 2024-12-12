import json
import os
from functions import *
from functions import Player

def save_game(player, filename="game_save.json"):
    game_state = {
        "name": player.name,
        "health": player.health,
        "position_x": player.x,
        "position_y": player.y,
        "inventory": player.inventory
    }
    with open(filename, 'w') as file:
        json.dump(game_state, file)



# Loading the game state from a file (example with JSON)
def load_game(filename="game_save.json"):
    try:
        with open(filename, 'r') as file:
            state = json.load(file)
            return state
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return None

# Example of how to load the game and apply the loaded state to the player
def apply_game_state(player, game_state):
    if game_state:
        player.name = game_state.get("name", player.name)
        player.health = game_state.get("health", player.health)  # Default to current health if not found
        player.x = game_state.get("position_x", player.x)
        player.y = game_state.get("position_y", player.y)  # Default to current position if not found
        player.inventory = game_state.get("inventory", player.inventory)


def start_new_game():
    p1 = Player()  # Initialize player with default health and position
    print("Starting a new game...")
    print("Whats your name?")
    p1.name = input("> ")
    print("Welcome to Hilles Hall where you have Python for lunch and Java for Dinner")
    print("You have been programming all night upstairs and you've been locked up")
    print("You are looking for keys to get out of the Lab H204")
    return p1


def list_saved_games():
    saved_games = []
    for f in os.listdir():
        if f.startswith("game_") and f.endswith(".json"):
            saved_games.append(f)
    if saved_games:
        print("Saved games:")
        for idx, game in enumerate(saved_games, 1):
            print(f"{idx}. {game}")

        return saved_games
    else:
        print("No saved games found.")
        return []
