import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage

log_widget = None  # Global reference

def create_log_panel_gui(parent_width):
    global log_widget

    # Outer frame (Bottom-right section)
    outer_frame = tk.Frame(bg="white")

    # Inner frame split: left and right inside outer_frame
    left_inner_frame = tk.Frame(outer_frame, bg="white")
    left_inner_frame.place(x=0, y=0, width=parent_width//2, relheight=1)

    right_inner_frame = tk.Frame(outer_frame, bg="white")
    right_inner_frame.place(x=parent_width//2, y=0, width=parent_width//2, relheight=1)

    # Log panel inside right_inner_frame
    title_label = tk.Label(right_inner_frame, text="Launcher Logs", font=("Helvetica", 16, "bold"),
                           bg="white", fg="black")
    title_label.pack(pady=(10, 0))

    log_widget = scrolledtext.ScrolledText(
        right_inner_frame, wrap=tk.WORD, font=("Arial", 11),
        bg="#e6ffe6", fg="black", state="disabled", height=10
    )
    log_widget.pack(padx=10, pady=10, fill="both", expand=True)

    return outer_frame

def log_message(msg):
    global log_widget
    if log_widget:
        log_widget.configure(state="normal")
        log_widget.insert(tk.END, f"{msg}\n")
        log_widget.yview(tk.END)  # Auto-scroll
        log_widget.configure(state="disabled")
    


# -------------------------------------------------------------------------------------------------------
def create_log_panel_gui(parent_width):
    global log_widget

    outer_frame = tk.Frame(bg="white")

    # Split vertically into left and right parts
    left_inner_frame = tk.Frame(outer_frame, bg="white")
    left_inner_frame.place(x=0, y=0, width=parent_width//2, relheight=1)

    right_inner_frame = tk.Frame(outer_frame, bg="white")
    right_inner_frame.place(x=parent_width//2, y=0, width=parent_width//2, relheight=1)

    # === Action Button Definitions ===
    def log_action(label):
        log_message(f"{label} button pressed")

    # Buttons with standard color and labels
    control_buttons = [
        ("Launch", "#28a745", "▶️"),
        ("Pause", "#ffc107", "⏸️"),
        ("Stop", "#dc3545", "⏹️"),
        ("Reset", "#007bff", "🔄"),
        ("Snapshot", "#6c757d", "📷"),
    ]

    for label, color, icon in control_buttons:
        btn = tk.Button(
            left_inner_frame,
            text=f"{icon} {label}",
            font=("Segoe UI", 12, "bold"),
            bg=color, fg="white",
            activebackground=color,
            relief="raised",
            borderwidth=2,
            command=lambda l=label: log_action(l)
        )
        btn.pack(pady=8, ipadx=6, ipady=4, fill="x", padx=10)

    # === Log area on right ===
    title_label = tk.Label(right_inner_frame, text="Launcher Logs", font=("Helvetica", 16, "bold"),
                           bg="white", fg="black")
    title_label.pack(pady=(10, 0))

    log_widget = scrolledtext.ScrolledText(
        right_inner_frame, wrap=tk.WORD, font=("Arial", 11),
        bg="#e6ffe6", fg="black", state="disabled", height=10
    )
    log_widget.pack(padx=10, pady=10, fill="both", expand=True)

    return outer_frame

