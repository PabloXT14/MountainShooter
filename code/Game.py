import pygame

from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS
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

            selected_option = menu.run()

            # NEW GAME (1 PLAYER)
            if selected_option == MENU_OPTIONS[0]:
                pass
            # NEW GAME (2 PLAYERS - COOPERATIVE)
            elif selected_option == MENU_OPTIONS[1]:
                pass
            # NEW GAME (2 PLAYERS - COMPETITIVE)
            elif selected_option == MENU_OPTIONS[2]:
                pass
            # SCORE
            elif selected_option == MENU_OPTIONS[3]:
                pass
            # QUIT
            elif selected_option == MENU_OPTIONS[4]:
                running = False  # Stop the loop
                pygame.quit()  # Close the window
                quit()  # Close the program
            else:
                pass
