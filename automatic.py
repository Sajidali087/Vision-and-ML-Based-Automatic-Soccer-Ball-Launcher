import tkinter as tk
from PIL import Image, ImageTk
import cv2
from utils.video_capture import capture_frames  # Make sure this returns BGR frames
from auto_UI.detection_info import PlayerDetectionPanel  # Importing the PlayerDetectionPanel
from auto_UI.system_status import SystemFrameStatsPanel  # Importing the SystemFrameStatsPanel
from auto_UI.launch_setting import LaunchSetting  # Importing the SystemStatusPanel
from auto_UI.log_panel import LogPanel  # Importing the log panel module
from utils.adjust_orientation import PIDDetector
from utils.yolo_detector import YoloDetector  # Importing YoloDetector
import shared_state  # Importing shared state for global variables
from utils.frame_drawer import draw_and_annotate_frame  # Importing the function for drawing and annotating frames

class TitleBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.configure(height=60)
        self.pack_propagate(False)

        self.title_label = tk.Label(
            self,
            text="⚽ Automatic Mode - Soccer Ball Launcher ⚽",
            font=("Helvetica", 24, "bold"),
            bg="white",
            fg="#222222",
            anchor="center"
        )
        self.title_label.pack(fill="both", expand=True, pady=10)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Automatic Mode GUI")
        self.geometry("1366x768")
        self.configure(bg="white")

        # Initialize the YOLO detector
        self.yolo_detector = YoloDetector()

        # Add top title bar
        self.title_bar = TitleBar(self)
        self.title_bar.pack(fill="x")

        # Create Player Detection Panel (top-left)
        self.player_detection_panel = PlayerDetectionPanel(self)
        self.player_detection_panel.place(x=40, y=80)  # Previously y=70

        # Create System & Frame Stats Panel (bottom-left)
        self.system_frame_stats_panel = SystemFrameStatsPanel(self)
        self.system_frame_stats_panel.place(x=40, y=400)  # Adjusted to be bottom-left

        # Inside App.__init__()
        self.system_status_panel = LaunchSetting(self)
        self.system_status_panel.place(x=980, y=70)

        # Bottom-right Log Panel
        self.log_panel = LogPanel(self)
        self.log_panel.place(x=980, y=380)  # Adjust the X, Y if needed

        # Create video frame container
        self.video_frame = tk.Frame(self, width=640, height=480, bg="black")
        self.video_label = tk.Label(self.video_frame)
        self.video_label.pack()
        self.video_frame.place(x=300, y=70)  # Position the video frame to avoid overlap with player panel

        # Start video
        self.capture_generator = capture_frames()
        self.first_frame = next(self.capture_generator)  # Get the first frame to get dimensions
        self.video_width = self.first_frame.shape[1]  # Width of the frame
        self.video_height = self.first_frame.shape[0]  # Height of the frame

        self.after(100, self.center_video_frame)  # Center once the window is ready
        self.update_video_feed()

    def center_video_frame(self):
        screen_width = self.winfo_screenwidth()
        x_center = (screen_width - self.video_width) // 2  # Center the video frame
        self.video_frame.place(x=x_center, y=55)  # Adjusting the vertical position as well

    def update_video_feed(self):
        try:
            frame = next(self.capture_generator)
            image_height, image_width, _ = frame.shape
            # Detect persons using YOLO
            frame, person_center_x, person_height, distance_m, distance_ft = self.yolo_detector.detect_person(frame)
            if person_center_x is not None:

                detector = PIDDetector()
                frame = detector.detect_and_control(frame, person_center_x, image_height)
                frame = draw_and_annotate_frame(frame, person_center_x, person_height, distance_m, distance_ft, 45, shared_state.fps)
            
            # dump in shared_state file
            shared_state.person_center_x = person_center_x
            shared_state.person_height = person_height
            shared_state.distance_m = distance_m
            shared_state.distance_ft = distance_ft
            # image_height, image_width, _ = frame.shape
            # Convert BGR to RGB to fix color
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            image = Image.fromarray(frame_rgb)
            photo = ImageTk.PhotoImage(image=image)

            self.video_label.configure(image=photo)
            self.video_label.image = photo

        except Exception as e:
            print(f"[ERROR] {e}")

        self.after(30, self.update_video_feed)  # ~30 fps


def run_auto_mode():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    run_auto_mode()
