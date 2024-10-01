# Python program for A* Search Algorithm
import math
import heapq


# Function for reading the source and destination coordinates. No need to modify this function.
# It is called from inside the main() function.

def read_src_dest_from_file(input_file):
    try:
        # Reading the content of the input file
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
            src = eval(lines[0].strip())
            dest = eval(lines[1].strip())
        return src, dest

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
        return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


# Define the Cell class

class Cell:
    def __init__(self):
      # Parent cell's row index
        self.parent_i = 0
    # Parent cell's column index
        self.parent_j = 0
 # Total cost of the cell (g + h)
        self.f = float('inf')
    # Cost from start to this cell
        self.g = float('inf')
    # Heuristic cost from this cell to destination
        self.h = 0


# Define the size of the grid
ROW = 9
COL = 10

# Check if a cell is valid (within the grid)


def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# Check if a cell is unblocked


def is_unblocked(grid, row, col):
    return grid[row][col] == 1

# Check if a cell is the destination


def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# Calculate the heuristic value of a cell (Euclidean distance to destination)

def calculate_h_value(row, col, dest):
    return math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2)

# Trace the path from source to destination

def trace_path(cell_details, dest):
    print("The Path is ")
    path = []
    row = dest[0]
    col = dest[1]

    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    path.append((row, col))
    path.reverse()

    for i in path:
        print("->", i, end=" ")
    print()

# Implement the A* search algorithm

def a_star_search(grid, src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or the destination is blocked")
        return

    # Check if we are already at the destination
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return

    # Initialize the closed list (visited cells)
    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    # Initialize the start cell details
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        p = heapq.heappop(open_list)
        i, j = p[1], p[2]
        closed_list[i][j] = True

        # Generate all possible children
        for add_i, add_j in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            next_i, next_j = i + add_i, j + add_j
            if is_valid(next_i, next_j) and is_unblocked(grid, next_i, next_j) and not closed_list[next_i][next_j]:
                if is_destination(next_i, next_j, dest):
                    cell_details[next_i][next_j].parent_i = i
                    cell_details[next_i][next_j].parent_j = j
                    print("The destination cell is found")
                    trace_path(cell_details, dest)
                    found_dest = True
                    return

                else:
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(next_i, next_j, dest)
                    f_new = g_new + h_new

                    if cell_details[next_i][next_j].f == float('inf') or cell_details[next_i][next_j].f > f_new:
                        heapq.heappush(open_list, (f_new, next_i, next_j))
                        cell_details[next_i][next_j].f = f_new
                        cell_details[next_i][next_j].g = g_new
                        cell_details[next_i][next_j].h = h_new
                        cell_details[next_i][next_j].parent_i = i
                        cell_details[next_i][next_j].parent_j = j

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")


# Driver Code

def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    # Paths to read from an input file
    
    input_file = "Sample IO/io1/in.txt"
    # input_file = "Sample IO/io2/in.txt"
    # input_file = "Sample IO/io3/in.txt"

    # Read from input file and store variables
    src, dest = read_src_dest_from_file(input_file)

    # Run the A* search algorithm
    a_star_search(grid, src, dest)


if __name__ == "__main__":
    main()
