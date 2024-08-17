import customtkinter as tk
from . import start
from core import logic
from tkinter import messagebox, filedialog
from utils import colors


class NoteScreen(tk.CTkFrame):
    def __init__(self, master, note_text: str, note_title: str):
        super().__init__(master=master)
        self.note_title_entry = None
        self.textbox = None
        self.note_text = note_text
        self.header()
        self.note_title(note_title)
        self.note_textbox()

    def header(self):
        button_frame = tk.CTkFrame(self)

        back_btn = tk.CTkButton(
            button_frame,
            text='Back',
            font=('Arial', 16),
            height=1,
            width=5,
            command=self.back_to_start
        )
        back_btn.grid(row=0, column=0, sticky='w', padx=2.5)

        save_button = tk.CTkButton(
            button_frame,
            text='Save Note',
            font=('Arial', 16),
            height=1,
            width=10,
            command=self.save_note
        )
        save_button.grid(row=0, column=1, sticky='w', padx=2.5)

        button_frame.grid(row=0, column=0, sticky='w')

    def note_title(self, title):
        self.note_title_entry = tk.CTkEntry(
            self,
            placeholder_text="Untitled Note",
            font=('Arial', 25),
            height=1,
            width=500,
            corner_radius=0,
            fg_color=colors.BACKGROUND_COLOR,
            border_color=colors.BACKGROUND_COLOR
        )

        if title != "":
            self.note_title_entry.insert(tk.END, title)

        self.note_title_entry.grid(row=1, column=0, columnspan=2, sticky='w', padx=(15, 0))
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def note_textbox(self):
        self.textbox = tk.CTkTextbox(
            self,
            font=('Arial', 12),
            wrap='word',
            width=200,
            fg_color=colors.BACKGROUND_COLOR
        )
        self.textbox.insert(tk.END, self.note_text)

        self.textbox.grid(row=2, column=0, padx=20, sticky='nsew')
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def back_to_start(self):
        self.destroy()

        start_screen = start.StartScreen(self.master)
        start_screen.pack(fill='both', expand=True)

    def save_note(self):
        folder_selected = filedialog.askdirectory(title='Select Folder')

        if folder_selected:
            title = self.note_title_entry.get()

            if title:
                logic.save_note(f'{folder_selected}/{title}.txt', text=self.textbox.get('1.0', tk.END).strip())
                messagebox.showinfo('Saved Note', 'Note has been saved successfully')
            else:
                messagebox.showinfo('Input Error', 'Please enter a filename')
