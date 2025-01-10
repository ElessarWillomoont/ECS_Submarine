from entity_factory import create_entity_with_components

def create_seaweed(ecs_manager, rel_x, rel_y):
    return create_entity_with_components(
        ecs_manager, "assets/seaweed.png", 0.5, rel_x, rel_y
    )
