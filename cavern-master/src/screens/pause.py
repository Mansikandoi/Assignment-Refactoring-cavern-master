class PauseScreen:
    """
    Pause overlay screen that freezes game simulation while displaying pause UI.
    """
    def __init__(self, app, play_screen):
        self.app = app
        self.play_screen = play_screen  # Keep reference to return to

    def update(self, input_state):
        # Check for unpause (P key pressed)
        if input_state.pause_pressed:
            # Resume game
            self.app.change_screen(self.play_screen)

    def draw(self):
        from main import screen, draw_text, WIDTH

        # Draw the frozen game state underneath
        self.play_screen.draw()

        # Draw semi-transparent overlay (simulated with repeated blits)
        # Note: Pygame Zero doesn't have easy alpha blending, so we'll just draw text

        # Draw "PAUSED" text
        draw_text("PAUSED", 200)

        # Draw instruction
        draw_text("PRESS P TO RESUME", 250)