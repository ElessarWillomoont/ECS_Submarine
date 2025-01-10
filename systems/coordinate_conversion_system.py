class CoordinateConversionSystem:
    def __init__(self, screen_width, screen_height, horizon_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.horizon_height = horizon_height

    def update(self, entities, delta_time):
        for entity in entities.values():
            rel_pos = entity.get_component("RelativePosition")
            abs_pos = entity.get_component("Position")
            if rel_pos and abs_pos:
                abs_pos.x = rel_pos.rel_x * self.screen_width
                abs_pos.y = self.horizon_height + (rel_pos.rel_y * (self.screen_height // 2))
