import random

# Function to generate initial grid with matches
def generate_initial_grid(rows, cols):
    symbols = ['+', '-', '*', '/']
    grid = [[random.choice(symbols) for _ in range(cols)] for _ in range(rows)]
    
    # Ensure there are matches initially
    for i in range(rows):
        for j in range(cols - 2):
            if grid[i][j] == grid[i][j + 1] == grid[i][j + 2]:
                grid[i][j], grid[i][j+1] = random.sample(symbols, 2)
    
    for j in range(cols):
        for i in range(rows - 2):
            if grid[i][j] == grid[i + 1][j] == grid[i + 2][j]:
                symbols_copy = symbols.copy()
                symbols_copy.remove(grid[i][j])
                grid[i][j] = random.choice(symbols_copy)
                
    return grid

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Function to check if there are any matches
def check_matches(grid):
    rows = len(grid)
    cols = len(grid[0])
    matches = set()

    # Check horizontal matches
    for i in range(rows):
        for j in range(cols - 2):
            if grid[i][j] == grid[i][j + 1] == grid[i][j + 2]:
                matches.add((i, j))
                matches.add((i, j + 1))
                matches.add((i, j + 2))

    # Check vertical matches
    for i in range(rows - 2):
        for j in range(cols):
            if grid[i][j] == grid[i + 1][j] == grid[i + 2][j]:
                matches.add((i, j))
                matches.add((i + 1, j))
                matches.add((i + 2, j))

    return matches

# Function to remove matches and update the grid
def remove_matches(grid, matches):
    for row, col in matches:
        grid[row][col] = ' '

# Function to drop symbols and fill empty spaces
def drop_symbols(grid):
    rows = len(grid)
    cols = len(grid[0])

    for j in range(cols):
        for i in range(rows - 1, -1, -1):
            if grid[i][j] == ' ':
                for k in range(i, 0, -1):
                    grid[k][j] = grid[k - 1][j]
                grid[0][j] = random.choice(['+', '-', '*', '/'])

def play_game():
    rows = 7
    cols = 8
    score = 0

    # Generate initial grid
    grid = generate_initial_grid(rows, cols)

    for frame in range(100):
        print("\nFrame", frame + 1)
        print_grid(grid)

        # Check matches
        matches = check_matches(grid)

        # If no matches found, break the loop
        if not matches:
            break

        # Remove matches and update the grid
        remove_matches(grid, matches)

        # Increment score based on number of matches
        score += len(matches)

        # Drop symbols and fill empty spaces
        drop_symbols(grid)

    return grid, score

def main():
    # Play the game
    final_grid, final_score = play_game()

    # Print final grid
    print("\nFinal Grid:")
    print_grid(final_grid)

    # Print final score
    print("Final Score:", final_score)

if __name__ == "__main__":
    main()
