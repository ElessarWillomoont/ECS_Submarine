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
    create_soil,
)


class MyGame(arcade.Window):
    MOVE_DISTANCE = 20  # Distance to move with each key press

    def __init__(self):
        super().__init__(1280, 720, "ECS Submarine Game")
        arcade.set_background_color(arcade.color.BLACK)

        # Load background images
        self.background_sky = arcade.load_texture("assets/Background_Sky.png")
        self.background_ocean = arcade.load_texture("assets/Background.png")

        # Initialize horizon height (default to middle of screen)
        self.horizon_height = self.height // 2

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
        # Draw the dynamic background
        self.draw_background()

        # Update and draw all entities
        self.ecs_manager.update(0)

    def draw_background(self):
        # Calculate the scale factor to maintain the aspect ratio
        sky_scale = self.width / self.background_sky.width
        ocean_scale = self.width / self.background_ocean.width

        # Calculate the display height for both images
        sky_height = self.background_sky.height * sky_scale
        ocean_height = self.background_ocean.height * ocean_scale

        # Draw the sky part
        arcade.draw_lrwh_rectangle_textured(
            0,
            self.horizon_height,  # Y position starts at horizon
            self.width,
            sky_height,
            self.background_sky,
        )

        # Draw the ocean part
        arcade.draw_lrwh_rectangle_textured(
            0,
            self.horizon_height - ocean_height,  # Adjust ocean to start below the horizon
            self.width,
            ocean_height,
            self.background_ocean,
        )

        # Add a gradient transition at the horizon
        gradient_height = 50  # Height of the gradient region
        for i in range(gradient_height):
            alpha = int(255 * (1 - i / gradient_height))  # Gradually decrease opacity
            arcade.draw_rectangle_filled(
                self.width / 2,  # Centered horizontally
                self.horizon_height - i,  # Vertical position moves down
                self.width,  # Full width of the screen
                1,  # Height of each gradient step
                (0, 0, 0, alpha)  # Semi-transparent black (adjust if needed)
            )


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
        elif key == arcade.key.V:
            # Increase horizon height (sky expands)
            self.horizon_height = min(self.horizon_height + 20, self.height)
        elif key == arcade.key.B:
            # Decrease horizon height (ocean expands)
            self.horizon_height = max(self.horizon_height - 20, 0)

    def update(self, delta_time):
        self.ecs_manager.update(delta_time)


if __name__ == "__main__":
    MyGame()
    arcade.run()
