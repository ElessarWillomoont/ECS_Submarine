class MovementSystem:
    def update(self, entities, delta_time):
        for entity in entities.values():
            position = entity.get_component("Position")
            movement = entity.get_component("Movement")
            if position and movement:
                position.x += movement.speed_x * delta_time
                position.y += movement.speed_y * delta_time