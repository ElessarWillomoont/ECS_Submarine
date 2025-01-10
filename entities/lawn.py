from entity_factory import create_entity_with_components

def create_lawn(ecs_manager, rel_x, rel_y):
    return create_entity_with_components(
        ecs_manager, "assets/lawn.png", 0.6, rel_x, rel_y
    )
