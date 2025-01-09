from components.position import Position
from components.render import Render
import arcade

def create_soil(ecs_manager):
    soil = ecs_manager.create_entity()
    soil_sprite = arcade.Sprite("assets/soil.png", 0.5)
    soil.add_component("Position", Position(400, 50))
    soil.add_component("Render", Render(soil_sprite))
    return soil
