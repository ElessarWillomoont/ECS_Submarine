from entity_factory import create_entity_with_components

def create_whale(ecs_manager, rel_x, rel_y):
    return create_entity_with_components(
        ecs_manager, "assets/whale.png", 0.8, rel_x, rel_y
    )
