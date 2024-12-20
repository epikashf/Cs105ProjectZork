from mapdisplay import *
from functions import *
from savefile import *
from battle3 import final_battle
from randommaze import random_maze_game
from graphics import intro_graphics, outro_graphics
import os
from asciimatics.screen import Screen


# game loop using these functions
def game_loop():

    Screen.wrapper(intro_graphics)
    os.system('cls' if os.name == 'nt' else 'clear')

    maps = [map_1, map_2, map_3] # List of maps
    mapdisplays = [map_1display, map_2display, map_3display]
    print("Welcome to Hilles game!")
    filename = None
    current_map_index = 0
    visited = set()

    choice = input("Do you want to start a new game or load a saved game? (new/load): ").strip().lower()

    if choice == "load":
        saved_games = list_saved_games()

        if saved_games:
            game_choice = int(input("Enter the number of the game you want to load: ")) - 1
            if 0 <= game_choice < len(saved_games):
                game_file = saved_games[game_choice]
                loaded_game_state = load_game(game_file)
                if loaded_game_state:
                    p1 = Player()  # Initialize player with default values
                    apply_game_state(p1, loaded_game_state)
                    filename = game_file
                    current_map_index = loaded_game_state.get("current_map_index", 0)
                    visited = set(tuple(x) if isinstance(x, list) else x for x in loaded_game_state.get("visited", []))
                    print(f"Game '{game_file}' loaded successfully!")
                    print(f"Welcome back {p1.name}!")
                else:
                    print("Error loading the selected game.")
                    p1 = start_new_game()  # In case something went wrong, start a new game
            else:
                print("Invalid choice.")
                p1 = start_new_game()
        else:
            print("No saved games found.")
            p1 = start_new_game()  # If no saved games, start a new game
    else:
        p1 = start_new_game()

    while current_map_index < len(maps):  # Loop through all maps
        currentmap = maps[current_map_index]
        currentdisplay = mapdisplays[current_map_index]

        while True:
            current = p1.x, p1.y

            currentdisplay = update_map(currentdisplay, current, visited)
            mapdisplays[current_map_index] = currentdisplay
            print_map(currentdisplay)
            print("Enter N for North, S for South, E for East, W for West")
            print("Enter [help] for more instructions.")

            user_input = input("> ").strip().lower()

            if user_input == "current":
                print(current_place(p1))
            elif user_input == "help":
                print("Enter [stats] to see your current stats")
                print("Enter [current] to see your current position")
                print("Enter [save] to save your game")
                print("Enter [quit] to save and quit the game")
                print("Enter U or Up to go up, D or Down to go down, L or Left to go Left, R or Right to go Right")
                print("Enter N or North to go up, S or South to go down, W or West to go Left, E or East to go Right")
            elif user_input in ["north", "n", "up", "u"]:
                go_north(currentmap, p1, visited)
            elif user_input in ["south", "s", "down", "d"]:
                go_south(currentmap, p1, visited)
            elif user_input in ["east", "e", "right", "r"]:
                go_east(currentmap, p1, visited)
            elif user_input in ["west", "w", "left", "l"]:
                go_west(currentmap, p1, visited)
            elif user_input == "stats":
                p1.show_stats()
            elif user_input == "save":
                if filename:
                    save_game(p1, current_map_index, visited, filename)
            elif user_input == "quit":
                save_choice = input("Do you want to save your game? (yes/no): ").strip().lower()
                if save_choice == "yes":
                    if filename:  # Overwrite the existing file
                        save_game(p1, current_map_index, visited, filename)
                    else:
                        filename = input("Enter a filename to save your game (e.g., 'game_1'): ").strip()
                        filename = "game_" + filename + ".json"
                        save_game(p1, current_map_index, visited, filename)  # Save the game with a custom filename
                print("Thanks for playing! Goodbye!")
                exit()
            else:
                print("Invalid input! Try again.")

            if currentmap == map_1:
                if hilleskey(p1):
                    print("You have a key now!")
                    p1.add_item("Hilles Key")
                    continue

                if onecard(p1):
                    print("You found your One Card!")
                    p1.add_item("One Card")
                    continue

                if hersheys(p1):
                    print("You found Hersheys and you ate it!")
                    print("Health +10")
                    p1.modify_health(10)
                    continue
                if randommazemap1(p1):
                    random_maze_game()
                    continue

                if linux_cat_game(p1):
                    battlemap1(p1.health, focal_fossa)
                    continue

            if currentmap == map_2:

                if randommazemap2(p1):
                    random_maze_game()
                    continue

                if linux_cat_gamemap2(p1):
                    focal_fossa_battlemap2(p1)
                    continue

            if currentmap == map_3:

                if map_3_battlegame(p1):
                    final_battle()
                    continue


            if currentmap == map_1 and goal_reachedmap1(p1):
                print("You successfully left Lab H204! You're now in Hilles Hall.")
                p1.reset_position()  # Reset position for a new game
                reset_visited(visited)
                current_map_index += 1
                break
            if currentmap == map_2 and goal_reachedmap2(p1):
                print("You successfully left Lab H204! You're now trying to reach the Bus Stop to leave to Bryn Mawr.")
                p1.reset_position()  # Reset position for a new game
                reset_visited(visited)
                current_map_index += 1
                break
            if currentmap == map_3 and goal_reachedmap3(p1):
                Screen.wrapper(outro_graphics)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()


# Run the game

game_loop()

