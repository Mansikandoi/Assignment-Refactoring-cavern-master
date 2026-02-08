class App:
    def __init__(self):
        self.screen = None

    def change_screen(self, new_screen):
        self.screen = new_screen

    def update(self):
        self.screen.update()

    def draw(self):
        self.screen.draw()
