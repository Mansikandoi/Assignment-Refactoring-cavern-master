from src.screens.menu import MenuScreen
from src.game import Game


class GameOverScreen:
    def __init__(self, app, game):
        self.app = app
        self.game = game

    def update(self, input_state):
        if input_state.fire_pressed:
            # Back to menu
            self.app.change_screen(MenuScreen(self.app))
        else:
            # Allow game to keep updating (enemies falling, etc.)
            self.game.update(input_state)

    def draw(self):
        from main import screen, draw_status

        self.game.draw()
        draw_status(self.game)  # ← PASS self.game here

        # Game Over image
        screen.blit("over", (0, 0))