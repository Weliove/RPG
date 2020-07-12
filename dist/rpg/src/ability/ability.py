from src.file_methods import create_entity, update_entity


class Ability:
    def __init__(self, name, cast_time, components, requirements, conditions, effects, description):
        self.name = name
        self.cast_time = cast_time
        self.components = components
        self.requirements = requirements
        self.conditions = conditions
        self.effects = effects
        self.description = description

        self.file = 'abilities_file'
        self.folder = 'abilities_folder'

        self.ability = {
            'name': self.name,
            'cast_time': self.cast_time,
            'components': self.components,
            'requirements': self.requirements,
            'conditions': self.conditions,
            'effects': self.effects,
            'description': self.description
        }

    def get_ability(self):
        return self.ability

    def create_ability(self, name, file_name):
        return create_entity(name, file_name, self.get_ability(), self.file, self.folder)

    def update_ability(self, name, current_name, file_name):
        return update_entity(name, current_name, file_name, self.get_ability(), self.file, self.folder)
