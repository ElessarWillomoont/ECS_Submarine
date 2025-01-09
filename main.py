import arcade
from ecs import ECSManager
from components.position import Position
from components.render import Render
from components.movement import Movement
from systems.render_system import RenderSystem
from systems.movement_system import MovementSystem
from systems.logic_system import LogicSystem


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "ECS Game")
        arcade.set_background_color(arcade.color.BLACK)

        # 初始化 ECS
        self.ecs_manager = ECSManager()
        self.command_queue = []

        # 添加系统
        self.ecs_manager.add_system(RenderSystem())
        self.ecs_manager.add_system(MovementSystem())
        self.ecs_manager.add_system(LogicSystem(self.command_queue))

        # 创建实体
        player = self.ecs_manager.create_entity()
        sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 0.5)
        player.add_component("Position", Position(400, 300))
        player.add_component("Render", Render(sprite))
        player.add_component("Movement", Movement(0, 0))

    def on_draw(self):
        arcade.start_render()
        self.ecs_manager.update(0)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.command_queue.append("move_north")

    def update(self, delta_time):
        self.ecs_manager.update(delta_time)


if __name__ == "__main__":
    MyGame()
    arcade.run()
