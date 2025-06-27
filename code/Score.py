import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FONTS,
    COLOR_YELLOW,
    SCORE_TEXT_POSITIONS,
    MENU_OPTIONS,
)


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

            # Desenha os textos
            self.score_text(
                text="YOU WIN!!",
                text_size=48,
                text_color=COLOR_YELLOW,
                text_center_pos=SCORE_TEXT_POSITIONS["Title"],
            )

            if game_mode == MENU_OPTIONS[0]:
                text = "Player 1 enter your name (4 characters): "

            # Atualiza a tela
            pygame.display.update()

    def score_text(
        self, text: str, text_size: int, text_color: tuple, text_center_pos: tuple
    ):
        text_font: Font = pygame.font.SysFont(name=FONTS, size=text_size)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(source=text_surf, dest=text_rect)
