# yolo_detector.py
import cv2
from ultralytics import YOLO
from utils.distance_predictor import DistancePredictor  # Uses the same class

class YoloDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)
        self.distance_predictor = DistancePredictor()

    def detect_person(self, frame):
        results = self.model(frame, classes=[0])  # Class 0 = person
        image_height, image_width, _ = frame.shape
        scale = 2  # Important for height scaling
        detected_center_x, h = None, 0
        distance_in_ft, distance_in_m = 0, 0

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

        return frame, detected_center_x, h, distance_in_m, distance_in_ft
