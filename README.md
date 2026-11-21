# Tic-Tac-Toe with Simple AI

## About the Project
This project is a Python-based Tic-Tac-Toe game where a human player competes against a computer-controlled opponent.

The computer uses basic AI decision-making rules to select its moves, making the game interactive and challenging.

## Features
- Human vs Computer gameplay.
- Interactive 3×3 game board.
- Basic AI opponent.
- Detects immediate winning opportunities.
- Blocks the player's winning moves.
- Prioritizes the center position.
- Randomly selects available positions when necessary.
- Detects win, loss, and draw conditions.
- Handles invalid user inputs.

## Technologies Used
- Python 3
- Random Module
- Lists
- Functions
- Conditional Statements
- Loops

## How to Run

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project folder.

3. Run the Python file:

   ```bash
   python TicTacToeGame.py
   ```

## How to Play
- The human player uses X.
- The computer uses O.
- Enter a number between 1 and 9 to select a board position.

### Board Position Guide

```text
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
```

## AI Logic
The computer follows a simple decision-making strategy:

1. Checks whether it can win immediately.
2. Blocks the player's winning opportunity.
3. Selects the center position if available.
4. Chooses a random available position.

## Learning Outcomes
- Understanding Python functions and lists.
- Implementing game logic.
- Working with random selection.
- Understanding basic AI decision-making.
- Handling winning, losing, and draw conditions.

## Author
Developed as part of the CodeOrbitTech Internship.
