import tkinter as tk
from tkinter import ttk
from tkinter import font

from src import popup_showinfo
from src.ability.ability import Ability


class EditAbility(ttk.Frame):
    def __init__(self, parent, ability, show_home):
        super().__init__(parent)

        self.parent = parent
        self.ability = ability
        self.show_home = show_home
        self.font = font.Font(size=11)

        # --- Properties ---
        property_name = ability['name']
        property_cast_time = ability['cast_time']
        property_components = ability['components']

        # --- Variables ---
        self.ability_name = tk.StringVar(value=property_name)
        self.ability_cast_time = tk.StringVar(value=property_cast_time)
        self.ability_components = tk.StringVar(value=property_components)

        # --- Widgets ---
        self.requirements_entry = tk.Text()
        self.conditions_entry = tk.Text()
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        ability_container = ttk.Frame(self)
        ability_container.grid(row=0, column=0, sticky="NSEW")
        ability_container.columnconfigure(0, weight=1)

        self.create_edit_ability_interface(ability_container, ability)

    def create_edit_ability_interface(self, container, ability):
        # --- Properties ---
        property_requirements = ability['requirements']
        property_conditions = ability['conditions']
        property_effects = ability['effects']
        property_description = ability['description']

        # --- Name ---

        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="W")

        name_entry = ttk.Entry(
            container,
            textvariable=self.ability_name,
            width=50
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # --- Cast Time ---

        cast_time_label = ttk.Label(
            container,
            text="Casting"
        )
        cast_time_label.grid(row=1, column=0, sticky="W")

        cast_time_entry = ttk.Entry(
            container,
            textvariable=self.ability_cast_time,
            width=50
        )
        cast_time_entry.grid(row=1, column=1, sticky="EW")

        # --- Components ---

        components_label = ttk.Label(
            container,
            text="Component"
        )
        components_label.grid(row=2, column=0, sticky="W")

        components_entry = ttk.Entry(
            container,
            textvariable=self.ability_components,
            width=50
        )
        components_entry.grid(row=2, column=1, sticky="EW")

        # --- Requirements ---

        requirements_label = ttk.Label(
            container,
            text="Req"
        )
        requirements_label.grid(row=3, column=0, sticky="W")

        self.requirements_entry = tk.Text(
            container,
            width=1,
            height=3
        )
        self.requirements_entry.grid(row=3, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=3, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, property_requirements)

        # --- Conditions ---

        conditions_label = ttk.Label(
            container,
            text="Conditions"
        )
        conditions_label.grid(row=4, column=0, sticky="W")

        self.conditions_entry = tk.Text(
            container,
            width=1,
            height=3
        )
        self.conditions_entry.grid(row=4, column=1, sticky="EW")

        conditions_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.conditions_entry.yview
        )
        conditions_scroll.grid(row=4, column=2, sticky="ns")

        self.conditions_entry["yscrollcommand"] = conditions_scroll.set

        self.conditions_entry.insert(tk.END, property_conditions)

        # --- Effects ---

        effects_label = ttk.Label(
            container,
            text="Effects"
        )
        effects_label.grid(row=5, column=0, sticky="W")

        self.effects_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.effects_entry.grid(row=5, column=1, sticky="EW")

        effects_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.effects_entry.yview
        )
        effects_scroll.grid(row=5, column=2, sticky="ns")

        self.effects_entry["yscrollcommand"] = effects_scroll.set

        self.effects_entry.insert(tk.END, property_effects)

        # --- Description ---

        description_label = ttk.Label(
            container,
            text="Description"
        )
        description_label.grid(row=6, column=0, sticky="W")

        self.description_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.description_entry.grid(row=6, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=6, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, property_description)

    def save_entity(self):
        current_name = self.ability['name'].replace(" ", "_")
        name = self.ability_name.get()
        cast_time = self.ability_cast_time.get()
        components = self.ability_components.get()
        requirements = self.get_text_data(self.requirements_entry)
        conditions = self.get_text_data(self.conditions_entry)
        effects = self.get_text_data(self.effects_entry)
        description = self.get_text_data(self.description_entry)

        if name == '':
            popup_showinfo("Please, insert a name!")
            return

        if cast_time == '':
            cast_time = '0'

        if components == '':
            components = 'None'

        if requirements == '':
            requirements = 'None'

        if conditions == '':
            conditions = 'None'

        if effects == '':
            effects = 'None'

        if description == '':
            description = 'None'

        temp_name = name.lower().replace(" ", "_")
        file_name = temp_name + ".txt"

        ability = Ability(name, cast_time, components, requirements, conditions, effects, description)
        create_ability = ability.update_ability(temp_name, current_name, file_name)

        if create_ability:
            popup_showinfo("Success!")
            self.show_home()

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
