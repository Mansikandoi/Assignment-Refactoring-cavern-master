from dataclasses import dataclass

@dataclass
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool
    pause_pressed: bool  # New: P key edge detection


class InputManager:
    def __init__(self):
        self.prev_space = False
        self.prev_up = False
        self.prev_p = False  # Track P key state

    def build(self, keyboard):
        # Current states
        space = keyboard.space
        up = keyboard.up
        p = keyboard.p  # P key for pause

        # Edge detection
        fire_pressed = space and not self.prev_space
        jump_pressed = up and not self.prev_up
        pause_pressed = p and not self.prev_p  # Pause edge

        state = InputState(
            left=keyboard.left,
            right=keyboard.right,
            jump_pressed=jump_pressed,
            fire_pressed=fire_pressed,
            fire_held=space,
            pause_pressed=pause_pressed
        )

        # Save for next frame
        self.prev_space = space
        self.prev_up = up
        self.prev_p = p

        return state