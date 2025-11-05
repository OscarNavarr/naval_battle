# -*- coding: utf-8 -*-
from grid import create_grid, print_grid
from game import ask_send_missile, is_game_over
from score import displayHighScores, calculScore, saveFinalScore, getPlayerRank

def main():
    """Main game function — controls the full Battleship flow"""
    print("=== BATTLESHIP ===\n")
    
    # Display top scores
    displayHighScores()

    # Create random 8x8 grid
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

    score = calculScore(grid)
    print(f"\n🏆 VICTORY! You sank all ships in {shots} shots.")
    print(f"Your final score: {score} points")

    # Ask for pseudo and save
    pseudo = input("Enter your name for the high scores: ").strip()
    saveFinalScore(pseudo, score)

    rank = getPlayerRank(pseudo)
    if rank:
        print(f"🎖️  You are ranked #{rank} among all players!")


if __name__ == "__main__":
    main()
