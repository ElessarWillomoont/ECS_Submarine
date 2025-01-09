from components.position import Position
from components.render import Render
import arcade

def create_lighthouse(ecs_manager):
    lighthouse = ecs_manager.create_entity()
    lighthouse_sprite = arcade.Sprite("assets/lighthouse.png", 0.7)
    lighthouse.add_component("Position", Position(1000, 500))
    lighthouse.add_component("Render", Render(lighthouse_sprite))
    return lighthouse
