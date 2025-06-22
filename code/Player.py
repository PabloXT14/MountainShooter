import pygame

from code.Entity import Entity
from code.Constants import ENTITIES_SPEED, WINDOW_HEIGHT, WINDOW_WIDTH


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        speed = ENTITIES_SPEED[self.name]

        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.top -= speed

        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.top += speed

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.left -= speed

        if pressed_key[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.left += speed
