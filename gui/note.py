import tkinter as tk
from . import start
from core import logic
from tkinter import messagebox, filedialog


class NoteScreen(tk.Frame):
    def __init__(self, master, note_text: str):
        super().__init__(master=master)
        self.textbox = None
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
            width=10,
            command=self.save_note
        )
        save_button.grid(row=0, column=1, sticky='w', padx=2.5)

        button_frame.grid(row=0, column=0, sticky='w')

    def note_textbox(self):
        self.textbox = tk.Text(
            self,
            font=('Arial', 12),
            wrap='word',
            width=200
        )
        self.textbox.insert(tk.END, self.note_text)

        self.textbox.grid(row=1, column=0, padx=20, pady=10, sticky='nsew')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def back_to_start(self):
        self.destroy()

        start_screen = start.StartScreen(self.master)
        start_screen.pack(fill='both', expand=True)

    def save_note(self):
        folder_selected = filedialog.askdirectory(title='Select Folder')

        if folder_selected:
            self.enter_filename(folder_selected=folder_selected)

            print(folder_selected)

    def enter_filename(self, folder_selected):
        def on_confirm():
            note_content = self.textbox
            filename = entry.get()
            if filename:
                logic.save_note(f'{folder_selected}/{filename}.txt', text=note_content.get('1.0', tk.END).strip())
                messagebox.showinfo('Saved Note', 'Note has been saved successfully')
            else:
                messagebox.showinfo('Input Error', 'Please enter a filename')

        def on_cancel():
            top.destroy()

        top = tk.Toplevel(self)
        top.title("Enter Filename")

        tk.Label(top, text="Filename:").pack(pady=5)
        entry = tk.Entry(top, width=50)
        entry.pack(pady=5)

        btn_frame = tk.Frame(top)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Confirm", command=on_confirm).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancel", command=on_cancel).pack(side=tk.LEFT, padx=5)
