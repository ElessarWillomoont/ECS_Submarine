class LogicSystem:
    def __init__(self, command_queue):
        self.command_queue = command_queue

    def update(self, entities, delta_time):
        while self.command_queue:
            command = self.command_queue.pop(0)
            # 简单解析命令并更新实体
            if command == "move_north":
                for entity in entities.values():
                    movement = entity.get_component("Movement")
                    if movement:
                        movement.speed_y = 100