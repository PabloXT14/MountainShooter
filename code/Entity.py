from abc import ABC, abstractmethod

import pygame
from pygame import Surface, Rect

from code.Constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    ENTITY_HEALTH,
    ENTITY_DAMAGE,
    ENTITY_SCORE,
)


class Entity(ABC):
    def __init__(self, name: str, position: tuple, resize_to_screen: bool = False):
        self.name = name
        self.original_image = pygame.image.load(f"./assets/{name}.png").convert_alpha()

        if resize_to_screen:
            self.surf: Surface = pygame.transform.scale(
                self.original_image, (WINDOW_WIDTH, WINDOW_HEIGHT)
            )
        else:
            self.surf: Surface = self.original_image

        self.rect: Rect = self.surf.get_rect(left=position[0], top=position[1])

        self.speed = 0

        self.health = ENTITY_HEALTH[self.name]

        self.damage = ENTITY_DAMAGE[self.name]

        self.last_entity_to_cause_damage = None

        self.score = ENTITY_SCORE[self.name]

    @abstractmethod
    def move(self):
        pass
