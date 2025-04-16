import tkinter as tk
from PIL import Image, ImageTk
import UI.angle_meter as angle_meter
import UI.range as range
import UI.log_panel as log_panel
import cv2

# Create root window
window = tk.Tk()
window.title("Automatics Soccer Ball Launcher: Vision Based")

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Adjust height to avoid taskbar overlap (e.g., subtract 80 pixels)
adjusted_height = screen_height - 80
adjusted_width = screen_width

# Center window on screen
x_offset = 0
y_offset = (screen_height - adjusted_height) // 2
window.geometry(f"{adjusted_width}x{adjusted_height}+{x_offset}+{y_offset}")

# Canvas for layout and lines
canvas = tk.Canvas(window, width=adjusted_width, height=adjusted_height)
canvas.pack()
canvas.create_line(adjusted_width//2, 0, adjusted_width//2, adjusted_height, width=1, fill="white")
canvas.create_line(0, adjusted_height//2, adjusted_width, adjusted_height//2, width=1, fill="black")
print(adjusted_width, adjusted_height)

# Video label on top-right
video_label = tk.Label(window)
video_label.place(x=adjusted_width//2, y=0, width=adjusted_width//2, height=adjusted_height//2)

def update_video_frame_from_detection(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb_frame)
    img_tk = ImageTk.PhotoImage(image=img)
    video_label.config(image=img_tk)
    video_label.image = img_tk

# Top-left: Angle meter
top_left_frame = angle_meter.create_angle_meter_gui()
top_left_frame.place(x=0, y=0, width=adjusted_width//2, height=adjusted_height//2)

# Bottom-left: Range controller
bottom_left_frame = range.create_distance_control_gui()
bottom_left_frame.place(x=0, y=adjusted_height//2, width=adjusted_width//2, height=adjusted_height//2)

# Bottom-right: Log panel
bottom_right_frame = log_panel.create_log_panel_gui(parent_width=adjusted_width//2)
bottom_right_frame.place(
    x=adjusted_width//2,
    y=adjusted_height//2,
    width=adjusted_width//2,
    height=adjusted_height//2
)

# GUI runner
def run_gui(start_detection_thread):
    start_detection_thread()
    window.mainloop()
