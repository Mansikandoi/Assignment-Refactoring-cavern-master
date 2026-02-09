from src.screens.game_over import GameOverScreen
from src.screens.pause import PauseScreen


class PlayScreen:
    def __init__(self, app, game):
        self.app = app
        self.game = game

    def update(self, input_state):
        # Check for pause first (before game logic)
        if input_state.pause_pressed:
            self.app.change_screen(PauseScreen(self.app, self))
            return  # Don't update game this frame

        # Player dead?
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            self.app.change_screen(
                GameOverScreen(self.app, self.game)
            )
        else:
            self.game.update(input_state)

    def draw(self):
        from main import draw_status

        self.game.draw()
        draw_status(self.game)