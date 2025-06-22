from code.Entity import Entity

from code.Constants import WINDOW_WIDTH, ENTITIES_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name=name, position=position, resize_to_screen=True)
        pass

    def move(self):
        self.rect.centerx -= ENTITIES_SPEED[self.name]

        if self.rect.right <= 0:
            # Move the background to the right
            self.rect.left = WINDOW_WIDTH
