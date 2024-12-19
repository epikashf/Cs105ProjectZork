from mapdisplay import *
from functions import *
from stats import *
from savefile import *
# from graphics import demo
# from asciimatics import *

# Player starting position

# game loop using these functions
def game_loop():

    maps = [map_1, map_2, map_3] # List of maps
    mapdisplays = [map_1display, map_2display, map_3display]
    print("Welcome to Hilles game!")
    filename = None
    current_map_index = 0

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


            user_input = input("> ").strip().lower()

            if user_input == "current":
                print(current_place(p1))
            elif user_input in ["north", "n", "up", "u"]:
                go_north(currentmap, p1)
            elif user_input in ["south", "s", "down", "d"]:
                go_south(currentmap, p1)
            elif user_input in ["east", "e", "right", "r"]:
                go_east(currentmap, p1)
            elif user_input in ["west", "w", "left", "l"]:
                go_west(currentmap, p1)
            elif user_input == "stats":
                p1.show_stats()
            elif user_input == "save":
                if filename:
                    save_game(p1, filename)
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


            # Check for goal
            if goal_reached(p1):
                print("Congratulations! You've reached your goal!")


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

                if linux_cat_game(p1):
                    battlemap1(p1.health, focal_fossa)
                    continue

            if currentmap == map_2:

                if linux_cat_gamemap2(p1):
                    focal_fossa_battlemap2(p1.health)
                    continue

            if currentmap == map_3:
                pass


            if currentmap == map_1 and goal_reached(p1):
                print("Map 1 completed! Moving to Map 2.")
                p1.reset_position()  # Reset position for a new game
                reset_visited()
                current_map_index += 1
                break
            if currentmap == map_2 and goal_reached(p1):
                print("Map 2 completed! Moving to Map 3.")
                p1.reset_position()  # Reset position for a new game
                reset_visited()
                current_map_index += 1
                break
            if currentmap == map_3 and goal_reached(p1):
                print("Map 3 completed! Congratulations!")
                break
# Run the game

game_loop()

