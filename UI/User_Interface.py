import tkinter as tk
from PIL import Image, ImageTk
import UI.angle_meter as angle_meter
import UI.range as range
import UI.log_panel as log_panel
import cv2

# Global window and label
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.title("Automatics Soccer Ball Launcher: Vision Based")

canvas = tk.Canvas(window, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_line(screen_width//2, 0, screen_width//2, screen_height, width=1, fill="white")
canvas.create_line(0, (screen_height)//2, screen_width, screen_height//2, width=1, fill="black")
print(screen_width, screen_height)
video_label = tk.Label(window)
video_label.place(x=screen_width//2, y=0, width=screen_width//2, height=screen_height//2)

def update_video_frame_from_detection(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb_frame)
    img_tk = ImageTk.PhotoImage(image=img)
    video_label.config(image=img_tk)
    video_label.image = img_tk

top_left_frame = angle_meter.create_angle_meter_gui()
top_left_frame.place(x=0, y=0, width=screen_width//2, height=screen_height//2)

bottom_left_frame = range.create_distance_control_gui()
bottom_left_frame.place(x=0, y=screen_height//2, width=screen_width//2, height=screen_height//2)

bottom_right_frame = log_panel.create_log_panel_gui(parent_width=screen_width//2)
bottom_right_frame.place(
    x=screen_width//2,
    y=screen_height//2,
    width=screen_width//2,
    height=screen_height//2
)

# ✅ NEW: Launch GUI and start detection in thread
def run_gui(start_detection_thread):
    # Start detection thread
    start_detection_thread()
    # Run GUI in main thread
    window.mainloop()
