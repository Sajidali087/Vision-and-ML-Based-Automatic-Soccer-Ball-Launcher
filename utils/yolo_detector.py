# yolo_detector.py
import cv2
from ultralytics import YOLO
from utils.distance_predictor import DistancePredictor
import shared_state  # <-- Import your shared state file

class YoloDetector:
    def __init__(self, model_path="models/yolov8n.pt"):
        self.model = YOLO(model_path)
        self.distance_predictor = DistancePredictor()

    def detect_person(self, frame):
        results = self.model(frame, classes=[0])  # Class 0 = person

        image_height, image_width, _ = frame.shape
        shared_state.video_height = image_height
        shared_state.video_width = image_width

        # Reset shared state defaults
        shared_state.person_detected = False
        shared_state.person_height = 0
        shared_state.person_center_x = None
        shared_state.distance_m = 0
        shared_state.distance_ft = 0

        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                if class_id == 0:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    h = y2 - y1
                    height_norm = h / image_height
                    distance_in_ft = self.distance_predictor.predict_distance(height_norm)
                    distance_in_m = distance_in_ft / 3.281
                    detected_center_x = (x1 + x2) // 2

                    # Draw box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 128, 0), 2)
                    cv2.line(frame, (detected_center_x, y1), (detected_center_x, y2), (0, 0, 255), 1)

                    # Update shared state
                    shared_state.person_detected = True
                    shared_state.person_height = h
                    shared_state.person_center_x = detected_center_x
                    shared_state.distance_ft = distance_in_ft
                    shared_state.distance_m = distance_in_m
                    shared_state.person_height_norm = height_norm

        return frame, shared_state.person_center_x, shared_state.person_height, shared_state.distance_m, shared_state.distance_ft
