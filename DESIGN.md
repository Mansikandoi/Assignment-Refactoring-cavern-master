# Design Documentation

## Architecture Overview

This refactoring transforms a monolithic procedural game into a maintainable object-oriented architecture using established design patterns.

## 1. Screens Architecture (State Pattern)

### Problem
The original code used global state variables and conditional branching:
```python
# Original approach
state = STATE_MENU
def update():
    if state == STATE_MENU:
        # menu logic
    elif state == STATE_PLAY:
        # play logic
    elif state == STATE_GAME_OVER:
        # game over logic
```

### Solution
Each game state is now an independent screen object with its own `update()` and `draw()` methods.

**Screen Interface:**
```python
class Screen:
    def update(self, input_state): ...
    def draw(self): ...
```

**Implementations:**
- **MenuScreen**: Displays title, manages game start
- **PlayScreen**: Main gameplay, handles pause and death transitions
- **PauseScreen**: Overlay that freezes simulation, allows resume
- **GameOverScreen**: Displays final state, allows return to menu

**Benefits:**
- Each screen is self-contained and testable
- State transitions are explicit via `app.change_screen()`
- No global state pollution
- Easy to add new screens (e.g., settings, high scores)

### App Controller
The `App` class owns the current screen and delegates all updates/draws:

```python
class App:
    def __init__(self):
        self.screen = None
        self.input = InputManager()
    
    def update(self):
        input_state = self.input.build(keyboard)
        self.screen.update(input_state)
    
    def draw(self):
        self.screen.draw()
```

## 2. Input Design (Command Pattern)

### Problem
The original code scattered keyboard access throughout:
```python
# In Player.update()
if keyboard.left:
    move_left()
if keyboard.space and not space_down:
    fire_orb()
```

This created tight coupling and made edge detection (button pressed vs. held) error-prone.

### Solution
**InputState Snapshot:**
```python
@dataclass
class InputState:
    left: bool          # Currently held
    right: bool         # Currently held
    jump_pressed: bool  # Pressed THIS frame (edge)
    fire_pressed: bool  # Pressed THIS frame (edge)
    fire_held: bool     # Currently held (for blowing orbs)
    pause_pressed: bool # Pressed THIS frame (edge)
```

**InputManager:**
Built once per frame in `App.update()`, provides:
- **Edge detection**: Compares current frame to previous frame
- **Centralized logic**: All keyboard access in one place
- **Testability**: Easy to inject mock input states

**Key insight:** Differentiating "pressed" (edge) vs. "held" (level) is crucial:
- Jump/Fire use edge detection (one action per button press)
- Movement/Blow use level detection (continuous while held)

## 3. Pause Implementation

### Requirements
- Freeze all game simulation (no entity updates, no spawns, no timers)
- Continue rendering the frozen game state
- Display pause overlay
- Resume cleanly on unpause

### Implementation Strategy

**Option A: Pause as a Screen** (Chosen)
```python
class PauseScreen:
    def __init__(self, app, play_screen):
        self.play_screen = play_screen  # Keep reference
    
    def update(self, input_state):
        if input_state.pause_pressed:
            app.change_screen(self.play_screen)  # Resume
    
    def draw(self):
        self.play_screen.draw()  # Draw frozen game
        draw_text("PAUSED", ...)  # Add overlay
```

**Why this works:**
- When paused, `PauseScreen.update()` does NOT call `game.update()`
- Game state is frozen (no timer increments, no entity movement)
- Drawing still occurs, showing the frozen moment
- Resume simply switches back to `PlayScreen`

**Alternative considered:** Boolean flag in `PlayScreen`
- Rejected because it mixes pause state into gameplay screen
- Violates single responsibility principle
- Harder to extend (what if we want pause menu options?)

### Pause Flow
1. User presses P during gameplay
2. `PlayScreen.update()` detects `pause_pressed`
3. `PlayScreen` creates `PauseScreen(app, self)` and passes itself
4. `App` switches to `PauseScreen`
5. While paused: Game simulation stops, visuals persist
6. User presses P again
7. `PauseScreen.update()` detects `pause_pressed`
8. `App` switches back to the saved `PlayScreen` reference
9. Gameplay resumes exactly where it left off

**Critical detail:** `PauseScreen` must store a reference to the original `PlayScreen` instance (not create a new one), otherwise game state would be lost.

## 4. Design Principles Applied

### Single Responsibility
- Each screen handles ONE game state
- `InputManager` handles ONLY input processing
- `Game` handles ONLY simulation logic

### Open/Closed
- Easy to add new screens without modifying existing code
- Easy to add new input types (e.g., gamepad support)

### Dependency Inversion
- Screens depend on `InputState` abstraction, not `keyboard` directly
- `App` depends on screen interface, not concrete implementations

## 5. Trade-offs & Limitations

### Kept from Original
- `main.py` still contains game constants, entity classes, and drawing helpers
- This is acceptable because refactoring scope was limited to state management and input

### Not Implemented
- Unit tests (out of scope, but architecture is testable)
- Complete separation of rendering from game logic
- Asset management system

### Future Improvements
- Move entity classes to `src/entities/`
- Extract drawing code to rendering layer
- Add configuration file for game constants
- Implement save/load system using screen architecture
- Add settings screen for volume, controls, etc.

## 6. Why This Architecture Matters

**Maintainability:** Each component can be understood and modified independently.

**Testability:** Input and state can be mocked without running full game.

**Extensibility:** New features (leaderboards, multiplayer, settings) can be added as new screens.

**Debuggability:** State transitions are explicit and logged via `change_screen()`.

---

**Total refactoring effort:** ~300 lines added/changed, zero gameplay impact.
