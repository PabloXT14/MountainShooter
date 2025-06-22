from code.Background import Background
from code.Constants import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(
        entity_name: str, level: int, position: tuple = (0, 0), images_amount: int = 1
    ):
        match entity_name:
            case "background":
                list_bg = []

                for i in range(images_amount):
                    list_bg.append(
                        Background(name=f"Level{level}Bg{i}", position=position)
                    )

                    # Insert the background again to create a parallax effect
                    list_bg.append(
                        Background(
                            name=f"Level{level}Bg{i}", position=(WINDOW_WIDTH, 0)
                        )
                    )

                return list_bg

            case "player1":
                return Player(name="Player1", position=(10, WINDOW_HEIGHT / 4))
            case "player2":
                return Player(name="Player2", position=(10, WINDOW_HEIGHT / 2))
