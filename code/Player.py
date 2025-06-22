import pygame

from code.Entity import Entity
from code.Constants import (
    ENTITIES_SPEED,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    PLAYER_KEY_UP,
    PLAYER_KEY_DOWN,
    PLAYER_KEY_LEFT,
    PLAYER_KEY_RIGHT,
)


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        speed = ENTITIES_SPEED[self.name]

        pressed_key_up = PLAYER_KEY_UP[self.name]
        pressed_key_down = PLAYER_KEY_DOWN[self.name]
        pressed_key_left = PLAYER_KEY_LEFT[self.name]
        pressed_key_right = PLAYER_KEY_RIGHT[self.name]

        if pressed_key[pressed_key_up] and self.rect.top > 0:
            self.rect.top -= speed

        if pressed_key[pressed_key_down] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.top += speed

        if pressed_key[pressed_key_left] and self.rect.left > 0:
            self.rect.left -= speed

        if pressed_key[pressed_key_right] and self.rect.right < WINDOW_WIDTH:
            self.rect.left += speed
