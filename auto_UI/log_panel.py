import tkinter as tk
from auto_UI.THEME import THEME  # Import THEME dictionary

class LogPanel(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="Log Panel",
            font=THEME["title_font"],
            padx=10,
            pady=10,
            bg=THEME["background_color"],
            fg=THEME["text_color"],
            bd=2,
            relief="groove"
        )
        self.configure(width=300, height=300)  # Set specific width and height for the frame
        self.pack_propagate(False)  # Prevent resizing of the frame
        
        # Info Labels (example logs)
        self.log_1 = tk.Label(self, text="▸ 12:01 - Player detected", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.log_2 = tk.Label(self, text="▸ 12:01 - Launch speed 68%", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.log_3 = tk.Label(self, text="▸ 12:01 - Ball launched", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.log_4 = tk.Label(self, text="▸ 12:02 - Player out of frame", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])

        # Pack labels with some spacing
        self.log_1.pack(anchor="w", pady=2)
        self.log_2.pack(anchor="w", pady=2)
        self.log_3.pack(anchor="w", pady=2)
        self.log_4.pack(anchor="w", pady=2)
