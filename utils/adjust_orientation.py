import cv2
from utils.arduino_handler import ArduinoHandler
from utils.pid_controller import PIDController
import utils.video_capture as capture_frames # You must ensure this has a get_frame() function
from config import PID_KP, PID_KI, PID_KD, INTEGRAL_LIMIT, CENTER_OFFSET, CUSTOM_WIDTH, TEXT_FONT, CUSTOM_RESOLUTION

class PIDDetector:
    def __init__(self):
        # Initialize Arduino handler
        try:
            self.arduino_handler = ArduinoHandler()
            print("Arduino Handler initialized.")
        except Exception as e:
            print(f"Error initializing Arduino Handler: {e}")
            self.arduino_handler = None

        # Initialize PID controller
        try:
            self.pid_controller = PIDController(PID_KP, PID_KI, PID_KD, INTEGRAL_LIMIT)
            print("PID Controller initialized.")
        except Exception as e:
            print(f"Error initializing PID Controller: {e}")
            self.pid_controller = None

        # Set defaults
        self.center_x = None
        # self.CENT_OFFSET = 5
        self.person_in_front = False

    def detect_and_control(self, frame, detected_center_x, image_height):
        try:
            image_height = int(image_height)
            detected_center_x = int(detected_center_x)

            if self.center_x is None:
                self.center_x = frame.shape[1] // 2  # Set frame center_x based on first frame

            if self.pid_controller is None:
                print("PID Controller not initialized properly.")
                return frame

            # Compute PID output
            pid_output = self.pid_controller.compute(self.center_x, detected_center_x, CUSTOM_WIDTH)

            # Send data to Arduino
            if self.arduino_handler:
                self.arduino_handler.send_data(pid_output)

            # Determine if player is in front
            self.person_in_front = (self.center_x - CENTER_OFFSET) <= detected_center_x <= (self.center_x + CENTER_OFFSET)

            # Draw center line area
            for i in range(-CENTER_OFFSET, CENTER_OFFSET + 1):
                line_x = self.center_x + i
                cv2.line(frame, (int(line_x), 0), (int(line_x), image_height), (0, 255, 0), 2)

            # Debug info
            cv2.putText(frame, f'PID Output: {pid_output:.2f}', (10, 200),
                        TEXT_FONT, 0.7, (255, 0, 0), 2)
            # cv2.putText(frame, f'(Player X: {detected_center_x}, Center X: {self.center_x})',
            #             (10, 230), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            if self.person_in_front:
                cv2.putText(frame, "Player is in front of the camera", (10, 260),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            return frame

        except Exception as e:
            print(f"[ERROR] during PID detection and control: {e}")
            return frame

    def process_frame(self):
        # Assuming video_capture.get_frame() returns a frame or None
        frame = capture_frames()  # Replace with actual frame capture logic
        frame  = cv2.resize(frame, (CUSTOM_RESOLUTION))  # Resize to custom resolution
        if frame is None:
            print("No frame received from video capture.")
            return

        # Get image dimensions
        height, width = frame.shape[:2]

        # Calculate image center (optional: done in __init__)
        if self.center_x is None:
            self.center_x = width // 2

        # Simulated detection: Assume player at center-left (replace this with actual detection logic)
        # detected_center_x = int(width * 0.3)  # Fake player position for testing

        # # Call PID and visualization
        # result_frame = self.detect_and_control(frame, detected_center_x, height)

        # Show result
        # # cv2.imshow("PID Control Output", frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     return False  # Stop loop

        # return True  # Continue loop

if __name__ == "__main__":
    pid_detector = PIDDetector()

    print("Starting PID video processing. Press 'q' to exit.")
    while True:
        continue_loop = pid_detector.process_frame()
        if continue_loop is False:
            break

    cv2.destroyAllWindows()
