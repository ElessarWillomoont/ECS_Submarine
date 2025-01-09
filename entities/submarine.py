from components.position import Position
from components.render import Render
from components.movement import Movement
import arcade

def create_submarine(ecs_manager):
    submarine = ecs_manager.create_entity()
    submarine_sprite = arcade.Sprite("assets/submarine.png", 0.5)
    submarine.add_component("Position", Position(400, 300))
    submarine.add_component("Render", Render(submarine_sprite))
    submarine.add_component("Movement", Movement(0, 0))
    return submarine
