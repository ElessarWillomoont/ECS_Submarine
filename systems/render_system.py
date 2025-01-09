import arcade

class RenderSystem:
    def update(self, entities, delta_time):
        for entity in entities.values():
            position = entity.get_component("Position")
            render = entity.get_component("Render")
            if position and render:
                render.sprite.center_x = position.x
                render.sprite.center_y = position.y
                render.sprite.draw()