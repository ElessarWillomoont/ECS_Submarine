import arcade
from ecs import ECSManager
from systems.render_system import RenderSystem
from systems.movement_system import MovementSystem
from systems.logic_system import LogicSystem
from systems.coordinate_conversion_system import CoordinateConversionSystem
from entities import (
    create_lighthouse,
    create_lawn,
    create_warship,
    create_fish,
    create_shark,
    create_whale,
    create_seaweed,
    create_submarine,
)

class MyGame(arcade.Window):
    MOVE_DISTANCE = 0.08  # Distance to move with each key press in relative coordinates

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

        # Add systems
        self.ecs_manager.add_system(RenderSystem())
        self.ecs_manager.add_system(MovementSystem())
        self.ecs_manager.add_system(LogicSystem(self.command_queue))
        self.ecs_manager.add_system(
            CoordinateConversionSystem(self.width, self.height, self.horizon_height)
        )

        self.create_entities()

    def create_entities(self):
        # Player-controlled submarine
        self.player = create_submarine(self.ecs_manager)
        submarine_position = self.player.get_component("Position")
        print(f"Submarine created at absolute position: ({submarine_position.x}, {submarine_position.y})")

        # Create warships on the horizon
        for i in range(3):
            warship = create_warship(self.ecs_manager, rel_x=0.2 + i * 0.2, rel_y=0.0)
            warship_position = warship.get_component("Position")
            print(f"Warship {i+1} created at absolute position: ({warship_position.x}, {warship_position.y})")

        # Create lawns extending from the left side of the horizon
        for i in range(3):
            lawn = create_lawn(self.ecs_manager, rel_x=0.05 + i * 0.1, rel_y=-0.1)
            lawn_position = lawn.get_component("Position")
            print(f"Lawn {i+1} created at absolute position: ({lawn_position.x}, {lawn_position.y})")

        # Create lighthouse with base on the horizon
        lighthouse = create_lighthouse(self.ecs_manager, rel_x=0.8, rel_y=-0.2)
        lighthouse_position = lighthouse.get_component("Position")
        print(f"Lighthouse created at absolute position: ({lighthouse_position.x}, {lighthouse_position.y})")

        # Create sea life below the horizon
        fish = create_fish(self.ecs_manager, rel_x=0.3, rel_y=-0.5)
        shark = create_shark(self.ecs_manager, rel_x=0.5, rel_y=-0.6)
        whale = create_whale(self.ecs_manager, rel_x=0.7, rel_y=-0.7)
        seaweed = create_seaweed(self.ecs_manager, rel_x=0.4, rel_y=-0.8)

    def on_draw(self):
        arcade.start_render()
        # Draw the dynamic background
        self.draw_background()
        # Update and draw all entities
        self.ecs_manager.update(0)

    def draw_background(self):
        sky_scale = self.width / self.background_sky.width
        ocean_scale = self.width / self.background_ocean.width
        sky_height = self.background_sky.height * sky_scale
        ocean_height = self.background_ocean.height * ocean_scale

        arcade.draw_lrwh_rectangle_textured(
            0, self.horizon_height, self.width, sky_height, self.background_sky
        )
        arcade.draw_lrwh_rectangle_textured(
            0, self.horizon_height - ocean_height, self.width, ocean_height, self.background_ocean
        )

    def on_key_press(self, key, modifiers):
        movement = self.player.get_component("Movement")
        if key == arcade.key.UP:
            movement.speed_y = self.MOVE_DISTANCE
        elif key == arcade.key.DOWN:
            movement.speed_y = -self.MOVE_DISTANCE
        elif key == arcade.key.LEFT:
            movement.speed_x = -self.MOVE_DISTANCE
        elif key == arcade.key.RIGHT:
            movement.speed_x = self.MOVE_DISTANCE
        elif key == arcade.key.V:
            self.horizon_height = min(self.horizon_height + 20, self.height)
        elif key == arcade.key.B:
            self.horizon_height = max(self.horizon_height - 20, 0)

    def on_key_release(self, key, modifiers):
        movement = self.player.get_component("Movement")
        if key in [arcade.key.UP, arcade.key.DOWN]:
            movement.speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            movement.speed_x = 0

    def update(self, delta_time):
        for system in self.ecs_manager.systems:
            if isinstance(system, CoordinateConversionSystem):
                system.horizon_height = self.horizon_height
        self.ecs_manager.update(delta_time)


if __name__ == "__main__":
    MyGame()
    arcade.run()
