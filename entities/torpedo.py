from components.position import Position
from components.render import Render
import arcade

def create_torpedo(ecs_manager):
    torpedo = ecs_manager.create_entity()
    torpedo_sprite = arcade.Sprite("assets/torpedo.png", 0.2)
    torpedo.add_component("Position", Position(400, 300))
    torpedo.add_component("Render", Render(torpedo_sprite))
    return torpedo
