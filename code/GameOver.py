import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FONTS,
    COLOR_WHITE,
    COLOR_BLACK,
    COLOR_RED,
)


class GameOver:
    def __init__(self, window: Surface):
        self.window = window

    def show(self):
        self.window.fill(color=COLOR_BLACK)

        self.game_over_text(
            text="GAME OVER",
            text_size=48,
            text_color=COLOR_RED,
            text_center_pos=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2),
        )

        self.game_over_text(
            text="Press ESC to return to menu",
            text_size=14,
            text_color=COLOR_WHITE,
            text_center_pos=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 30),
        )

        # Música de fundo
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/GameOver.mp3")
        pygame.mixer.music.play(loops=-1)  # -1 para loop infinito
        pygame.mixer.music.set_volume(0.3)

        running = True

        while running:
            # Eventos
            for event in pygame.event.get():
                # Quando o jogador fecha a janela
                if event.type == pygame.QUIT:
                    running = False  # Stop the loop
                    pygame.quit()  # Close the window
                    quit()  # End pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.flip()

    def game_over_text(
        self, text: str, text_size: int, text_color: tuple, text_center_pos: tuple
    ):
        text_font: Font = pygame.font.Font(FONTS, text_size)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(source=text_surf, dest=text_rect)
