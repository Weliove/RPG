import tkinter as tk
from tkinter import ttk, font

from src.popup_window import *
from src.user.edit_ability import EditAbility
from src.user.edit_avatar import EditAvatar
from src.user.edit_item import EditItem
from src.user.edit_title import EditTitle


class EditInterface(ttk.Frame):
    def __init__(self, parent, database_type_value, show_home):
        super().__init__(parent, style="FramesBackgroundColor.TFrame")

        self.parent = parent
        self.show_home = show_home
        self.database_type_value = database_type_value
        entity = parent.entity
        self.entity = entity

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.edit_interface_scroll = EditInterfaceScroll(self)
        self.edit_interface_scroll.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

        self.edit_interface_scroll.create_edit_interface_container(entity)


class EditInterfaceScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.font = font.Font(size=11)

        self.edit_interface = None

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

    def create_edit_interface_container(self, entity):
        container = self.container
        database_type_value = container.database_type_value

        # --- Entity Widgets ---

        if database_type_value == 'avatars_folder':
            self.edit_interface = EditAvatar(self.screen, entity, self.container.show_home)
        elif database_type_value == 'weapons_folder' or database_type_value == 'armors_folder':
            self.edit_interface = EditItem(self.screen, entity, self.container.show_home)
        elif database_type_value == 'abilities_folder':
            self.edit_interface = EditAbility(self.screen, entity, self.container.show_home)
        elif database_type_value == 'titles_folder':
            self.edit_interface = EditTitle(self.screen, entity, self.container.show_home)
        else:
            popup_showinfo("Error, database type value not found!")
            return

        self.edit_interface.grid(row=0, column=0, sticky="NSEW")
        self.edit_interface.columnconfigure(0, weight=1)

        # Adds the same pads to all children of the container
        for child in self.edit_interface.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # --- Button Container ---

        edit_interface_button_container = ttk.Frame(self.screen)
        edit_interface_button_container.grid(row=1, column=0, sticky="EW")
        edit_interface_button_container.rowconfigure(0, weight=1)
        edit_interface_button_container.columnconfigure(0, weight=1)

        # --- Button Widgets ---

        self.create_edit_interface_buttons(edit_interface_button_container)

        # Adds the same pads to all children of the container
        for child in edit_interface_button_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_edit_interface_buttons(self, container):
        edit_button = ttk.Button(
            container,
            text="Save",
            command=self.save_edition,
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

    def save_edition(self):
        self.edit_interface.save_entity()
