class Entity:
    """Entity class representing an object in the game."""
    def __init__(self, entity_id):
        self.id = entity_id
        self.components = {}

    def add_component(self, component_type, component):
        """Add a component to the entity."""
        self.components[component_type] = component

    def get_component(self, component_type):
        """Retrieve a component of the specified type."""
        return self.components.get(component_type)


class ECSManager:
    """ECS Manager to handle all entities and systems."""
    def __init__(self):
        self.entities = {}
        self.systems = []

    def create_entity(self):
        """Create a new entity and add it to the entity list."""
        entity_id = len(self.entities) + 1
        entity = Entity(entity_id)
        self.entities[entity_id] = entity
        return entity

    def add_system(self, system):
        """Add a system to the ECS manager."""
        self.systems.append(system)

    def update(self, delta_time):
        """Update all systems with the current entities and delta time."""
        for system in self.systems:
            system.update(self.entities, delta_time)
