from entity_factory import create_entity_with_components

def create_warship(ecs_manager, rel_x, rel_y):
    return create_entity_with_components(
        ecs_manager, "assets/warship.png", 0.5, rel_x, rel_y
    )
