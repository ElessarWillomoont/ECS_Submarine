from components.position import Position
from components.render import Render
import arcade

def create_fish(ecs_manager):
    fish = ecs_manager.create_entity()
    fish_sprite = arcade.Sprite("assets/fish.png", 0.3)
    fish.add_component("Position", Position(700, 500))
    fish.add_component("Render", Render(fish_sprite))
    return fish
