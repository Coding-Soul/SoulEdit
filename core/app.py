import tkinter as tk
from gui import start


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.version = '0.2'
        self.settings()
        self.show_frame(start.StartScreen)

    def settings(self):
        self.geometry('800x500')
        self.title(f'SoulNote - {self.version}')

    def show_frame(self, frame_class):
        frame = frame_class(self)
        frame.pack(fill='both', expand=True)
