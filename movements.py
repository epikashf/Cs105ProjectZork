from LoadMapsDict import coordinates


def current_location():
    current = coordinates[(4, 0)]

    if user_response.lower == "west" or "w" or "left" or 'l':
        current = go_west()
        return current



    if user_response.lower == "east" or "e" or "right" or 'r':
        current = go_east()
        return current

    if user_response.lower == "north" or "n" or "up" or'u':
        current = go_north()
        return current

    if user_response.lower == "south" or "s" or "down" or 'd':
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












