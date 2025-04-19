# pid_detector.py

import cv2
from utils.arduino_handler import ArduinoHandler
from utils.pid_controller import PIDController
from utils.video_capture import capture_frames
from config import PID_KP, PID_KI, PID_KD, INTEGRAL_LIMIT, CENTER_OFFSET, TEXT_FONT


class PIDDetector:
    def __init__(self):
        # Initialize Arduino handler and PID controller
        try:
            self.arduino_handler = ArduinoHandler()
            print("Arduino Handler initialized.")
        except Exception as e:
            print(f"Error initializing Arduino Handler: {e}")
            self.arduino_handler = None

        try:
            self.pid_controller = PIDController(PID_KP, PID_KI, PID_KD, INTEGRAL_LIMIT)
            print("PID Controller initialized.")
        except Exception as e:
            print(f"Error initializing PID Controller: {e}")
            self.pid_controller = None

        self.center_x = None  # Set to None initially, will be calculated based on first frame
        self.person_in_front = False

    def detect_and_control(self, frame, detected_center_x, image_height):
        # try:
        detected_center_x = int(detected_center_x)

        # Initialize the center_x value from frame width
        if self.center_x is None:
            self.center_x = int(frame.shape[1] / 2)

        # Handle PID controller logic
        if self.pid_controller is None:
            print("PID Controller not initialized properly.")
            return frame

        pid_output = self.pid_controller.compute(self.center_x, detected_center_x, frame.shape[1])

        # Send the PID output data to the Arduino if it's initialized
        if self.arduino_handler:
            self.arduino_handler.send_data(pid_output)

        # Check if the player is within the threshold of the center
        self.person_in_front = (self.center_x - CENTER_OFFSET) <= detected_center_x <= (self.center_x + CENTER_OFFSET)

        # Draw a line representing the center on the frame
        for i in range(-CENTER_OFFSET, CENTER_OFFSET + 1):
            line_x = self.center_x + i
            cv2.line(frame, (int(line_x), 0), (int(line_x), image_height), (0, 255, 0), 2)

        # Show PID output on the frame
        cv2.putText(frame, f'PID Output: {pid_output:.2f}', (10, 200),
                    TEXT_FONT, 0.7, (255, 0, 0), 2)

        if self.person_in_front:
            cv2.putText(frame, "Player is in front of the camera", (10, 260),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        return frame

        # except Exception as e:
        #     print(f"[ERROR] during PID detection and control: {e}")
        #     return frame

    def run(self):
        print("Starting PID Detector...")
        try:
            for frame in capture_frames():  # Capture frames from the generator
                height, width = frame.shape[:2]

                if self.center_x is None:
                    self.center_x = width // 2

                # Simulated detected object center (replace with actual detection logic)
                detected_center_x = int(width * 0.3)  # This simulates the center of a player (replace it)

                result_frame = self.detect_and_control(frame, detected_center_x, height)

                cv2.imshow("PID Control Output", result_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            print(f"[ERROR] Could not process frame: {e}")
        finally:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    detector = PIDDetector()
    detector.run()
