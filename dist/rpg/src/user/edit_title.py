import tkinter as tk
from tkinter import ttk
from tkinter import font

from src import popup_showinfo
from src.title.title import Title


class EditTitle(ttk.Frame):
    def __init__(self, parent, title, show_home):
        super().__init__(parent)

        self.parent = parent
        self.title = title
        self.show_home = show_home
        self.font = font.Font(size=11)

        # --- Properties ---
        property_name = title['name']

        # --- Attributes ---
        self.title_name = tk.StringVar(value=property_name)

        # --- Widgets ---
        self.requirements_entry = tk.Text()
        self.description_entry = tk.Text()

        ability_container = ttk.Frame(self)
        ability_container.grid(row=0, column=0, sticky="NSEW")
        ability_container.columnconfigure(0, weight=1)

        self.create_edit_title_interface(ability_container, title)

    def create_edit_title_interface(self, container, title):
        # --- Properties ---
        property_requirements = title['requirements']
        property_description = title['description']

        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="W")

        name_entry = ttk.Entry(
            container,
            textvariable=self.title_name,
            width=50
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # --- Requirements ---

        requirements_label = ttk.Label(
            container,
            text="Requirements"
        )
        requirements_label.grid(row=1, column=0, sticky="W")

        self.requirements_entry = tk.Text(
            container,
            width=1,
            height=5
        )
        self.requirements_entry.grid(row=1, column=1, sticky="EW")

        requirements_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.requirements_entry.yview
        )
        requirements_scroll.grid(row=1, column=2, sticky="ns")

        self.requirements_entry["yscrollcommand"] = requirements_scroll.set

        self.requirements_entry.insert(tk.END, property_requirements)

        # --- Description ---

        description_label = ttk.Label(
            container,
            text="Description"
        )
        description_label.grid(row=2, column=0, sticky="W")

        self.description_entry = tk.Text(
            container,
            width=1,
            height=10
        )
        self.description_entry.grid(row=2, column=1, sticky="EW")

        description_scroll = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.description_entry.yview
        )
        description_scroll.grid(row=2, column=2, sticky="ns")

        self.description_entry["yscrollcommand"] = description_scroll.set

        self.description_entry.insert(tk.END, property_description)

    def save_entity(self):
        name = self.title_name.get()
        requirements = self.get_text_data(self.requirements_entry)
        description = self.get_text_data(self.requirements_entry)

        if name == '':
            popup_showinfo("Please, insert a name!")
            return

        if requirements == '':
            requirements = "None"

        if description == '':
            description = "None"

        temp_name = name.lower().replace(" ", "_")
        file_name = temp_name + ".txt"

        title = Title(name, requirements, description)
        create_title = title.create_title(temp_name, file_name)

        if create_title:
            self.show_home()

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
