from src.screens.game_over import GameOverScreen


class PlayScreen:
    def __init__(self, app, game):
        self.app = app
        self.game = game

    def update(self):
        # Player dead?
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            self.app.change_screen(
                GameOverScreen(self.app, self.game)
            )
        else:
            self.game.update()

    def draw(self):
        from main import draw_status

        self.game.draw()
        draw_status()
