import json
import os
from src.popup_window import *

# --- Essentials ---
essentials_folder = "essentials\\"

# --- Avatar ---
avatars_folder = essentials_folder + "avatars\\"
avatars_file = avatars_folder + "avatars.txt"

# --- Abilities ---
abilities_folder = essentials_folder + "abilities\\"
abilities_file = abilities_folder + "abilities.txt"

# --- Items ---
# items_folder = essentials_folder + "items\\"
# items_file = items_folder + "items.txt"

# --- Weapons ---
weapons_folder = essentials_folder + "weapons\\"
weapons_file = weapons_folder + "weapons.txt"

# --- Armors ---
armors_folder = essentials_folder + "armors\\"
armors_file = armors_folder + "armors.txt"

# --- Mobs ---
mobs_folder = essentials_folder + "mobs\\"
mobs_file = mobs_folder + "mobs.txt"

# --- Titles ---
titles_folder = essentials_folder + "titles\\"
titles_file = titles_folder + "titles.txt"

# --- Entities Dictionary ---
entities = {
    'essentials_folder': essentials_folder,
    'avatars_folder': avatars_folder,
    'avatars_file': avatars_file,
    'abilities_folder': abilities_folder,
    'abilities_file': abilities_file,
    'weapons_folder': weapons_folder,
    'weapons_file': weapons_file,
    'armors_folder': armors_folder,
    'armors_file': armors_file,
    'mobs_folder': mobs_folder,
    'mobs_file': mobs_file,
    'titles_folder': titles_folder,
    'titles_file': titles_file
}


# --- Entity ---
def create_entity(name, file_name, entity, database_file, folder):
    with open(entities[database_file], "r") as file:
        lines = file.readlines()

        for temp_entity_name in lines:
            if temp_entity_name.strip() == name:
                popup_showinfo(f"{name} already exists!")
                return False

    with open(entities[database_file], "a") as file:
        file.write(name + "\n")

    with open(entities[folder] + file_name, "w") as file:
        json.dump(entity, file)

    return True


def update_entity(name, current_name, file_name, entity, database_file, folder):
    name_is_different = False

    current_name_lower = current_name.lower()

    with open(entities[database_file], "r") as file:
        lines = file.readlines()

        for temp_entity_name in lines:
            if temp_entity_name.strip() == current_name_lower and current_name_lower != name:
                name_is_different = True
                break

    if name_is_different:
        name_index = lines.index(current_name_lower + '\n')
        lines[name_index] = name + '\n'

        result_names = ""
        for item in lines:
            result_names += item

        with open(entities[database_file], "w") as file:
            file.write(result_names)

        os.remove(entities[folder] + current_name_lower + '.txt')

        if database_file == 'abilities_file':
            print('dfsdfdsf')
            update_avatar_ability_name(name, current_name_lower)

    with open(entities[folder] + file_name, "w") as file:
        json.dump(entity, file)

    return True


def update_avatar_ability_name(name, current_name):
    local_entities = []

    print(f'name: {name} current_name: {current_name}')

    with open(entities['avatars_file'], "r") as file:
        lines = file.readlines()

        for avatar in lines:
            local_entities.append(avatar.strip())

    for avatar in local_entities:
        with open(entities['avatars_folder'] + avatar + '.txt', "r") as file:
            temp_avatar = json.load(file)

        for ability in temp_avatar['abilities']:
            print(f'ability: {ability} current_name: {current_name}')
            if ability == current_name:
                print('é igual')
                ability_index = temp_avatar['abilities'].index(ability)
                print(f'index: {ability_index}')
                temp_avatar['abilities'][ability_index] = name

                with open(entities['avatars_folder'] + avatar + '.txt', "w") as file:
                    json.dump(temp_avatar, file)



def check_entity_existence(entity_name, database_file):
    local_entities = []

    with open(entities[database_file], "r") as file:
        lines = file.readlines()

        for temp_entity_name in lines:
            if entity_name in temp_entity_name.strip():
                local_entities.append(temp_entity_name.strip())

    return local_entities


def get_json_entity(file_name, folder):
    with open(entities[folder] + file_name + ".txt", "r") as file:
        local_entity = json.load(file)

    return local_entity


def get_all_file_names(database_file):
    local_entities = []

    with open(entities[database_file], "r") as file:
        lines = file.readlines()

        for temp_entity_name in lines:
            local_entities.append(temp_entity_name.strip())

    final_result = sorted(local_entities)
    final_result.insert(0, "None")

    return tuple(final_result)
