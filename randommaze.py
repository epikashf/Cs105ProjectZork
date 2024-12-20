import random


def generate_random_maze(width, height, allowed_coordinates):
    # Create an empty grid with walls
    maze = [['#' for _ in range(width)] for _ in range(height)]

    # Starting point is at top-left corner
    start = (1, 1)
    maze[start[0]][start[1]] = 'S'

    # End point is at bottom-right corner (on the opposite side)
    end = (height - 3, width - 2)
    maze[end[0]][end[1]] = 'E'

    # Convert allowed_coordinates to a set for fast lookup
    allowed_set = set(allowed_coordinates)

    # Randomly carve paths within allowed coordinates
    def carve_paths(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if (nx, ny) in allowed_set and maze[nx][ny] == '#':
                maze[nx][ny] = ' '
                maze[x + dx][y + dy] = ' '
                carve_paths(nx, ny)

    # Carve paths starting from the start point
    carve_paths(start[0], start[1])

    # Ensure the end point is accessible
    carve_paths(end[0], end[1])

    return maze, start, end


# Display function to print the maze
def print_maze(maze):
    for row in maze:
        print(" ".join(row))


# Maze challenge logic
def random_maze_game():
    print("Stage 4: Maze Challenge")
    print("You’ve entered a dark maze! Navigate from S to E to escape.")

    # Maze size is 50x20
    width = 20
    height = 15

    # Define allowed coordinates where the maze can be carved
    allowed_coordinates = [
        (x, y)
        for x in range(1, height - 1, 2)
        for y in range(1, width - 1, 2)
    ]

    # Generate the maze with specific allowed coordinates
    maze, start, end = generate_random_maze(width, height, allowed_coordinates)

    # Print the maze
    print_maze(maze)

    # Player movement logic
    current_pos = start
    directions = ['up', 'down', 'left', 'right', 'u', 'd', 'l', 'r', 'e', 'w', 'n', 's']

    while current_pos != end:
        move = input("Enter your move (u for up, d for down, r for right, l for left): ").lower()

        # Check if the move is valid
        if move not in directions:
            print("Invalid move. Choose from 'up', 'down', 'left', 'right'.")
            continue

        # Calculate new position based on the move
        x, y = current_pos
        if move in ['u', 'up', 'n'] and x > 0 and maze[x - 1][y] != '#':
            current_pos = (x - 1, y)
        elif move in ['d', 'down', 's'] and x < height - 1 and maze[x + 1][y] != '#':
            current_pos = (x + 1, y)
        elif move in ['l', 'left', 'w'] and y > 0 and maze[x][y - 1] != '#':
            current_pos = (x, y - 1)
        elif move in ['r', 'right', 'e'] and y < width - 1 and maze[x][y + 1] != '#':
            current_pos = (x, y + 1)
        else:
            print("You can't move in that direction, there's a wall.")
            continue

        # Display updated maze
        print("\nYou are now at position:", current_pos)
        maze_copy = [row[:] for row in maze]  # Create a copy to avoid modifying the original maze
        maze_copy[current_pos[0]][current_pos[1]] = 'P'  # Mark player's position
        print_maze(maze_copy)

    print("Congratulations! You've reached the exit!")
    return True  # Add return statement to indicate the stage was completed


