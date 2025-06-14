from abc import ABC, abstractmethod

import pygame
from pygame import Surface

from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.original_image = pygame.image.load(f"./assets/{name}.png").convert_alpha()
        self.surf: Surface = pygame.transform.scale(
            self.original_image, (WINDOW_WIDTH, WINDOW_HEIGHT)
        )
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 1

    @abstractmethod
    def move(self):
        pass
