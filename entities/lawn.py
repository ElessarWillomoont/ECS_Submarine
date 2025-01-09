from components.position import Position
from components.render import Render
import arcade

def create_lawn(ecs_manager):
    lawn = ecs_manager.create_entity()
    lawn_sprite = arcade.Sprite("assets/lawn.png", 0.6)
    lawn.add_component("Position", Position(600, 100))
    lawn.add_component("Render", Render(lawn_sprite))
    return lawn
