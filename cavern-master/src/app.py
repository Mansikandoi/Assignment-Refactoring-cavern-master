from src.input import InputManager

class App:
    def __init__(self):
        self.screen = None
        self.input = InputManager()

    def change_screen(self, new_screen):
        self.screen = new_screen

    def update(self):
        from main import keyboard

        input_state = self.input.build(keyboard)
        self.screen.update(input_state)

    def draw(self):
        self.screen.draw()
