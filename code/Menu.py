import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect

from code.Constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    COLOR_ORANGE,
    COLOR_WHITE,
    COLOR_YELLOW,
    MENU_OPTIONS,
    FONTS,
)


class Menu:
    def __init__(self, window: Surface):
        self.window = window

        # Carrega a imagem
        self.original_img = pygame.image.load("./assets/MenuBg.png").convert_alpha()

        # Redimensiona a imagem para caber na tela
        self.surface = pygame.transform.scale(
            self.original_img, (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        # Desenha um retângulo na posição 0,0
        self.rect = self.surface.get_rect(left=0, top=0)

        # Música de fundo
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/Menu.mp3")
        pygame.mixer.music.play(loops=-1)  # -1 para loop infinito
        pygame.mixer.music.set_volume(0.5)  # define o volume (0.0 a 1.0)

    def run(self):
        running = True
        selected_option = 0

        while running:
            # Desenha a imagem
            self.window.blit(source=self.surface, dest=self.rect)

            # Desenha o textos no menu
            self.menu_text(
                text="MOUNTAIN",
                text_size=50,
                text_color=COLOR_ORANGE,
                text_center_pos=(WINDOW_WIDTH / 2, 70),
            )

            self.menu_text(
                text="SHOOTER",
                text_size=50,
                text_color=COLOR_ORANGE,
                text_center_pos=(WINDOW_WIDTH / 2, 120),
            )

            self.menu_text(
                text="NOME: PABLO ALAN",
                text_size=10,
                text_color=COLOR_WHITE,
                text_center_pos=(84, WINDOW_HEIGHT - 10),
            )

            self.menu_text(
                text="RU: 4571923",
                text_size=10,
                text_color=COLOR_WHITE,
                text_center_pos=(WINDOW_WIDTH - 60, WINDOW_HEIGHT - 10),
            )

            for i, option in enumerate(MENU_OPTIONS):
                self.menu_text(
                    text_size=16,
                    text=option,
                    text_color=COLOR_YELLOW if i == selected_option else COLOR_WHITE,
                    text_center_pos=(WINDOW_WIDTH / 2, 200 + i * 30),
                )

            # Atualiza a tela
            pygame.display.flip()

            # Events
            for event in pygame.event.get():
                # Check if the window was closed
                if event.type == pygame.QUIT:
                    running = False  # Stop the loop
                    pygame.quit()  # Close the window
                    quit()  # Close the program

                # Check key down events
                if event.type == pygame.KEYDOWN:
                    # Check if the up or down arrow keys were pressed
                    if event.key == pygame.K_UP:
                        selected_option = (
                            selected_option - 1
                            if selected_option > 0
                            else len(MENU_OPTIONS) - 1
                        )
                    elif event.key == pygame.K_DOWN:
                        selected_option = (
                            selected_option + 1
                            if selected_option < len(MENU_OPTIONS) - 1
                            else 0
                        )
                    # Check if press ENTER
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[selected_option]

    def menu_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple
    ):
        text_font: Font = pygame.font.SysFont(name=FONTS, size=text_size)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(source=text_surf, dest=text_rect)
