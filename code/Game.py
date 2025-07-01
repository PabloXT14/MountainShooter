import pygame

from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS, LEVELS
from code.Menu import Menu
from code.Level import Level
from code.Score import Score
from code.GameOver import GameOver


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

            # Score Screen
            score = Score(window=self.window)

            # Game Over Screen
            game_over = GameOver(window=self.window)

            # LEVEL OPTIONS
            if selected_option in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                # Loop de níveis
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
                        game_over.show()
                        break

                    # Se o jogador ganhar/passar do último nível, salva o score
                    if level_data["level_number"] == len(LEVELS):
                        score.save(
                            game_mode=selected_option,
                            players_score=players_score,
                        )

            # SCORE
            elif selected_option == MENU_OPTIONS[3]:
                score.show()

            # QUIT
            elif selected_option == MENU_OPTIONS[4]:
                running = False  # Stop the loop
                pygame.quit()  # Close the window
                quit()  # Close the program
            else:
                pass
