# -*- coding: utf-8 -*-
import json
import os
from grid import print_grid

GAME_FILE = "game.txt"
SCORES_FILE = "scores.json"


# -------------------------------------------------
# 1) Save turn history to file
# -------------------------------------------------
def saveTurnInFile(cellName, result, grid):
    """
    Saves the result of each turn into 'game.txt' and prints the full grid (ships visible).
    Example line: 'Tir en A1 manqué'
    """
    # Reset the file if it doesn't exist (new game)
    if not os.path.exists(GAME_FILE):
        with open(GAME_FILE, "w", encoding="utf-8") as f:
            f.write("=== GAME HISTORY ===\n\n")

    # Append the result of the current turn
    with open(GAME_FILE, "a", encoding="utf-8") as f:
        f.write(f"Tir en {cellName} {'réussi' if result else 'manqué'}\n")
        print_grid(grid, reveal=True, file=f)  # custom version for saving
        f.write("\n")


# -------------------------------------------------
# 2) Score calculation
# -------------------------------------------------
def calculScore(grid):
    """
    Calculates and returns the score for the given grid.
    +700 points per hit ('h')
    -100 points per miss ('m')
    """
    score = 0
    for row in grid:
        for cell in row:
            if cell == 'h':
                score += 700
            elif cell == 'm':
                score -= 100
    return score


# -------------------------------------------------
# 3) Save score and pseudo
# -------------------------------------------------
def saveFinalScore(pseudo, score):
    """
    Saves the player's pseudo and score into 'scores.json'.
    """
    scores_data = []

    # Load existing scores if file exists
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            try:
                scores_data = json.load(f)
            except json.JSONDecodeError:
                scores_data = []

    # Add the new score
    scores_data.append([pseudo, score])

    # Save back to file
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores_data, f, ensure_ascii=False, indent=2)


# -------------------------------------------------
# 4) Display high scores
# -------------------------------------------------
def displayHighScores():
    """
    Displays the top 3 high scores from 'scores.json'.
    """
    if not os.path.exists(SCORES_FILE):
        print("No high scores yet.\n")
        return

    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        try:
            scores_data = json.load(f)
        except json.JSONDecodeError:
            print("No valid scores found.\n")
            return

    if not scores_data:
        print("No high scores yet.\n")
        return

    # Sort from highest to lowest
    scores_data.sort(key=lambda x: x[1], reverse=True)

    print("\n🏆 TOP 3 HIGH SCORES 🏆")
    for i, (pseudo, score) in enumerate(scores_data[:3], start=1):
        print(f"{i}. {pseudo} - {score} points")
    print()


def getPlayerRank(pseudo):
    """Returns the rank of the player among all scores."""
    if not os.path.exists(SCORES_FILE):
        return None

    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        try:
            scores_data = json.load(f)
        except json.JSONDecodeError:
            return None

    scores_data.sort(key=lambda x: x[1], reverse=True)

    for i, (p, s) in enumerate(scores_data, start=1):
        if p == pseudo:
            return i
    return None
