import tkinter as tk
from PIL import Image, ImageTk
import UI.angle_meter as angle_meter
import UI.range as range
import UI.log_panel as log_panel
import cv2
from threading import Thread
from config import CUSTOM_RESOLUTION, SCALE_RESOLUTION
# import shared_state

# GUI setup
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.title("Automatic Soccer Ball Launcher: Vision Based")

canvas = tk.Canvas(window, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_line(screen_width // 2, 0, screen_width // 2, screen_height, width=1, fill="white")
canvas.create_line(0, screen_height // 2, screen_width, screen_height // 2, width=1, fill="black")

video_label = tk.Label(window)
video_label.place(x=screen_width // 2, y=0, width=screen_width // 2, height=screen_height // 2)

def update_video_frame_from_detection(frame):
    frame = cv2.resize(frame, (int(CUSTOM_RESOLUTION[0]*SCALE_RESOLUTION), int(CUSTOM_RESOLUTION[1]*SCALE_RESOLUTION)))  # Resize to custom resolution
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb_frame)
    img_tk = ImageTk.PhotoImage(image=img)

    if video_label.winfo_exists():  # ✅ Prevent update after window is closed
        video_label.config(image=img_tk)
        video_label.image = img_tk


# Add control panels
top_left_frame = angle_meter.create_angle_meter_gui()
top_left_frame.place(x=0, y=0, width=screen_width // 2, height=screen_height // 2)

bottom_left_frame = range.create_distance_control_gui()
bottom_left_frame.place(x=0, y=screen_height // 2, width=screen_width // 2, height=screen_height // 2)

bottom_right_frame = log_panel.create_log_panel_gui(parent_width=screen_width // 2)
bottom_right_frame.place(x=screen_width // 2, y=screen_height // 2, width=screen_width // 2, height=screen_height // 2)

def start_detection_thread():
    def detection_loop():
        cap = cv2.VideoCapture(0)
        from utils.yolo_detector import YoloDetector
        yolo = YoloDetector()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Detect and update GUI
            frame, *_ = yolo.detect_person(frame)

            if window.winfo_exists():
                update_video_frame_from_detection(frame)
            else:
                break

        cap.release()

    Thread(target=detection_loop, daemon=True).start()

def run_gui(start_detection_thread):
    start_detection_thread()
    window.mainloop()

# Call this to launch
if __name__ == "__main__":
    run_gui()
