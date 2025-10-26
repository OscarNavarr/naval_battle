# -*- coding: utf-8 -*-
import random

# Icons
sea_icon = "🌊"
ship_icon = "⛵"
hit_icon = "💥"
miss_icon = "💦"

# 1) Create the 8x8 grid
def create_empty_grid():
    """Creates an empty 8x8 grid"""
    grid = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(' ')
        grid.append(row)
    return grid

# Place ships manually (for testing)
def place_ships_manually(grid):
    """Places 3 ships on the grid"""
    # Ship of 2 cells (horizontal on row 0)
    grid[0][1] = 'b'
    grid[0][2] = 'b'
    
    # Ship of 3 cells (vertical in column 3)
    grid[4][3] = 'b'
    grid[5][3] = 'b'
    grid[6][3] = 'b'
    
    # Ship of 4 cells (horizontal on row 7)
    grid[7][4] = 'b'
    grid[7][5] = 'b'
    grid[7][6] = 'b'
    grid[7][7] = 'b'
    
    return grid

# 3) Function to display the grid
def print_grid(grid):
    """Displays the grid in the console"""
    # Column headers
    print("  A  B  C  D  E  F  G  H")
    
    # Each row
    for row_index in range(8):
        row_display = str(row_index + 1) + " "
        for col_index in range(8):
            cell = grid[row_index][col_index]
            
            if cell == ' ':
                row_display += sea_icon + " "
            elif cell == 'b':
                row_display += ship_icon + " "
            elif cell == 'h':
                row_display += hit_icon + " "
            elif cell == 'm':
                row_display += miss_icon + " "
            else:
                row_display += sea_icon + " "
        
        print(row_display)

# 4) Function to send a missile
def send_missile_at(grid, row_index, column_index):
    """
    Sends a missile to the specified coordinates
    Returns True if it hits a ship, False otherwise
    """
    cell = grid[row_index][column_index]
    
    # Check if this cell has already been targeted
    if cell == 'h' or cell == 'm':
        print("⚠️  You already fired at this cell!")
        return None
    
    # Check if there is a ship
    if cell == 'b':
        grid[row_index][column_index] = 'h'
        print("💥 HIT!")
        return True
    else:
        grid[row_index][column_index] = 'm'
        print("💦 Miss...")
        return False

# 7) Function to ask the user for coordinates
def ask_send_missile(grid):
    """Asks the user for coordinates and fires"""
    print("\n--- Your turn ---")
    
    # Ask for column
    column_input = input("Enter column (A-H): ").upper()
    while column_input not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        print("Invalid column. Use A-H.")
        column_input = input("Enter column (A-H): ").upper()
    
    # Convert letter to index
    column_index = ord(column_input) - ord('A')
    
    # Ask for row
    row_input = input("Enter row (1-8): ")
    while not row_input.isdigit() or int(row_input) < 1 or int(row_input) > 8:
        print("Invalid row. Use 1-8.")
        row_input = input("Enter row (1-8): ")
    
    row_index = int(row_input) - 1
    
    # Fire
    send_missile_at(grid, row_index, column_index)

# 8) Function to check if the game is over
def is_game_over(grid):
    """Returns True if all ships have been sunk"""
    for row in grid:
        for cell in row:
            if cell == 'b':
                return False
    return True

# 9) Main function
def main():
    """Main game function"""
    print("=== BATTLESHIP ===\n")
    
    # Create and prepare the grid
    grid = create_empty_grid()
    grid = place_ships_manually(grid)
    
    # Shot counter
    shots = 0
    
    # Main game loop
    while not is_game_over(grid):
        print("\n" + "="*30)
        print_grid(grid)
        ask_send_missile(grid)
        shots += 1
    
    # End of game
    print("\n" + "="*30)
    print_grid(grid)
    print(f"\n VICTORY! You sank all ships in {shots} shots.")

# BONUS: Create random grid
def create_grid(nb_column, nb_row):
    """Generates a grid with randomly placed ships"""
    grid = []
    for i in range(nb_row):
        row = []
        for j in range(nb_column):
            row.append(' ')
        grid.append(row)
    
    # Ship sizes: 5, 4, 3, 3, 2
    ships = [5, 4, 3, 3, 2]
    
    for ship_size in ships:
        placed = False
        attempts = 0
        
        while not placed and attempts < 100:
            attempts += 1
            # Random direction: 0=horizontal, 1=vertical
            direction = random.randint(0, 1)
            
            if direction == 0:  # Horizontal
                row = random.randint(0, nb_row - 1)
                col = random.randint(0, nb_column - ship_size)
                
                # Check if there is space
                can_place = True
                for i in range(ship_size):
                    if grid[row][col + i] != ' ':
                        can_place = False
                        break
                
                if can_place:
                    for i in range(ship_size):
                        grid[row][col + i] = 'b'
                    placed = True
            
            else:  # Vertical
                row = random.randint(0, nb_row - ship_size)
                col = random.randint(0, nb_column - 1)
                
                # Check if there is space
                can_place = True
                for i in range(ship_size):
                    if grid[row + i][col] != ' ':
                        can_place = False
                        break
                
                if can_place:
                    for i in range(ship_size):
                        grid[row + i][col] = 'b'
                    placed = True
    
    return grid

# Run the game
if __name__ == "__main__":
    main()
