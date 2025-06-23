import pygame

from code.Entity import Entity
from code.Constants import ENTITIES_SPEED, WINDOW_WIDTH


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITIES_SPEED[self.name]
