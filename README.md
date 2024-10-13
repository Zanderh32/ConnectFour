# Connect 4 Game in Python

This project is a Python implementation of the classic **Connect 4** game. Two players alternate turns, dropping their coins (red or yellow) into a 7x6 grid, aiming to connect four of their coins in a row either horizontally, vertically, or diagonally.

## Features

- **Two-Player Mode**: The game supports two players, where Player 1 uses the red coin ("R") and Player 2 uses the yellow coin ("Y").
- **Dynamic Board Display**: The game displays the board after every turn, showing the updated state of the game.
- **Win Detection**: The game checks for a win after each move. A player wins if they connect four coins horizontally, vertically, or diagonally.
- **Real-Time Interaction**: Players enter their move in real-time by selecting the column to drop their coin.

## How It Works

1. **Player Input**:
   - Players take turns selecting a column (from 0 to 6) in which they want to drop their coin.

2. **Coin Placement**:
   - The coin is placed in the lowest available position in the selected column.

3. **Win Check**:
   - After each move, the game checks for four consecutive coins of the same type horizontally, vertically, or diagonally.

4. **Game Over**:
   - If a player successfully connects four coins, they win, and the game prints a victory message.
   - If no more moves are possible (board is full), the game results in a tie.
