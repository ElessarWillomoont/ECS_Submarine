import arcade
from ecs import ECSManager
from systems.render_system import RenderSystem
from systems.movement_system import MovementSystem
from systems.logic_system import LogicSystem
from entities import (
    create_submarine,
    create_warship,
    create_volcano,
    create_fish,
    create_shark,
    create_torpedo,
    create_mine,
    create_seaweed,
    create_whale,
    create_lighthouse,
    create_lawn,
    create_soil
)


class MyGame(arcade.Window):
    MOVE_DISTANCE = 20  # Distance to move with each key press

    def __init__(self):
        super().__init__(1280, 720, "ECS Submarine Game")
        arcade.set_background_color(arcade.color.BLACK)

        self.background = arcade.load_texture("assets/Background.png")

        self.ecs_manager = ECSManager()
        self.command_queue = []

        self.ecs_manager.add_system(RenderSystem())
        self.ecs_manager.add_system(MovementSystem())
        self.ecs_manager.add_system(LogicSystem(self.command_queue))

        self.create_entities()

    def create_entities(self):
        self.player = create_submarine(self.ecs_manager)
        create_warship(self.ecs_manager)
        create_volcano(self.ecs_manager)
        create_fish(self.ecs_manager)
        create_shark(self.ecs_manager)
        create_torpedo(self.ecs_manager)
        create_mine(self.ecs_manager)
        create_seaweed(self.ecs_manager)
        create_whale(self.ecs_manager)
        create_lighthouse(self.ecs_manager)
        create_lawn(self.ecs_manager) 
        create_soil(self.ecs_manager) 

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.ecs_manager.update(0)

    def on_key_press(self, key, modifiers):
        position = self.player.get_component("Position")
        if key == arcade.key.UP:
            position.y += self.MOVE_DISTANCE
        elif key == arcade.key.DOWN:
            position.y -= self.MOVE_DISTANCE
        elif key == arcade.key.LEFT:
            position.x -= self.MOVE_DISTANCE
        elif key == arcade.key.RIGHT:
            position.x += self.MOVE_DISTANCE

    def update(self, delta_time):
        self.ecs_manager.update(delta_time)


if __name__ == "__main__":
    MyGame()
    arcade.run()
