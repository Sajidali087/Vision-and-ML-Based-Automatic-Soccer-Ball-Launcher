import tkinter as tk
from auto_UI.THEME import THEME  # Import THEME dictionary

class PlayerDetectionPanel(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="Player Detection Info",
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
        self.player_detected = tk.Label(self, text="▸ Player Detected: Yes", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.player_id = tk.Label(self, text="▸ Player ID: #3", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.jersey_color = tk.Label(self, text="▸ Jersey Color: Red", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.pixel_height = tk.Label(self, text="▸ Pixel Height: 280 px", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.distance = tk.Label(self, text="▸ Distance: 5.2 meters", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.position = tk.Label(self, text="▸ Position: Center-Right", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.pid_output = tk.Label(self, text="▸ PID Output: 0.73", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.status = tk.Label(self, text="▸ Status: Target Acquired", anchor="w", bg=THEME["panel_color"], font=("Helvetica", 10, "bold"))

        # Pack labels with some spacing
        self.player_detected.pack(anchor="w", pady=2)
        self.player_id.pack(anchor="w", pady=2)
        self.jersey_color.pack(anchor="w", pady=2)
        self.pixel_height.pack(anchor="w", pady=2)
        self.distance.pack(anchor="w", pady=2)
        self.position.pack(anchor="w", pady=2)
        self.pid_output.pack(anchor="w", pady=2)
        self.status.pack(anchor="w", pady=2)

