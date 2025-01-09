from components.position import Position
from components.render import Render
import arcade

def create_seaweed(ecs_manager):
    seaweed = ecs_manager.create_entity()
    seaweed_sprite = arcade.Sprite("assets/seaweed.png", 0.5)
    seaweed.add_component("Position", Position(100, 150))
    seaweed.add_component("Render", Render(seaweed_sprite))
    return seaweed
