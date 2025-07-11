import pygame
from pygame import Surface
from pygame import Rect
from pygame.font import Font
from random import choice

from code.Entity import Entity
from code.Player import Player
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.Constants import (
    FONTS,
    COLOR_WHITE,
    COLOR_GREEN,
    COLOR_CYAN,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    MENU_OPTIONS,
    EVENT_ENEMY,
    EVENT_TIMEOUT,
    ENEMY_SPAWN_TIME,
    TIMEOUT_DECREMENT_STEP,
    TIMEOUT_LIMIT,
)
from code.EntityMediator import EntityMediator


class Level:
    def __init__(
        self,
        window: Surface,
        name: str,
        level_number: int,
        bg_images_amount: int,
        players_score: list[int],
        game_mode: str,
    ):
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.level_number = level_number
        self.timeout = (
            TIMEOUT_LIMIT * 2 if level_number == 3 else TIMEOUT_LIMIT
        )  # Tempo limite do nível em milissegundos

        self.players_score = players_score

        self.entity_list: list[Entity] = []

        # Background
        self.entity_list.extend(
            EntityFactory.get_entity(
                entity_name="background",
                level=level_number,
                images_amount=bg_images_amount,
            )
        )

        # Players
        player1 = EntityFactory.get_entity(entity_name="player1", images_amount=1)
        player1.score = players_score[0]

        self.entity_list.append(player1)

        if self.game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            player2 = EntityFactory.get_entity(entity_name="player2", images_amount=1)
            player2.score = players_score[1]

            self.entity_list.append(player2)

        # Registro de evento de inimigo (-1 para loop infinito)
        pygame.time.set_timer(event=EVENT_ENEMY, millis=ENEMY_SPAWN_TIME, loops=-1)

        # Registro de evento de timeout (para checar se o jogador ganhou ou perdeu)
        pygame.time.set_timer(
            event=EVENT_TIMEOUT, millis=TIMEOUT_DECREMENT_STEP, loops=-1
        )

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
            # Resetando variável de controle de morte
            is_player_dead = True

            # Controla a taxa de quadros
            clock.tick(60)  # 60 FPS

            # Eventos
            for event in pygame.event.get():
                # Quando o jogador fecha a janela
                if event.type == pygame.QUIT:
                    running = False  # Stop the loop
                    pygame.quit()  # Close the window
                    quit()  # End pygame

                # Gera um novo inimigo
                if event.type == EVENT_ENEMY:
                    if self.level_number == 3:
                        enemy_choice = "enemy3"
                    else:
                        enemy_choice = choice(("enemy1", "enemy2"))

                    self.entity_list.append(
                        EntityFactory.get_entity(
                            entity_name=enemy_choice, images_amount=1
                        )
                    )

                # Checa se o timeout acabou
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_DECREMENT_STEP

                    if self.timeout <= 0:
                        # Registrando score
                        for entity in self.entity_list:
                            if isinstance(entity, Player):
                                if entity.name == "Player1":
                                    self.players_score[0] = entity.score
                                elif entity.name == "Player2":
                                    self.players_score[1] = entity.score

                        running = False
                        return True

            # Desenha todas entidades, Registro de shot, Check game over
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)

                entity.move()  # Move the entity

                # Registrando entidade de shot
                if isinstance(entity, (Player, Enemy)):
                    shoot = entity.shoot()

                    if shoot:
                        self.entity_list.append(shoot)

                # Textos de Score e HUD
                if entity.name == "Player1":
                    self.level_text(
                        text_size=14,
                        text=f"{entity.name} - Health: {entity.health} | Score: {entity.score}",
                        text_color=COLOR_GREEN,
                        text_position=(10, 25),
                    )

                if entity.name == "Player2":
                    self.level_text(
                        text_size=14,
                        text=f"{entity.name} - Health: {entity.health} | Score: {entity.score}",
                        text_color=COLOR_CYAN,
                        text_position=(10, 45),
                    )

                # Check game over
                if isinstance(entity, Player):
                    is_player_dead = False

            # Check game over
            if is_player_dead:
                running = False
                return False

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
        text_font: Font = pygame.font.Font(FONTS, text_size)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        text_rect: Rect = text_surf.get_rect(
            left=text_position[0], top=text_position[1]
        )

        self.window.blit(source=text_surf, dest=text_rect)
