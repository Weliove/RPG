import tkinter as tk
from tkinter import ttk
from tkinter import font

from src import popup_showinfo
from src.file_methods import get_all_file_names
from src.item.item import Item
from src.item.item_properties import get_item_types


class EditItem(ttk.Frame):
    def __init__(self, parent, item, show_home):
        super().__init__(parent)

        self.parent = parent
        self.item = item
        self.show_home = show_home
        self.font = font.Font(size=11)

        # --- Item Properties ---

        property_name = item['name']
        property_type = item['type']
        property_damage = item['damage']
        property_life_points = item['life_points']
        property_red = item['red']
        property_range = item['range']
        property_area = item['area']

        # --- Item Variables ---

        self.item_types = get_item_types()
        self.abilities = get_all_file_names('abilities_file')
        self.item_abilities = tk.StringVar(value=self.abilities)

        self.item_name = tk.StringVar(value=property_name)

        item_type_index = self.get_item_index(property_type, self.item_types)
        self.item_type = tk.StringVar(value=self.item_types[item_type_index])

        self.item_damage = tk.StringVar(value=property_damage)

        self.item_life_points = tk.StringVar(value=property_life_points)

        self.item_reduction = tk.StringVar(value=property_red)

        self.item_range = tk.StringVar(value=property_range)

        self.item_area = tk.StringVar(value=property_area)

        self.item_effects = tk.StringVar()

        # -----------------------

        self.abilities_entry = tk.Listbox()
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        item_container = ttk.Frame(self)
        item_container.grid(row=0, column=0, sticky="NSEW")
        item_container.columnconfigure(0, weight=1)

        self.create_edit_item_interface(item_container, item)

    def get_item_index(self, property_item, item_list):
        armor_index = 0

        if property_item in item_list:
            armor_index = item_list.index(property_item)

        return armor_index

    def create_edit_item_interface(self, container, item):
        property_abilities = item['abilities']
        property_effects = item['effects']
        property_description = item['description']

        # --- Name ---

        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="W")

        name_entry = ttk.Entry(
            container,
            textvariable=self.item_name,
            width=50
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # --- Type ---

        type_label = ttk.Label(
            container,
            text="Type"
        )
        type_label.grid(row=1, column=0, sticky="W")

        type_entry = ttk.Combobox(
            container,
            textvariable=self.item_type,
            values=self.item_types,
            state="readonly"
        )
        type_entry.grid(row=1, column=1, sticky="EW")

        # --- Reduction ---

        reduction_label = ttk.Label(
            container,
            text="Reduction"
        )
        reduction_label.grid(row=2, column=0, sticky="W")

        reduction_entry = ttk.Entry(
            container,
            textvariable=self.item_reduction,
            width=50
        )
        reduction_entry.grid(row=2, column=1, sticky="EW")

        # --- Damage ---

        damage_label = ttk.Label(
            container,
            text="Damage"
        )
        damage_label.grid(row=3, column=0, sticky="W")

        damage_entry = ttk.Entry(
            container,
            textvariable=self.item_damage,
            width=50
        )
        damage_entry.grid(row=3, column=1, sticky="EW")

        # --- Range ---

        range_label = ttk.Label(
            container,
            text="Range"
        )
        range_label.grid(row=4, column=0, sticky="W")

        range_entry = ttk.Entry(
            container,
            textvariable=self.item_range,
            width=50
        )
        range_entry.grid(row=4, column=1, sticky="EW")

        # --- HP ---

        life_points_label = ttk.Label(
            container,
            text="HP"
        )
        life_points_label.grid(row=5, column=0, sticky="W")

        life_points_entry = ttk.Spinbox(
            container,
            from_=0,
            increment=1,
            justify="center",
            textvariable=self.item_life_points,
            width=10
        )
        life_points_entry.grid(row=5, column=1, sticky="EW")

        # --- Area ---

        area_label = ttk.Label(
            container,
            text="Area"
        )
        area_label.grid(row=6, column=0, sticky="W")

        area_entry = ttk.Combobox(
            container,
            textvariable=self.item_area,
            values=('No', 'Yes'),
            state="readonly"
        )
        area_entry.grid(row=6, column=1, sticky="EW")

        # --- Abilities ---

        abilities_label = ttk.Label(
            container,
            text="Abilities"
        )
        abilities_label.grid(row=7, column=0, sticky="W")

        self.abilities_entry = tk.Listbox(
            container,
            listvariable=self.item_abilities,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            height=5
        )
        self.abilities_entry.grid(row=7, column=1, sticky="EW")

        abilities_scrollbar = ttk.Scrollbar(container, orient="vertical")
        abilities_scrollbar.config(command=self.abilities_entry.yview)
        abilities_scrollbar.grid(row=7, column=2, sticky="NS")

        self.abilities_entry.config(yscrollcommand=abilities_scrollbar.set)

        self.set_stored_items(self.abilities_entry, property_abilities, self.abilities)

        # --- Effects ---
        effects_label = ttk.Label(
            container,
            text="Effects"
        )
        effects_label.grid(row=8, column=0, sticky="W")

        self.effects_entry = tk.Text(
            container,
            width=1,
            height=10
        )
        self.effects_entry.grid(row=8, column=1, sticky="EW")

        effects_entry_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_entry_scroll.grid(row=8, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_entry_scroll.set

        self.effects_entry.insert(tk.END, property_effects)

        # --- Description ---

        description_label = ttk.Label(
            container,
            text="Description"
        )
        description_label.grid(row=12, column=0, sticky="EW")

        self.description_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.description_entry.grid(row=12, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=12, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, property_description)

    def set_stored_items(self, list_widget, stored_items, total_list):
        for item in stored_items:
            if item in stored_items:
                item_index = total_list.index(item)
                list_widget.select_set(item_index)

    def save_entity(self):
        current_item_name = self.item['name'].replace(" ", "_")
        item_name = self.item_name.get()
        item_type = self.item_type.get()
        item_reduction = self.item_reduction.get()
        item_damage = self.item_damage.get()
        item_range = self.item_range.get()
        item_hp = self.item_life_points.get()
        item_area = self.item_area.get()
        item_abilities = self.handle_selection_change(self.abilities_entry, self.abilities)
        item_effects = self.get_text_data(self.effects_entry)
        item_description = self.get_text_data(self.description_entry)

        if item_name == '':
            popup_showinfo("Please, type a name.")

        if item_reduction == '':
            item_reduction = '0'

        if item_damage == '':
            item_damage = '0'

        if item_range == '':
            item_range = '0'

        if item_hp == '' or item_hp == '0' or int(item_hp) < 0:
            item_hp = '0'

        if item_effects == '':
            item_effects = 'None'

        temp_name = item_name.lower().replace(" ", "_")
        file_name = temp_name + ".txt"

        item = Item(
            item_name,
            item_type,
            item_reduction,
            item_damage,
            item_range,
            item_hp,
            item_area,
            item_abilities,
            item_effects,
            item_description
        )
        update_item = item.update_item(temp_name, current_item_name, file_name)

        if update_item:
            self.show_home()

    def handle_selection_change(self, list_widget, total_list):
        selected_indices = list_widget.curselection()
        result_list = []

        for i in selected_indices:
            result_list.append(total_list[i])

        return tuple(result_list)

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')

