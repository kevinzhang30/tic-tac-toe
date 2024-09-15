Sure! Here's a draft README file for your Tic-Tac-Toe project. Feel free to adjust any details as needed:

---

# Tic-Tac-Toe Game

This is a simple two-player **Tic-Tac-Toe** game built using Python's Tkinter library. The game features a menu screen with a button that leads to the game interface.

## Features

- **Menu Screen**: Start the game from a welcoming menu.
- **Game Board**: Play Tic-Tac-Toe with another player on the same device.
- **Game Mechanics**: The game includes turn-based play, win/draw detection, and restart functionality.

## In Progress

The single-player feature is yet to be implemented. The current version only supports two-player gameplay.

## Installation

To run this game, ensure you have Python installed. Then, clone this repository and run the `main.py` file.

### Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Usage

1. **Run the Game**: Execute the `main.py` file to start the game.
2. **Menu Screen**: Click the "Two Players" button to enter the game.
3. **Gameplay**: Click on the grid to place your X or O. The game will notify you if there’s a win or draw.

## Code Explanation

- **`main.py`**: Contains the main game logic and GUI setup.
- **`board.py`**: Contains the `Board` class, which handles game state and logic.

### Key Components

- **Game State**: Managed by the `Board` class in `board.py`.
- **Game Display**: Managed by Tkinter in `main.py`.
- **Restart Functionality**: Allows players to reset the game board.
