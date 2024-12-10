from map import *
from functions import *
from stats import *

# Player starting position


# game loop using these functions
def game_loop():
    p1 = Player()
    """Main game loop."""
    print("Welcome to the game!")
    print("Whats your name?")
    p1.name = input(">")
    print("Type 'north', 'south', 'east', or 'west' to move.")
    print("Type 'quit' to exit the game.")

    while True:
        global mapdisplay
        current = x, y
        mapdisplay = update_map(mapdisplay, current, visited)

        user_input = input("> ").strip().lower()

        if user_input == "current":
            print(current_place())
        elif user_input == "map":
            print("Here is the map:")
            print_map(mapdisplay)
        elif user_input in ["north", "n", "up", "u"]:
            go_north()
        elif user_input in ["south", "s", "down", "d"]:
            go_south()
        elif user_input in ["east", "e", "right", "r"]:
            go_east()
        elif user_input in ["west", "w", "left", "l"]:
            go_west()
        elif user_input == "stats":
            p1.show_stats()
        elif user_input == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input! Try again.")


        # Check for goal
        if goal_reached():
            print("Congratulations! You've reached the goal!")
            break

        if hilleskey():
            print("You have a key now!")
            p1.add_item("Hilles Key")
            continue
            #Append key to inventory

        if onecard():
            print("You found your One Card!")
            p1.add_item("One Card")
            #Append one card to inventory
            continue

        if hersheys():
            print("You found Hersheys and you ate it!")
            print("Health +10")
            p1.modify_health(10)
            continue

        if linux_cat_game():
            battle(p1.health, focal_fossa)


# Run the game
game_loop()