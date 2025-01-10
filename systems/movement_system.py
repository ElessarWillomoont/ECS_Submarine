class MovementSystem:
    def update(self, entities, delta_time):
        for entity in entities.values():
            rel_position = entity.get_component("RelativePosition")
            movement = entity.get_component("Movement")
            if rel_position and movement:
                # Update relative position based on movement speed and delta time
                rel_position.rel_x += movement.speed_x * delta_time
                rel_position.rel_y += movement.speed_y * delta_time
                
                # Clamp the relative position to stay within valid range
                rel_position.rel_x = max(0.0, min(1.0, rel_position.rel_x))
                rel_position.rel_y = max(-1.0, min(1.0, rel_position.rel_y))
