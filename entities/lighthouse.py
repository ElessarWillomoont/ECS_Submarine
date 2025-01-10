from entity_factory import create_entity_with_components

def create_lighthouse(ecs_manager, rel_x, rel_y):
    return create_entity_with_components(
        ecs_manager, "assets/lighthouse.png", 0.7, rel_x, rel_y
    )
