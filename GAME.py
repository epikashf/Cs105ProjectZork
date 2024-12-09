from map import *
from functions import *

# Player starting position
x, y = 5, 1
max_x, max_y, min_x, min_y = 10, 4, 1, 1


# Example game loop using these functions
def game_loop():
    """Main game loop."""
    print("Welcome to the game!")
    print("Type 'north', 'south', 'east', or 'west' to move.")
    print("Type 'quit' to exit the game.")

    while True:
        user_input = input("> ").strip().lower()

        if user_input == "current":
            print(current_place())
        elif user_input == "map":
            print(map1list)
        elif user_input in ["north", "n", "up", "u"]:
            go_north()
        elif user_input in ["south", "s", "down", "d"]:
            go_south()
        elif user_input in ["east", "e", "right", "r"]:
            go_east()
        elif user_input in ["west", "w", "left", "l"]:
            go_west()
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
            continue
            #Append key to inventory

        if onecard():
            print("You found your One Card!")
            #Append one card to inventory
            continue

        if hersheys():
            print("You found Hersheys and you ate it!")
            print("Health +10")
            # Health is added by 10
            continue


# Run the game
game_loop()