from components.position import Position
from components.render import Render
import arcade

def create_shark(ecs_manager):
    shark = ecs_manager.create_entity()
    shark_sprite = arcade.Sprite("assets/shark.png", 0.5)
    shark.add_component("Position", Position(300, 600))
    shark.add_component("Render", Render(shark_sprite))
    return shark
