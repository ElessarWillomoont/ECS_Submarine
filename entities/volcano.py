from components.position import Position
from components.render import Render
import arcade

def create_volcano(ecs_manager):
    volcano = ecs_manager.create_entity()
    volcano_sprite = arcade.Sprite("assets/volcano.png", 0.5)
    volcano.add_component("Position", Position(200, 100))
    volcano.add_component("Render", Render(volcano_sprite))
    return volcano
