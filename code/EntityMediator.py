from code.Entity import Entity
from code.Enemy import Enemy


class EntityMediator:
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for entity in entity_list:

            EntityMediator.__verify_collision_window(entity=entity)

    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Enemy):
            # Destroy the enemy if it goes out of the window
            if entity.rect.right <= 0:
                entity.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)
