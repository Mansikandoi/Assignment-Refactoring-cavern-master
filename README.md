# Cavern - Refactored Bubble Bobble Clone

A refactored version of the Pygame Zero Bubble Bobble-style game, originally from [Code the Classics](https://github.com/Wireframe-Magazine/Code-the-Classics/tree/master/cavern-master).

## Overview

This project refactors the original monolithic game code into a maintainable, object-oriented architecture while preserving the original gameplay experience.

## Requirements

- Python 3.5 or higher
- Pygame Zero 1.2 or higher

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd cavern-master
```

2. Install dependencies:
```bash
pip install pgzero pygame
```

## How to Run

Run the game using Pygame Zero:

```bash
pgzrun main.py
```

Or using Python directly:

```bash
python3 main.py
```

## Controls

- **Arrow Keys (Left/Right)**: Move player
- **Arrow Key (Up)**: Jump
- **Space**: Fire orb (hold to blow further)
- **P**: Pause/Resume game (during gameplay)

## Game Objective

Trap enemies in bubbles and pop them to clear levels. Collect fruit for points and power-ups for health/extra lives.

## Architecture Changes

### Original Structure
The original code was a single monolithic file with:
- Global state variables controlling game flow
- Direct keyboard polling scattered throughout
- Conditional branching in global `update()` and `draw()` functions

### Refactored Structure

```
cavern-master/
├── src/
│   ├── screens/          # Screen state objects
│   │   ├── menu.py       # Menu screen
│   │   ├── play.py       # Main gameplay screen
│   │   ├── pause.py      # Pause overlay
│   │   └── game_over.py  # Game over screen
│   ├── app.py            # Application controller
│   ├── input.py          # Input management & edge detection
│   └── game.py           # Core game logic
├── main.py               # Pygame Zero entry point
└── README.md
```

### Key Improvements

1. **State Pattern (Task A)**: Replaced global state branching with screen objects
2. **Command Pattern (Task B)**: Centralized input handling with edge detection
3. **Pause Feature (Task C)**: Clean pause/resume without simulation leaks

## Running Tests

Currently, this project uses manual testing. To test:

1. **Menu → Play transition**: Press SPACE on menu
2. **Gameplay**: Verify all controls work (move, jump, fire orbs)
3. **Pause**: Press P during gameplay, verify game freezes
4. **Resume**: Press P again, verify game continues smoothly
5. **Game Over**: Lose all lives, verify game over screen appears
6. **Return to Menu**: Press SPACE on game over screen

### Test Checklist

- Menu screen displays and animates
- Starting game creates player successfully
- Player movement (left/right) works
- Player jumping works
- Orb firing works (single press)
- Orb blowing works (hold space)
- Pause freezes all game simulation
- Pause overlay displays correctly
- Resume continues game cleanly
- Enemies spawn and move
- Collision detection works
- Level progression works
- Game over triggers when lives < 0
- Return to menu from game over works

## Project Structure Details

### `main.py`
Pygame Zero entry point containing:
- Global constants and level data
- Thin `update()` and `draw()` delegates to `App`
- Helper functions (`draw_text`, `draw_status`, etc.)

### `src/app.py`
Application controller managing screen transitions.

### `src/input.py`
Centralized input handling with:
- `InputState` dataclass for frame input snapshot
- `InputManager` for edge detection (pressed this frame vs. held)

### `src/game.py`
Core game simulation containing:
- `Game` class managing entities, levels, and game state
- All entity classes (`Player`, `Robot`, `Orb`, `Bolt`, etc.)
- Collision detection and game logic

### `src/screens/`
Individual screen implementations following the State pattern.

## Development Notes

- Gameplay behavior is intentionally preserved from the original
- Asset files (images, sounds, music) are not included in the repository
- See `DESIGN.md` for detailed architecture decisions

## Credits

- Original game code: [Wireframe Magazine - Code the Classics](https://github.com/Wireframe-Magazine/Code-the-Classics)
- Refactoring: Mansi Kandoi

## License

See original project license.
