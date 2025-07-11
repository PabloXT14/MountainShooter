import pygame

from code.Entity import Entity
from code.EnemyShot import EnemyShot
from code.Constants import ENTITIES_SPEED, ENTITY_SHOT_DELAY


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITIES_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1

        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

            return EnemyShot(name=f"{self.name}Shot", position=self.rect.center)
