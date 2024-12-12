def loadMap(filename: str) -> list[list[int]]:
    """
    Reads a file containing a 2D map and returns it as a nested list of integers.

    Args:
        filename (str): The name of the file containing the map.

    Returns:
        list[list[int]]: A nested list representing the 2D map.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Parsing the dimensions from the first line (e.g., 10x10)
        dimensions = lines[0].strip().split('x')
        rows, cols = int(dimensions[0]), int(dimensions[1])

        # Creating the grid by parsing the remaining lines
        grid = []
        for line in lines[1:]:
            grid.append([int(char) for char in line.strip()])

        # Validate grid dimensions
        # if len(grid) != rows or any(len(row) != cols for row in grid):
        #     raise ValueError("The map dimensions do not match the specified size.")

        return grid

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def convert_to_string_list(map_data):
    return ["".join(map(str, row)) for row in map_data]


# Example usage
map_data = loadMap('map1.txt')

if map_data:
    for row in map_data:
        print(row)

