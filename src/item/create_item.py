import tkinter as tk
from tkinter import ttk
from tkinter import font

from src import popup_showinfo
from src.file_methods import get_all_file_names
from src.item.item import Item
from src.item.item_properties import get_item_types


class CreateItem(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.parent = parent
        self.show_home = show_home

        # --- Items Variables ---
        self.item_types = get_item_types()
        self.abilities = get_all_file_names('abilities_file')
        self.item_abilities = tk.StringVar(value=self.abilities)

        self.item_name = tk.StringVar()

        self.item_type = tk.StringVar(value=self.item_types[0])

        self.item_damage = tk.StringVar(value='0')

        self.item_life_points = tk.StringVar(value='0')

        self.item_reduction = tk.StringVar(value='0')

        self.item_range = tk.StringVar(value='1')

        self.item_area = tk.StringVar(value='No')

        self.item_effects = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_item_scroll = CreateItemScroll(self)
        self.create_item_scroll.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

        self.create_item_scroll.create_item_container()


class CreateItemScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.font = font.Font(size=11)

        self.abilities_entry = tk.Listbox()
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

    def create_item_container(self):
        items_container = ttk.Frame(self.screen)
        items_container.grid(row=0, column=0, sticky="EW")
        items_container.columnconfigure(0, weight=1)

        self.create_item_widgets(items_container)

        buttons_container = ttk.Frame(self.screen)
        buttons_container.grid(row=1, column=0, sticky="EW")
        buttons_container.columnconfigure(0, weight=1)

        self.create_button_widgets(buttons_container)

        for item_child in items_container.winfo_children():
            item_child.grid_configure(pady=5)

        for button_child in buttons_container.winfo_children():
            button_child.grid_configure(padx=5, pady=5)

    def create_item_widgets(self, container):
        local_pad = (5, 1)

        # --- Name ---

        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, padx=local_pad, sticky="W")

        name_entry = ttk.Entry(
            container,
            textvariable=self.container.item_name,
            width=50
        )
        name_entry.grid(row=0, column=1, sticky="EW")

        # --- Type ---

        type_label = ttk.Label(
            container,
            text="Type"
        )
        type_label.grid(row=1, column=0, padx=local_pad, sticky="W")

        type_entry = ttk.Combobox(
            container,
            textvariable=self.container.item_type,
            values=self.container.item_types,
            state="readonly"
        )
        type_entry.grid(row=1, column=1, sticky="EW")

        # --- Reduction ---

        reduction_label = ttk.Label(
            container,
            text="Reduction"
        )
        reduction_label.grid(row=2, column=0, padx=local_pad, sticky="W")

        reduction_entry = ttk.Entry(
            container,
            textvariable=self.container.item_reduction,
            width=50
        )
        reduction_entry.grid(row=2, column=1, sticky="EW")

        # --- Damage ---

        damage_label = ttk.Label(
            container,
            text="Damage"
        )
        damage_label.grid(row=3, column=0, padx=local_pad, sticky="W")

        damage_entry = ttk.Entry(
            container,
            textvariable=self.container.item_damage,
            width=50
        )
        damage_entry.grid(row=3, column=1, sticky="EW")

        # --- Range ---

        range_label = ttk.Label(
            container,
            text="Range"
        )
        range_label.grid(row=4, column=0, padx=local_pad, sticky="W")

        range_entry = ttk.Entry(
            container,
            textvariable=self.container.item_range,
            width=50
        )
        range_entry.grid(row=4, column=1, sticky="EW")

        # --- HP ---

        life_points_label = ttk.Label(
            container,
            text="HP"
        )
        life_points_label.grid(row=5, column=0, padx=local_pad, sticky="W")

        life_points_entry = ttk.Spinbox(
            container,
            from_=0,
            increment=1,
            justify="center",
            textvariable=self.container.item_life_points,
            width=10
        )
        life_points_entry.grid(row=5, column=1, sticky="EW")

        # --- Area ---

        area_label = ttk.Label(
            container,
            text="Area"
        )
        area_label.grid(row=6, column=0, padx=local_pad, sticky="W")

        area_entry = ttk.Combobox(
            container,
            textvariable=self.container.item_area,
            values=('No', 'Yes'),
            state="readonly"
        )
        area_entry.grid(row=6, column=1, sticky="EW")

        # --- Abilities ---

        abilities_label = ttk.Label(
            container,
            text="Abilities"
        )
        abilities_label.grid(row=7, column=0, padx=local_pad, sticky="W")

        self.abilities_entry = tk.Listbox(
            container,
            listvariable=self.container.item_abilities,
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

        # --- Effects ---
        effects_label = ttk.Label(
            container,
            text="Effects"
        )
        effects_label.grid(row=8, column=0, padx=local_pad, sticky="W")

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

    def create_button_widgets(self, container):
        create_button = ttk.Button(
            container,
            text="Create",
            command=self.create_item,
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

    def create_item(self):
        item_name = self.container.item_name.get()
        item_type = self.container.item_type.get()
        item_reduction = self.container.item_reduction.get()
        item_damage = self.container.item_damage.get()
        item_range = self.container.item_range.get()
        item_hp = self.container.item_life_points.get()
        item_area = self.container.item_area.get()
        item_abilities = self.handle_selection_change(self.abilities_entry, self.container.abilities)
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
        create_item = item.create_item(temp_name, file_name)

        if create_item:
            self.container.show_home()

    def handle_selection_change(self, list_widget, total_list):
        selected_indices = list_widget.curselection()
        result_list = []

        for i in selected_indices:
            result_list.append(total_list[i])

        return tuple(result_list)

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')
