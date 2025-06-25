from code.Entity import Entity
from code.Enemy import Enemy
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.EnemyShot import EnemyShot
from code.Constants import WINDOW_WIDTH


class EntityMediator:
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]

            EntityMediator.__verify_collision_window(entity=entity1)

            # Check collision between entities
            for j in range(i + 1, len(entity_list)):
                # [i + 1] -> to avoid comparing the same entity with itself, and avoid comparing the same entity twice
                entity2 = entity_list[j]

                EntityMediator.__verify_collision_entity(
                    entity1=entity1, entity2=entity2
                )

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
    def __verify_collision_entity(entity1: Entity, entity2: Entity):
        has_interacted = False

        # Check collision between EnemyShot and Player
        if isinstance(entity1, EnemyShot) and isinstance(entity2, Player):
            has_interacted = True
        elif isinstance(entity1, Player) and isinstance(entity2, EnemyShot):
            has_interacted = True

        # Check collision between PlayerShot and Enemy
        elif isinstance(entity1, PlayerShot) and isinstance(entity2, Enemy):
            has_interacted = True
        elif isinstance(entity1, Enemy) and isinstance(entity2, PlayerShot):
            has_interacted = True

        # Check side collisions
        if has_interacted:
            if (
                entity1.rect.right >= entity2.rect.left
                and entity1.rect.left <= entity2.rect.right
                and entity1.rect.bottom >= entity2.rect.top
                and entity1.rect.top <= entity2.rect.bottom
            ):
                entity1.health -= entity2.damage
                entity2.health -= entity1.damage

                entity1.last_entity_to_cause_damage = entity2.name
                entity2.last_entity_to_cause_damage = entity1.name

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                entity_list.remove(entity)
