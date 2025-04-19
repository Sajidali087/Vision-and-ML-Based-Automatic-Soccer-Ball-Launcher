import tkinter as tk
from auto_UI.THEME import THEME  # Import THEME dictionary

class LaunchSetting(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="Launch Stats",
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
        
        # Info Labels
        self.launch_angle = tk.Label(self, text="▸ Launch Angle: 45°", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.launch_speed = tk.Label(self, text="▸ Launch Speed: 68%", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.ball_launched = tk.Label(self, text="▸ Ball Launched: Yes", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])

        # Pack labels with some spacing
        self.launch_angle.pack(anchor="w", pady=2)
        self.launch_speed.pack(anchor="w", pady=2)
        self.ball_launched.pack(anchor="w", pady=2)
