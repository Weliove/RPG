from tkinter import ttk
from src.popup_window import *
from src.title.title import Title


class CreateTitle(ttk.Frame):
    def __init__(self, parent, show_home):
        super().__init__(parent)

        self.show_home = show_home

        self.title_name = tk.StringVar()

        self.requirements_entry = tk.Text()
        self.description_entry = tk.Text()

        # --- Create Widgets ---

        title_widgets_frame = ttk.Frame(self)
        title_widgets_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
        title_widgets_frame.columnconfigure(0, weight=1)

        self.create_title_widgets(title_widgets_frame)

        for child in title_widgets_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # --- Create Buttons Container ---

        button_container = ttk.Frame(self)
        button_container.grid(row=1, column=0, padx=10, pady=10, sticky="EW")
        button_container.columnconfigure(0, weight=1)

        self.create_title_buttons(button_container)

        for child in button_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def create_title_widgets(self, container):
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

    def create_title_buttons(self, button_container):
        # --- Create Title Button ---

        create_button = ttk.Button(
            button_container,
            text="Create",
            command=self.create_title_handler,
            cursor="hand2"
        )
        create_button.grid(row=0, column=0, sticky="EW")

        # --- Back Home Button ---

        back_button = ttk.Button(
            button_container,
            text="← Back",
            command=self.show_home,
            cursor="hand2"
        )
        back_button.grid(row=1, column=0, sticky="EW")

    def create_title_handler(self):
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
