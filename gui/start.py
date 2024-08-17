import tkinter as tk
from tkinter import ttk
from gui.note import NoteScreen


class StartScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.welcome_label()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.button_layout()

    def welcome_label(self):
        label = ttk.Label(self,
                          text='Welcome to Soul Note',
                          font=('Arial', 18)
                          )
        label.grid(row=0, column=0, columnspan=2)

    def button_layout(self):
        new_note_btn = ttk.Button(
            self,
            text='New Note',
            command=self.new_note_interaction
        )
        new_note_btn.grid(row=1, column=0, sticky='e')

        open_note_btn = ttk.Button(
            self,
            text='Open Recent Note',
            command=self.open_recent_note_interaction
        )
        open_note_btn.grid(row=1, column=1, sticky='w')

    def new_note_interaction(self):
        self.destroy()

        note_screen = NoteScreen(self.master, note_text='')
        note_screen.pack(fill='both', expand=True)

    def open_recent_note_interaction(self):
        self.destroy()

        note_screen = NoteScreen(self.master, note_text='Bereits vorhandener Text')
        note_screen.pack(fill='both', expand=True)
