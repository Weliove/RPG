import tkinter as tk
from tkinter.messagebox import showinfo


def popup_window():
    window = tk.Toplevel()

    label = tk.Label(window, text="Hello World!")
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')


def popup_showinfo(message):
    showinfo("ShowInfo", message)
