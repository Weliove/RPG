from src.file_methods import create_entity, update_entity


class Title:
    def __init__(self, name, requirements, description):
        self.name = name
        self.description = description
        self.requirements = requirements

        self.file = 'titles_file'
        self.folder = 'titles_folder'

        self.title = {
            'name': self.name,
            'requirements': self.requirements,
            'description': self.description
        }

    def get_title(self):
        return self.title

    def create_title(self, name, file_name):
        return create_entity(name, file_name, self.get_title(), self.file, self.folder)

    def update_title(self, name, current_name, file_name):
        return update_entity(name, current_name, file_name, self.get_title(), self.file, self.folder)
