import tkinter as tk
from tkinter import ttk
from tkinter import font

from src import popup_showinfo
from src.avatar.avatar import Avatar
from src.avatar.avatar_properties import AvatarProperties
from src.file_methods import get_all_file_names


class EditAvatar(ttk.Frame):
    def __init__(self, parent, avatar, show_home):
        super().__init__(parent)

        # --- Avatar Properties ---

        self.parent = parent
        self.avatar = avatar
        self.show_home = show_home
        self.font = font.Font(size=11)

        avatar_properties = AvatarProperties()

        property_name = avatar['name']
        property_life_points = avatar['life_points']
        property_adrenaline = avatar['adrenaline']
        property_class = avatar['class']
        property_armor = avatar['armor']
        property_physical_ab = avatar['physical_ab']

        # --- Get Properties ---

        self.MAX_HP = avatar_properties.MAX_HP
        self.MAX_AD = avatar_properties.MAX_AD

        self.classes_values = avatar_properties.classes_values
        self.type_values = avatar_properties.type_values

        self.weapons_values = avatar_properties.weapons_values
        self.armors_values = avatar_properties.armors_values
        self.titles_values = avatar_properties.titles_values

        # --- Variables ---

        self.avatar_special_weapons = get_all_file_names('weapons_file')
        self.avatar_special_armors = get_all_file_names('armors_file')

        class_index = self.classes_values.index(property_class)
        armor_index = self.get_item_index(property_armor, self.armors_values)
        special_armor_index = self.get_item_index(property_armor, self.avatar_special_armors)

        self.avatar_name = tk.StringVar(value=property_name)

        self.avatar_hp = tk.StringVar(value=property_life_points)

        self.avatar_ad = tk.StringVar(value=property_adrenaline)

        self.avatar_class = tk.StringVar(value=self.classes_values[class_index])

        self.avatar_weapon = tk.StringVar(value=self.weapons_values[0])
        self.avatar_weapons = tk.StringVar(value=self.weapons_values)
        self.avatar_armor = tk.StringVar(value=self.armors_values[armor_index])

        # --- Special ---
        self.avatar_weapons_special = tk.StringVar(value=self.avatar_special_weapons)
        self.avatar_armor_special = tk.StringVar(value=self.avatar_special_armors[special_armor_index])

        self.avatar_physical_ab = tk.StringVar(value=property_physical_ab)

        self.avatar_titles = tk.StringVar(value=self.titles_values)

        self.abilities = get_all_file_names('abilities_file')
        self.avatar_abilities = tk.StringVar(value=self.abilities)

        # --------------

        self.weapon_entry = tk.Listbox()
        self.weapon_special_entry = tk.Listbox()
        self.title_entry = tk.Listbox()
        self.ability_entry = tk.Listbox()
        self.description_entry = tk.Text()

        avatar_container = ttk.Frame(self)
        avatar_container.grid(row=0, column=0, sticky="NSEW")
        avatar_container.columnconfigure(0, weight=1)

        self.create_edit_avatar_interface(avatar_container, avatar)

    def get_item_index(self, property_item, item_list):
        armor_index = 0

        if property_item in item_list:
            armor_index = item_list.index(property_item)

        return armor_index

    def create_edit_avatar_interface(self, container, avatar):
        property_weapon = avatar['weapon']
        property_title = avatar['title']
        property_abilities = avatar['abilities']
        property_description = avatar['description']

        # --- Name ---

        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="W")

        name_entry = ttk.Entry(
            container,
            textvariable=self.avatar_name,
            width=50
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # --- HP ---

        hp_label = ttk.Label(
            container,
            text="HP"
        )
        hp_label.grid(row=1, column=0, sticky="W")

        hp_entry = ttk.Spinbox(
            container,
            from_=1,
            to=self.MAX_HP,
            increment=1,
            justify="center",
            textvariable=self.avatar_hp,
            width=10
        )
        hp_entry.grid(row=1, column=1, sticky="EW")

        # --- Adrenaline ---

        adrenaline_label = ttk.Label(
            container,
            text="Adrenaline"
        )
        adrenaline_label.grid(row=2, column=0, sticky="W")

        adrenaline_entry = ttk.Spinbox(
            container,
            from_=1,
            to=self.MAX_AD,
            increment=1,
            justify="center",
            textvariable=self.avatar_ad,
            width=10
        )
        adrenaline_entry.grid(row=2, column=1, sticky="EW")

        # --- Class ---

        class_label = ttk.Label(
            container,
            text="Class"
        )
        class_label.grid(row=3, column=0, sticky="W")

        class_entry = ttk.Combobox(
            container,
            textvariable=self.avatar_class,
            values=self.classes_values,
            state="readonly"
        )
        class_entry.grid(row=3, column=1, sticky="EW")

        # --- Weapon ---

        weapon_label = ttk.Label(
            container,
            text="Weapons"
        )
        weapon_label.grid(row=4, column=0, sticky="W")

        self.weapon_entry = tk.Listbox(
            container,
            listvariable=self.avatar_weapons,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.weapon_entry.grid(row=4, column=1, sticky="EW")

        weapon_scrollbar = ttk.Scrollbar(container, orient="vertical")
        weapon_scrollbar.config(command=self.weapon_entry.yview)
        weapon_scrollbar.grid(row=4, column=2, sticky="NS")

        self.weapon_entry.config(yscrollcommand=weapon_scrollbar.set)

        if len(property_weapon) > 0:
            self.set_stored_items(self.weapon_entry, [property_weapon[0]], self.weapons_values)
        else:
            self.weapon_entry.select_set(0)

        # --- Special Weapons ---

        weapon_special_label = ttk.Label(
            container,
            text="S. Weapons"
        )
        weapon_special_label.grid(row=5, column=0, sticky="W")

        self.weapon_special_entry = tk.Listbox(
            container,
            listvariable=self.avatar_weapons_special,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.weapon_special_entry.grid(row=5, column=1, sticky="EW")

        weapon_special_scrollbar = ttk.Scrollbar(container, orient="vertical")
        weapon_special_scrollbar.config(command=self.weapon_special_entry.yview)
        weapon_special_scrollbar.grid(row=5, column=2, sticky="NS")

        self.weapon_special_entry.config(yscrollcommand=weapon_special_scrollbar.set)

        if len(property_weapon) > 0:
            self.set_stored_items(self.weapon_special_entry, property_weapon[1:], self.avatar_special_weapons)
        else:
            self.weapon_special_entry.select_set(0)

        # --- Armor ---

        armor_label = ttk.Label(
            container,
            text="Armor"
        )
        armor_label.grid(row=6, column=0, sticky="W")

        armor_entry = ttk.Combobox(
            container,
            textvariable=self.avatar_armor,
            values=self.armors_values,
            state="readonly"
        )
        armor_entry.grid(row=6, column=1, sticky="EW")

        # --- Special Armor ---

        armor_special_label = ttk.Label(
            container,
            text="S. Armor"
        )
        armor_special_label.grid(row=7, column=0, sticky="W")

        armor_special_entry = ttk.Combobox(
            container,
            textvariable=self.avatar_armor_special,
            values=self.avatar_special_armors,
            state="readonly"
        )
        armor_special_entry.grid(row=7, column=1, sticky="EW")

        # --- Physical Ab ---

        physical_ab_label = ttk.Label(
            container,
            text="Physical Ab."
        )
        physical_ab_label.grid(row=8, column=0, sticky="W")

        physical_ab_entry = ttk.Entry(
            container,
            textvariable=self.avatar_physical_ab,
            width=50
        )
        physical_ab_entry.grid(row=8, column=1, sticky="EW")

        # --- Title ---

        title_label = ttk.Label(
            container,
            text="Titles"
        )
        title_label.grid(row=9, column=0, sticky="W")

        self.title_entry = tk.Listbox(
            container,
            listvariable=self.avatar_titles,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.title_entry.grid(row=9, column=1, sticky="EW")

        title_scrollbar = ttk.Scrollbar(container, orient="vertical")
        title_scrollbar.config(command=self.title_entry.yview)
        title_scrollbar.grid(row=9, column=2, sticky="NS")

        self.title_entry.config(yscrollcommand=title_scrollbar.set)

        self.set_stored_items(self.title_entry, property_title, self.titles_values)

        # --- Ability ---

        ability_label = ttk.Label(
            container,
            text="Abilities"
        )
        ability_label.grid(row=10, column=0, sticky="W")

        self.ability_entry = tk.Listbox(
            container,
            listvariable=self.avatar_abilities,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.ability_entry.grid(row=10, column=1, sticky="EW")

        ability_scrollbar = ttk.Scrollbar(container, orient="vertical")
        ability_scrollbar.config(command=self.ability_entry.yview)
        ability_scrollbar.grid(row=10, column=2, sticky="NS")

        self.ability_entry.config(yscrollcommand=ability_scrollbar.set)

        self.set_stored_items(self.ability_entry, property_abilities, self.abilities)

        # --- Description ---

        description_label = ttk.Label(
            container,
            text="Description"
        )
        description_label.grid(row=11, column=0, sticky="EW")

        self.description_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.description_entry.grid(row=11, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=11, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, property_description)

    def set_stored_items(self, list_widget, stored_items, total_list):
        for item in stored_items:
            if item in stored_items:
                item_index = total_list.index(item)
                list_widget.select_set(item_index)

    def save_entity(self):
        current_name = self.avatar['name'].replace(" ", "_")
        name = self.avatar_name.get()
        hp = self.avatar_hp.get()
        ad = self.avatar_ad.get()
        _class = self.avatar_class.get()
        weapon = self.handle_selection_change(self.weapon_entry, self.weapons_values)
        special_weapon = self.handle_selection_change(self.weapon_special_entry, self.avatar_special_weapons)
        armor = self.avatar_armor.get()
        special_armor = self.avatar_armor_special.get()
        physical_ab = self.avatar_physical_ab.get()
        title = self.handle_selection_change(self.title_entry, self.titles_values)
        ability = self.handle_selection_change(self.ability_entry, self.abilities)
        description = self.get_text_data(self.description_entry)

        weapon_result = weapon + special_weapon
        armor_result = special_armor

        if special_armor == "None":
            armor_result = armor

        if name == '':
            popup_showinfo("Please, type a name.")
            return

        if hp == '' or hp == '0' or int(hp) < 0:
            hp = '1'

        if ad == '' or ad == '0' or int(ad) < 0:
            ad = '1'

        if physical_ab == '':
            physical_ab = 'None'

        if len(title) == 0:
            title = ['None']

        if len(ability) == 0:
            ability = ['None']

        if len(description) == 0:
            description = 'None'

        temp_name = name.lower().replace(" ", "_")
        file_name = temp_name + ".txt"

        avatar = Avatar(name, hp, ad, _class, weapon_result, armor_result, physical_ab, title, ability, description)
        update_avatar = avatar.update_avatar(temp_name, current_name, file_name)

        if update_avatar:
            self.show_home()

    def handle_selection_change(self, list_widget, total_list):
        selected_indices = list_widget.curselection()
        result_list = []

        for i in selected_indices:
            result_list.append(total_list[i])

        return tuple(result_list)

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
