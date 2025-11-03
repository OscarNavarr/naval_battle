# -*- coding: utf-8 -*-
from grid import create_grid, print_grid
from game import ask_send_missile, is_game_over


def main():
    """Main game function — controls the full Battleship flow"""
    print("=== BATTLESHIP ===\n")
    
    # Create a random 8x8 grid with ships placed
    grid = create_grid(8, 8)
    shots = 0

    # Main game loop
    while not is_game_over(grid):
        print("\n" + "=" * 30)
        print_grid(grid)
        ask_send_missile(grid)
        shots += 1

    # End of the game
    print("\n" + "=" * 30)
    print_grid(grid)
    print(f"\n🏆 VICTORY! You sank all ships in {shots} shots.")


if __name__ == "__main__":
    main()
