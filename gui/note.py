import tkinter as tk
from . import start


class NoteScreen(tk.Frame):
    def __init__(self, master, note_text: str):
        super().__init__(master=master)
        self.note_text = note_text
        self.header()
        self.note_textbox()

    def header(self):
        button_frame = tk.Frame(self)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        back_btn = tk.Button(
            button_frame,
            text='Back',
            font=('Arial', 16),
            height=1,
            width=5,
            command=self.back_to_start
        )
        back_btn.grid(row=0, column=0, sticky='w', padx=2.5)

        save_button = tk.Button(
            button_frame,
            text='Save Note',
            font=('Arial', 16),
            height=1,
            width=10
        )
        save_button.grid(row=0, column=1, sticky='w', padx=2.5)

        button_frame.grid(row=0, column=0, sticky='w')

    def note_textbox(self):
        textbox = tk.Text(
            self,
            font=('Arial', 12),
            wrap='word',
            width=200
        )
        textbox.insert(tk.END, self.note_text)

        textbox.grid(row=1, column=0, padx=20, pady=10, sticky='nsew')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def back_to_start(self):
        self.destroy()

        start_screen = start.StartScreen(self.master)
        start_screen.pack(fill='both', expand=True)
