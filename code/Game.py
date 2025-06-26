import pygame

from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS, LEVELS
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
            # Players score
            players_score = [0, 0]  # [Player 1, Player 2]

            # Set Menu
            menu = Menu(window=self.window)

            selected_option = menu.run()

            # LEVEL OPTIONS
            if selected_option in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                # level = Level(
                #     window=self.window, name="Level1", game_mode=selected_option
                # )

                # level_result = level.run()
                for level_data in LEVELS:
                    level = Level(
                        window=self.window,
                        game_mode=selected_option,
                        name=level_data["name"],
                        level_number=level_data["level_number"],
                        bg_images_amount=level_data["bg_images_amount"],
                        players_score=players_score,
                    )

                    level_result = level.run()

                    # Se o jogador falhar/perder, sai do loop de níveis
                    if not level_result:
                        # TODO: Mostrar tela de derrota (dica: copiar do Menu)
                        break

            # QUIT
            elif selected_option == MENU_OPTIONS[4]:
                running = False  # Stop the loop
                pygame.quit()  # Close the window
                quit()  # Close the program
            else:
                pass
