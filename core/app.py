import customtkinter as ctk
from gui import start


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.settings()
        self.show_frame(start.StartScreen)

    def settings(self):
        self.geometry('800x500')
        self.title(f'SoulEdit')

    def show_frame(self, frame_class):
        frame = frame_class(self)
        frame.pack(fill='both', expand=True)
