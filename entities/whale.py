from components.position import Position
from components.render import Render
import arcade

def create_whale(ecs_manager):
    whale = ecs_manager.create_entity()
    whale_sprite = arcade.Sprite("assets/whale.png", 0.8)
    whale.add_component("Position", Position(500, 300))
    whale.add_component("Render", Render(whale_sprite))
    return whale
