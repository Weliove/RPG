import tkinter as tk
from tkinter import ttk

from src import popup_showinfo
from src.ability.ability import Ability


class CreateAbility(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        # --- Variables ---
        self.ability_name = tk.StringVar()
        self.ability_cast_time = tk.StringVar()
        self.ability_components = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_ability_scroll = CreateAbilityScroll(self)
        self.create_ability_scroll.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.create_ability_scroll.create_ability_container()


class CreateAbilityScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.requirements_entry = tk.Text()
        self.conditions_entry = tk.Text()
        self.effects_entry = tk.Text()
        self.description_entry = tk.Text()

        self.screen = tk.Frame(container)
        self.screen.columnconfigure(0, weight=1)

        self.scrollable_window = self.create_window((0, 0), window=self.screen, anchor="nw")

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.screen.bind("<Configure>", configure_scroll_region)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

    def create_ability_container(self):
        ability_container = ttk.Frame(self.screen)
        ability_container.grid(row=0, column=0, sticky="EW")
        ability_container.columnconfigure(0, weight=1)

        self.create_ability_widgets(ability_container)

        for item_child in ability_container.winfo_children():
            item_child.grid_configure(padx=5, pady=5)

        buttons_container = ttk.Frame(self.screen)
        buttons_container.grid(row=1, column=0, sticky="EW")
        buttons_container.columnconfigure(0, weight=1)

        self.create_ability_buttons(buttons_container)

        for button_child in buttons_container.winfo_children():
            button_child.grid_configure(padx=5, pady=5)

    def create_ability_widgets(self, container):
        # --- Name ---

        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="W")

        name_entry = ttk.Entry(
            container,
            textvariable=self.container.ability_name,
            width=50
        )
        name_entry.grid(row=0, column=1, sticky="EW")
        name_entry.focus()

        # --- Cast Time ---

        cast_time_label = ttk.Label(
            container,
            text="Casting"
        )
        cast_time_label.grid(row=1, column=0, sticky="W")

        cast_time_entry = ttk.Entry(
            container,
            textvariable=self.container.ability_cast_time,
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
            textvariable=self.container.ability_components,
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

    def create_ability_buttons(self, container):
        create_button = ttk.Button(
            container,
            text="Create",
            command=self.create_ability,
            cursor="hand2"
        )
        create_button.grid(row=0, column=0, sticky="EW")

        back_button = ttk.Button(
            container,
            text="← Back",
            command=self.container.show_home,
            cursor="hand2"
        )
        back_button.grid(row=1, column=0, sticky="EW")

    def create_ability(self):
        name = self.container.ability_name.get()
        cast_time = self.container.ability_cast_time.get()
        components = self.container.ability_components.get()
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
        create_ability = ability.create_ability(temp_name, file_name)

        if create_ability:
            self.container.show_home()

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
