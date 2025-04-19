import tkinter as tk
from utils.video_capture import capture_frames


def launch_manual_mode(gui_root):
    gui_root.after(1000, lambda: _launch_manual(gui_root))  # Delay launch to show transition


def launch_auto_mode(gui_root):
    gui_root.after(1000, lambda: _launch_auto(gui_root))  # Delay launch to show transition


def _launch_manual(gui_root):
    gui_root.destroy()
    print("[INFO] Running in MANUAL mode.")
    from manual import run_manual_mode
    run_manual_mode(capture_frames())


def _launch_auto(gui_root):
    gui_root.destroy()
    print("[INFO] Running in AUTOMATIC mode.")
    from automatic import run_auto_mode
    run_auto_mode()


def main():
    root = tk.Tk()
    root.title("Select Mode - Soccer Ball Launcher")

    # Set size and center the window
    window_width = 400
    window_height = 280
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.configure(bg="white")

    # Project Title
    project_title = tk.Label(root, text="Smart Soccer Ball Launcher", font=("Arial", 18, "bold"), bg="white", fg="darkblue")
    project_title.pack(pady=10)

    # Label
    label = tk.Label(root, text="Select Mode", font=("Arial", 14), bg="white")
    label.pack(pady=10)

    # Button Frame
    button_frame = tk.Frame(root, bg="white")
    button_frame.pack(pady=10)

    # Manual Button
    manual_btn = tk.Button(button_frame, text="Manual Mode", font=("Arial", 12),
                           width=15, command=lambda: launch_manual_mode(root))
    manual_btn.grid(row=0, column=0, padx=10)

    # Auto Button
    auto_btn = tk.Button(button_frame, text="Auto Mode", font=("Arial", 12),
                         width=15, command=lambda: launch_auto_mode(root))
    auto_btn.grid(row=0, column=1, padx=10)

    # Exit Button
    exit_btn = tk.Button(root, text="Exit", font=("Arial", 12),
                         width=15, bg="red", fg="white", command=root.destroy)
    exit_btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
