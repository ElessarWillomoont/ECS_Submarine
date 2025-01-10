# entity_factory.py

from components.relative_position import RelativePosition
from components.position import Position
from components.render import Render
import arcade

def create_entity_with_components(ecs_manager, sprite_path, scale, rel_x, rel_y):
    """
    Create an entity with common components: RelativePosition, Position, and Render.

    Parameters:
        ecs_manager: ECSManager
            The ECS manager to create and manage the entity.
        sprite_path: str
            Path to the sprite image.
        scale: float
            Scale factor for the sprite.
        rel_x: float
            X position relative to the screen width (0.0 ~ 1.0).
        rel_y: float
            Y position relative to the horizon height (-1.0 ~ 1.0).

    Returns:
        entity: Entity
            The created entity with the specified components.
    """
    entity = ecs_manager.create_entity()
    sprite = arcade.Sprite(sprite_path, scale)
    entity.add_component("RelativePosition", RelativePosition(rel_x, rel_y))
    entity.add_component("Position", Position(0, 0))  # Initialize absolute position as (0, 0)
    entity.add_component("Render", Render(sprite))
    return entity
