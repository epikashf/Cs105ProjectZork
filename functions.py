from map import map1

x, y = 5, 1
max_x, max_y, min_x, min_y = 10, 4, 1, 1


def current_place():
    """Returns the player's current location."""
    return f"({x}, {y})"

def goal_reached() -> bool:
    """Checks if the player has reached the goal location."""
    goal_x, goal_y = 6, 4
    return (x, y) == (goal_x, goal_y)

def onecard() -> bool:
    """Checks if the player has reached the goal location."""
    onecard_x, onecard_y = 9, 2
    return (x, y) == (onecard_x, onecard_y)

def hilleskey() -> bool:
    """Checks if the player has reached the goal location."""
    hilleskey_x, hilleskey_y = 9, 2
    return (x, y) == (hilleskey_x, hilleskey_y)

def hersheys() -> bool:
    """Checks if the player has reached the goal location."""
    hersheys_x, hersheys_y = 5, 3
    return (x, y) == (hersheys_x, hersheys_y)


# Movement check functions
def can_go_north() -> bool:
    """Checks if the player can move north."""
    return min_y < y and map1.get((x, y - 1), 1) == 1

def can_go_south() -> bool:
    """Checks if the player can move south."""
    return y < max_y and map1.get((x, y + 1), 1) == 1

def can_go_east() -> bool:
    """Checks if the player can move east."""
    return x < max_x and map1.get((x + 1, y), 1) == 1

def can_go_west() -> bool:
    """Checks if the player can move west."""
    return min_x < x and map1.get((x - 1, y), 1) == 1

# Movement actions
def go_north():
    """Moves the player north if possible."""
    global y
    if can_go_north():
        y -= 1
        print(f"You moved north to {current_place()}")
    else:
        print("You can't go north!")

def go_south():
    """Moves the player south if possible."""
    global y
    if can_go_south():
        y += 1
        print(f"You moved south to {current_place()}")
    else:
        print("You can't go south!")

def go_east():
    """Moves the player east if possible."""
    global x
    if can_go_east():
        x += 1
        print(f"You moved east to {current_place()}")
    else:
        print("You can't go east!")

def go_west():
    """Moves the player west if possible."""
    global x
    if can_go_west():
        x -= 1
        print(f"You moved west to {current_place()}")
    else:
        print("You can't go west!")
