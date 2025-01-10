from entity_factory import create_entity_with_components
from components.movement import Movement

def create_submarine(ecs_manager):
    submarine = create_entity_with_components(
        ecs_manager, "assets/submarine.png", 0.5, 0.5, -0.5
    )
    submarine.add_component("Movement", Movement(0, 0))  # Add Movement component
    return submarine
