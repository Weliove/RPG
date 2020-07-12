from src.file_methods import create_entity, update_entity


class Avatar:
    def __init__(self, name, life_points, adrenaline, _class, weapon, armor, physical_ab, title, abilities, description):
        self.name = name
        self.life_points = life_points
        self.adrenaline = adrenaline
        self._class = _class
        self.weapon = weapon
        self.armor = armor
        self.physical_ab = physical_ab
        self.title = title
        self.abilities = abilities
        self.description = description

        self.file = 'avatars_file'
        self.folder = 'avatars_folder'

        self.avatar = {
            'name': self.name,
            'life_points': self.life_points,
            'adrenaline': self.adrenaline,
            'class': self._class,
            'weapon': self.weapon,
            'armor': self.armor,
            'physical_ab': self.physical_ab,
            'title': self.title,
            'abilities': self.abilities,
            'description': self.description
        }

    def get_avatar(self):
        return self.avatar

    def create_avatar(self, name, file_name):
        return create_entity(name, file_name, self.get_avatar(), self.file, self.folder)

    def update_avatar(self, name, current_name, file_name):
        return update_entity(name, current_name, file_name, self.get_avatar(), self.file, self.folder)
