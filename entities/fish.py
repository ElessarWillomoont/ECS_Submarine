from entity_factory import create_entity_with_components

def create_fish(ecs_manager, rel_x, rel_y):
    return create_entity_with_components(
        ecs_manager, "assets/fish.png", 0.3, rel_x, rel_y
    )
