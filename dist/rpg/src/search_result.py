import tkinter as tk
from tkinter import ttk
from src.file_methods import get_json_entity
import json


class SearchResult(ttk.Frame):
    def __init__(self, parent, result, database_type_value, show_home):
        super().__init__(parent, style="FramesBackgroundColor.TFrame")

        self.parent = parent
        self.result = result
        self.database_type_value = database_type_value
        self.show_home = show_home

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.search_result_scroll = SearchResultScroll(self)
        self.search_result_scroll.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

        self.search_result_scroll.create_search_result_container()


class SearchResultScroll(tk.Canvas):
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

    def create_search_result_container(self):
        result_container = ttk.Frame(self.screen)
        result_container.grid(row=0, column=0, sticky="EW")
        result_container.columnconfigure(0, weight=1)

        self.create_result_widgets(result_container)

    def create_result_widgets(self, container):
        items = self.container.result

        for item in items:
            item_button = ttk.Button(
                container,
                text=item.replace("_", " "),
                command=lambda cur_item=item: self.choose_result(cur_item),
                cursor="hand2"
            )
            item_button.grid(column=0, padx=5, pady=5, sticky="EW")

        back_button = ttk.Button(
            container,
            text="← Back",
            command=self.local_show_home,
            cursor="hand2"
        )
        back_button.grid(column=0, padx=5, pady=5, sticky="EW")

    def choose_result(self, file_name):
        self.container.result.clear()
        self.container.parent.entity = get_json_entity(file_name, self.container.database_type_value)
        self.container.parent.show_user_interface(self.container.database_type_value)

    def local_show_home(self):
        self.container.result.clear()
        self.container.show_home()
