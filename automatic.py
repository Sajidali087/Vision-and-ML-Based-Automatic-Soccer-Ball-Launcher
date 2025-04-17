import tkinter as tk
from PIL import Image, ImageTk
import cv2
from utils.video_capture import capture_frames  # Make sure this exists and works
from config import CUSTOM_RESOLUTION  # Ensure it's a tuple like (640, 480)

class AutoModeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("Automatic Mode - Soccer Ball Launcher")
        self.configure(bg="black")

        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set window size to screen size minus taskbar height (assuming 40px for taskbar)
        self.geometry(f"{screen_width}x{screen_height - 40}+0+0")
        self.resizable(False, False)

        # Create canvas to display video
        self.canvas = tk.Canvas(self, width=screen_width, height=screen_height - 40)
        self.canvas.pack()

        # Create a label to hold the video feed
        self.video_label = tk.Label(self)
        self.video_label.place(x=0, y=0, width=screen_width, height=screen_height - 40)

        # Start capturing frames from the webcam using the capture_frames generator
        self.capture_generator = capture_frames()

        # Start video feed
        self.update_video_feed()

    def update_video_feed(self):
        try:
            frame = next(self.capture_generator)
            print("[INFO] Frame captured from webcam.")
            print(frame.shape)

            # Optional: Resize to custom resolution
            # frame = cv2.resize(frame, CUSTOM_RESOLUTION)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            img_tk = ImageTk.PhotoImage(image=img)

            self.video_label.config(image=img_tk)
            self.video_label.image = img_tk

        except StopIteration:
            print("[ERROR] Failed to get video frame.")
            self.quit()

        self.after(10, self.update_video_feed)

# ✅ Function you can import elsewhere
def run_auto_mode():
    app = AutoModeApp()
    app.mainloop()

# ✅ Test block to run directly from this file
if __name__ == "__main__":
    run_auto_mode()
