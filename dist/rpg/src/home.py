from tkinter import ttk

from src.popup_window import *
from src.file_methods import check_entity_existence


class Home(ttk.Frame):
    def __init__(self, parent, show_create_avatar, show_create_item, show_create_ability, show_create_title):
        super().__init__(parent, style="FramesBackgroundColor.TFrame")

        type_values = sorted(["Avatar", "Weapon", "Armor", "Title", "Ability"])

        self.database_type_values = {
            'Avatar': 'avatars_file',
            'Weapon': 'weapons_file',
            'Armor': 'armors_file',
            'Title': 'titles_file',
            'Ability': 'abilities_file'
        }

        self.folder_type_values = {
            'Avatar': 'avatars_folder',
            'Weapon': 'weapons_folder',
            'Armor': 'armors_folder',
            'Title': 'titles_folder',
            'Ability': 'abilities_folder'
        }

        self.type_values = tuple(type_values)
        self.type_choice = tk.StringVar()
        self.type_choice.set(self.type_values[0])

        self.parent = parent
        self.show_create_avatar = show_create_avatar
        self.show_create_item = show_create_item
        self.show_create_ability = show_create_ability
        self.show_create_title = show_create_title

        # Items/Avatars
        self.search_result = []

        self.columnconfigure(0, weight=1)

        self.avatar = {}
        self.entity_name = tk.StringVar()

        # --- 1st Frame ---

        home_frame = ttk.Frame(self, style="FramesBackgroundColor.TFrame")
        home_frame.grid(row=0, column=0, padx=10, pady=10, sticky="EW")
        home_frame.columnconfigure(0, weight=1)
        home_frame.rowconfigure(1, weight=1)

        # --- Avatar Widgets ---

        self.create_avatar_widgets(home_frame)

        # --- 2nd Frame ---

        button_container = ttk.Frame(self, style="FramesBackgroundColor.TFrame")
        button_container.grid(row=1, column=0, padx=10, pady=10, sticky="EW")
        button_container.columnconfigure(0, weight=1)

        # --- Button Widgets ---

        self.create_button_widgets(button_container)

    def create_avatar_widgets(self, container):
        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

        name_entry = ttk.Entry(
            container,
            textvariable=self.entity_name,
            width=50
        )
        name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="EW")
        name_entry.focus()

        name_entry.bind("<Return>", self.search_entity)
        name_entry.bind("<KP_Enter>", self.search_entity)

        type_search_label = ttk.Label(
            container,
            text="Type"
        )
        type_search_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

        type_search_entry = ttk.Combobox(
            container,
            textvariable=self.type_choice,
            values=self.type_values,
            state="readonly"
        )
        type_search_entry.grid(row=1, column=1, padx=5, pady=5, sticky="EW")

    def create_button_widgets(self, container):
        submit_button = ttk.Button(
            container,
            text="Search",
            command=self.search_entity,
            cursor="hand2"
        )
        submit_button.grid(row=0, column=0, sticky="EW")

        create_avatar_button = ttk.Button(
            container,
            text="Create Avatar",
            command=self.show_create_avatar,
            cursor="hand2"
        )
        create_avatar_button.grid(row=1, column=0, sticky="EW")

        create_item_button = ttk.Button(
            container,
            text="Create Item",
            command=self.show_create_item,
            cursor="hand2"
        )
        create_item_button.grid(row=2, column=0, sticky="EW")

        create_ability_button = ttk.Button(
            container,
            text="Create Ability",
            command=self.show_create_ability,
            cursor="hand2"
        )
        create_ability_button.grid(row=3, column=0, sticky="EW")

        create_title_button = ttk.Button(
            container,
            text="Create Title",
            command=self.show_create_title,
            cursor="hand2"
        )
        create_title_button.grid(row=4, column=0, sticky="EW")

        # Add pad for all children of container
        for child in container.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def search_entity(self, *args):
        entity_name = self.entity_name.get().lower().replace(" ", "_")
        type_choice = self.type_choice.get()
        database_type_values = self.database_type_values
        folder_type_values = self.folder_type_values
        check_existence = False

        # Checks if the avatar is stored in database file
        self.search_result = check_entity_existence(entity_name, database_type_values[type_choice])

        if self.search_result:
            check_existence = True

        # If the avatar is stored in database avatars.txt gets all properties from the main file
        if check_existence:
            self.parent.show_search_result(self.search_result, folder_type_values[type_choice])
            self.entity_name.set("")
        else:
            popup_showinfo(f"{entity_name} not found!")
