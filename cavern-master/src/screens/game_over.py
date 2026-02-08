from src.screens.menu import MenuScreen
from src.game import Game


class GameOverScreen:
    def __init__(self, app, game):
        self.app = app
        self.game = game

    def update(self):
        from main import space_pressed

        if space_pressed():
            # Back to menu
            self.app.change_screen(MenuScreen(self.app))

    def draw(self):
        from main import screen, draw_status

        self.game.draw()
        draw_status()

        # Game Over image
        screen.blit("over", (0, 0))
