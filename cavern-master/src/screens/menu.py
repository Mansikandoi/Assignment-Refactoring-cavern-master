from src.screens.play import PlayScreen
from src.game import Game, Player


class MenuScreen:
    def __init__(self, app):
        self.app = app

        # Create game WITHOUT player (like original menu)
        self.game = Game()

    def update(self):
        from main import space_pressed

        if space_pressed():
            # Start new game
            game = Game(Player())
            self.app.change_screen(PlayScreen(self.app, game))
        else:
            self.game.update()

    def draw(self):
        from main import screen

        self.game.draw()

        # Title
        screen.blit("title", (0, 0))

        # SPACE animation (copied from original)
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))
