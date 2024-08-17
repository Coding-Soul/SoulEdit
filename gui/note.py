import tkinter as tk
from . import start


class NoteScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.header()
        self.note_textbox()

    def header(self):
        back_btn = tk.Button(
            self,
            text='Back',
            font=('Arial', 16),
            height=1,
            width=5,
            command=self.back_to_start
        )
        back_btn.grid(row=0, column=0, sticky='w')
        self.grid_columnconfigure(0, weight=1)

    def note_textbox(self):
        textbox = tk.Text(
            self,
            font=('Arial', 18),
            wrap='word',
            width=200
        )

        textbox.grid(row=1, column=0, padx=20, pady=10, sticky='nsew')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def back_to_start(self):
        self.destroy()

        start_screen = start.StartScreen(self.master)
        start_screen.pack(fill='both', expand=True)
