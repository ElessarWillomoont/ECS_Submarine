class Entity:
    """实体类，表示游戏中的一个对象。"""
    def __init__(self, entity_id):
        self.id = entity_id
        self.components = {}

    def add_component(self, component_type, component):
        self.components[component_type] = component

    def get_component(self, component_type):
        return self.components.get(component_type)


class ECSManager:
    """ECS 管理器，管理所有实体和系统。"""
    def __init__(self):
        self.entities = {}
        self.systems = []

    def create_entity(self):
        entity_id = len(self.entities) + 1
        entity = Entity(entity_id)
        self.entities[entity_id] = entity
        return entity

    def add_system(self, system):
        self.systems.append(system)

    def update(self, delta_time):
        for system in self.systems:
            system.update(self.entities, delta_time)
