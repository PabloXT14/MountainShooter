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

        # Música de fundo
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/Menu.mp3")
        pygame.mixer.music.play(loops=-1)  # -1 para loop infinito
        pygame.mixer.music.set_volume(0.5)  # define o volume (0.0 a 1.0)

    def run(self):
        running = True

        while running:
            self.window.blit(source=self.surface, dest=self.rect)

            pygame.display.flip()  # Atualiza a tela

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close the window
                    quit()  # Close the program
                    running = False  # Stop the loop
