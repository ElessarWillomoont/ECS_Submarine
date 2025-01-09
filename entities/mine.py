from components.position import Position
from components.render import Render
import arcade

def create_mine(ecs_manager):
    mine = ecs_manager.create_entity()
    mine_sprite = arcade.Sprite("assets/mine.png", 0.3)
    mine.add_component("Position", Position(800, 200))
    mine.add_component("Render", Render(mine_sprite))
    return mine
