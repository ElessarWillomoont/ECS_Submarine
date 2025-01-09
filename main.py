import arcade
from ecs import ECSManager
from components.position import Position
from components.render import Render
from components.movement import Movement
from systems.render_system import RenderSystem
from systems.movement_system import MovementSystem
from systems.logic_system import LogicSystem


class MyGame(arcade.Window):
    MOVE_DISTANCE = 20  # Distance to move with each key press

    def __init__(self):
        super().__init__(800, 600, "ECS Submarine Game")
        arcade.set_background_color(arcade.color.BLACK)

        # Load the background image
        self.background = arcade.load_texture("assets/Background.png")

        # Initialize ECS
        self.ecs_manager = ECSManager()
        self.command_queue = []

        # Add systems
        self.ecs_manager.add_system(RenderSystem())
        self.ecs_manager.add_system(MovementSystem())
        self.ecs_manager.add_system(LogicSystem(self.command_queue))

        # Create entity
        self.player = self.ecs_manager.create_entity()
        submarine_sprite = arcade.Sprite("assets/submarine.png", 0.5)
        self.player.add_component("Position", Position(400, 300))
        self.player.add_component("Render", Render(submarine_sprite))
        # Movement is no longer used for movement logic but retained for future extensions
        self.player.add_component("Movement", Movement(0, 0))

    def on_draw(self):
        arcade.start_render()
        # Draw the background
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)

        # Update and draw all entities
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
