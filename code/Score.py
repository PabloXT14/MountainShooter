from math import ceil
from datetime import datetime
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FONTS,
    COLOR_YELLOW,
    COLOR_WHITE,
    SCORE_TEXT_POSITIONS,
    MENU_OPTIONS,
)
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window

        # Carrega a imagem
        self.original_img = pygame.image.load("./assets/ScoreBg.png").convert_alpha()

        # Redimensiona a imagem para caber na tela
        self.surface = pygame.transform.scale(
            self.original_img, (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        # Desenha um retângulo na posição 0,0
        self.rect = self.surface.get_rect(left=0, top=0)

    def show(self):
        running = True

        # Música de fundo
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/Score.mp3")
        pygame.mixer.music.play(loops=-1)  # -1 para loop infinito
        pygame.mixer.music.set_volume(0.5)  # define o volume (0.0 a 1.0)

        # Desenha a imagem
        self.window.blit(source=self.surface, dest=self.rect)

        while running:
            # Eventos
            for event in pygame.event.get():
                # Quando o jogador fecha a janela
                if event.type == pygame.QUIT:
                    running = False  # Stop the loop
                    pygame.quit()  # Close the window
                    quit()  # Close the program

            # Atualiza a tela
            pygame.display.update()

    def save(self, game_mode: str, players_score: list):
        running = True

        # Música de fundo
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/Score.mp3")
        pygame.mixer.music.play(loops=-1)  # -1 para loop infinito
        pygame.mixer.music.set_volume(0.5)  # define o volume (0.0 a 1.0)

        # Save score in database
        db_proxy = DBProxy(db_name="./data/database.db")

        player_name = ""

        while running:
            # Desenha a imagem
            self.window.blit(source=self.surface, dest=self.rect)

            # Desenha o título
            self.score_text(
                text="YOU WIN!!",
                text_size=48,
                text_color=COLOR_YELLOW,
                text_center_pos=SCORE_TEXT_POSITIONS["Title"],
            )

            # Pegando o nome e score do jogador de acordo com o modo de jogo
            if game_mode == MENU_OPTIONS[0]:
                score = players_score[0]

                text = "Player 1 enter your name (4 characters): "
            elif game_mode == MENU_OPTIONS[1]:
                score = ceil((players_score[0] + players_score[1]) / 2)

                text = "Enter Team name (4 characters): "
            elif game_mode == MENU_OPTIONS[2]:
                if players_score[0] >= players_score[1]:
                    score = players_score[0]

                    text = "Player 1 enter your name (4 characters): "
                else:
                    score = players_score[1]

                    text = "Player 2 enter your name (4 characters): "

            # Eventos
            for event in pygame.event.get():
                # Quando o jogador fecha a janela
                if event.type == pygame.QUIT:
                    running = False  # Stop the loop
                    pygame.quit()  # Close the window
                    quit()  # Close the program

                # Pegando name do player
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]

                    elif event.key == pygame.K_RETURN and len(player_name) == 4:
                        db_proxy.save(
                            score_dict={
                                "name": player_name,
                                "score": score,
                                "date": self.get_formatted_date(),
                            }
                        )

                        running = False

                    elif len(player_name) < 4:
                        player_name += event.unicode

            self.score_text(
                text=f"{str(score)} points",
                text_size=24,
                text_color=COLOR_YELLOW,
                text_center_pos=SCORE_TEXT_POSITIONS["Score"],
            )

            self.score_text(
                text=text,
                text_size=14,
                text_color=COLOR_WHITE,
                text_center_pos=SCORE_TEXT_POSITIONS["EnterName"],
            )

            self.score_text(
                text=player_name.upper(),
                text_size=16,
                text_color=COLOR_YELLOW,
                text_center_pos=SCORE_TEXT_POSITIONS["Name"],
            )

            # Atualiza a tela
            pygame.display.update()

    def score_text(
        self, text: str, text_size: int, text_color: tuple, text_center_pos: tuple
    ):
        text_font: Font = pygame.font.SysFont(name=FONTS, size=text_size)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(source=text_surf, dest=text_rect)

    def get_formatted_date(self):
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%H:%M")
        current_date = current_datetime.strftime("%d/%m/%Y")

        return f"{current_date} - {current_time}"
