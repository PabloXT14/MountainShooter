from code.Entity import Entity
from code.Enemy import Enemy
from code.PlayerShot import PlayerShot
from code.EnemyShot import EnemyShot
from code.Constants import WINDOW_WIDTH


class EntityMediator:
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for entity in entity_list:

            EntityMediator.__verify_collision_window(entity=entity)

    @staticmethod
    def __verify_collision_window(entity: Entity):
        # Destroy the enemy if it goes out of the window
        if isinstance(entity, Enemy):
            if entity.rect.right <= 0:
                entity.health = 0

        # Destroy PlayerShot if it goes out of the window
        if isinstance(entity, PlayerShot):
            if entity.rect.left >= WINDOW_WIDTH:
                entity.health = 0

        # Destroy EnemyShot if it goes out of the window
        if isinstance(entity, EnemyShot):
            if entity.rect.right <= 0:
                entity.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)
