import random

def generate_random_maze(width, height):
    # Create an empty grid with walls
    maze = [['#' for _ in range(width)] for _ in range(height)]

    # Starting point is at top-left corner
    start = (1, 1)
    maze[start[0]][start[1]] = 'S'

    # End point is at bottom-right corner (on the opposite side)
    end = (height - 2, width - 2)
    maze[end[0]][end[1]] = 'E'

    # Randomly remove walls to create paths, but ensure walls block the middle
    def carve_paths(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < height - 1 and 0 < ny < width - 1 and maze[nx][ny] == '#':
                maze[nx][ny] = ' '
                maze[x + dx][y + dy] = ' '
                carve_paths(nx, ny)

    # Carve paths starting from the start point
    carve_paths(start[0], start[1])

    # Ensure the end point is accessible by carving paths towards it
    carve_paths(end[0], end[1])

    # Add some random walls in the middle to make it challenging
    for i in range(3, height - 3):
        for j in range(3, width - 3):
            if maze[i][j] == ' ' and random.random() < 0.2:
                maze[i][j] = '#'

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
    width = 60
    height = 20
    maze, start, end = generate_random_maze(width, height)

    # Print the maze
    print_maze(maze)

    # Player movement logic
    current_pos = start
    directions = ['up', 'down', 'left', 'right']

    while current_pos != end:
        move = input("Enter your move (up, down, left, right): ").lower()

        # Check if the move is valid
        if move not in directions:
            print("Invalid move. Choose from 'up', 'down', 'left', 'right'.")
            continue

        # Calculate new position based on the move
        x, y = current_pos
        if move == 'up' and x > 0 and maze[x - 1][y] != '#':
            current_pos = (x - 1, y)
        elif move == 'down' and x < height - 1 and maze[x + 1][y] != '#':
            current_pos = (x + 1, y)
        elif move == 'left' and y > 0 and maze[x][y - 1] != '#':
            current_pos = (x, y - 1)
        elif move == 'right' and y < width - 1 and maze[x][y + 1] != '#':
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

# Run the maze game
if __name__ == "__main__":
    random_maze_game()
