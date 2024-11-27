from LoadMapsDict import coordinates
from MainGame import user_int


def current_location():
    current = coordinates[(4, 0)]
    if user_input.lower == "west", "w", "left", 'l':
        current = go_west() v


    if user_input.lower == "east", "e", "right", 'r':
        current = go_east()


    if user_input.lower == "north", "n", "up", 'u':
        current = go_north()

    if user_input.lower == "south", "s", "down", 'd':
        current = go_south()

        return current



def go_west():
    current_location() #x-1


def go_east():
    current_location()  # x+1


def go_north():
    current_location()  # y+1


def go_south():
    current_location()  # y-1












