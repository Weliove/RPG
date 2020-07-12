from src.file_methods import create_entity, update_entity


class Item:
    def __init__(self, name, _type, red, damage, _range, life_points, area, abilities, effects, description):
        self.name = name
        self._type = _type
        self.red = red
        self.damage = damage
        self._range = _range
        self.life_points = life_points
        self.area = area
        self.abilities = abilities
        self.effects = effects
        self.description = description

        if _type == 'Armor':
            self.type_database_item = 'armors'
        else:
            self.type_database_item = 'weapons'

        self.item = {
            'name': self.name,
            'type': self._type,
            'red': self.red,
            'damage': self.damage,
            'range': self._range,
            'life_points': self.life_points,
            'area': self.area,
            'abilities': self.abilities,
            'effects': self.effects,
            'description': self.description
        }

    def get_item(self):
        return self.item

    def create_item(self, name, file_name):
        return create_entity(
            name,
            file_name,
            self.get_item(),
            self.type_database_item + '_file',
            self.type_database_item + '_folder'
        )

    def update_item(self, name, current_name, file_name):
        return update_entity(
            name,
            current_name,
            file_name,
            self.get_item(),
            self.type_database_item + '_file',
            self.type_database_item + '_folder'
        )
