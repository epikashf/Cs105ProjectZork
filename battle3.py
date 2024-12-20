import random

def logic_gates_challenge():
    print("\nStage 1: Logical Gates Challenge")
    print("The enemy is trying to overwhelm you with binary logic! Identify the correct logic gate.\n")

    logic_gate_data = [
        {"inputs": ("1010", "1100"), "output": "1000", "gate": "AND"},
        {"inputs": ("1010", "1100"), "output": "1110", "gate": "OR"},
        {"inputs": ("1010",), "output": "0101", "gate": "NOT"}
    ]
    random.shuffle(logic_gate_data)
    for data in logic_gate_data:
        inputs = " , ".join(data["inputs"]) if len(data["inputs"]) > 1 else data["inputs"][0]
        print(f"Inputs: {inputs}")
        print(f"Output: {data['output']}")
        response = input("Which logic gate is this? (AND/OR/NOT): ").strip().upper()
        if response != data["gate"]:
            print(f"Incorrect! The correct answer was {data['gate']}.")
            return False
    print("Great work! You've passed Stage 1.\n")
    return True


# Stage 2: The Mysterious Puzzle Box
def counter_hack_challenge():
    print("\nStage 2: The Mysterious Puzzle Box")
    print(
        "You’ve found a strange box in the middle of the battlefield. It’s locked with a combination, and only by solving its clues will you open it.\n")
    print("Each clue brings you closer to unlocking the mystery. Figure it out!")

    # Puzzle clues
    clues = [
        {"clue": "The first number is how many sides a triangle has.", "answer": "3"},
        {"clue": "The second number is the number of letters in the word 'elephant'.", "answer": "8"},
        {"clue": "The third number is how many legs a spider has.", "answer": "8"},
        {"clue": "The fourth number is the number of days in a week.", "answer": "7"},
        {"clue": "The fifth number is the number of planets in our solar system (not counting Pluto!).", "answer": "8"}
    ]

    # Shuffle clues for randomness
    random.shuffle(clues)

    print("Here are your clues:\n")
    for i, clue in enumerate(clues, 1):
        print(f"Clue {i}: {clue['clue']}")

    print("\nNow, guess the correct combination to unlock the box. Type the numbers in order.\n")

    # Player guesses the combination
    guesses = []
    for i in range(5):
        guess = input(f"Guess the digit #{i + 1} in the combination: ").strip()  # Update prompt to make it more clear
        guesses.append(guess)

    # Check if the guesses match the correct combination
    correct_combination = ["3", "8", "8", "7", "8"]
    if guesses == correct_combination:
        print("\nCongratulations! You’ve unlocked the mysterious box and revealed a hidden treasure inside!")
        return True
    else:
        print("\nThe box remains locked. Looks like you missed the right combination. Try again!")
        return False


# Stage 3: Jumbled Cipher Challenge
def jumbled_cipher_challenge():
    print("\nStage 3: Jumbled Cipher Challenge")
    print("The enemy is hiding the key in scrambled words! Unscramble them to finish the fight.\n")

    cs_words = [
        "algorithm", "binary", "function",
        "variable", "python", "array",
        "loop", "class", "object", "network"
    ]
    selected_words = random.sample(cs_words, 5)
    scrambled_dict = {scramble_word(word): word for word in selected_words}

    correct_guesses = 0
    for scrambled, actual in scrambled_dict.items():
        print(f"Jumbled word: {scrambled}")
        guess = input("Your guess: ").strip().lower()
        if guess == actual:
            print("Correct!\n")
            correct_guesses += 1
        else:
            print(f"Wrong! The correct word was: {actual}\n")

    print(f"You unscrambled {correct_guesses} out of {len(scrambled_dict)} words.")
    return correct_guesses == len(scrambled_dict)


# Helper function to scramble words
def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)


# Stage 4: Maze generation function
def generate_maze(width, height):
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
def maze_challenge():
    print("Stage 4: Maze Challenge")
    print("You’ve entered a dark maze! Navigate from S to E to escape.")

    # Maze size is 20x20
    width = 20
    height = 20
    maze, start, end = generate_maze(width, height)

    # Print the maze
    print_maze(maze)

    # Player movement logic
    current_pos = start
    directions = ['up', 'down', 'left', 'right', 'u', 'd', 'l', 'r', 'e', 'w', 'n', 's']

    while current_pos != end:
        move = input("Enter your move (up, down, left, right): ").lower().strip()

        # Check if the move is valid
        if move not in directions:
            print("Invalid move. Choose from 'up', 'down', 'left', 'right'.")
            continue

        # Calculate new position based on the move
        x, y = current_pos
        if move in ["up", "u", "n"] and x > 0 and maze[x - 1][y] != '#':
            current_pos = (x - 1, y)
        elif move in ["down", "d", "s"] and x < height - 1 and maze[x + 1][y] != '#':
            current_pos = (x + 1, y)
        elif move in ["left", "l", "w"] and y > 0 and maze[x][y - 1] != '#':
            current_pos = (x, y - 1)
        elif move in ["right", "r", "e"] and y < width - 1 and maze[x][y + 1] != '#':
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


# Final Battle: All stages
def final_battle():
    print("Welcome to the Final Battle! Complete all four stages to defeat the enemy and win.\n")

    stages = [logic_gates_challenge, counter_hack_challenge, jumbled_cipher_challenge, maze_challenge]
    stage_names = ["Stage 1: Logical Gates Challenge", "Stage 2: The Mysterious Puzzle Box",
                   "Stage 3: Jumbled Cipher Challenge", "Stage 4: Maze Challenge"]

    current_stage = 0
    while current_stage < len(stages):
        print(f"\nYou are now at {stage_names[current_stage]}")
        stage_completed = stages[current_stage]()
        if stage_completed:
            if current_stage == len(stages) - 1:  # Last stage
                print("\nYou have defeated the final battle and won the game!")
                return
            else:
                print(f"Great job! You've completed {stage_names[current_stage]}. Moving to the next stage.\n")
                current_stage += 1
        else:
            print(f"You failed {stage_names[current_stage]}. Press 'r' to restart this stage or 'q' to quit the game.")
            retry = input().strip().lower()
            if retry == 'r':
                print(f"\nRestarting {stage_names[current_stage]}...\n")
                continue
            else:
                print("Game Over. Better luck next time!")
                return


#
# # Run the final battle
# if __name__ == "__main__":
#     final_battle()


