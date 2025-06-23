import pygame
from pygame import Surface
from pygame import Rect
from pygame.font import Font
from random import choice

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Constants import (
    FONTS,
    COLOR_WHITE,
    WINDOW_HEIGHT,
    MENU_OPTIONS,
    EVENT_ENEMY,
    ENEMY_SPAWN_TIME,
)
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: list[Entity] = []

        # Background
        self.entity_list.extend(
            EntityFactory.get_entity(entity_name="background", level=1, images_amount=7)
        )

        # Players
        self.entity_list.append(
            EntityFactory.get_entity(entity_name="player1", images_amount=1)
        )

        if self.game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(
                EntityFactory.get_entity(entity_name="player2", images_amount=1)
            )

        # Registro de evento de inimigo
        pygame.time.set_timer(event=EVENT_ENEMY, millis=ENEMY_SPAWN_TIME, loops=-1)

        self.timeout = 20000  # Tempo limite do nível em milissegundos

    def run(self):

        running = True

        # Música de fundo
        pygame.mixer.init()
        pygame.mixer.music.load(f"./assets/{self.name}.mp3")
        pygame.mixer.music.play(loops=-1)  # -1 para loop infinito
        pygame.mixer.music.set_volume(0.3)  # define o volume (0.0 a 1.0)

        # Relógio para controlar a taxa de quadros
        clock = pygame.time.Clock()

        while running:
            # Controla a taxa de quadros
            clock.tick(60)  # 60 FPS

            # Eventos
            for event in pygame.event.get():
                # Quando o jogador fecha a janela
                if event.type == pygame.QUIT:
                    running = False  # Stop the loop
                    pygame.quit()  # Close the window
                    quit()  # Close the program
                # Gera um novo inimigo
                if event.type == EVENT_ENEMY:
                    enemy_choice = choice(("enemy1", "enemy2"))

                    self.entity_list.append(
                        EntityFactory.get_entity(
                            entity_name=enemy_choice, images_amount=1
                        )
                    )

            # Desenha as entidades
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)

                entity.move()  # Move the entity

            # Desenha os textos do nível
            self.level_text(
                text_size=14,
                text=f"{self.name} - Timeout {self.timeout // 1000}s",
                text_color=COLOR_WHITE,
                text_position=(10, 5),
            )

            self.level_text(
                text_size=14,
                text=f"FPS: {int(clock.get_fps())}",
                text_color=COLOR_WHITE,
                text_position=(10, WINDOW_HEIGHT - 35),
            )

            self.level_text(
                text_size=14,
                text=f"Entidades: {len(self.entity_list)}",
                text_color=COLOR_WHITE,
                text_position=(10, WINDOW_HEIGHT - 20),
            )

            # Atualiza a tela
            pygame.display.flip()

            # Verificação de colisões
            EntityMediator.verify_collision(entity_list=self.entity_list)

            # Verificação de saúde
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(
        self, text_size: int, text: str, text_color: tuple, text_position: tuple
    ):
        text_font: Font = pygame.font.SysFont(name=FONTS, size=text_size)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        text_rect: Rect = text_surf.get_rect(
            left=text_position[0], top=text_position[1]
        )

        self.window.blit(source=text_surf, dest=text_rect)
