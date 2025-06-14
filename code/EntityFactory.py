from code.Background import Background


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

                return list_bg
