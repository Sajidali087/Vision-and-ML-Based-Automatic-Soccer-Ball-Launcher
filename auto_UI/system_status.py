import tkinter as tk
from auto_UI.THEME import THEME  # Import THEME dictionary

class SystemFrameStatsPanel(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="System & Frame Stats",
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
        self.fps = tk.Label(self, text="▸ FPS: 29.8", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.cpu_temp = tk.Label(self, text="▸ CPU Temp: 55°C", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.ram_usage = tk.Label(self, text="▸ RAM Usage: 52%", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.rpi_uptime = tk.Label(self, text="▸ RPi Uptime: 01:32:11", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.frame_size = tk.Label(self, text="▸ Frame Size: 480x640 px", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])
        self.resolution_mode = tk.Label(self, text="▸ Resolution Mode: Custom", anchor="w", bg=THEME["panel_color"], font=THEME["label_font"])

        # Pack labels with some spacing
        self.fps.pack(anchor="w", pady=2)
        self.cpu_temp.pack(anchor="w", pady=2)
        self.ram_usage.pack(anchor="w", pady=2)
        self.rpi_uptime.pack(anchor="w", pady=2)
        self.frame_size.pack(anchor="w", pady=2)
        self.resolution_mode.pack(anchor="w", pady=2)
