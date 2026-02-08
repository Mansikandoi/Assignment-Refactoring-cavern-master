from dataclasses import dataclass

@dataclass
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool


class InputManager:
    def __init__(self):
        self.prev_space = False
        self.prev_up = False

    def build(self, keyboard):
        # Current states
        space = keyboard.space
        up = keyboard.up

        # Edge detection
        fire_pressed = space and not self.prev_space
        jump_pressed = up and not self.prev_up

        state = InputState(
            left=keyboard.left,
            right=keyboard.right,
            jump_pressed=jump_pressed,
            fire_pressed=fire_pressed,
            fire_held=space
        )

        # Save for next frame
        self.prev_space = space
        self.prev_up = up

        return state
