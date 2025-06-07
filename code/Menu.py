import pygame

from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT


class Menu:
    def __init__(self, window: pygame.Surface):
        self.window = window

        # Carrega a imagem
        self.original_img = pygame.image.load("./assets/MenuBg.png").convert_alpha()

        # Redimensiona a imagem para caber na tela
        self.surface = pygame.transform.scale(
            self.original_img, (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        # Desenha um retângulo na posição 0,0
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        self.window.blit(source=self.surface, dest=self.rect)

        pygame.display.flip()  # Atualiza a tela
