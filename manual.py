import cv2
import time
import threading
import UI.User_Interface as gui
import UI.angle_meter as angle_meter
from utils.adjust_orientation import PIDDetector
from utils.yolo_detector import YoloDetector
from utils.frame_drawer import draw_and_annotate_frame  # Import the function for drawing and annotating frames

def run_manual_mode(frame_generator):
    yolo = YoloDetector()
    pid_detector = PIDDetector()
    fps_list = []

    def detection_pid_loop():
        for frame in frame_generator:
            start_time = time.time()

            scale = 2
            # frame = cv2.resize(frame, (int(480 / scale), int(640 / scale)))
            image_height, image_width, _ = frame.shape
            center_x = image_width // 2

            # YOLO Detection + Distance
            frame, detected_center_x, h, distance_in_m, distance_in_ft = yolo.detect_person(frame)
            angle = angle_meter.get_current_angle() / 4

            # FPS Calculation and updating UI information
            def fps():
                elapsed_time = time.time() - start_time
                fps = 1 / max(elapsed_time, 1e-6)
                fps_list.append(fps)
                if len(fps_list) > 10:
                    fps_list.pop(0)
                avg_fps = sum(fps_list) / len(fps_list)
                return avg_fps

            if detected_center_x is not None:
                frame = pid_detector.detect_and_control(frame, detected_center_x, image_height)
                frame = draw_and_annotate_frame(frame, detected_center_x, h, distance_in_m, distance_in_ft, angle, fps())
                gui.update_video_frame_from_detection(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

    def start_thread():
        threading.Thread(target=detection_pid_loop, daemon=True).start()

    gui.run_gui(start_thread)
