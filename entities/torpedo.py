from entity_factory import create_entity_with_components

def create_torpedo(ecs_manager, rel_x, rel_y):
    return create_entity_with_components(
        ecs_manager, "assets/torpedo.png", 0.2, rel_x, rel_y
    )
