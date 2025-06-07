import pygame

from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Window
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

        pygame.display.set_caption("Mountain Shooter")

    def run(self):
        running = True

        while running:
            # Set Menu
            menu = Menu(window=self.window)

            menu.run()

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close the window
                    quit()  # Close the program
                    running = False  # Stop the loop
