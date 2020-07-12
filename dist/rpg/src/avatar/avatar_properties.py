from src.item.item_properties import *
from src.title.title_properties import get_title_names


class AvatarProperties:
    def __init__(self):

        self.MAX_HP = 3000
        self.MAX_AD = 500

        WEAPON_PROPERTY = 0
        self.weapons_values = self.get_properties(WEAPON_PROPERTY)

        ARMOR_PROPERTY = 1
        self.armors_values = self.get_properties(ARMOR_PROPERTY)

        TITLE_PROPERTY = 2
        self.titles_values = self.get_properties(TITLE_PROPERTY)

        CLASS_PROPERTY = 3
        self.classes_values = self.get_properties(CLASS_PROPERTY)

        TYPE_PROPERTY = 4
        self.type_values = self.get_properties(TYPE_PROPERTY)

    def get_weapons_properties(self):
        return get_weapons_properties()

    def get_armors_properties(self):
        return get_armors_properties()

    def get_titles_properties(self):
        return get_title_names()

    def get_classes_properties(self):
        CLASSES_PROPERTIES = [
            "Warrior",
            "Thief",
            "Guardian",
            "Reaper",
            "Support",
            "Esper"
        ]
        result = sorted(CLASSES_PROPERTIES)
        result.insert(0, "None")
        return result

    def get_type_properties(self):
        TYPE_PROPERTIES = (
            "Player",
            "NPC",
            "Monster"
        )
        return sorted(TYPE_PROPERTIES)

    def get_proficiencies_properties(self):
        PROFICIENCIES_PROPERTIES = [
            "Arcanism",
            "Manufacturing",
            "Athletics",
            "Occult",
            "Medicine",
            "Nature",
            "Survival",
            "Stealth",
            "Religion",
            "Society",
            "Intimidation",
            "Logia",
            "Diplomacy",
            "Concealment"
        ]
        result = sorted(PROFICIENCIES_PROPERTIES)
        result.insert(0, "None")
        return result

    def get_properties(self, property_type):
        value = ()

        # 0 = Weapons
        # 1 = Armors
        # 2 = Titles
        # 3 = Classes
        # 4 = Type

        if property_type == 0:
            value = self.get_weapons_properties()
        elif property_type == 1:
            value = self.get_armors_properties()
        elif property_type == 2:
            value = self.get_titles_properties()
        elif property_type == 3:
            value = self.get_classes_properties()
        elif property_type == 4:
            value = self.get_type_properties()

        return value
