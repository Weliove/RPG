import tkinter as tk
from tkinter import ttk

from src.avatar.avatar import Avatar
from src.file_methods import get_json_entity
from src.item.item_properties import get_weapons_properties, get_armors_properties
from src.popup_window import *


class UserInterface(ttk.Frame):
    def __init__(self, parent, database_type_value, show_home):
        super().__init__(parent, style="FramesBackgroundColor.TFrame")

        self.parent = parent
        self.show_home = show_home
        self.database_type_value = database_type_value
        entity = parent.entity
        self.entity = entity

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.user_interface_scroll = UserInterfaceScroll(self)
        self.user_interface_scroll.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

        self.user_interface_scroll.create_user_interface_container(entity)


class UserInterfaceScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.screen = tk.Frame(container)
        self.screen.columnconfigure(0, weight=1)

        self.scrollable_window = self.create_window((0, 0), window=self.screen, anchor="nw")

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.screen.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mouse_wheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

    def _on_mouse_wheel(self, event):
        self.yview_scroll(-int(event.delta/120), "units")

    def create_user_interface_container(self, entity):
        container = self.container

        # --- Avatar Container ---

        user_interface_container = ttk.Frame(self.screen)
        user_interface_container.grid(row=0, column=0, sticky="NSEW")
        user_interface_container.columnconfigure(0, weight=1)

        # --- Entity Widgets ---

        if container.database_type_value == 'avatars_folder':
            self.create_avatar_interface(user_interface_container, entity)
        elif container.database_type_value == 'weapons_folder' or container.database_type_value == 'armors_folder':
            self.create_item_interface(user_interface_container, entity)
        elif container.database_type_value == 'titles_folder':
            self.create_title_interface(user_interface_container, entity)
        elif container.database_type_value == 'abilities_folder':
            self.create_ability_interface(user_interface_container, entity)

        # Adds the same pads to all children of the container
        for child in user_interface_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # --- Button Container ---

        user_interface_button_container = ttk.Frame(self.screen)
        user_interface_button_container.grid(row=1, column=0, sticky="EW")
        user_interface_button_container.rowconfigure(0, weight=1)
        user_interface_button_container.columnconfigure(0, weight=1)

        # --- Button Widgets ---

        self.create_user_interface_buttons(user_interface_button_container)

        # Adds the same pads to all children of the container
        for child in user_interface_button_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_avatar_interface(self, container, avatar):
        # --- Avatar Properties ---

        property_name = avatar['name']
        property_life_points = avatar['life_points']
        property_adrenaline = avatar['adrenaline']
        property_class = avatar['class']
        property_weapon = avatar['weapon']
        property_armor = avatar['armor']
        property_physical_ab = avatar['physical_ab']
        property_title = avatar['title']
        property_abilities = avatar['abilities']
        property_description = avatar['description']

        # --- Avatar Widgets ---

        avatar_name = ttk.Label(
            container,
            text=f"Name: {property_name}"
        )
        avatar_name.grid(row=0, column=0, sticky="W")

        avatar_life_points = ttk.Label(
            container,
            text=f"HP: {property_life_points}"
        )
        avatar_life_points.grid(row=1, column=0, sticky="W")

        avatar_adrenaline = ttk.Label(
            container,
            text=f"Adrenaline: {property_adrenaline}"
        )
        avatar_adrenaline.grid(row=2, column=0, sticky="W")

        avatar_class = ttk.Label(
            container,
            text=f"Class: {property_class}"
        )
        avatar_class.grid(row=3, column=0, sticky="W")

        avatar_weapon = ttk.Label(
            container,
            text=f"Weapon(s):\n{self.generate_weapons(property_weapon)}"
        )
        avatar_weapon.grid(row=4, column=0, sticky="W")

        avatar_armor = ttk.Label(
            container,
            text=f"Armor: {self.generate_armor(property_armor)}"
        )
        avatar_armor.grid(row=5, column=0, sticky="W")

        avatar_physical_ab = ttk.Label(
            container,
            text=f"Physical Ab.: {property_physical_ab}"
        )
        avatar_physical_ab.grid(row=6, column=0, sticky="EW")

        avatar_titles = ttk.Label(
            container,
            text=f"Title(s):\n{self.generate_titles(property_title)}"
        )
        avatar_titles.grid(row=7, column=0, sticky="W")

        avatar_abilities = ttk.Label(
            container,
            text=f"Abilities:\n{self.generate_abilities(property_abilities)}"
        )
        avatar_abilities.grid(row=8, column=0, sticky="W")

        avatar_description = ttk.Label(
            container,
            text=f"Description: {property_description}"
        )
        avatar_description.grid(row=9, column=0, sticky="EW")

        def reconfigure_labels(event):
            avatar_weapon.configure(wraplength=container.winfo_width() - 25)
            avatar_armor.configure(wraplength=container.winfo_width() - 25)
            avatar_titles.configure(wraplength=container.winfo_width() - 25)
            avatar_abilities.configure(wraplength=container.winfo_width() - 25)
            avatar_description.configure(wraplength=container.winfo_width() - 25)

        container.bind("<Configure>", reconfigure_labels)

    def create_item_interface(self, container, item):
        # --- Item Properties ---

        property_name = item['name']
        property_type = item['type']
        property_red = item['red']
        property_damage = item['damage']
        property_range = item['range']
        property_life_points = item['life_points']
        property_area = item['area']
        property_abilities = item['abilities']
        property_effects = item['effects']
        property_description = item['description']

        # --- Item Widgets ---

        item_name = ttk.Label(
            container,
            text=f"Name: {property_name}"
        )
        item_name.grid(row=0, column=0, sticky="EW")

        item_type = ttk.Label(
            container,
            text=f"Type: {property_type}"
        )
        item_type.grid(row=1, column=0, sticky="EW")

        item_red = ttk.Label(
            container,
            text=f"Reduction: {property_red}"
        )
        item_red.grid(row=2, column=0, sticky="EW")

        item_damage = ttk.Label(
            container,
            text=f"Damage: {property_damage}"
        )
        item_damage.grid(row=3, column=0, sticky="EW")

        item_range = ttk.Label(
            container,
            text=f"Range: {property_range}"
        )
        item_range.grid(row=4, column=0, sticky="EW")

        item_life_points = ttk.Label(
            container,
            text=f"HP: {property_life_points}"
        )
        item_life_points.grid(row=5, column=0, sticky="EW")

        item_area = ttk.Label(
            container,
            text=f"Area: {property_area}"
        )
        item_area.grid(row=6, column=0, sticky="EW")

        item_abilities = ttk.Label(
            container,
            text=f"Abilities:\n{self.generate_abilities(property_abilities)}"
        )
        item_abilities.grid(row=7, column=0, sticky="EW")

        item_effects = ttk.Label(
            container,
            text=f"Effects:\n{property_effects}"
        )
        item_effects.grid(row=8, column=0, sticky="EW")

        item_description = ttk.Label(
            container,
            text=f"Description: {property_description}"
        )
        item_description.grid(row=9, column=0, sticky="EW")

        def reconfigure_labels(event):
            item_abilities.configure(wraplength=container.winfo_width() - 25)
            item_effects.configure(wraplength=container.winfo_width() - 25)
            item_description.configure(wraplength=container.winfo_width() - 25)

        container.bind("<Configure>", reconfigure_labels)

    def create_title_interface(self, container, title):
        # --- Item Properties ---

        property_name = title['name']
        property_requirements = title['requirements']
        property_description = title['description']

        # --- Title Widgets ---

        title_name = ttk.Label(
            container,
            text=f"Name: {property_name}"
        )
        title_name.grid(row=0, column=0, sticky="EW")

        title_requirements = ttk.Label(
            container,
            text=f"Requirements:\n{property_requirements}"
        )
        title_requirements.grid(row=1, column=0, sticky="EW")

        title_description = ttk.Label(
            container,
            text=f"Description:\n{property_description}"
        )
        title_description.grid(row=2, column=0, sticky="EW")

        def reconfigure_labels(event):
            title_requirements.configure(wraplength=container.winfo_width() - 25)
            title_description.configure(wraplength=container.winfo_width() - 25)

        container.bind("<Configure>", reconfigure_labels)

    def create_ability_interface(self, container, ability):
        # --- Ability Properties ---

        property_name = ability['name']
        property_cast_time = ability['cast_time']
        property_components = ability['components']
        property_requirements = ability['requirements']
        property_conditions = ability['conditions']
        property_effects = ability['effects']
        property_description = ability['description']

        # --- Ability Widgets ---

        ability_name = ttk.Label(
            container,
            text=f"Name: {property_name}"
        )
        ability_name.grid(row=0, column=0, sticky="EW")

        ability_cast_time = ttk.Label(
            container,
            text=f"Cast Time: {property_cast_time}"
        )
        ability_cast_time.grid(row=1, column=0, sticky="EW")

        ability_components = ttk.Label(
            container,
            text=f"Components:\n{property_components}"
        )
        ability_components.grid(row=2, column=0, sticky="EW")

        ability_requirements = ttk.Label(
            container,
            text=f"Requirements:\n{property_requirements}"
        )
        ability_requirements.grid(row=3, column=0, sticky="EW")

        ability_conditions = ttk.Label(
            container,
            text=f"Conditions:\n{property_conditions}"
        )
        ability_conditions.grid(row=4, column=0, sticky="EW")

        ability_effects = ttk.Label(
            container,
            text=f"Effects:\n{property_effects}"
        )
        ability_effects.grid(row=5, column=0, sticky="EW")

        ability_description = ttk.Label(
            container,
            text=f"Description: {property_description}"
        )
        ability_description.grid(row=6, column=0, sticky="EW")

        def reconfigure_labels(event):
            ability_components.configure(wraplength=container.winfo_width() - 25)
            ability_requirements.configure(wraplength=container.winfo_width() - 25)
            ability_conditions.configure(wraplength=container.winfo_width() - 25)
            ability_effects.configure(wraplength=container.winfo_width() - 25)
            ability_description.configure(wraplength=container.winfo_width() - 25)

        container.bind("<Configure>", reconfigure_labels)

    def create_user_interface_buttons(self, container):
        edit_button = ttk.Button(
            container,
            text="Edit",
            command=self.edit_event,
            cursor="hand2"
        )
        edit_button.grid(row=0, column=0, sticky="EW")

        back_button = ttk.Button(
            container,
            text="← Back",
            command=self.container.show_home,
            cursor="hand2"
        )
        back_button.grid(row=1, column=0, sticky="EW")

    def generate_weapons(self, weapons):
        weapon_string = ""

        if len(weapons) == 0:
            return "None"

        for weapon in weapons:
            if weapon not in get_weapons_properties():
                weapon_properties = get_json_entity(weapon, 'weapons_folder')
                weapon_string += f"\n{weapon.replace('_', ' ').capitalize()}\n" \
                                 f"Reduction: {weapon_properties['red']}\n" \
                                 f"Damage: {weapon_properties['damage']}\n" \
                                 f"Range: {weapon_properties['range']}\n" \
                                 f"HP: {weapon_properties['life_points']}\n" \
                                 f"Area: {weapon_properties['area']}\n" \
                                 f"Abilities: {self.generate_abilities(weapon_properties['abilities'])}\n" \
                                 f"Effects: {weapon_properties['effects']}\n" \
                                 f"Description: {weapon_properties['description']}"
            else:
                weapon_string += f"{weapon.capitalize()}\n"

        return weapon_string

    def generate_armor(self, armor):
        armor_string = armor

        if armor not in get_armors_properties():
            armor_string = ""
            armor_properties = get_json_entity(armor, 'armors_folder')

            armor_string += f"\n{armor.replace('_', ' ')}\n" \
                            f"Reduction: {armor_properties['red']}\n" \
                            f"Damage: {armor_properties['damage']}\n" \
                            f"Range: {armor_properties['range']}\n" \
                            f"HP: {armor_properties['life_points']}\n" \
                            f"Area: {armor_properties['area']}\n" \
                            f"Abilities: {self.generate_abilities(armor_properties['abilities'])}\n" \
                            f"Effects: {armor_properties['effects']}\n" \
                            f"Description: {armor_properties['description']}"

        return armor_string

    def generate_abilities(self, abilities):
        ability_string = ""

        if len(abilities) == 0 or len(abilities) == 1 and abilities[0] == "None":
            return "None"

        for ability in abilities:
            ability_effects = get_json_entity(ability, 'abilities_folder')
            ability_string += ability.replace("_", " ").capitalize() + ": " + ability_effects['effects'] + "\n\n"

        return ability_string

    def generate_titles(self, titles):
        title_string = ""

        if len(titles) == 0 or len(titles) == 1 and titles[0] == "None":
            return "None"

        for title in titles:
            title_description = get_json_entity(title, 'titles_folder')
            title_string += title + ": " + title_description['description'] + "\n\n"

        return title_string

    def edit_event(self):
        self.container.parent.show_edit_interface(self.container.database_type_value)
