import pygame
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(
            EntityFactory.get_entity(entity_name="background", level=2, images_amount=5)
        )

    def run(self):
        running = True

        while running:
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Stop the loop
                    pygame.quit()  # Close the window
                    quit()  # Close the program

            # Desenha as entidades
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)

            pygame.display.flip()
