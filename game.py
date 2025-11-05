# -*- coding: utf-8 -*-
from grid import print_grid, cellNameToIndex
from score import saveTurnInFile, calculScore
# Icons 
hit_icon = "💥"
miss_icon = "💦"

def send_missile_at(grid, row_index, column_index):
    """
    Envoie un missile sur la cellule donnée.
    Retourne True si un bateau est touché, False sinon.
    """
    cell = grid[row_index][column_index]
    
    # Vérifie si la case a déjà été ciblée
    if cell == 'h' or cell == 'm':
        print("⚠️  You already fired at this cell!")
        return None
    
    # Vérifie si un bateau est présent
    if cell == 'b':
        grid[row_index][column_index] = 'h'
        print(f"{hit_icon} HIT!")
        return True
    else:
        grid[row_index][column_index] = 'm'
        print(f"{miss_icon} Miss...")
        return False


def ask_send_missile(grid):
    """Asks the user for coordinates (like A2) and fires"""
    print("\n--- Your turn ---")
    
    while True:
        cell_name = input("Enter cell (e.g., A2): ").strip()
        try:
            row_index, column_index = cellNameToIndex(cell_name)
            break
        except ValueError as e:
            print(f"❌ Error: {e}. Try again.")
    
    result = send_missile_at(grid, row_index, column_index)
    if result is not None:
        saveTurnInFile(cell_name, result, grid)


def is_game_over(grid):
    """
    Retourne True si tous les bateaux ont été coulés.
    """
    for row in grid:
        for cell in row:
            if cell == 'b':
                return False
    return True
