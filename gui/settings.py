import customtkinter as tk
from utils import colors
from gui import start


class SettingsScreen(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.header()
        self.settings_label()

    def header(self):
        button_frame = tk.CTkFrame(self, fg_color=colors.BACKGROUND_COLOR)

        back_btn = tk.CTkButton(
            button_frame,
            text='Back',
            font=('Arial', 16),
            command=self.back_to_start,
            height=25,
            width=50
        )
        back_btn.grid(row=0, column=0, padx=(10, 0), pady=(5, 0))

        button_frame.grid(row=0, column=0, pady=(5, 30), sticky='w')

    def settings_label(self):
        settings_ctk_label = tk.CTkLabel(
            self,
            text='General Settings',
            font=('Arial', 20)
        )
        settings_ctk_label.grid(row=1, column=0, sticky='w', columnspan=2)

    def back_to_start(self):
        self.destroy()

        start_screen = start.StartScreen(self.master)
        start_screen.pack(fill='both', expand=True)
