# -*- coding: utf-8 -*-
import random

# Icons for display
sea_icon = "🌊"
ship_icon = "⛵"
hit_icon = "💥"
miss_icon = "💦"


def create_empty_grid():
    """Creates an empty 8x8 grid filled with spaces"""
    grid = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(' ')
        grid.append(row)
    return grid


def place_ships_manually(grid):
    """Places 3 ships manually on the grid (used for testing)"""
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


def print_grid(grid):
    """Displays the grid in the console (ships are hidden)"""
    print("  A  B  C  D  E  F  G  H")
    for row_index in range(8):
        row_display = str(row_index + 1) + " "
        for col_index in range(8):
            cell = grid[row_index][col_index]
            if cell == ' ':
                row_display += sea_icon + " "
            elif cell == 'b':
                # Hide ships from player
                row_display += sea_icon + " "
            elif cell == 'h':
                row_display += hit_icon + " "
            elif cell == 'm':
                row_display += miss_icon + " "
            else:
                row_display += sea_icon + " "
        print(row_display)


def cellNameToIndex(cellName):
    """
    Converts a cell name like 'A2' to a tuple of indexes (row_index, column_index)
    Example: A2 -> (1, 0)
    Raises ValueError if the input is invalid.
    """
    if len(cellName) < 2 or len(cellName) > 3:
        raise ValueError("Invalid cell name format.")

    col_letter = cellName[0].upper()
    if col_letter not in "ABCDEFGH":
        raise ValueError("Invalid column letter. Use A-H.")

    try:
        row_number = int(cellName[1:])
    except ValueError:
        raise ValueError("Invalid row number.")

    if not (1 <= row_number <= 8):
        raise ValueError("Row number must be between 1 and 8.")

    column_index = ord(col_letter) - ord('A')
    row_index = row_number - 1

    return (row_index, column_index)


def create_grid(nb_column, nb_row):
    """
    Creates a grid and places ships randomly.
    Ship sizes:
      - 1 aircraft carrier (5 cells)
      - 1 cruiser (4 cells)
      - 2 destroyers (3 cells)
      - 1 torpedo boat (2 cells)
    """
    grid = [[' ' for _ in range(nb_column)] for _ in range(nb_row)]
    ships = [5, 4, 3, 3, 2]

    for ship_size in ships:
        grid = place_boat(ship_size, grid, nb_column, nb_row)

    return grid


def place_boat(boat_size, grid, nb_column, nb_row):
    """
    Places a single ship of size 'boat_size' randomly on the grid.
    Ensures the ship does not overlap and stays within the grid.
    """
    new_grid = [row[:] for row in grid]  # Copy grid
    placed = False

    while not placed:
        direction = random.randint(0, 1)  # 0 = horizontal, 1 = vertical

        if direction == 0:
            # Horizontal placement
            row = random.randint(0, nb_row - 1)
            col = random.randint(0, nb_column - boat_size)
            if all(new_grid[row][col + i] == ' ' for i in range(boat_size)):
                for i in range(boat_size):
                    new_grid[row][col + i] = 'b'
                placed = True

        else:
            # Vertical placement
            row = random.randint(0, nb_row - boat_size)
            col = random.randint(0, nb_column - 1)
            if all(new_grid[row + i][col] == ' ' for i in range(boat_size)):
                for i in range(boat_size):
                    new_grid[row + i][col] = 'b'
                placed = True

    return new_grid
