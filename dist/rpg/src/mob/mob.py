from src.file_methods import create_entity


class Mob:
    def __init__(self, name, hp, ad, _class, weapon, armor, title, abilities):
        self.name = name
        self.hp = int(hp)
        self.ad = int(ad)
        self._class = _class
        self.weapon = weapon
        self.armor = armor
        self.title = title
        self.abilities = abilities

        self.mob = {
            'name': self.name,
            'life_points': self.hp,
            'adrenaline': self.ad,
            'class': self._class,
            'weapon': self.weapon,
            'armor': self.armor,
            'title': self.title,
            'abilities': self.abilities
        }

    def get_mob(self):
        return self.mob

    def create_mob(self, name, file_name):
        return create_entity(name, file_name, self.get_mob(), 'mobs_file', 'mobs_folder')
