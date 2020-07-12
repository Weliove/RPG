from tkinter import ttk
from tkinter import font
from src.avatar.avatar_properties import AvatarProperties
from src.avatar.avatar import Avatar
from src.file_methods import get_all_file_names
from src.popup_window import *


class CreateAvatar(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        avatar_properties = AvatarProperties()

        # --- Get Properties ---

        self.MAX_HP = avatar_properties.MAX_HP
        self.MAX_AD = avatar_properties.MAX_AD

        self.classes_values = avatar_properties.classes_values
        self.type_values = avatar_properties.type_values

        self.weapons_values = avatar_properties.weapons_values
        self.armors_values = avatar_properties.armors_values
        self.titles_values = avatar_properties.titles_values

        # --- Variables ---

        self.avatar_name = tk.StringVar()

        self.avatar_hp = tk.StringVar(value="1")

        self.avatar_ad = tk.StringVar(value="1")

        self.avatar_class = tk.StringVar(value=self.classes_values[0])

        self.avatar_type = tk.StringVar(value=self.type_values[0])

        self.avatar_weapon = tk.StringVar(value=self.weapons_values[0])
        self.avatar_weapons = tk.StringVar(value=self.weapons_values)

        self.avatar_special_weapons = get_all_file_names('weapons_file')
        self.avatar_weapons_special = tk.StringVar(value=self.avatar_special_weapons)

        self.avatar_armor = tk.StringVar(value=self.armors_values[0])

        self.avatar_special_armors = get_all_file_names('armors_file')
        self.avatar_armor_special = tk.StringVar(value=self.avatar_special_armors[0])

        self.avatar_physical_ab = tk.StringVar(value='None')

        self.avatar_titles = tk.StringVar(value=self.titles_values)

        self.abilities = get_all_file_names('abilities_file')
        self.avatar_abilities = tk.StringVar(value=self.abilities)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_avatar_scroll = CreateAvatarScroll(self)
        self.create_avatar_scroll.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

        self.create_avatar_scroll.create_avatar_container()


class CreateAvatarScroll(tk.Canvas):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        # --- Custom ---

        self.container = container

        self.font = font.Font(size=11)

        self.weapon_entry = tk.Listbox()
        self.weapon_special_entry = tk.Listbox()
        self.title_entry = tk.Listbox()
        self.ability_entry = tk.Listbox()
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

    def create_avatar_container(self):
        avatar_widgets_frame = ttk.Frame(self.screen)
        avatar_widgets_frame.grid(row=0, column=0, sticky="NSEW")
        avatar_widgets_frame.columnconfigure(0, weight=1)
        avatar_widgets_frame.rowconfigure(1, weight=1)

        # --- Properties ---

        self.create_avatar_properties(avatar_widgets_frame)

        # --- Weapon & Armor ---

        self.create_equip_widgets(avatar_widgets_frame)

        # --- Title ---

        self.create_avatar_titles(avatar_widgets_frame)

        # --- Ability ---

        self.create_avatar_abilities(avatar_widgets_frame)

        # --- Buttons ---

        button_container = ttk.Frame(self.screen)
        button_container.grid(row=1, column=0, sticky="EW")
        button_container.columnconfigure(0, weight=1)

        self.create_avatar_buttons(button_container)

        for child in avatar_widgets_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_avatar_properties(self, container):
        # --- Name ---

        name_label = ttk.Label(
            container,
            text="Name"
        )
        name_label.grid(row=0, column=0, sticky="W")

        name_entry = ttk.Entry(
            container,
            textvariable=self.container.avatar_name,
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
            to=self.container.MAX_HP,
            increment=1,
            justify="center",
            textvariable=self.container.avatar_hp,
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
            to=self.container.MAX_AD,
            increment=1,
            justify="center",
            textvariable=self.container.avatar_ad,
            width=10
        )
        adrenaline_entry.grid(row=2, column=1, sticky="EW")

        # --- Avatar Type ---

        type_label = ttk.Label(
            container,
            text="Type"
        )
        type_label.grid(row=3, column=0, sticky="W")

        type_entry = ttk.Combobox(
            container,
            textvariable=self.container.avatar_type,
            values=self.container.type_values,
            state="readonly"
        )
        type_entry.grid(row=3, column=1, sticky="EW")

        # --- Class ---

        _class_label = ttk.Label(
            container,
            text="Class"
        )
        _class_label.grid(row=4, column=0, sticky="W")

        _class_entry = ttk.Combobox(
            container,
            textvariable=self.container.avatar_class,
            values=self.container.classes_values,
            state="readonly"
        )
        _class_entry.grid(row=4, column=1, sticky="EW")

    def create_equip_widgets(self, container):
        # --- Weapon ---

        weapon_label = ttk.Label(
            container,
            text="Weapons"
        )
        weapon_label.grid(row=5, column=0, sticky="W")

        self.weapon_entry = tk.Listbox(
            container,
            listvariable=self.container.avatar_weapons,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.weapon_entry.grid(row=5, column=1, sticky="EW")

        weapon_scrollbar = ttk.Scrollbar(container, orient="vertical")
        weapon_scrollbar.config(command=self.weapon_entry.yview)
        weapon_scrollbar.grid(row=5, column=2, sticky="NS")

        self.weapon_entry.config(yscrollcommand=weapon_scrollbar.set)

        # --- Special Weapons ---

        weapon_special_label = ttk.Label(
            container,
            text="S. Weapons"
        )
        weapon_special_label.grid(row=6, column=0, sticky="W")

        self.weapon_special_entry = tk.Listbox(
            container,
            listvariable=self.container.avatar_weapons_special,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.weapon_special_entry.grid(row=6, column=1, sticky="EW")

        weapon_special_scrollbar = ttk.Scrollbar(container, orient="vertical")
        weapon_special_scrollbar.config(command=self.weapon_special_entry.yview)
        weapon_special_scrollbar.grid(row=6, column=2, sticky="NS")

        self.weapon_special_entry.config(yscrollcommand=weapon_special_scrollbar.set)

        # --- Armor ---

        armor_label = ttk.Label(
            container,
            text="Armor"
        )
        armor_label.grid(row=7, column=0, sticky="W")

        armor_entry = ttk.Combobox(
            container,
            textvariable=self.container.avatar_armor,
            values=self.container.armors_values,
            state="readonly"
        )
        armor_entry.grid(row=7, column=1, sticky="EW")

        # --- Special Armor ---

        armor_special_label = ttk.Label(
            container,
            text="S. Armor"
        )
        armor_special_label.grid(row=8, column=0, sticky="W")

        armor_special_entry = ttk.Combobox(
            container,
            textvariable=self.container.avatar_armor_special,
            values=self.container.avatar_special_armors,
            state="readonly"
        )
        armor_special_entry.grid(row=8, column=1, sticky="EW")

        # --- Physical Ab ---

        physical_ab_label = ttk.Label(
            container,
            text="Physical Ab."
        )
        physical_ab_label.grid(row=9, column=0, sticky="W")

        physical_ab_entry = ttk.Entry(
            container,
            textvariable=self.container.avatar_physical_ab,
            width=50
        )
        physical_ab_entry.grid(row=9, column=1, sticky="EW")

    def create_avatar_titles(self, container):
        # --- Title ---

        title_label = ttk.Label(
            container,
            text="Titles"
        )
        title_label.grid(row=10, column=0, sticky="W")

        self.title_entry = tk.Listbox(
            container,
            listvariable=self.container.avatar_titles,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.title_entry.grid(row=10, column=1, sticky="EW")

        title_scrollbar = ttk.Scrollbar(container, orient="vertical")
        title_scrollbar.config(command=self.title_entry.yview)
        title_scrollbar.grid(row=10, column=2, sticky="NS")

        self.title_entry.config(yscrollcommand=title_scrollbar.set)

    def create_avatar_abilities(self, container):
        # --- Ability ---

        ability_label = ttk.Label(
            container,
            text="Abilities"
        )
        ability_label.grid(row=11, column=0, sticky="W")

        self.ability_entry = tk.Listbox(
            container,
            listvariable=self.container.avatar_abilities,
            selectmode="extended",
            exportselection=False,
            selectbackground="#2CCC5B",
            highlightcolor="#1DE557",
            font=self.font,
            width=1,
            height=5
        )
        self.ability_entry.grid(row=11, column=1, sticky="EW")

        ability_scrollbar = ttk.Scrollbar(container, orient="vertical")
        ability_scrollbar.config(command=self.ability_entry.yview)
        ability_scrollbar.grid(row=11, column=2, sticky="NS")

        self.ability_entry.config(yscrollcommand=ability_scrollbar.set)

    def create_avatar_description(self, container):
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

    def create_avatar_buttons(self, button_container):
        # --- Create Avatar Button ---

        create_button = ttk.Button(
            button_container,
            text="Create",
            command=self.create_avatar_handler,
            cursor="hand2"
        )
        create_button.grid(row=0, column=0, padx=5, pady=5, sticky="EW")

        # --- Back Home Button ---

        back_button = ttk.Button(
            button_container,
            text="← Back",
            command=self.container.show_home,
            cursor="hand2"
        )
        back_button.grid(row=1, column=0, padx=5, pady=5, sticky="EW")

    def create_avatar_handler(self):
        name = self.container.avatar_name.get()
        hp = self.container.avatar_hp.get()
        ad = self.container.avatar_ad.get()
        _class = self.container.avatar_class.get()
        weapon = self.handle_selection_change(self.weapon_entry, self.container.weapons_values)
        special_weapon = self.handle_selection_change(self.weapon_special_entry, self.container.avatar_special_weapons)
        armor = self.container.avatar_armor.get()
        special_armor = self.container.avatar_armor_special.get()
        physical_ab = self.container.avatar_physical_ab.get()
        title = self.handle_selection_change(self.title_entry, self.container.titles_values)
        ability = self.handle_selection_change(self.ability_entry, self.container.abilities)
        description = self.get_text_data(self.description_entry)

        weapon_result = weapon + special_weapon
        armor_result = special_armor

        if special_armor == "None":
            armor_result = armor

        if name == '':
            popup_showinfo("Please, type a name.")
            return

        if hp == '' or hp == '0':
            hp = '1'

        if ad == '' or ad == '0':
            ad = '1'

        if physical_ab == '':
            physical_ab = 'None'

        if len(ability) == 0:
            ability = ['None']

        if len(description) == 0:
            description = 'None'

        if len(title) == 0:
            title = ['None']

        temp_name = name.lower().replace(" ", "_")
        file_name = temp_name + ".txt"

        avatar = Avatar(name, hp, ad, _class, weapon_result, armor_result, physical_ab, title, ability, description)
        create_avatar = avatar.create_avatar(temp_name, file_name)

        if create_avatar:
            self.container.show_home()

    def handle_selection_change(self, list_widget, total_list):
        selected_indices = list_widget.curselection()
        result_list = []

        for i in selected_indices:
            result_list.append(total_list[i])

        return tuple(result_list)

    def get_text_data(self, text_widget):
        return text_widget.get("1.0", 'end-1c')

