import customtkinter as tk

from core import logic
from gui.note import NoteScreen
from utils import colors
from gui.settings import SettingsScreen
from tkinter import filedialog


class StartScreen(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.welcome_label()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.button_layout()

    def welcome_label(self):
        label = tk.CTkLabel(self,
                            text='Welcome to Soul Note',
                            font=('Arial', 18)
                            )
        label.grid(row=0, column=0, columnspan=2)

    def button_layout(self):
        button_frame = tk.CTkFrame(self, fg_color=colors.BACKGROUND_COLOR)

        new_note_btn = tk.CTkButton(
            button_frame,
            text='New Note',
            command=self.new_note_interaction
        )
        new_note_btn.grid(row=1, column=0, sticky='w', padx=10)

        open_note_btn = tk.CTkButton(
            button_frame,
            text='Open Recent Note',
            command=self.open_recent_note_interaction
        )
        open_note_btn.grid(row=1, column=1, sticky='w')

        settings_btn = tk.CTkButton(
            button_frame,
            text='Settings',
            command=self.open_settings_interaction
        )
        settings_btn.grid(row=1, column=2, sticky='w', padx=10)

        button_frame.grid(row=1, column=0, columnspan=2)

    def new_note_interaction(self):
        self.destroy()

        note_screen = NoteScreen(self.master, note_text='', note_title="")
        note_screen.pack(fill='both', expand=True)

    def open_recent_note_interaction(self):
        directory = filedialog.askopenfilename(
            title='Open a note',
            initialdir='/',
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.txt"))
        )

        if directory:
            print(directory)
            self.destroy()

            note_info = logic.open_note(directory)
            note_screen = NoteScreen(self.master, note_text=note_info[1], note_title=note_info[0])
            note_screen.pack(fill='both', expand=True)

    def open_settings_interaction(self):
        self.destroy()

        settings_screen = SettingsScreen(self.master)
        settings_screen.pack(fill='both', expand=True)
