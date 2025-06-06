import random
from collections import deque

def generate_random_maze(width, height, allowed_coordinates):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    start = (1, 1)
    maze[start[0]][start[1]] = 'S'

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

    carve_paths(start[0], start[1])

    def get_reachable_cells():
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] in [' ', 'S']:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        return visited

    reachable = get_reachable_cells()

    # Compute distances from S to all reachable cells
    def get_distances_from_S():
        dist = {start: 0}
        q = deque([start])
        while q:
            cx, cy = q.popleft()
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) in reachable and (nx, ny) not in dist:
                    dist[(nx, ny)] = dist[(cx, cy)] + 1
                    q.append((nx, ny))
        return dist

    dist_map = get_distances_from_S()
    # Select the farthest reachable cell from S as the exit
    end_cell = max(dist_map, key=dist_map.get)
    maze[end_cell[0]][end_cell[1]] = 'E'

    return maze, start, end_cell


# Display function to print the maze
def print_maze(maze):
    for row in maze:
        print(" ".join(row))


# Maze challenge logic
def random_maze_game():
    print("Stage 4: Maze Challenge")
    print("You’ve entered a dark maze! Navigate from S to E to escape.")

    # Maze size
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


if __name__ == "__main__":
    random_maze_game()



