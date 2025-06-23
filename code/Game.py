import pygame

from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS
from code.Menu import Menu
from code.Level import Level


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

            # LEVEL OPTIONS
            if selected_option in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level = Level(
                    window=self.window, name="Level1", game_mode=selected_option
                )

                level_result = level.run()
            # QUIT
            elif selected_option == MENU_OPTIONS[4]:
                running = False  # Stop the loop
                pygame.quit()  # Close the window
                quit()  # Close the program
            else:
                pass
