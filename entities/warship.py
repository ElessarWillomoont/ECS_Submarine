from components.position import Position
from components.render import Render
import arcade

def create_warship(ecs_manager):
    warship = ecs_manager.create_entity()
    warship_sprite = arcade.Sprite("assets/warship.png", 0.5)
    warship.add_component("Position", Position(600, 400))
    warship.add_component("Render", Render(warship_sprite))
    return warship
