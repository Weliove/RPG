import re
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from src import Home
from src import CreateItem
from src import CreateAvatar
from src import UserInterface
from src.ability.create_ability import CreateAbility
from src.search_result import SearchResult
from src.title.create_title import CreateTitle
from src.user.edit_interface import EditInterface


class Rpg(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("RPG - Home")
        self.resizable(False, False)
        self.iconbitmap("src\\icon\\dbz.ico")

        self.frames = dict()
        self.entity = None

        self.home_frame = Home(
            self,
            # lambda: self.show_frame(CreateAvatar),
            lambda: self.show_create_avatar(),
            # lambda: self.show_frame(CreateItem),
            lambda: self.show_create_item(),
            lambda: self.show_frame(CreateAbility),
            lambda: self.show_frame(CreateTitle)
        )
        self.home_frame.grid(row=0, column=0, sticky="NSEW")

        self.create_avatar_frame = None

        self.create_item_frame = None

        self.create_title_frame = CreateTitle(self, lambda: self.show_frame(Home))
        self.create_title_frame.grid(row=0, column=0, sticky="NSEW")

        self.create_ability_frame = CreateAbility(self, lambda: self.show_frame(Home))
        self.create_ability_frame.grid(row=0, column=0, sticky="NSEW")

        self.search_result_frame = None

        self.user_interface_frame = None

        self.edit_interface_frame = None

        self.frames[Home] = self.home_frame
        # self.frames[CreateAvatar] = self.create_avatar_frame
        # self.frames[CreateItem] = self.create_item_frame
        self.frames[CreateAbility] = self.create_ability_frame
        self.frames[CreateTitle] = self.create_title_frame

        self.show_frame(Home)

    def show_frame(self, container):
        local_title = " "
        local_title_array = re.findall('[A-Z][^A-Z]*', str(container.__name__))
        self.title(f"RPG - {local_title.join(local_title_array)}")
        frame = self.frames[container]
        frame.tkraise()

    def show_create_avatar(self):
        self.check_frame_existence(self.create_avatar_frame)

        self.create_avatar_frame = CreateAvatar(self, lambda: self.show_frame(Home))
        self.create_avatar_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[CreateAvatar] = self.create_avatar_frame
        self.show_frame(CreateAvatar)

    def show_create_item(self):
        self.check_frame_existence(self.create_item_frame)

        self.create_item_frame = CreateItem(self, lambda: self.show_frame(Home))
        self.create_item_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[CreateItem] = self.create_item_frame
        self.show_frame(CreateItem)

    def show_search_result(self, search_result, database_type_value):
        self.check_frame_existence(self.search_result_frame)

        self.search_result_frame = SearchResult(
            self,
            search_result,
            database_type_value,
            lambda: self.show_frame(Home)
        )
        self.search_result_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[SearchResult] = self.search_result_frame
        self.show_frame(SearchResult)

    def show_user_interface(self, database_type_value):
        self.check_frame_existence(self.user_interface_frame)

        self.user_interface_frame = UserInterface(self, database_type_value, lambda: self.show_frame(Home))
        self.user_interface_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[UserInterface] = self.user_interface_frame
        self.show_frame(UserInterface)

    def show_edit_interface(self, database_type_value):
        self.check_frame_existence(self.edit_interface_frame)

        self.edit_interface_frame = EditInterface(self, database_type_value, lambda: self.show_frame(Home))
        self.edit_interface_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[EditInterface] = self.edit_interface_frame
        self.show_frame(EditInterface)

    def check_frame_existence(self, frame):
        if frame is not None and frame.winfo_exists():
            frame.destroy()


root = Rpg()

# Default window background color
root['background'] = "#DCDAD5"

style = ttk.Style(root)
style.theme_use("clam")

# Frame background color
style.configure("FramesBackgroundColor.TFrame", background="#DCDAD5")

# Button background color
style.configure("ButtonBackgroundColor.TButton", borderwidth=0, background="#DCDAD5", foreground="#FFFFFF")
style.map(
    "ButtonBackgroundColor.TButton",
    background=[("pressed", "#141314"), ("active", "#2b2a2b")]
)

font.nametofont("TkDefaultFont").configure(size=12)

root.mainloop()
